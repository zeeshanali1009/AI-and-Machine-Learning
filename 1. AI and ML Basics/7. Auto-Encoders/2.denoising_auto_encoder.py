import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load MNIST Data (Unlabeled - we only use X)
(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()

# Step 2: Normalize (Scale between 0 and 1)
x_train = x_train.astype("float32") / 255.
x_test = x_test.astype("float32") / 255.

# Step 3: Reshape for CNN (Add channel dimension)
x_train = np.reshape(x_train, (-1, 28, 28, 1))
x_test = np.reshape(x_test, (-1, 28, 28, 1))

# Step 4: Add Noise
noise_factor = 0.5
x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape)
x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)

# Clip the noisy data to stay between 0 and 1
x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_test_noisy = np.clip(x_test_noisy, 0., 1.)

# Step 5: Build the Autoencoder
input_img = tf.keras.Input(shape=(28, 28, 1), name="Input")

# Encoder
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same', name="Enc_Conv1")(input_img)
x = layers.MaxPooling2D((2, 2), padding='same', name="Enc_Pool1")(x)
x = layers.Conv2D(16, (3, 3), activation='relu', padding='same', name="Enc_Conv2")(x)
encoded = layers.MaxPooling2D((2, 2), padding='same', name="Encoded")(x)

# Decoder
x = layers.Conv2D(16, (3, 3), activation='relu', padding='same', name="Dec_Conv1")(encoded)
x = layers.UpSampling2D((2, 2), name="Dec_Upsample1")(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same', name="Dec_Conv2")(x)
x = layers.UpSampling2D((2, 2), name="Dec_Upsample2")(x)
decoded = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same', name="Output")(x)

# Step 6: Create and Compile Model
autoencoder = models.Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.summary()

# Step 7: Train the Model (Noisy input → Clean output)
autoencoder.fit(
    x_train_noisy, x_train,
    epochs=5,
    batch_size=128,
    shuffle=True,
    validation_data=(x_test_noisy, x_test)
)

# Step 8: Predict (Denoise)
denoised_imgs = autoencoder.predict(x_test_noisy)

# Step 9: Display Results (Noisy → Denoised → Original)
n = 10
plt.figure(figsize=(15, 5))
for i in range(n):
    # Noisy Input
    plt.subplot(3, n, i + 1)
    plt.imshow(x_test_noisy[i].reshape(28, 28), cmap='gray')
    plt.title("Noisy")
    plt.axis('off')

    # Denoised Output
    plt.subplot(3, n, i + 1 + n)
    plt.imshow(denoised_imgs[i].reshape(28, 28), cmap='gray')
    plt.title("Denoised")
    plt.axis('off')

    # Original
    plt.subplot(3, n, i + 1 + 2 * n)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title("Original")
    plt.axis('off')

plt.tight_layout()
plt.suptitle("Denoising Autoencoder - Top: Noisy, Middle: Denoised, Bottom: Original", fontsize=14, y=1.05)
plt.show()
