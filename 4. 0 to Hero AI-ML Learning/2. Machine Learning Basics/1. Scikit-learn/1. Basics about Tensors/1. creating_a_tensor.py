import tensorflow as tf

# creating a tensor
a  = tf.constant([1,2,3])
b  = tf.constant([4,5,6])

# perform element wise addition
c=  tf.add(a,b)

# perform element wise multiplication
c=  tf.multiply(a,b)

print(c)



# creting the random tensors
# from the noraml distribution
random_normal = tf.random.normal([3,3], mean = 0.0, stddev = 1.0)
# from uniform distribution
random_uniform = tf.random.uniform([3,3], minval = 0, maxval = 10)

print(random_normal)
print(random_uniform)


# changing the shape of the tensor
# original tensor
tensor = tf.constant([1,2,3])
# adding the new dimension
expand_tensor  = tf.expand_dims(tensor, 0)
print(expand_tensor)
# removing the single dimensions
squeezed_tensor  = tf.squeeze(tensor)
print(squeezed_tensor)



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

















