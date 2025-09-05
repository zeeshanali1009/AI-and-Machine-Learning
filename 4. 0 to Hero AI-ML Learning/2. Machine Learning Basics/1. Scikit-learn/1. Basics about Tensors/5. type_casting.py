import tensorflow as tf

# changing the type of the tensors
int_tensor  = tf.constant([1,2,3],dtype = tf.int32)
# cast to float
float_tensor  = tf.cast(int_tensor, tf.float32)
print(float_tensor)
