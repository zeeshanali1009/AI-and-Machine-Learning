import tensorflow as tf

# creating a tensor
a  = tf.constant([1,2,3])
b  = tf.constant([4,5,6])

# perform element wise addition
c=  tf.add(a,b)

# perform element wise multiplication
c=  tf.multiply(a,b)

print(c)



















