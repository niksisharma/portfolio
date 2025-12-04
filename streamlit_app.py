import streamlit as st
from pathlib import Path
import config

# Page config
st.set_page_config(
    page_title=f"{config.PERSONAL_INFO['name']} - Portfolio",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    css_file = Path(__file__).parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Modern Top Navigation Bar
st.markdown(f"""
<div class="top-nav">
    <div class="nav-container">
        <div class="nav-brand">{config.PERSONAL_INFO['name']}</div>
        <div class="nav-links">
            <a class="nav-link" href="/" target="_self">Home</a>
            <a class="nav-link" href="/Overview" target="_self">Overview</a>
            <a class="nav-link" href="/Projects" target="_self">Projects</a>
            <a class="nav-link" href="/Reflection" target="_self">Reflection</a>
            <a class="nav-link" href="/Video" target="_self">Video</a>
            <a class="nav-link" href="/About" target="_self">About</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section - Modern Landing
st.markdown(f"""
<div class="hero-section">
    <h1>{config.PERSONAL_INFO['name']}</h1>
    <div class="subtitle">{config.PERSONAL_INFO['title']}</div>
    <p style="font-size: 1.1rem; margin-top: 1rem;">{config.PERSONAL_INFO['tagline']}</p>
</div>
""", unsafe_allow_html=True)

# Navigation Cards - Quick Access
st.markdown('<div class="section-header">Portfolio Sections</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>📋 Overview</h3>
        </div>
        <div class="card-body">
            <p>Program learning outcomes, project summaries, and achievement explanations</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Overview →", "/Overview", use_container_width=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>💻 Projects</h3>
        </div>
        <div class="card-body">
            <p>Detailed descriptions of 6 data science projects from the MS program</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Projects →", "/Projects", use_container_width=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>📝 Reflection</h3>
        </div>
        <div class="card-body">
            <p>In-depth reflection on the MS Applied Data Science program experience</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Reflection →", "/Reflection", use_container_width=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Technical Skills Section
st.markdown('<div class="section-header">Technical Skills</div>', unsafe_allow_html=True)

cols = st.columns(4)
for idx, skill in enumerate(config.SKILLS):
    with cols[idx % 4]:
        st.markdown(f"""
        <div class="skill-card">
            <h3>{skill['name']}</h3>
            <div class="skill-level">{skill['level']}</div>
        </div>
        """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Research Interests
st.markdown('<div class="section-header">Research Interests</div>', unsafe_allow_html=True)

cols = st.columns(3)
for idx, interest in enumerate(config.INTERESTS):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon">{interest['icon']}</div>
            <h3>{interest['name']}</h3>
        </div>
        """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Quick Stats
st.markdown('<div class="section-header">At a Glance</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">6</div>
        <div class="stat-label">Projects Completed</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">6</div>
        <div class="stat-label">Learning Outcomes</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">{len(config.SKILLS)}</div>
        <div class="stat-label">Technical Skills</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">3.88</div>
        <div class="stat-label">GPA</div>
    </div>
    """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Connect Section
st.markdown('<div class="section-header">Connect</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">📧</div>
        <h3>Email</h3>
    </div>
    """, unsafe_allow_html=True)
    if config.PERSONAL_INFO.get('email'):
        st.link_button("Send Email", f"mailto:{config.PERSONAL_INFO['email']}", use_container_width=True)

with col2:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">💼</div>
        <h3>LinkedIn</h3>
    </div>
    """, unsafe_allow_html=True)
    if config.PERSONAL_INFO.get('linkedin'):
        st.link_button("Connect", config.PERSONAL_INFO['linkedin'], use_container_width=True)

with col3:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">💻</div>
        <h3>GitHub</h3>
    </div>
    """, unsafe_allow_html=True)
    if config.PERSONAL_INFO.get('github'):
        st.link_button("Follow", config.PERSONAL_INFO['github'], use_container_width=True)

with col4:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">🎥</div>
        <h3>Video</h3>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Watch Presentation", "/Video", use_container_width=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 4rem; padding: 2rem;">
    <div class="divider" style="margin-bottom: 2rem;"></div>
    <p style="color: var(--text-tertiary); font-size: 0.9rem;">
        MS Applied Data Science Portfolio | Syracuse University | © 2025 {config.PERSONAL_INFO['name']}
    </p>
</div>
""", unsafe_allow_html=True)
