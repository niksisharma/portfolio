import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import config

# Page config
st.set_page_config(
    page_title=f"Video Presentation - {config.PERSONAL_INFO['name']}",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    css_file = Path(__file__).parent.parent / "assets" / "style.css"
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

# Page Header
st.markdown("""
<div style="text-align: center; margin: 3rem 0 2rem 0;">
    <h1>Video Presentation</h1>
    <p style="font-size: 1.2rem; color: var(--text-secondary); margin-top: 1rem;">
        A 1-2 minute summary of my MS Applied Data Science program experience
    </p>
</div>
""", unsafe_allow_html=True)

# Video Container
st.markdown("""
<div class="video-container">
    <div class="video-placeholder">
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🎥</div>
            <div>Video presentation coming soon</div>
            <div style="font-size: 0.9rem; color: var(--text-muted); margin-top: 0.5rem;">
                YouTube embed will appear here
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="max-width: 800px; margin: 2rem auto; padding: 0 2rem;">
    <p style="color: var(--text-tertiary); font-size: 0.95rem; text-align: center; font-style: italic;">
        To add your video: Upload to YouTube, then replace the placeholder above with:<br/>
        <code style="background: var(--bg-light-gray); padding: 0.5rem; border-radius: 6px; display: inline-block; margin-top: 0.5rem;">
        &lt;div class="video-wrapper"&gt;&lt;iframe src="YOUR_YOUTUBE_EMBED_URL"&gt;&lt;/iframe&gt;&lt;/div&gt;
        </code>
    </p>
</div>
""", unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Video Topics Overview
st.markdown('<div class="section-header">Presentation Topics</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>📚 Program Summary</h3>
        </div>
        <div class="card-body">
            <ul style="color: var(--text-secondary); line-height: 1.8;">
                <li>Overall thoughts on the MS Applied Data Science program</li>
                <li>Key learnings and takeaways</li>
                <li>How the program prepared me for data science careers</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>🎯 Learning Outcomes</h3>
        </div>
        <div class="card-body">
            <ul style="color: var(--text-secondary); line-height: 1.8;">
                <li>How I achieved the 6 program learning outcomes</li>
                <li>Highlight of 2-3 key projects</li>
                <li>Skills developed throughout the program</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Quick Links
st.markdown('<div class="section-header">Explore More</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>📋 Overview</h3>
        </div>
        <div class="card-body">
            <p>Read detailed explanations of learning outcomes and project achievements</p>
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
            <p>Explore technical details of all 6 projects from my portfolio</p>
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
            <p>Read my 3000-word reflection on the program experience</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Reflection →", "/Reflection", use_container_width=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 4rem; padding: 2rem;">
    <div class="divider" style="margin-bottom: 2rem;"></div>
    <p style="color: var(--text-tertiary); font-size: 0.9rem;">
        MS Applied Data Science Portfolio | Syracuse University | © 2025 {config.PERSONAL_INFO['name']}
    </p>
</div>
""", unsafe_allow_html=True)
