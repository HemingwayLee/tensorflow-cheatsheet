# Run jupyter with conda 
https://stackoverflow.com/questions/37085665/in-which-conda-environment-is-jupyter-executing  
https://blog.csdn.net/u011606714/article/details/77741324  

# Comparison  
* RNN is for time time series data
* RNN has gradient vanish problem
* LSTM/GRU internal gate design can fix gradient vanish problem (not entirely)
* Attention is the solution for that

## Gradient vanish (gradient explode) problem
* Not just RNN, deep feed forward NN also has gradient vanish problem

### Why we have gradient vanish problem

### Solution for Gradient vanish problem
* LSTM/GRU gate design
* Shortcut
* Use ReLu


https://blog.csdn.net/cppjava_/article/details/68941436  
https://blog.csdn.net/qq_25737169/article/details/78847691  
