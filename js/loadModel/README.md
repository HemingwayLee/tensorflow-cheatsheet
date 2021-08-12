# How
## `ori.html`
* load `data/my-model-45.json` and `data/my-model-45.weights.bin`

## `iris.html`
* load `data/iris.json` and `data/group1-shared1fo1.bin`

## `http.html`
### load by http request
* open `http.html`
  * specify the json file only, it will send another request to get `bin` file
* run a http server in `data` folder
```
http-server -p 3000 --cors
```

# Note
* `python3 -m "http.server" 8888` does not support `CORS`
* let's use another http server
```
npm install http-server -g
http-server -p 3000 --cors
```

