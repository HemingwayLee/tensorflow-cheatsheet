# Tensorflow
[Feed Forward Example](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/FeedForward.ipynb)

## What are Tensors
* Tensors are higher dimensional arrays with a uniform type (called a `dtype`)
* It stands apart from numpy array as it offers other methods
* It can be converted into numpy array (v1 and v2 use different functions to convert)
* We can do basic math on tensors, including addition, element-wise multiplication, and matrix multiplication

## What is the difference between `tf.Placeholder` and `tf.Variable`
[variables](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Variable.ipynb): They are used to store the state of a graph. They must be initialized before using.  
[placeholders](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Placeholder.ipynb): They are used to feed external data into a graph.

## What is Computational Graph?
A computational graph is a directed graph where the nodes correspond to operations or variables. Variables can feed their value into operations, and operations can feed their output into other operations. This way, every node in the graph defines a function of the variables.  

![computational_graph](https://user-images.githubusercontent.com/8428372/72130257-4bfd9680-33bc-11ea-975b-a39dc219a58d.png)

## Ref  
https://www.tensorflow.org/guide/tensor?hl=en  
