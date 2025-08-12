# Decision Tree Classification with Flask Web App

##  Overview
This project demonstrates how to use a **Decision Tree Classifier** for predicting whether an email is **Spam** or **Not Spam**.  
The machine learning model is built using **scikit-learn** and integrated into a **Flask web application** with HTML & CSS for the frontend.

---

##  Features
- **Decision Tree Classifier** trained on a CSV dataset.
- **Flask** backend for handling requests and predictions.
- **HTML + CSS** frontend for a simple, user-friendly interface.
- User can **input text** and get predictions instantly.
- Well-structured code with `model.py`, `app.py`, and templates.

---

## Project Structure
---
```
decision_tree_spam/
│
├── model.py # Trains and saves the Decision Tree model
├── app.py # Flask application for serving predictions
├── templates/
│ ├── index.html # Main input form page
│ └── result.html # Displays prediction results
├── static/
│ └── style.css # CSS for frontend styling
├── dataset.csv # Sample dataset (spam/not spam emails)
├── requirements.txt # Required Python dependencies
└── README.md # Project documentation
```
---

##  Requirements

Install dependencies:
```
pip install -r requirements.txt\

```
## Dataset
The dataset (dataset.csv) contains two columns:

text: Email content.

label: spam or not spam.
---
```
Example:
text,label
"Congratulations! You have won a free ticket!",spam
"Meeting scheduled for tomorrow",not spam
```
---
## How It Works
  Model Training (model.py)

    -> Reads the CSV dataset.

    -> Cleans and preprocesses the text.

    -> Trains a Decision Tree Classifier.

    -> Saves the model as model.pkl.

  Web Application (app.py)

    -> Loads the saved model.

    -> Takes user input from the HTML form.

    -> Predicts if the text is spam or not spam.

    -> Displays results on a new page.

##  Running the Project
  1️⃣ Train the Model
  ```
python model.py
```
2️⃣ Run Flask App
```
python app.py
```
3️⃣ Open Browser
```
http://127.0.0.1:5000/
```
## Screenshots
  Home Page
  ---
  <img width="894" height="530" alt="Screenshot 2025-08-12 101808" src="https://github.com/user-attachments/assets/7fa843c3-d5d1-49c0-b7e8-4b543439705f" />
  
  Prediction Result
  ---
  <img width="896" height="518" alt="Screenshot 2025-08-12 101819" src="https://github.com/user-attachments/assets/5ce7eccb-defb-4191-9b0d-c9c25a6d4e47" />

  
