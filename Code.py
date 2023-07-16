from flask import Flask, jsonify, request
from Data import Data
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":Data,
        "message":"success",

    }), 200

@app.route("/stars")
def star():
    name = request.args.get("name")
    star_data = next(item for item in Data if item["name"]== name )
    return jsonify({
        "data":star_data,
        "message":"success"

    }),200  

if __name__ == "__main__":
    
    app.run(debug = True)
