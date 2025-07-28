# Step 1: Required Packages and Data
import tensorflow as tf
from tf.keras.datasets import mnist
from tf.keras.models import Sequential
from tf.keras.layers import Dense, Flatten
from tf.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np


# Step 2: Load and Split Data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 3: Display Sample Images
plt.figure(figsize=(8, 6))
for i in range(12):
    plt.subplot(3, 4, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()

# Step 4: Flattening the Images (28x28 to 784)
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# Step 5: Min-Max Scaling (0 to 1)
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Step 6: Processing Target Variable (One-hot encoding)
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Step 7: Setting Hyperparameters
input_dim = 784  # 28x28
hidden_units = 128
output_classes = 10
epochs = 10
batch_size = 32

# Step 8: Building the Model
model = Sequential()
model.add(Dense(hidden_units, activation='relu', input_shape=(input_dim,)))
model.add(Dense(output_classes, activation='softmax'))

# Step 9: Compilation
model.compile(
    loss='categorical_crossentropy',  # use binary_crossentropy for binary class
    optimizer='sgd',  # stochastic gradient descent
    metrics=['accuracy']
)

# Step 10: Parameter Calculation (optional print)
model.summary()

# Step 11: Training the Model
history = model.fit(x_train, y_train_cat, epochs=epochs, batch_size=batch_size, validation_split=0.2)

# Step 12: Testing the Model
test_loss, test_acc = model.evaluate(x_test, y_test_cat)
print(f"Test Accuracy: {test_acc:.4f}")

# Step 13: Predict and Take 20 Samples
predictions = model.predict(x_test[:20])
predicted_labels = np.argmax(predictions, axis=1)

# Step 14: Display Results
plt.figure(figsize=(10, 6))
for i in range(20):
    plt.subplot(4, 5, i+1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Pred: {predicted_labels[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
