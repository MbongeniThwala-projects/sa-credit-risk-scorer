import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
df = pd.read_csv('sa_credit_data.csv')

# Check for missing values
print(df.isnull().sum())

# Separate features from target
feature_columns = ['age', 'monthly_income', 'active_debt', 'credit_utilization_ratio', 'days_in_arrears']
X = df[feature_columns]
y = df['default_flag']

# Split BEFORE scaling, to avoid data leakage
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale — fit only on training data, apply same transform to test data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Training set shape:", X_train_scaled.shape)
print("Test set shape:", X_test_scaled.shape)

joblib.dump(X_train_scaled, "X_train_scaled.pk1")
joblib.dump(X_test_scaled, 'X_test_scaled.pk1')
joblib.dump(y_train, 'y_train.pk1')
joblib.dump(y_test, 'y_test.pk1')
joblib.dump(scaler, 'scaler.pk1')

print("Saved all preprocessed files.")