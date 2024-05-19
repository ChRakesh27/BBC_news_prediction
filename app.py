from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

clfModel = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route("/", methods=['POST'])
def predictCat():
    data = request.get_json()
    text=data['text']
    vec = vectorizer.transform(text)
    pred = clfModel.predict(vec)
    res=list(pred)
    return jsonify(res)

if __name__ == '__main__':
    app.run()