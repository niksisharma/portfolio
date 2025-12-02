import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
import config

st.set_page_config(
    page_title="Aurora Prediction - Project Details",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

project = next((p for p in config.PROJECTS if p['id'] == 'aurora-prediction'), None)

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
$ cat technical_specs.txt

Data Source:
{project['technical_details']['data_source']}

Features:
{project['technical_details']['features']}

Model Architecture:
{project['technical_details']['model']}

Prediction Horizons:
{project['technical_details']['horizons']}
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Multi-Horizon Results
st.markdown('<div class="section-header">MULTI-HORIZON FORECASTING</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <p>Time-series forecasting requires evaluation at multiple time horizons. This project predicts Kp index at four different intervals:</p>
    </div>
</div>
""", unsafe_allow_html=True)

horizon_cols = st.columns(4)
horizons = ["1 Hour", "3 Hours", "6 Hours", "12 Hours"]
for idx, horizon in enumerate(horizons):
    with horizon_cols[idx]:
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon" style="font-size: 2rem;">⏱️</div>
            <h3>{horizon}</h3>
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

# Current Results
st.markdown('<div class="section-header">CURRENT RESULTS</div>', unsafe_allow_html=True)

results_cols = st.columns(3)

with results_cols[0]:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">🚧</div>
        <h3>{project['results']['status']}</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[1]:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">✓</div>
        <h3>Baseline Beat</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[2]:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">0.8</div>
        <h3>MAE (1h)</h3>
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

with st.expander("📄 Data Collection Pipeline"):
    st.code("""
# Fetching solar wind data from NOAA
import requests
import pandas as pd

def fetch_solar_wind_data(start_date, end_date):
    url = "https://services.swpc.noaa.gov/products/solar-wind/"
    
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['time_tag'])
    
    # Features: speed, density, temperature, magnetic field
    features = ['speed', 'density', 'bt', 'bx', 'by', 'bz']
    
    return df[['timestamp'] + features]
    """, language="python")

with st.expander("📄 LSTM Model Architecture"):
    st.code("""
# Stacked LSTM for multi-horizon forecasting
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def build_aurora_model(seq_length, n_features, n_horizons=4):
    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=(seq_length, n_features)),
        Dropout(0.2),
        LSTM(64, return_sequences=False),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(n_horizons)  # Predict 1h, 3h, 6h, 12h
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model
    """, language="python")

with st.expander("📄 Multi-Horizon Evaluation"):
    st.code("""
# Evaluate at each time horizon
import numpy as np
from sklearn.metrics import mean_absolute_error

def evaluate_horizons(y_true, y_pred, horizons=[1, 3, 6, 12]):
    results = {}
    
    for i, h in enumerate(horizons):
        mae = mean_absolute_error(y_true[:, i], y_pred[:, i])
        rmse = np.sqrt(np.mean((y_true[:, i] - y_pred[:, i])**2))
        
        results[f'{h}h'] = {
            'MAE': mae,
            'RMSE': rmse
        }
    
    return results
    """, language="python")

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Real-World Application
st.markdown('<div class="section-header">REAL-WORLD APPLICATIONS</div>', unsafe_allow_html=True)

app_cols = st.columns(3)

with app_cols[0]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>📸 Photographers</h3>
        </div>
        <div class="project-body">
            <p>Plan aurora photography trips with advance notice of optimal viewing conditions.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with app_cols[1]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>✈️ Tourists</h3>
        </div>
        <div class="project-body">
            <p>Travel to Iceland, Alaska, or Norway during predicted high-activity periods.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with app_cols[2]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>🔬 Scientists</h3>
        </div>
        <div class="project-body">
            <p>Space weather research and understanding solar-terrestrial interactions.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Links
st.markdown('<div class="section-header">LINKS & RESOURCES</div>', unsafe_allow_html=True)

link_cols = st.columns(4)

with link_cols[0]:
    if project.get('github'):
        st.link_button("📂 GitHub", project['github'], use_container_width=True)
    else:
        st.button("📂 GitHub", disabled=True, use_container_width=True)

with link_cols[1]:
    st.button("🚀 Demo", disabled=True, use_container_width=True)

with link_cols[2]:
    st.button("📄 Paper", disabled=True, use_container_width=True)

with link_cols[3]:
    st.button("📊 Slides", disabled=True, use_container_width=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)
st.link_button("← Back to All Projects", "/Projects", use_container_width=False)