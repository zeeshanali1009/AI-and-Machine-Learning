import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# 1. Load MNIST data
(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()

# 2. Display sample input images
plt.figure(figsize=(8, 4))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.axis("off")
plt.suptitle("Original Images")
plt.show()

# 3. Scale and reshape
x_train = x_train.astype("float32") / 255.
x_test = x_test.astype("float32") / 255.
x_train = np.reshape(x_train, (-1, 28, 28, 1))
x_test = np.reshape(x_test, (-1, 28, 28, 1))

# 4. Build Autoencoder
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

# 5. Model creation
autoencoder = models.Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# 6. Summary
autoencoder.summary()

# 7. Training
autoencoder.fit(x_train, x_train,
                epochs=10,
                batch_size=128,
                shuffle=True,
                validation_data=(x_test, x_test))

# 8. Predict using the trained model
decoded_imgs = autoencoder.predict(x_test)

# 9. Display original vs reconstructed
n = 10
plt.figure(figsize=(10, 4))
for i in range(n):
    # Original
    plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.axis('off')
    # Reconstructed
    plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28), cmap='gray')
    plt.axis('off')
plt.suptitle("Original (Top) vs Reconstructed (Bottom)")
plt.tight_layout()
plt.show()
