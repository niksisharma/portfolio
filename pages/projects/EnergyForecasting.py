import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
import config

st.set_page_config(
    page_title="Energy Forecasting - Project Details",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

project = next((p for p in config.PROJECTS if p['id'] == 'energy-forecasting'), None)

# Top Navigation
st.markdown(f"""
<div class="top-nav">
    <div class="nav-container">
        <div class="nav-brand">{config.PERSONAL_INFO['name'].upper()}.EXE</div>
        <div class="nav-links">
            <a class="nav-link" href="/" target="_self">Home</a>
            <a class="nav-link" href="/Overview" target="_self">Overview</a>
            <a class="nav-link" href="/Projects" target="_self">Projects</a>
            <a class="nav-link" href="/Reflection" target="_self">Reflection</a>
            <a class="nav-link" href="/About" target="_self">About</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Project Header
st.markdown(f"""
<div class="hero-window">
    <div class="window-titlebar">
        <div class="window-title">PROJECT.EXE - {project['title'].upper()}</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>{project['title']}</h1>
        <div class="subtitle">{project['subtitle']}</div>
        <p>{project['short_description']}</p>
        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-label">Status:</span>
                <span class="stat-value">{project['status']}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Timeline:</span>
                <span class="stat-value">{project['date']}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Course:</span>
                <span class="stat-value">{project.get('course', 'Independent')}</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Learning Outcomes
st.markdown('<div class="section-header">LEARNING OUTCOMES ACHIEVED</div>', unsafe_allow_html=True)

lo_cols = st.columns(len(project['learning_outcomes']))
for idx, lo_id in enumerate(project['learning_outcomes']):
    lo = config.LEARNING_OUTCOMES[lo_id]
    with lo_cols[idx]:
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon" style="font-size: 3rem;">{lo['number']}</div>
            <h3>LO{lo['number']}</h3>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="project-info" style="margin-top: 2rem;">
    <div class="project-body">
        <h3 style="color: var(--primary-teal);">How This Project Demonstrates Learning Outcomes:</h3>
    </div>
</div>
""", unsafe_allow_html=True)

for lo_id in project['learning_outcomes']:
    lo = config.LEARNING_OUTCOMES[lo_id]
    explanation = project['lo_explanations'][lo_id]
    
    st.markdown(f"""
    <div class="skill-card" style="text-align: left; margin-bottom: 1rem;">
        <h3 style="margin-bottom: 0.5rem;">LO{lo['number']}: {lo['title']}</h3>
        <div class="skill-level" style="color: var(--text-gray); font-size: 0.9rem; margin-bottom: 0.5rem;">
            {lo['description']}
        </div>
        <p style="color: var(--text-dark); margin-top: 0.5rem;">
            ✓ {explanation}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Problem & Solution
st.markdown('<div class="section-header">PROBLEM & SOLUTION</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="project-info">
        <div class="project-header">
            <h3>Problem Statement</h3>
        </div>
        <div class="project-body">
            <p>{project['problem_statement']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="project-info">
        <div class="project-header">
            <h3>Solution Approach</h3>
        </div>
        <div class="project-body">
            <p>{project['solution']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Technical Details
st.markdown('<div class="section-header">TECHNICAL IMPLEMENTATION</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="terminal">
$ cat system_design.txt

Data: {project['technical_details']['data']}
Features: {project['technical_details']['features']}
Model: {project['technical_details']['model']}
Interpretability: {project['technical_details']['interpretability']}
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Tech Stack
st.markdown('<div class="section-header">TECHNOLOGIES USED</div>', unsafe_allow_html=True)

tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])

st.markdown(f"""
<div class="project-info">
    <div class="project-body">
        <div class="tech-tags">
            {tech_tags}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Results
st.markdown('<div class="section-header">RESULTS & SUSTAINABILITY IMPACT</div>', unsafe_allow_html=True)

results_cols = st.columns(3)

with results_cols[0]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">15%</div>
        <h3>MAPE</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[1]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">-12%</div>
        <h3>Energy Waste</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[2]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">🏢</div>
        <h3>Per-Building Optim.</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Ethical Considerations
st.markdown('<div class="section-header">ETHICAL & ENVIRONMENTAL CONSIDERATIONS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <h3 style="color: var(--primary-teal); margin-bottom: 1rem;">Sustainability Ethics (LO6)</h3>
        <p>This project demonstrates applying ethics in data science through environmental responsibility. Key considerations:</p>
    </div>
</div>
""", unsafe_allow_html=True)

ethics_cols = st.columns(3)

with ethics_cols[0]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Environmental Impact</h3>
        <p style="color: var(--text-dark);">Reducing energy waste directly addresses climate change and sustainability</p>
    </div>
    """, unsafe_allow_html=True)

with ethics_cols[1]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Transparency</h3>
        <p style="color: var(--text-dark);">SHAP values make model decisions explainable to facilities management</p>
    </div>
    """, unsafe_allow_html=True)

with ethics_cols[2]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Fairness</h3>
        <p style="color: var(--text-dark);">Ensuring energy savings don't compromise occupant comfort or access</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Challenges
st.markdown('<div class="section-header">CHALLENGES & LEARNINGS</div>', unsafe_allow_html=True)

for idx, challenge in enumerate(project['challenges'], 1):
    st.markdown(f"""
    <div class="skill-card" style="text-align: left; margin-bottom: 1rem;">
        <h3 style="margin-bottom: 0.5rem;">Challenge {idx}</h3>
        <p style="color: var(--text-dark);">{challenge}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Code Samples
st.markdown('<div class="section-header">CODE SAMPLES</div>', unsafe_allow_html=True)

with st.expander("📄 Feature Engineering"):
    st.code("""
# Creating features for energy prediction
import pandas as pd
import numpy as np

def engineer_energy_features(df, weather_df, occupancy_df):
    # Merge data sources
    df = df.merge(weather_df, on='timestamp')
    df = df.merge(occupancy_df, on='timestamp')
    
    # Time features
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6])
    df['is_holiday'] = df['timestamp'].dt.date.isin(holidays)
    
    # Lag features
    for lag in [1, 24, 168]:  # 1h, 1day, 1week
        df[f'energy_lag_{lag}'] = df['energy'].shift(lag)
    
    # Weather interaction features
    df['temp_diff'] = df['outdoor_temp'] - 70  # Difference from comfort temp
    df['heating_load'] = np.maximum(0, 70 - df['outdoor_temp'])
    df['cooling_load'] = np.maximum(0, df['outdoor_temp'] - 70)
    
    return df
    """, language="python")

with st.expander("📄 XGBoost Model Training"):
    st.code("""
# Training XGBoost with temporal cross-validation
import xgboost as xgb
from sklearn.model_selection import TimeSeriesSplit

def train_energy_model(X, y):
    # Temporal cross-validation (important for time-series!)
    tscv = TimeSeriesSplit(n_splits=5)
    
    params = {
        'objective': 'reg:squarederror',
        'max_depth': 6,
        'learning_rate': 0.05,
        'n_estimators': 500,
        'subsample': 0.8,
        'colsample_bytree': 0.8
    }
    
    model = xgb.XGBRegressor(**params)
    
    for train_idx, val_idx in tscv.split(X):
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
        
        model.fit(X_train, y_train, 
                 eval_set=[(X_val, y_val)],
                 early_stopping_rounds=50,
                 verbose=False)
    
    return model
    """, language="python")

with st.expander("📄 SHAP Interpretability"):
    st.code("""
# Explaining predictions with SHAP
import shap

def explain_predictions(model, X):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': np.abs(shap_values).mean(axis=0)
    }).sort_values('importance', ascending=False)
    
    print("Top 5 Features:")
    print(feature_importance.head())
    
    # Visualize
    shap.summary_plot(shap_values, X)
    
    # For facilities managers: which features drive high consumption?
    high_energy_days = X[y > y.quantile(0.9)]
    shap.force_plot(explainer.expected_value, 
                   shap_values[high_energy_days.index], 
                   high_energy_days)
    
    return feature_importance
    """, language="python")

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Links
st.markdown('<div class="section-header">LINKS & RESOURCES</div>', unsafe_allow_html=True)

link_cols = st.columns(4)
for i in range(4):
    with link_cols[i]:
        st.button(["📂 GitHub", "📊 Dashboard", "📄 Report", "🎥 Presentation"][i], 
                 disabled=True, use_container_width=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)
st.link_button("← Back to All Projects", "/Projects", use_container_width=False)