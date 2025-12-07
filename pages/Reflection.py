import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import config

st.set_page_config(
    page_title=f"Reflection - {config.PERSONAL_INFO['name']}",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
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

# Blog Post Container
st.markdown(f"""
<div class="blog-post">
<div class="hero-section" style="background: linear-gradient(135deg, rgba(168, 216, 234, 0.3) 0%, rgba(184, 212, 186, 0.3) 50%, rgba(245, 183, 177, 0.2) 100%); padding: 4rem 2rem; border-radius: 16px; margin-bottom: 2rem;">
        <h1 style="color: #212121;">{config.BLOG_POST['title']}</h1>
    </div>
""", unsafe_allow_html=True)

# Blog Content Sections
for idx, section in enumerate(config.BLOG_POST['sections'], 1):
    st.markdown(f"""
    <div class="blog-content">
        <h2>{idx}. {section['heading']}</h2>
    """, unsafe_allow_html=True)

    # Split content into paragraphs for better formatting
    paragraphs = section['content'].strip().split('\n\n')
    for para in paragraphs:
        if para.strip():
            st.markdown(f"<p>{para.strip()}</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Close blog post container
st.markdown("</div>", unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Related Links
st.markdown('<div class="section-header" style="text-align: center; margin-top: 3rem;">Explore More</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>📋 Overview</h3>
        </div>
        <div class="card-body">
            <p>Read about how I achieved the program learning outcomes</p>
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
            <p>Explore detailed technical descriptions of all projects</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Projects →", "/Projects", use_container_width=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3>🎥 Video</h3>
        </div>
        <div class="card-body">
            <p>Watch my program summary presentation</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Watch Video →", "/Video", use_container_width=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 4rem; padding: 2rem;">
    <div class="divider" style="margin-bottom: 2rem;"></div>
    <p style="color: var(--text-tertiary); font-size: 0.9rem;">
        MS Applied Data Science Portfolio | Syracuse University | © 2025 {config.PERSONAL_INFO['name']}
    </p>
</div>
""", unsafe_allow_html=True)
