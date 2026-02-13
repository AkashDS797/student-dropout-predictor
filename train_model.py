import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Loading data...")
df = pd.read_csv('dataset.csv')
df = df[df['Target'] != 'Enrolled']
df['Target'] = df['Target'].map({'Dropout': 0, 'Graduate': 1})

# Feature Selection: The 6 most impactful variables
features = [
    'Tuition fees up to date',
    'Scholarship holder',
    'Age at enrollment',
    'Curricular units 1st sem (approved)',
    'Curricular units 2nd sem (approved)',
    'Curricular units 2nd sem (grade)'
]

X = df[features]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training optimized model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'dropout_model_lite.pkl')
print("Success! Optimized model saved as 'dropout_model_lite.pkl'.")