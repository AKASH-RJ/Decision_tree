import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("spam_dataset.csv")

# Encode target
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])  # Spam=1, Not Spam=0

# Features & target
X = df[['word_count', 'num_links', 'contains_offer']]
y = df['label']

# Train model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X, y)

# Save model & encoder
joblib.dump(model, "decision_tree_spam.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("✅ Model trained and saved successfully!")
