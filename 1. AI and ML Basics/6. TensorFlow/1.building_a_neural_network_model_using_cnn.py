# Step 1: Load Packages
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Check Device (CPU/GPU)
device_name = tf.config.list_physical_devices()
print("Available Devices:", device_name)

# Step 3: Load Dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Step 4: Optional - Split Validation Set
x_val = x_train[-5000:]
y_val = y_train[-5000:]
x_train = x_train[:-5000]
y_train = y_train[:-5000]

# Step 5: Display Sample Images
plt.figure(figsize=(10,2))
for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.axis('off')
plt.show()

# Step 6: Print Data Shapes
print("Train Shape:", x_train.shape)
print("Validation Shape:", x_val.shape)
print("Test Shape:", x_test.shape)

# Step 7: Reshape for CNN (Add channel = 1)
x_train = x_train.reshape(-1, 28, 28, 1)
x_val = x_val.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Step 8: Min-Max Scaling
x_train = x_train / 255.0
x_val = x_val / 255.0
x_test = x_test / 255.0

# Step 9: One Hot Encoding Labels
y_train = to_categorical(y_train, 10)
y_val = to_categorical(y_val, 10)
y_test = to_categorical(y_test, 10)

# Step 10–11: Build CNN Model
model = Sequential()

# Layer 1: Conv + MaxPool
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(MaxPooling2D((2,2)))

# Layer 2: Conv + MaxPool
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))

# Flatten & Dense Layers
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))  # 10 output classes

# Compile Model
model.compile(optimizer='sgd', 
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Summary
model.summary()

# Step 12: Parameters (manual)
# Example for first Conv2D layer:
# (3x3x1 + 1) * 32 = 320

# Step 13: Train the Model
model.fit(x_train, y_train, epochs=5, validation_data=(x_val, y_val))

# Step 14: Test the Model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Test Accuracy:", test_accuracy)

# Step 15: Predict 20 Samples
predictions = model.predict(x_test[:20])
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test[:20], axis=1)

plt.figure(figsize=(15, 3))
for i in range(20):
    plt.subplot(2, 10, i+1)
    plt.imshow(x_test[i].reshape(28,28), cmap='gray')
    plt.title(f"Pred: {predicted_classes[i]}\nTrue: {true_classes[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
