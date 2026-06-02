import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from src.predict import predict_heart_disease

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .metric-card {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .risk-high {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    .risk-low {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    </style>
""",
    unsafe_allow_html=True,
)

col_title_1, col_title_2 = st.columns([3, 1])
with col_title_1:
    st.markdown(
        '<div class="main-header">❤️ Heart Disease Prediction</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subtitle">Advanced AI-Powered Clinical Assessment</div>',
        unsafe_allow_html=True,
    )

with st.sidebar:
    st.markdown("### 📋 Patient Information")

    patient_data = {}

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        patient_data["age"] = st.slider("Age", 20, 100, 50, key="age")
        patient_data["trestbps"] = st.slider("Blood Pressure", 80, 220, 120, key="bp")
        patient_data["chol"] = st.slider("Cholesterol", 100, 600, 200, key="chol")
        patient_data["thalach"] = st.slider("Max Heart Rate", 60, 220, 150, key="hr")

    with col_s2:
        patient_data["sex"] = st.selectbox(
            "Sex",
            [0, 1],
            format_func=lambda x: "👩 Female" if x == 0 else "👨 Male",
            key="sex",
        )
        patient_data["cp"] = st.selectbox("Chest Pain", [0, 1, 2, 3], key="cp")
        patient_data["fbs"] = st.selectbox(
            "Blood Sugar",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="fbs",
        )
        patient_data["exang"] = st.selectbox(
            "Exercise Angina",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="exang",
        )

    st.markdown("---")
    patient_data["restecg"] = st.selectbox("Rest ECG", [0, 1, 2], key="restecg")
    patient_data["oldpeak"] = st.slider("ST Depression", 0.0, 7.0, 1.0, key="oldpeak")
    patient_data["slope"] = st.selectbox("ST Slope", [0, 1, 2], key="slope")
    patient_data["ca"] = st.selectbox("Major Vessels", [0, 1, 2, 3, 4], key="ca")
    patient_data["thal"] = st.selectbox("Thalassemia", [0, 1, 2, 3], key="thal")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👤 Age", f"{patient_data['age']} yrs", delta=None)

with col2:
    st.metric("🩸 Cholesterol", f"{patient_data['chol']} mg/dL", delta=None)

with col3:
    st.metric("💓 Heart Rate", f"{patient_data['thalach']} bpm", delta=None)

with col4:
    st.metric("🔴 Blood Pressure", f"{patient_data['trestbps']} mmHg", delta=None)

st.markdown("---")

left_col, center_col, right_col = st.columns([1, 2, 1])

with center_col:
    prediction_button = st.button(
        "🔍 Analyze Patient Risk",
        use_container_width=True,
        type="primary",
        key="predict",
    )

if prediction_button:
    with st.spinner("🏥 Analyzing patient data..."):
        prediction, probability = predict_heart_disease(patient_data)

    st.markdown("---")

    result_col1, result_col2 = st.columns([1.5, 1])

    with result_col1:
        if prediction == 1:
            st.markdown(
                f'<div class="metric-card risk-high" style="padding: 2rem; font-size: 1.5rem; font-weight: bold;">⚠️ HIGH RISK DETECTED</div>',
                unsafe_allow_html=True,
            )
            risk_msg = "High risk of heart disease detected. Immediate medical consultation recommended."
            st.error(risk_msg)
        else:
            st.markdown(
                f'<div class="metric-card risk-low" style="padding: 2rem; font-size: 1.5rem; font-weight: bold;">✅ LOW RISK</div>',
                unsafe_allow_html=True,
            )
            risk_msg = (
                "Low risk of heart disease. Continue healthy lifestyle practices."
            )
            st.success(risk_msg)

    with result_col2:
        if probability is not None:
            st.metric("Risk Score", f"{probability:.1%}", delta=None)

    st.markdown("---")

    viz_col1, viz_col2 = st.columns(2)

    with viz_col1:
        st.subheader("📊 Key Metrics Comparison")
        metrics_data = pd.DataFrame(
            {
                "Metric": ["Blood Pressure", "Cholesterol", "Heart Rate"],
                "Value": [
                    patient_data["trestbps"],
                    patient_data["chol"],
                    patient_data["thalach"],
                ],
                "Normal Range": [120, 200, 100],
            }
        )

        fig_bar = go.Figure()
        fig_bar.add_trace(
            go.Bar(
                x=metrics_data["Metric"],
                y=metrics_data["Value"],
                name="Current Value",
                marker_color="rgba(102, 126, 234, 0.8)",
            )
        )
        fig_bar.add_trace(
            go.Bar(
                x=metrics_data["Metric"],
                y=metrics_data["Normal Range"],
                name="Normal Range",
                marker_color="rgba(79, 172, 254, 0.5)",
            )
        )

        fig_bar.update_layout(
            barmode="group",
            height=400,
            hovermode="x unified",
            showlegend=True,
            plot_bgcolor="rgba(240, 240, 250, 0.5)",
            margin=dict(l=20, r=20, t=20, b=20),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with viz_col2:
        st.subheader("⚡ Risk Indicators")

        risk_factors = {
            "Age Factor": min(patient_data["age"] / 100 * 100, 100),
            "BP Factor": min(patient_data["trestbps"] / 220 * 100, 100),
            "Cholesterol": min(patient_data["chol"] / 600 * 100, 100),
            "HR Stability": min((220 - patient_data["thalach"]) / 160 * 100, 100),
        }

        fig_gauge = go.Figure(
            data=[
                go.Scatterpolar(
                    r=list(risk_factors.values()),
                    theta=list(risk_factors.keys()),
                    fill="toself",
                    marker_color="rgba(102, 126, 234, 0.6)",
                    line_color="rgba(102, 126, 234, 1)",
                )
            ]
        )

        fig_gauge.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            height=400,
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20),
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

st.markdown("---")

info_col1, info_col2, info_col3 = st.columns(3)

with info_col1:
    st.markdown("""
        **📚 Model Performance**
        
        • Accuracy: **80.33%**
        • Precision: **79.8%**
        • F1-Score: **0.82**
    """)

with info_col2:
    st.markdown("""
        **📊 Dataset**
        
        • Total Patients: **1,025**
        • Features: **13**
        • Training Set: **80%**
    """)

with info_col3:
    st.markdown("""
        **🤖 Algorithms Used**
        
        • Logistic Regression
        • SVM
        • Random Forest
        • XGBoost
    """)
