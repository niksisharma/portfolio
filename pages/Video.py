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
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Page Header
st.markdown("""
<div style="text-align: center; margin: 3rem 0 2rem 0;">
    <h1>Video Presentation</h1>
    <p style="font-size: 1.2rem; color: var(--text-secondary); margin-top: 1rem;">
        A short summary of my MS Applied Data Science program experience
    </p>
</div>
""", unsafe_allow_html=True)

# Video Container
video_embed_url = "https://drive.google.com/file/d/1aFP48rJ1Ea7Zdl4OmMYwrBBuPhcanHHK/preview"

st.markdown(f"""
<div style='position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; border-radius: 8px;'>
    <iframe src="{video_embed_url}"
            style='position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;'
            allow='autoplay; encrypted-media'
            allowfullscreen>
    </iframe>
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
