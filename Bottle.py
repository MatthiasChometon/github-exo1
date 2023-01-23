from bottle import route, run
from Add import add


@route("/hello/<a>/<b>")
def hello(a, b):
    return add(a, b)


run(host="localhost", port=8080, debug=True)
