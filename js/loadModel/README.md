# load by http request
* open `http.html`
  * specify the json file only, it will send another request to get `bin` file

## Note
* `python3 -m "http.server" 8888` does not support `CORS`
* let's use another http server
```
npm install http-server -g
http-server -p 3000 --cors
```
