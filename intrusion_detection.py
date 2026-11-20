# AI-Driven Intrusion Detection for Academic Records Systems
# PhD Research Preparation - University of Kent (2026)
# Author: Nicholas Osazuwa Okunwe
# Supervisor (M.Sc.): Prof. G.K. Obahiagbon

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

print("AI Intrusion Detection System - Starting...")

# 1. LOAD DATA
# Option A: If you have NSL-KDD or CIC-IDS2017 CSV, rename it to network_traffic.csv
# Option B: If no file, we create sample data for demo so code runs anywhere
try:
    df = pd.read_csv("network_traffic.csv")
    print("Loaded real dataset: network_traffic.csv")
except FileNotFoundError:
    print("No CSV found. Using sample demo data...")
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({
        "duration": np.random.randint(0, 1000, n),
        "src_bytes": np.random.randint(0, 10000, n),
        "dst_bytes": np.random.randint(0, 10000, n),
        "failed_logins": np.random.randint(0, 5, n),
        "count": np.random.randint(0, 500, n),
        "srv_count": np.random.randint(0, 500, n),
        "protocol_type": np.random.choice(["tcp", "udp", "icmp"], n),
        "service": np.random.choice(["http", "ftp", "ssh", "dns"], n),
        "flag": np.random.choice(["SF", "S0", "REJ"], n),
        "label": np.random.choice(["normal", "dos", "probe", "r2l"], n, p=[0.6, 0.2, 0.1, 0.1])
    })

print(f"Dataset shape: {df.shape}")
print(df.head())

# 2. PREPROCESSING
# Convert text columns to numbers
le = LabelEncoder()
for col in ["protocol_type", "service", "flag"]:
    if col in df.columns:
        df[col] = le.fit_transform(df[col].astype(str))

# Features (X) and Label (y)
# Change this if your CSV has different column names
if "label" in df.columns:
    X = df.drop("label", axis=1)
    y = df["label"]
else:
    print("ERROR: Your CSV must have a column named 'label'")
    exit()

# 3. SPLIT DATA: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# 4. TRAIN MODEL: Random Forest
print("Training Random Forest...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. EVALUATE
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n========== RESULTS ==========")
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 6. FEATURE IMPORTANCE - Which features matter most?
importances = model.feature_importances_
feature_names = X.columns
print("\nTop Features for Intrusion Detection:")
for name, imp in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{name}: {imp:.4f}")

# 7. PREDICT A NEW CONNECTION (Example)
print("\n--- Testing New Connection ---")
# Example: long duration, many failed logins = suspicious
sample = X_test.iloc[0:1]
prediction = model.predict(sample)
print(f"Prediction for sample connection: {prediction[0]}")

# Save model for future use
import pickle
with open("intrusion_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("\nModel saved as intrusion_model.pkl")
print("Done!")
