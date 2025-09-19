# 📊 Revenue Prediction App

A Machine Learning web app built with **Streamlit** to predict product revenue based on features like **Year, Brand, Price, Sales, and Ratings**.  
The model is trained using **Random Forest** and includes label encoding for categorical data.

---

## 🚀 Features
- User-friendly web interface with Streamlit.
- Predicts revenue based on multiple features.
- Handles categorical encoding for Brand.
- Easy deployment and portable model (`.pkl` files).

---

## 📂 Project Structure
revenue_prediction_app/
│── app.py # Streamlit web app
│── revenue_model.pkl # Trained ML model
│── brand_encoder.pkl # Label Encoder for Brand


## Description / About the App


The Revenue Prediction App is a machine learning-powered web application that allows users to predict the expected revenue of a product based on its key features.
It is designed to be user-friendly, making it easy for business analysts, product managers, or anyone interested in sales forecasting to use the model without writing any code.
🔹 Key Features:
User Inputs:

- Year: The year of the product release or sales data.
- Brand: The product brand (categorical, encoded internally).
- Price: Selling price of the product.
- Sales: Total units sold or expected sales volume.
- Ratings: Average customer ratings.
- 
Output:
Predicted Revenue: The estimated revenue based on the entered values, displayed instantly.
Benefits:
Quickly evaluate potential revenue before launching or adjusting pricing strategies.
Provides insights into how different features (price, brand, sales, ratings) affect revenue.
Simple web interface powered by Streamlit, requiring no coding experience

🔹 How It Works:
The backend uses a Random Forest Regressor trained on historical sales data.
Categorical features like Brand are converted into numeric values using Label Encoding.
The trained model predicts revenue when users submit the input form.

<img width="1920" height="1243" alt="Screenshot 2025-09-19 at 17 17 05" src="https://github.com/user-attachments/assets/06b39678-8536-4e53-8205-ad89c8a0af5d" />

