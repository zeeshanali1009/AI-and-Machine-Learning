import tensorflow as tf
# operations on the tensors
tensor = tf.constant([1,2,3])
# reshape a tensor
reshaped_tensor = tf.reshape(tensor, [3,1])
# slice a tensor
sliced_tensor  =tf.slice(tensor, [0],[2])
# mathematical operations
sum_tensor = tf.reduce_sum(tensor)

# print the result
print("Original Tensor: ", tensor)
print("Reshaped Tensor: ", reshaped_tensor)
print("Sliced Tensor: ", sliced_tensor)