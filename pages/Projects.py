import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import config

st.set_page_config(
    page_title=f"Projects - {config.PERSONAL_INFO['name']}",
    page_icon="💻",
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

# Page Header
st.markdown("""
<div style="text-align: center; margin: 3rem 0 2rem 0;">
    <h1>Project Portfolio</h1>
    <p style="font-size: 1.2rem; color: var(--text-secondary); margin-top: 1rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        A collection of data science and machine learning projects demonstrating end-to-end system development, from data collection to deployment.
    </p>
</div>
""", unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Project Grid
for project in config.PROJECTS:
    # Tech stack tags
    tech_tags_html = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack'][:6]])

    # Learning Outcomes badges
    los_badges = ''.join([f'<span class="lo-badge">{lo}</span>' for lo in project['learning_outcomes']])

    # Project Card with side-by-side layout using columns
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    content_col, image_col = st.columns([2, 1])

    with content_col:
        st.markdown(f"""
        <div class="project-header">
            <h3>{project['title']}</h3>
            <div class="project-meta">{project['date']} | {project['status']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="project-body">
            <p style="font-size: 1.15rem; font-weight: 600; color: var(--text-primary); margin-bottom: 0.75rem;">{project['subtitle']}</p>
            <p style="font-size: 1.05rem; line-height: 1.8;">{project['short_description']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Tech tags
        st.markdown('<div class="tech-label" style="margin-top: 1.5rem;">Technologies</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tech-tags">{tech_tags_html}</div>', unsafe_allow_html=True)

        # Learning Outcomes
        st.markdown('<div class="tech-label" style="margin-top: 1.5rem;">Learning Outcomes</div>', unsafe_allow_html=True)
        st.markdown(f'<div>{los_badges}</div>', unsafe_allow_html=True)

    with image_col:
        st.markdown("""
        <div class="project-image-container" style="width: 100%; aspect-ratio: 4/3; min-height: 220px; border-radius: 12px; overflow: hidden;">
            <div class="project-placeholder" style="font-size: 1rem;">Project Screenshot</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Buttons
    button_cols = st.columns([1, 1, 1, 2])

    with button_cols[0]:
        if project.get('id'):
            project_page_name = ''.join(word.capitalize() for word in project['id'].split('-'))
            st.link_button("View Details", f"/projects/{project_page_name}", use_container_width=True)

    with button_cols[1]:
        if project.get('github'):
            st.link_button("GitHub", project['github'], use_container_width=True)
        else:
            st.markdown('<div style="height: 38px;"></div>', unsafe_allow_html=True)

    with button_cols[2]:
        if project.get('demo'):
            st.link_button("Demo", project['demo'], use_container_width=True)
        else:
            st.markdown('<div style="height: 38px;"></div>', unsafe_allow_html=True)

    st.markdown('<div style="margin-bottom: 2rem;"></div>', unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Technology Stats
st.markdown('<div class="section-header">Technology Usage</div>', unsafe_allow_html=True)

# Count technology usage
tech_count = {}
for project in config.PROJECTS:
    for tech in project['tech_stack']:
        tech_count[tech] = tech_count.get(tech, 0) + 1

# Sort by usage
sorted_tech = sorted(tech_count.items(), key=lambda x: x[1], reverse=True)

st.markdown('<div class="card"><div class="card-body">', unsafe_allow_html=True)

tech_html = '<div class="tech-tags" style="margin: 0;">'
for tech, count in sorted_tech[:12]:  # Show top 12
    tech_html += f'<span class="tech-tag">{tech} ({count})</span>'
tech_html += '</div>'

st.markdown(tech_html, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="card" style="background: linear-gradient(135deg, var(--primary-sky-light), var(--accent-rose-light));">
    <div class="card-body" style="text-align: center;">
        <h3 style="margin-bottom: 1rem;">Want to Learn More?</h3>
        <p>Read my Overview for learning outcome explanations, or watch my Video presentation for a program summary.</p>
    </div>
</div>
""", unsafe_allow_html=True)

link_cols = st.columns(3)
with link_cols[0]:
    st.link_button("📋 View Overview", "/Overview", use_container_width=True)
with link_cols[1]:
    st.link_button("📝 Read Reflection", "/Reflection", use_container_width=True)
with link_cols[2]:
    st.link_button("🎥 Watch Video", "/Video", use_container_width=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 4rem; padding: 2rem;">
    <div class="divider" style="margin-bottom: 2rem;"></div>
    <p style="color: var(--text-tertiary); font-size: 0.9rem;">
        MS Applied Data Science Portfolio | Syracuse University | © 2025 {config.PERSONAL_INFO['name']}
    </p>
</div>
""", unsafe_allow_html=True)
