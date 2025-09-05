import tensorflow as tf

categories  = tf.constant([1,2,3])

# one hot encode the categories
one_hot_encode  = tf.one_hot (categories, depth =3)
print(one_hot_encode)

