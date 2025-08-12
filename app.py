from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model & encoder
model = joblib.load("decision_tree_spam.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            word_count = float(request.form["word_count"])
            num_links = float(request.form["num_links"])
            contains_offer = int(request.form["contains_offer"])

            user_data = np.array([[word_count, num_links, contains_offer]])
            pred = model.predict(user_data)[0]
            prediction = label_encoder.inverse_transform([pred])[0]
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

