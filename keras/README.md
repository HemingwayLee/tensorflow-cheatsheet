# Run jupyter with conda 
https://stackoverflow.com/questions/37085665/in-which-conda-environment-is-jupyter-executing  
https://blog.csdn.net/u011606714/article/details/77741324  

# Comparison  
* RNN is for time time series data
* RNN has gradient vanish problem
* LSTM/GRU internal gate design can fix gradient vanish problem (not entirely)
* Attention is the solution for that

## Gradient vanishing (gradient exploding) problem
It is a difficulty found in training artificial neural networks with gradient-based learning methods and backpropagation.  

* Not just RNN, deep feed forward NN also has gradient vanish problem
* Gradient vanishing: Gradient become smaller and smaller (the weights are updated slowly)
* Gradient exploding: Gradient become bigger and bigger (the value become NaN)

### Why we have gradient vanishing problem

### Solution for Gradient vanishing problem
* LSTM/GRU gate design
* Shortcut
* Use ReLu


https://blog.csdn.net/cppjava_/article/details/68941436  
https://blog.csdn.net/qq_25737169/article/details/78847691  
