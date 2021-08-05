# tensorflow serving
* It is a server which servers tensorflow models (or keras models)
  * Can be set up with or without `docker`
  * It is recommended to build tensorflow serving with `docker`
* It designed for `production` environments
* It deals with only the `inference aspect` of machine learning
* It provides clients with `versioned access` via a reference-counted lookup table
* It is part of MLOps
  * there are some other options on the cloud 
* It can server mutiple models or same models with multiple versions
* It supports many servables: Tensorflow models, embeddings, vocabularies, feature transformations and even non-Tensorflow-based machine learning models
* It exposes both `gRPC` as well as `HTTP` inference endpoints
  * `gRPC` is google `Remote Procedure Calls`
  * `gRPC`  uses `HTTP/2` for transport, `Protocol Buffers` as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts



