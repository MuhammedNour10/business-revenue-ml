import streamlit as st
import joblib
import pandas as pd

# تحميل النموذج والترميز
model = joblib.load("revenue_model.pkl")
encoder = joblib.load("brand_encoder.pkl")

st.title("📊 Revenue Prediction App")
st.write("أدخل القيم التالية للتنبؤ بالإيرادات:")

# مدخلات من المستخدم
year = st.number_input("Enter Year:", min_value=2000, max_value=2030, value=2024)
brand = st.text_input("Enter Brand:")
price = st.number_input("Enter Price:", min_value=0.0, step=0.1)
sales = st.number_input("Enter Sales:", min_value=0.0, step=1.0)
ratings = st.slider("Select Ratings:", 0.0, 5.0, 4.0)

# معالجة البراند
brand_encoded = None
if brand:
    try:
        brand_encoded = encoder.transform([brand])[0]
    except:
        st.error("❌ هذا البراند غير موجود في بيانات التدريب")

# زر التنبؤ
if st.button("🔮 Predict Revenue"):
    if brand_encoded is not None:
        input_data = pd.DataFrame(
            [[year, brand_encoded, price, sales, ratings]],
            columns=["Year", "Brand_encoded", "Price", "Sales", "Ratings"],
        )
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Predicted Revenue: {prediction:,.2f}")
    else:
        st.warning("⚠️ يرجى إدخال بيانات صحيحة")
