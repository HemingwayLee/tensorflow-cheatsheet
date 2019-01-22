import tensorflow as tf

#basic constant operatiopns
a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0) # also tf.float32 implicitly
print(a, b)

#To actually evaluate the nodes, 
# we must run the computational graph within a session.
sess = tf.Session()
print(sess.run([a, b]))

c = tf.add(a, b)
print("c:", c)
print("sess.run(c):", sess.run(c))
print("sess.run(a*b):", sess.run(a*b))