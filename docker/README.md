# What
* Basic setup for data proejct
  * Run docker on the cloud ~~(GPU)~~
  * Get data from data pipeline
  * run experiments and push the notebook code into source control

# How to run
* pull and run
```
docker pull jupyter/tensorflow-notebook@sha256:960351dcb9da1d5b57f5d57c32a8295a3231a28248b71491aba4f79a01e36ddd
docker tag <DOCKER_IMG_ID> jupyter/tensorflow-notebook:me
docker run -p 8899:8888 jupyter/tensorflow-notebook:me
```

* run with mounted volume
```
docker run -it --rm -p 8899:8888 -v $(pwd):/home/jovyan/work jupyter/tensorflow-notebook:me
```

# Ref
https://github.com/jupyter/docker-stacks  
https://hub.docker.com/r/jupyter/tensorflow-notebook/  

