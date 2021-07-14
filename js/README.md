# Why TF.js
* It supports browser and node.js
* Convert Pretrained Models to TensorFlow.js
  * It supports both TF and keras models 
    * Use `tensorflowjs_converter` to convert h5, or
    * Use `tensorflowjs` api in python to save mode in TF.js format
      * bin file and json file
  * Preprocessing and Postprocessing need to be done
* Train with javascript
  * Integrated with existing nodejs projects
  * The performance of javascript is slower than python in everything, [ref](https://dlabs.ai/blog/performance-comparison-javascript-vs-python-for-machine-learning/)
* It is easier to do visualization with browser
  * Data loading issues (performance and security) and training resource issues make it harder to train with browser

# Key difference
* no `numpy`
  * `reshape` and `np.expand_dims` are provided by `tf.js`

# Details
* use `--weight_shard_size_bytes` to get a single weights file in `tensorflowjs_converter`

# Note
* It might give you different result, [note](https://stackoverflow.com/questions/52683723/different-results-for-tensorflowjs-and-keras-on-same-model-and-tensor)

