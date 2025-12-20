💰 #Insurance Premium Prediction App

A Machine Learning–powered web application to predict insurance premiums based on user details such as age, BMI, gender, smoking habits, region, and number of children.
Built using Python, scikit-learn, and Streamlit, and deployed via GitHub.

<hr>

🚀 #Live Demo

👉 ## 🚀 Live Demo
<a href="https://insurancepremiumprediction-ldvqjoxdfdwqq3vfyhdq33.streamlit.app/" target="_blank">
Click here to view the live app
</a>


<hr>

📌 #Features

Predicts insurance premium using a trained RandomForestRegressor

Interactive and user-friendly UI built with Streamlit

Dropdown-based inputs with default values

BMI category helper (Underweight / Normal / Overweight / Obese)

Premium vs BMI comparison chart

Dark mode toggle

Indian currency formatting (₹)

Fully deployable via GitHub + Streamlit Cloud

<hr>
🧠 #Machine Learning Model

Algorithm: Random Forest Regressor

Library: scikit-learn

Target Variable: Insurance Charges / Premium

Evaluation Metric: RMSE (Root Mean Squared Error)

<hr>
📊 #Input Parameters

| Feature  | Description               |
| -------- | ------------------------- |
| Age      | Age of the insured person |
| Gender   | Male / Female             |
| BMI      | Body Mass Index           |
| Children | Number of dependents      |
| Smoker   | Smoking habit             |
| Region   | Residential region        |

<hr>
🛠️ #Tech Stack

Python

Streamlit

scikit-learn

pandas

matplotlib

joblib

<hr>
📁 #Project Structure
insurance-premium-prediction/
│
├── app.py                     # Streamlit application
├── insuranceclassifier.pkl    # Trained ML model
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation

<hr>
⚙️ #Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/your-username/insurance-premium-prediction.git
cd insurance-premium-prediction


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
<hr>
📦 #requirements.txt
streamlit
joblib
pandas
matplotlib
scikit-learn
<hr>
🌐 #Deployment

This project is deployed using Streamlit Community Cloud via GitHub.

Deployment steps:

Push code to GitHub

Go to https://share.streamlit.io

Select repository and premium_pred.py

Click Deploy



<hr>

📈 #Future Enhancements

PDF report download

Model confidence score

Risk profiling

API version using FastAPI

Mobile-first UI improvements


<hr>
🤝 #Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

<hr>
📄 #License

This project is licensed under the MIT License.

<hr>
👨‍💻 #Author

Ashis Gupta
Machine Learning & Full Stack Developer



