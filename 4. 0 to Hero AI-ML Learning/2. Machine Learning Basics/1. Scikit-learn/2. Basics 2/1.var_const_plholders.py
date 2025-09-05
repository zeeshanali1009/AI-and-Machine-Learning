import tensorflow as tf

# variabe
zero  =tf.variable(0)

# constant
one = tf.constant(1)

new_values   = tf.add(zero, one)

# variable value can be changed
update  = tf.assign(zero, new_values)

# uncomment during the demo
# update_constant = tf.assign(one, new_values)

init_op  = tf.global_variables_initializer()

sess = tf.Session()

# initialze the variables
sess.run(init_op)

print(sess.run(zero))
print(sess.run(one))

for _ in range(5):
    sess.run(update)
    print(sess.run(zero))


# string operations
hello  = tf.constant("hello")
world = tf.constant("world")
helloworld = tf.add(hello,world)
print(sess.run(helloworld))

# placeholder
a = tf.placeholder(tf.float32)
b = a*2
# feeding a placeholder with scalar
result  = sess.run(b,feed_dict={a:3})
# result  = sess.run(b,{a:3})
print(result)

#feeding a placeholder with vector of rank 1 
result  = sess.run(b,feed_dict = {a:[3,4,5]})
print(result)

# feeding a placeholder with multidimensional vector
dictionary  = {a:[[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]]}
result  = sess.run(b,feed_dict  =dictionary)

sess.close()

# common syntax for creating the session
with tf.Session() as sess:
    result  = sess.run(hello+world)
    print(result)
    # many more lines 
    # all lines will be executed in this session
    # no need for explicitly closing the session



