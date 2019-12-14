# tensorflow-cheatsheet

## What are Tensors
* Tensors are higher dimensional arrays
* It stands apart from numpy array as it offers other methods
* It can be converted into numpy array (v1 and v2 use different functions to convert)
* It requires prior knowledge of advanced calculus and linear algebra

## What is the difference between `tf.Placeholder` and `tf.Variable`
variables: They are used to store the state of a graph. They must be initialized before using.  
placeholders: They are used to feed external data into a graph.

## Install conda
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

