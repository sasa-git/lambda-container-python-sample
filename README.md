
Usage

```
$ docker build -t myfunction-dev:latest .
$ docker run --rm -p 9000:8080 myfunction-dev:latest

$ curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"name": "hello world"}'
```

or

```
$ docker compose build
$ docker compose up
$ curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"name": "hello world"}'

# restart after edit
$ docker compose restart lambda
```