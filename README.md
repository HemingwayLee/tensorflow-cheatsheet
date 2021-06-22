# tensorflow-cheatsheet
* A simple example
[Feed Forward Example](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/FeedForward.ipynb)
  * [What are tensors](https://github.com/HemingwayLee/tensorflow-cheatsheet/tree/master/Samples#what-are-tensors)
  * [What operations can be done on tensors](https://github.com/HemingwayLee/tensorflow-cheatsheet/tree/master/Samples#what-are-tensors)
  * [variables](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Variable.ipynb): They are used to store the state of a graph. They must be initialized before using.  
  * [placeholders](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Placeholder.ipynb): They are used to feed external data into a graph.
  * [linear model using variable and placeholders]()
  * [graph and session](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/docker/notebooks/Hello.ipynb)

## TFv1 vs TFv2

## [Compare with other libraries](https://github.com/HemingwayLee/ai-overview/blob/master/questions/libraries/README.md)

## Showing jupyter notebook on Github
https://nbviewer.jupyter.org/  

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

