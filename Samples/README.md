# Tensorflow
[Feed Forward Example](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/FeedForward.ipynb)

## What are Tensors
* Tensors are higher dimensional arrays with a uniform type (called a `dtype`)
* It stands apart from numpy array as it offers other methods
* It can be converted into numpy array (v1 and v2 use different functions to convert)
* We can do basic math on tensors (e.g., [example](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Hello.ipynb)), including [addition](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Hello.ipynb), element-wise multiplication, and [matrix multiplication](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/MatrixOperations.ipynb)

```python
import tensorflow as tf
a = tf.constant([[3., 3.]])
b = tf.constant([[2.],[2.]]) 
product = tf.matmul(a, b)
sess = tf.Session()
print("sess.run(a*b): ", sess.run(product))
```

## What is the difference between `tf.Placeholder` and `tf.Variable`
[variables](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Variable.ipynb): They are used to store the state of a graph. They must be initialized before using.  
[placeholders](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Placeholder.ipynb): They are used to feed external data into a graph.

```python
W = tf.Variable([[.1, .2, .3], [.2, .4, .6]], dtype=tf.float32)
b = tf.Variable([[.2], [.3]], dtype=tf.float32)
x = tf.placeholder(tf.float32)

linear_model = W*x + b

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(linear_model, {x: [1., 2., 3.]}))
```

## What is Computational Graph?
A computational graph is a directed graph where the nodes correspond to operations or variables. Variables can feed their value into operations, and operations can feed their output into other operations. This way, every node in the graph defines a function of the variables.  

* [graph and session](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/docker/notebooks/Hello.ipynb)

![computational_graph](https://user-images.githubusercontent.com/8428372/72130257-4bfd9680-33bc-11ea-975b-a39dc219a58d.png)

## `tf.contrib` is not able to run in TF2
The `tf.contrib` has made it easy for members of the community to contribute to TensorFlow. However, as the community has grown, the lack of scalability of the current approach for maintaining and supporting `tf.contrib` is not able to run in TF2.

## Ref  
https://www.tensorflow.org/guide/tensor?hl=en  
