import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
import config

st.set_page_config(
    page_title="Airbnb Occupancy - Project Details",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

project = next((p for p in config.PROJECTS if p['id'] == 'airbnb-occupancy'), None)

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
$ cat technical_approach.txt

Data Sources:
{project['technical_details']['data_sources']}

Features:
{project['technical_details']['features']}

Models:
{project['technical_details']['models']}

Forecast Horizons:
{project['technical_details']['forecast_horizon']}
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
st.markdown('<div class="section-header">RESULTS & IMPACT</div>', unsafe_allow_html=True)

results_cols = st.columns(3)

with results_cols[0]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">82%</div>
        <h3>Accuracy (30d)</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[1]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">Prophet+LSTM</div>
        <h3>Best Model</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[2]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">+15%</div>
        <h3>Revenue Optimization</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Business Impact
st.markdown('<div class="section-header">BUSINESS APPLICATIONS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <h3 style="color: var(--primary-teal); margin-bottom: 1rem;">Revenue Management Insights</h3>
        <p>This project demonstrates creating actionable business insights from data. Hosts can:</p>
    </div>
</div>
""", unsafe_allow_html=True)

app_cols = st.columns(3)

with app_cols[0]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Dynamic Pricing</h3>
        <p style="color: var(--text-dark);">Adjust prices based on predicted demand at different horizons</p>
    </div>
    """, unsafe_allow_html=True)

with app_cols[1]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Availability Strategy</h3>
        <p style="color: var(--text-dark);">Block/release dates strategically to maximize occupancy</p>
    </div>
    """, unsafe_allow_html=True)

with app_cols[2]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Marketing Timing</h3>
        <p style="color: var(--text-dark);">Promote listings during predicted low-occupancy periods</p>
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
# Creating time-series features for occupancy prediction
import pandas as pd
import numpy as np

def create_time_features(df):
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['is_holiday'] = df['date'].isin(holidays).astype(int)
    
    # Lag features
    for lag in [7, 14, 30]:
        df[f'occupancy_lag_{lag}'] = df['occupancy'].shift(lag)
    
    # Rolling statistics
    df['occupancy_rolling_7d'] = df['occupancy'].rolling(7).mean()
    df['occupancy_rolling_30d'] = df['occupancy'].rolling(30).mean()
    
    return df
    """, language="python")

with st.expander("📄 Prophet Model"):
    st.code("""
# Facebook Prophet for seasonality
from fbprophet import Prophet

def train_prophet_model(df):
    # Prophet requires specific column names
    prophet_df = df[['date', 'occupancy']].rename(
        columns={'date': 'ds', 'occupancy': 'y'}
    )
    
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        seasonality_mode='multiplicative'
    )
    
    # Add external regressors
    model.add_regressor('price')
    model.add_regressor('local_events')
    
    model.fit(prophet_df)
    return model
    """, language="python")

with st.expander("📄 Ensemble Prediction"):
    st.code("""
# Combining ARIMA, Prophet, and LSTM
def ensemble_predict(date, features):
    # Get predictions from each model
    arima_pred = arima_model.forecast(steps=30)
    prophet_pred = prophet_model.predict(future_df)['yhat'].values
    lstm_pred = lstm_model.predict(features)
    
    # Weighted average based on validation performance
    weights = {
        'arima': 0.2,
        'prophet': 0.4,
        'lstm': 0.4
    }
    
    ensemble = (
        weights['arima'] * arima_pred +
        weights['prophet'] * prophet_pred +
        weights['lstm'] * lstm_pred
    )
    
    return ensemble
    """, language="python")

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Links
st.markdown('<div class="section-header">LINKS & RESOURCES</div>', unsafe_allow_html=True)

link_cols = st.columns(4)
for i in range(4):
    with link_cols[i]:
        st.button(["📂 GitHub", "🚀 Demo", "📄 Report", "📊 Slides"][i], 
                 disabled=True, use_container_width=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)
st.link_button("← Back to All Projects", "/Projects", use_container_width=False)9-