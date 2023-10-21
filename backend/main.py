from flask import Flask, request, jsonify
from PIL import Image
from make_prediction import make_prediction

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def home():
    return "Hello. You've reached to the API for Tomato Leaf Disease Detection! Please send a POST request at '/predict_disease' route to find the probability of any disease of your Tomato Leaf."

@app.route("/predict_disease", methods=["POST"])
def process_image():
    file = request.files['image']
    img = Image.open(file.stream)
    return jsonify(make_prediction(img))

if __name__ == "__main__":
    #app.run(host='0.0.0.0',port=8080)
    app.run(debug=True) 