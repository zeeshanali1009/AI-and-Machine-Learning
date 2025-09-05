import tensorflow as tf

# changing the shape of the tensor
# original tensor
tensor = tf.constant([1,2,3])
# adding the new dimension
expand_tensor  = tf.expand_dims(tensor, 0)
print(expand_tensor)
# removing the single dimensions
squeezed_tensor  = tf.squeeze(tensor)
print(squeezed_tensor)