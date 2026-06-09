# import streamlit as st
# import pickle
# import numpy as np
# import plotly.graph_objects as go
# import time

# st.set_page_config(page_title="AI Diabetes Prediction", page_icon="🩺", layout="wide")

# # ---------- CSS ----------
# st.markdown("""
# <style>
# .stApp{
# background: linear-gradient(135deg,#dff6ff,#f8fbff,#ffffff);
# }
# .hero{
# padding:25px;
# border-radius:25px;
# background:linear-gradient(135deg,#00b4d8,#0077b6);
# color:white;
# text-align:center;
# box-shadow:0 10px 25px rgba(0,0,0,.15);
# }
# .glass{
# background:rgba(255,255,255,.75);
# backdrop-filter:blur(10px);
# padding:20px;
# border-radius:20px;
# box-shadow:0 8px 20px rgba(0,0,0,.08);
# }
# div.stButton > button{
# width:100%;
# height:60px;
# font-size:20px;
# font-weight:bold;
# border-radius:15px;
# background:linear-gradient(90deg,#00b4d8,#0077b6);
# color:white;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------- MODEL ----------
# model = pickle.load(open("diabetes_model.pkl","rb"))

# # ---------- HEADER ----------
# st.markdown("""
# <div class='hero'>
# <h1>🩺 AI Diabetes Prediction System</h1>
# <h4>Machine Learning Powered Healthcare Screening</h4>
# </div>
# """, unsafe_allow_html=True)

# st.write("")

# # ---------- SIDEBAR ----------
# st.sidebar.title("🏥 Dashboard")
# st.sidebar.success("Model Accuracy: 83.77%")
# st.sidebar.info("Features: TimesPregnant, Glucose, BloodPrs, SkinThickness, BMI, DiabetesFunct, Age")

# # ---------- PATIENT ----------
# st.subheader("👤 Patient Profile")

# c1,c2=st.columns(2)
# with c1:
#     patient_name=st.text_input("Patient Name")
# with c2:
#     gender=st.selectbox("Gender",["Male","Female"])

# st.subheader("📊 Medical Inputs")

# a,b=st.columns(2)

# with a:
#     times_pregnant=st.slider("Times Pregnant",0,20,0)
#     glucose=st.slider("Glucose Concentration",0,300,120)
#     blood_pressure=st.slider("Blood Pressure",0,200,70)
#     skin_thickness=st.slider("Skin Thickness",0,100,20)

# with b:
#     bmi=st.slider("BMI",10.0,50.0,25.0)
#     diabetes_funct=st.slider("Family History Diabetes Score",0.0,3.0,0.5)
#     age=st.slider("Age",1,100,30)

# st.subheader("📈 Live Health Overview")

# m1,m2,m3,m4=st.columns(4)
# m1.metric("Age",age)
# m2.metric("BMI",bmi)
# m3.metric("Glucose",glucose)
# m4.metric("Blood Pressure",blood_pressure)

# if bmi < 18.5:
#     st.warning("⚠ Underweight")
# elif bmi < 25:
#     st.success("✅ Healthy Weight")
# elif bmi < 30:
#     st.warning("⚠ Overweight")
# else:
#     st.error("🚨 Obese")

# if st.button("🔍 Analyze Diabetes Risk"):
#     data=np.array([[times_pregnant,glucose,blood_pressure,skin_thickness,bmi,diabetes_funct,age]])

#     with st.spinner("🧠 AI Analyzing Health Data..."):
#         time.sleep(2)

#     pred=model.predict(data)[0]
#     risk=model.predict_proba(data)[0][1]*100
#     health_score=100-risk

#     st.subheader("🎯 Risk Analytics")

#     fig = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=risk,
#         title={'text':"Diabetes Risk %"},
#         gauge={
#             'axis':{'range':[0,100]},
#             'steps':[
#                 {'range':[0,40],'color':'lightgreen'},
#                 {'range':[40,70],'color':'gold'},
#                 {'range':[70,100],'color':'salmon'}
#             ]
#         }
#     ))
#     st.plotly_chart(fig,use_container_width=True)

#     x1,x2=st.columns(2)
#     x1.metric("🎯 Risk Score",f"{risk:.2f}%")
#     x2.metric("💚 Health Score",f"{health_score:.2f}/100")

#     if pred==1:
#         st.error(f"⚠ HIGH RISK OF DIABETES ({risk:.2f}%)")
#     else:
#         st.success(f"✅ LOW RISK OF DIABETES ({risk:.2f}%)")

#     st.subheader("👤 Patient Summary")
#     st.markdown(f"""
#     **Name:** {patient_name if patient_name else 'N/A'}  
#     **Gender:** {gender}  
#     **Age:** {age}
#     """)

#     st.subheader("💡 Recommendations")
#     st.info("""
# 🥗 Eat healthy foods

# 🏃 Exercise regularly

# 💧 Stay hydrated

# 😴 Sleep 7-8 hours

# 🩺 Monitor blood sugar regularly

# 🚭 Avoid smoking
# """)

# st.markdown("---")
# st.markdown("<center>Made with ❤️ using Streamlit, Scikit-Learn & Plotly</center>", unsafe_allow_html=True)





import streamlit as st
import pickle, numpy as np, time
import plotly.graph_objects as go

