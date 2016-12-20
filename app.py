from flask import Flask, request
import lib
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data", methods=['POST'])
def take():
    if request.method == 'POST':
        v = request.get_json()
        print(v)
        cardinality = int(v["cardinality"])
        del(v["cardinality"])
        data = zip(v["fields"], v["values"])
        r = lib.RandomGen(cardinality, list(data))
        return (r.output())

if __name__ == "__main__":
    app.run()
