# tensorflow-cheatsheet
* A simple example
[Feed Forward Example](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/FeedForward.ipynb)
  * [What are tensors](https://github.com/HemingwayLee/tensorflow-cheatsheet/tree/master/Samples#what-are-tensors)
  * [What operations can be done on tensors](https://github.com/HemingwayLee/tensorflow-cheatsheet/tree/master/Samples#what-are-tensors)
  * [variables](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Variable.ipynb): They are used to store the state of a graph. They must be initialized before using.  
  * [placeholders](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/Samples/Placeholder.ipynb): They are used to feed external data into a graph.
  * [linear model using variable and placeholders]()
  * [graph and session](https://github.com/HemingwayLee/tensorflow-cheatsheet/blob/master/docker/notebooks/Hello.ipynb)

## When to build custom layers
* Layers are reusable common sets of useful operations
```
class MyStn(tf.keras.layers.Layer):
    def __init__(self, n_fc, B, W, H, C):
        super(MyStn, self).__init__()
        self.n_fc = n_fc
        self.B = B
        self.W = W
        self.H = H
        self.C = C

    def build(self, input_shape):
        initial = np.array([[1., 0, 0], [0, 1., 0]])
        initial = initial.astype('float32').flatten()

        # localization network
        W_fc1 = tf.Variable(tf.zeros([self.H*self.W*self.C, self.n_fc]), name='W_fc1')
        b_fc1 = tf.Variable(initial_value=initial, name='b_fc1')

        self.h_fc1 = tf.matmul(tf.zeros([self.B, self.H*self.W*self.C]), W_fc1) + b_fc1

    def call(self, inputs):
        return stn(inputs, self.h_fc1)
```

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

## Run with docker on GPU machine 
We can use `nvidia-smi` to check how many GPUs are there
```
docker run -it --rm --gpus all ...
docker run -it --rm --gpus device=0 ...
docker run -it --rm --gpus '"device=2,3"' ...
```

