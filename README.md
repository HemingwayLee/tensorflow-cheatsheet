# tensorflow-cheatsheet
* A simple example
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

## [Compare with other libraries](https://github.com/HemingwayLee/ai-overview/blob/master/questions/libraries/README.md)

## Ref  
https://www.tensorflow.org/guide/tensor?hl=en  


## Installation 
```
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt 
ipython kernel install --user --name=venv
jupyter notebook
```

## Installation with conda
```
conda install python=3.6
conda install tensorflow
```

```
conda activate
conda deactivate
```

```
conda activate my_keras_demo
```

Create an environment:
```
conda create --name myenv
conda create -n myenv python=3.4
conda create -n myenv scipy
conda create -n myenv scipy=0.15.0
```

Check environment:
```
conda env list
```

