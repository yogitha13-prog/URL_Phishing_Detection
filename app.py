from flask import Flask, render_template, request
import joblib

from feature_extractor import extract_features

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url']

    features = extract_features(url)

    result = model.predict([features])[0]

    if result == 1:
        prediction = "⚠️ Phishing URL Detected"
    else:
        prediction = "✅ Legitimate URL"

    return render_template(
        "index.html",
        prediction_text=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)