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
    <div class="blog-header">
        <h1>{config.BLOG_POST['title']}</h1>
        <div class="blog-meta">
            <span>📅 {config.BLOG_POST['date']}</span>
            <span>⏱️ {config.BLOG_POST['read_time']}</span>
            <span>📝 ~3000 words</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# # Table of Contents
# st.markdown("""
# <div style="background: var(--bg-light-gray); border-left: 4px solid var(--primary-sky); padding: 1.5rem; border-radius: var(--radius-md); margin-bottom: 2rem;">
#     <h3 style="margin-bottom: 1rem;">Table of Contents</h3>
#     <div class="blog-content" style="font-size: 0.95rem;">
# """, unsafe_allow_html=True)

# for idx, section in enumerate(config.BLOG_POST['sections'], 1):
#     st.markdown(f"{idx}. {section['heading']}")

# st.markdown("""
#     </div>
# </div>
# """, unsafe_allow_html=True)

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

# Instructions for adding reflection
st.markdown("""
<div class="card" style="max-width: 900px; margin: 2rem auto; background: var(--primary-sky-light);">
    <div class="card-header">
        <h3>📝 How to Add Your Reflection</h3>
    </div>
    <div class="card-body">
        <p><strong>To replace this placeholder with your 3000-word reflection:</strong></p>
        <ol style="line-height: 1.8; color: var(--text-secondary);">
            <li>Open <code>config.py</code></li>
            <li>Find the <code>BLOG_POST</code> dictionary (around line 352)</li>
            <li>Replace the placeholder content with your reflection text</li>
            <li>Structure it into sections (e.g., Introduction, Learning Outcomes, Projects, Favorite Class, Conclusion)</li>
            <li>Each section should have a "heading" and "content" field</li>
        </ol>
        <p style="margin-top: 1rem;"><strong>Your reflection should cover:</strong></p>
        <ul style="line-height: 1.8; color: var(--text-secondary);">
            <li>What you expected vs. what you learned</li>
            <li>How you achieved each learning outcome (with project examples)</li>
            <li>Description of 3 key projects and their contributions to your education</li>
            <li>Internship, iConsult, or outside projects (if applicable)</li>
            <li>Your favorite class and why</li>
            <li>Best parts of the program and biggest surprises</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

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
