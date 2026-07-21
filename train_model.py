import joblib
from xgboost import XGBClassifier
from sklearn.metrics import precision_score, recall_score, classification_report

# Load what preprocess.py already prepared
X_train_scaled = joblib.load('X_train_scaled.pkl')
X_test_scaled = joblib.load('X_test_scaled.pkl')
y_train = joblib.load('y_train.pkl')
y_test = joblib.load('y_test.pkl')

# Initialize and train
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42,
    scale_pos_weight=(y_train == 0).sum() / (y_train == 1).sum()
)
model.fit(X_train_scaled, y_train)

# Predict on the held-out test set
y_pred = model.predict(X_test_scaled)

# Evaluate
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
print()
print(classification_report(y_test, y_pred))