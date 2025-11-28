import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic dataset with 7 features (for demonstration)
X = np.random.rand(500, 7)  # 500 samples, 7 input features
y = np.random.randint(0, 5, size=500)  # 5 random crop classes

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("ml_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✔ model.pkl generated successfully!")
