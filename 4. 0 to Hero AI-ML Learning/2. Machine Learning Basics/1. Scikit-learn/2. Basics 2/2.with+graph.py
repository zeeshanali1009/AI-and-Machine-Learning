import tensorflow as tf 

graph = tf.get_default_graph()
graph = tf.get_operations()

a= tf.constant(10, name = "a")

operations  = graph.get_operations()
operations
# operations[0].node_def

b= tf.constant(20,name = "b")
operations  = graph.get_operations()
operations

# operations[1].node_def

# c = a+b (=30)
c=tf.add(a,b,name = "c")
operations  = graph.get_operations()
operations
# operations[2].node_def

# d = a*b = 200
d=tf.multiply(a,b,name="d")

operations  = graph.get_operations()
operations
# operations[3].node_def
# e = c*d = 6000
e=tf.multiply(c,d,name="e")

# operations[4].node_def
sess = tf.Session()

print(sess.run(e))

for op in graph.get_operations():print(op.name)
sess.close()





