📊 Revenue Prediction App (English Version)
A Machine Learning web application built with Streamlit to predict the expected revenue of a product based on its key features: Year, Brand, Price, Sales, and Ratings.
The model is trained using Random Forest and includes label encoding for categorical features like Brand.

🚀 Features
User-friendly web interface for easy interaction.
Predicts revenue based on multiple product features.
Automatically handles categorical encoding for Brand.
Portable model using .pkl files for easy deployment.

📂 Project Structure
revenue_prediction_app/
│── app.py                # Streamlit web app
│── revenue_model.pkl     # Trained ML model
│── brand_encoder.pkl     # Label Encoder for Brand


📝 Description / About the App
The Revenue Prediction App allows users to estimate the revenue of a product by entering its key features.
It is designed to be intuitive and accessible, so business analysts, product managers, or anyone interested in sales forecasting can use it without coding skills.
🔹 Key Features
User Inputs:
Year: Product release or sales year.
Brand: Product brand (automatically encoded internally).
Price: Selling price of the product.
Sales: Total units sold or expected sales volume.
Ratings: Average customer ratings.
Output:
Predicted Revenue: The estimated revenue based on the provided values, displayed instantly.
Benefits:
Quickly evaluate potential revenue before launching or adjusting pricing.
Gain insights into how different features affect revenue.
Simple interface powered by Streamlit, requiring no coding experience.
🔹 How It Works
Backend uses a Random Forest Regressor trained on historical sales data.
Categorical features like Brand are converted into numeric values using Label Encoding.
The trained model predicts revenue when users submit the input form.

🖼 Screenshot
<img width="1920" height="1243" alt="Revenue Prediction App Screenshot" src="https://github.com/user-attachments/assets/06b39678-8536-4e53-8205-ad89c8a0af5d" />


📊 تطبيق التنبؤ بالإيرادات (النسخة العربية)
هو تطبيق ويب مدعوم بالذكاء الاصطناعي (Machine Learning) مبني باستخدام Streamlit لتوقع الإيرادات المتوقعة لأي منتج بناءً على خصائصه الأساسية: السنة، العلامة التجارية، السعر، المبيعات، والتقييمات.
النموذج مستخدم فيه Random Forest مع Label Encoding للخصائص الفئوية مثل العلامة التجارية.

🚀 الميزات
واجهة مستخدم سهلة وبسيطة للتفاعل مع التطبيق.
توقع الإيرادات بناءً على عدة خصائص للمنتج.
معالجة تلقائية للخصائص الفئوية مثل العلامة التجارية.
نموذج قابل للنقل باستخدام ملفات .pkl لتسهيل النشر.

📂 هيكل المشروع

revenue_prediction_app/
│── app.py                # واجهة Streamlit
│── revenue_model.pkl     # النموذج المدرب
│── brand_encoder.pkl     # الترميز للعلامة التجارية

📝 وصف التطبيق
يتيح تطبيق التنبؤ بالإيرادات للمستخدمين تقدير الإيرادات لأي منتج عن طريق إدخال خصائصه الأساسية.
التطبيق مصمم ليكون بسيط وسهل الاستخدام، بحيث يمكن لأي شخص، سواء كان محلل أعمال أو مدير منتج، استخدامه دون الحاجة لأي مهارات برمجية.
🔹 الخصائص الرئيسية
مدخلات المستخدم:
السنة: سنة إطلاق المنتج أو بيانات المبيعات.
العلامة التجارية: يتم ترميزها تلقائيًا داخليًا.
السعر: سعر بيع المنتج.
المبيعات: إجمالي الوحدات المباعة أو المتوقع بيعها.
التقييمات: متوسط تقييمات العملاء.
المخرجات:
الإيرادات المتوقعة: القيمة التقديرية للإيرادات بناءً على البيانات المدخلة، تظهر فورًا.
الفوائد:
تقييم الإيرادات المحتملة بسرعة قبل الإطلاق أو تعديل الأسعار.
الحصول على رؤى حول تأثير الخصائص المختلفة على الإيرادات.
واجهة بسيطة تعمل بـ Streamlit بدون الحاجة للبرمجة.
🔹 طريقة العمل
يستخدم التطبيق Random Forest Regressor مدرب على بيانات المبيعات السابقة.
يتم تحويل الخصائص الفئوية مثل العلامة التجارية إلى أرقام باستخدام Label Encoding.
النموذج يقوم بتوقع الإيرادات عند إدخال المستخدم للبيانات.





