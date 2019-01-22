import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

# + provides a shortcut for tf.add(a, b)
adder_node = a + b 
adder_node2 = tf.add(a, b)

sess = tf.Session()
print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))
print(sess.run(adder_node2, {a: 3, b: 4.5}))
print(sess.run(adder_node2, {a: [1, 3], b: [2, 4]}))


add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

add_and_triple2 = adder_node2 * 3.
print(sess.run(add_and_triple2, {a: 3, b: 4.5}))