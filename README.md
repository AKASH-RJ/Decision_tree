#  Decision Tree Classifier – [Your Project Name]

A Flask-based web application that predicts **[your target prediction]** using a **Decision Tree Classifier** trained on **[your dataset details]**.

---

##  Overview

This project demonstrates how a **Decision Tree** can be used for classification problems.  
Users provide input through a simple web interface, and the app returns a prediction instantly.

---

##  Project Structure

decision-tree-project/
│
├── model.py # Trains and saves the Decision Tree model
├── decision_tree.pkl # Saved trained model
├── scaler.pkl # Saved scaler (if used)
├── app.py # Flask application
├── dataset.csv # Training dataset
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend form
├── static/
│ └── style.css # CSS styling
└── README.md # Project documentation


---

##  Dataset

**File:** `dataset.csv`

**Example Columns:**
- `feature1` (type) – description  
- `feature2` (type) – description  
- `feature3` (type) – description  
- `target` (int) – Target variable (1 = Positive, 0 = Negative)

📎 *(Replace with actual dataset link if available)*

---

##  Features

- Predicts **[your problem statement]** using a Decision Tree  
- Simple and interactive HTML/CSS interface  
- Pre-trained model for instant predictions  
- Handles numerical and categorical features  

---

## 🛠 Tech Stack

| Technology     | Use                  |
|----------------|----------------------|
| Python         | Core language        |
| Flask          | Web framework        |
| scikit-learn   | ML model training    |
| pandas         | Data handling        |
| NumPy          | Numerical operations |
| HTML/CSS       | Frontend styling     |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## 🛠 Installation

### Step 1: Clone the Repository
```
 git clone https://github.com/your-username/decision-tree-project.git
cd decision-tree-project

### Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Train the Model

python model.py

Step 4: Run the Flask App

python app.py

Open browser and go to:

 http://127.0.0.1:5000/



Screenshots

Input UI
