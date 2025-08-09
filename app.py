from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load dataset
df = pd.read_csv("spam_dataset.csv")

# Features & target
X = df.drop(columns=["is_spam"])
y = df["is_spam"]

# Feature names for form
X_columns = X.columns.tolist()

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = round(accuracy_score(y_test, model.predict(X_test)) * 100, 2)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", accuracy=accuracy, features=X_columns)

@app.route("/predict", methods=["POST"])
def predict():
    input_data = [float(request.form[f]) for f in X_columns]
    prediction = model.predict([input_data])[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return f"Prediction: {result}"

if __name__ == "__main__":
    app.run(debug=True)
