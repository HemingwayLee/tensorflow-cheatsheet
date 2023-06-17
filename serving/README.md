# tensorflow serving
## What
* It is a server which servers tensorflow models (or keras models)
  * Can be set up with or without `docker`
```
apt-get install tensorflow-model-server
```
  * It is recommended to build tensorflow serving with `docker`
* It is part of MLOps
  * there are some other options on the cloud 
    * e.g., Azure Machine Learning Workspace
  * It deals with only the `inference aspect` of machine learning
* It designed for `production` environments

## Features
* It provides clients with `versioned access` via a reference-counted lookup table
* It can server multiple models or same models with multiple versions
* It supports many servables: Tensorflow models, embeddings, vocabularies, feature transformations and even non-Tensorflow-based machine learning models
* It exposes both `gRPC` (port 8500) as well as `HTTP` (port 8501) inference endpoints
  * `gRPC` is google `Remote Procedure Calls`
  * `gRPC` uses `HTTP/2` for transport, `Protocol Buffers` as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts

## How to run
* Run by docker command
```
docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" \
    -e MODEL_NAME=half_plus_two \
    tensorflow/serving &
```

* inside dockerfile
```
tensorflow_model_server --port=8500 --rest_api_port=8501 \
  --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME}
```

## How to run on Ubuntu without docker
* Installation
```
apt-get install tensorflow-model-server
```
* Download `saved_model_half_plus_two_cpu` folder from [tensorflow/serving](https://github.com/tensorflow/serving)
* Open port 8500 and 8501 on an AWS EC2
* Run the following command to start tensorflow serving with tmux
```
tmux new-session -d -s run_tensorflow_serving 'tensorflow_model_server --port=8500 --rest_api_port=8501  --model_name="saved_model_half_plus_two_cpu" --model_base_path="/home/ubuntu/tfs/saved_model_half_plus_two_cpu/"'
```
* Open another terminal tab and run the following command to the AWS EC2
```
curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://<the_ip>:8501/v1/models/saved_model_half_plus_two_cpu:predict
```


