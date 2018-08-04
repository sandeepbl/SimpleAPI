from flask import Flask, jsonify, request
import json

api = Flask(__name__)


@api.route("/api", methods=["GET", "POST"])
def get():
    """
    - use curl command as below for GET:
    
      curl "http://localhost:9999/api"

    - use curl command as below for POST:
    
      curl -X POST -H "Content-Type: application/json" -d '{"input":"string"}' "http://localhost:9999/api"
    
    """
    if request.method == "POST":
        input_string = request.get_json()["input"]
        return jsonify(dict(output="Received <{}>".format(input_string)))
    return jsonify(dict(message="success"))


if __name__ == "__main__":
    api.run(port=9999, debug=True)
