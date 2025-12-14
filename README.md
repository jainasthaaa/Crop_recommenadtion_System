
## 🌾 Crop Recommendation System
# A Beginner-Friendly Machine Learning + Django Project

This is a simple and beginner-friendly project that helps recommend the best crop based on soil nutrients and environmental conditions.
It is perfect for students, beginners in Django, and anyone learning Machine Learning deployment.

# ⭐ Why This Project is Great for Learning

✔ Learn how to train an ML model

✔ Understand how to load and use the model inside Django

✔ Build a clean Bootstrap website

✔ Learn how to handle forms, POST requests & show predictions

✔ Beginner-friendly structure and very easy to extend

# 🌟 Features

🌱 Recommends the most suitable crop

📊 Uses a trained Random Forest ML model

🎨 Beautiful and simple UI

🧪 Easy-to-understand code

💡 Great project for beginners in ML + Django

# 🔧 Tech Used

Python

Django

Django restAPI

Scikit-learn

Bootstrap (Frontend)

# 📩 Inputs Used for Prediction

The model predicts the best crop using:

Nitrogen (N)

Phosphorus (P)

Potassium (K)

Temperature

Humidity

pH value

Rainfall

# 📁 Project Structure (Very Simple)
crop_recommendation/

│── crop_app/

│   ├── ml_model.pkl        # Trained model

│   ├── ml_code.py          # Prediction function

│   ├── views.py            # Django logic

│   ├── templates/
│   │    └── index.html     # Frontend page

│   └── static/
│        └── crop_app/      # Background image

│── manage.py

# 🛠 How to Run This Project
1️⃣ Clone the Project
git clone https://github.com/jainasthaaa/Crop_recommenadtion_System
cd crop_recommendation

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start the Server
python manage.py runserver


Website will open at:

👉 http://127.0.0.1:8000/

# 🚀 What You Can Learn From This Project

Loading ML models in Django

Handling HTML forms

Displaying predictions

Working with static files & templates

Basic full-stack ML deployment

# 🔮 Future Improvements (Beginner Ideas)

Add a results history table

Add a small API endpoint

Add charts for nutrients

Add multiple crop suggestions

# ❤️ Contribution

This is a beginner project — feel free to improve it, experiment, and learn!

# 📄 License

Open-source — free to use and modify.
