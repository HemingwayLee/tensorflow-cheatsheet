# What
* Basic setup for data proejct
  * Run docker on the cloud (GPU)
  * Get data from data pipeline
  * run experiments and push the notebook code into source control

# How to run
* pull and run
```
docker build -t mytf .
docker run -p 8888:8888 mytf
```

* run with mounted volume
```
docker run -it --rm -p 8899:8888 -v $(pwd):/home/proj/ mytf
```

# Ref
https://github.com/jupyter/docker-stacks  
https://hub.docker.com/r/jupyter/tensorflow-notebook/  