st.set_page_config(page_title="AI Diabetes Prediction Pro", page_icon="🩺", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {font-family:Poppins;}
.stApp{
background: linear-gradient(-45deg,#dff6ff,#f7fbff,#eef9ff,#ffffff);
background-size:400% 400%;
}

.hero{
padding:35px;
border-radius:28px;
background:linear-gradient(135deg,#00b4d8,#0077b6,#023e8a);
color:white;
text-align:center;
box-shadow:0 15px 35px rgba(0,0,0,.15);
}

.glass{
background:rgba(255,255,255,.75);
backdrop-filter:blur(14px);
padding:20px;
border-radius:24px;
box-shadow:0 8px 30px rgba(0,0,0,.08);
border:1px solid rgba(255,255,255,.5);
}

div.stButton > button{
width:100%;
height:68px;
font-size:22px;
font-weight:700;
border-radius:18px;
background:linear-gradient(90deg,#00b4d8,#0077b6);
color:white;
border:none;
}

.badge{
padding:10px 18px;
background:#e8f8ff;
border-radius:50px;
display:inline-block;
font-weight:600;
margin:4px;
}

.result-good{
padding:25px;
border-radius:20px;
background:linear-gradient(135deg,#2ecc71,#27ae60);
color:white;
text-align:center;
font-size:28px;
font-weight:700;
}

.result-bad{
padding:25px;
border-radius:20px;
background:linear-gradient(135deg,#ff6b6b,#c1121f);
color:white;
text-align:center;
font-size:28px;
font-weight:700;
}
</style>
""", unsafe_allow_html=True)

model = pickle.load(open("diabetes_model.pkl","rb"))

st.markdown("""
<div class='hero'>
<h1>🩺 AI Diabetes Prediction Pro</h1>
<h3>Advanced Healthcare Intelligence Dashboard</h3>
<p>Machine Learning • Predictive Analytics • Preventive Healthcare</p>
</div>
""", unsafe_allow_html=True)

st.write("")

with st.sidebar:
    st.title("🚀 Health Dashboard")
    st.success("Model Accuracy: 83.77%")
    st.markdown("### ✨ Features")
    st.markdown("""
- AI Risk Analysis
- Health Score
- Risk Gauge
- BMI Evaluation
- Smart Recommendations
- Interactive Dashboard
""")

left,right = st.columns([1,1])

with left:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("👤 Patient Information")
    name = st.text_input("Patient Name")
    gender = st.selectbox("Gender",["Male","Female"])
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("🏷️ Quick Tags")
    st.markdown("""
    <span class='badge'>AI Powered</span>
    <span class='badge'>Healthcare</span>
    <span class='badge'>Predictive Analytics</span>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

st.subheader("📊 Medical Parameters")

c1,c2 = st.columns(2)

with c1:
    tp = st.slider("Times Pregnant",0,20,0)
    gc = st.slider("Glucose Concentration",0,300,120)
    bp = st.slider("Blood Pressure",0,200,70)
    sk = st.slider("Skin Thickness",0,100,20)

with c2:
    bmi = st.slider("BMI",10.0,50.0,25.0)
    dfn = st.slider("Family History Diabetes Score",0.0,3.0,0.5)
    age = st.slider("Age",1,100,30)

st.subheader("📈 Live Metrics")
m1,m2,m3,m4 = st.columns(4)
m1.metric("Age", age)
m2.metric("BMI", bmi)
m3.metric("Glucose", gc)
m4.metric("Blood Pressure", bp)

if st.button("🧠 Analyze Diabetes Risk"):
    with st.spinner("Analyzing health data with AI..."):
        time.sleep(2)

    data = np.array([[tp,gc,bp,sk,bmi,dfn,age]])

    pred = model.predict(data)[0]
    risk = model.predict_proba(data)[0][1] * 100
    health = 100 - risk

    g1,g2 = st.columns([2,1])

    with g1:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk,
            title={'text':'Diabetes Risk %'},
            gauge={
                'axis':{'range':[0,100]},
                'steps':[
                    {'range':[0,40],'color':'#2ecc71'},
                    {'range':[40,70],'color':'#f1c40f'},
                    {'range':[70,100],'color':'#e74c3c'}
                ]
            }
        ))
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

    with g2:
        st.metric("🎯 Risk Score", f"{risk:.1f}%")
        st.metric("💚 Health Score", f"{health:.1f}/100")

        if bmi < 18.5:
            st.warning("Underweight")
        elif bmi < 25:
            st.success("Healthy BMI")
        elif bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Obese")

    if pred == 1:
        st.markdown(f"<div class='result-bad'>⚠️ HIGH RISK OF DIABETES<br>{risk:.1f}%</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-good'>✅ LOW RISK OF DIABETES<br>{risk:.1f}%</div>", unsafe_allow_html=True)

    st.subheader("💡 AI Recommendations")
    rec1,rec2,rec3 = st.columns(3)
    rec1.info("🥗 Maintain a balanced diet")
    rec2.info("🏃 Exercise 30 mins daily")
    rec3.info("💧 Stay hydrated & monitor glucose")

st.markdown("---")
st.markdown("<center><h4>🩺 Built with Streamlit • Plotly • Scikit-Learn</h4></center>", unsafe_allow_html=True)
