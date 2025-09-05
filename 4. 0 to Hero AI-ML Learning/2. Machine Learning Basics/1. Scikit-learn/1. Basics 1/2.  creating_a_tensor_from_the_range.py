import tensorflow as tf

# creting the random tensors
# from the noraml distribution
random_normal = tf.random.normal([3,3], mean = 0.0, stddev = 1.0)
# from uniform distribution
random_uniform = tf.random.uniform([3,3], minval = 0, maxval = 10)

print(random_normal)
print(random_uniform)

