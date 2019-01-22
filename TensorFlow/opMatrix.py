import tensorflow as tf

#a 1x2 matrix
a = tf.constant([[3., 3.]])

#a 2x1 matrix
b = tf.constant([[2.],[2.]]) 

product = tf.matmul(a, b)

sess = tf.Session()
print("sess.run(a*b):", sess.run(product))