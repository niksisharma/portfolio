import streamlit as st
from pathlib import Path
import config

st.set_page_config(
    page_title="Overview - Portfolio",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
def load_css():
    css_file = Path(__file__).parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Top Navigation Bar
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

# Page Header
st.markdown("""
<div class="hero-window">
    <div class="window-titlebar">
        <div class="window-title">OVERVIEW.SYS</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>Portfolio Overview</h1>
        <p>A comprehensive overview of my graduate program learning outcomes and project portfolio.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Learning Outcomes Section
st.markdown('<div class="section-header">LEARNING OUTCOMES</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="project-info" style="margin-bottom: 2rem;">
    <div class="project-body">
        {config.LEARNING_OUTCOMES.replace(chr(10), '<br>')}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Projects Overview
st.markdown('<div class="section-header">ALL PROJECTS</div>', unsafe_allow_html=True)

# Stats
col1, col2, col3, col4 = st.columns(4)

completed = len([p for p in config.PROJECTS if p['status'] == 'Completed'])
in_progress = len([p for p in config.PROJECTS if p['status'] == 'In Progress'])

with col1:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">7</div>
        <h3>Total Projects</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">{completed}</div>
        <h3>Completed</h3>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">{in_progress}</div>
        <h3>In Progress</h3>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">3</div>
        <h3>Featured</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Projects Table
st.markdown('<div class="section-header">PROJECT CATALOG</div>', unsafe_allow_html=True)

for project in config.PROJECTS:
    # Create collapsible section for each project
    with st.expander(f"🖥️ {project['title']} - {project['status']}"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**{project['subtitle']}**")
            st.markdown(f"*{project['date']}*")
            st.markdown(project['description'])
            
            # Tech stack
            st.markdown("**Technologies:**")
            tech_badges = " ".join([f"`{tech}`" for tech in project['tech_stack']])
            st.markdown(tech_badges)
        
        with col2:
            st.markdown("**Status**")
            status_color = "#00A9A5" if project['status'] == "Completed" else "#FF6700"
            st.markdown(f"<span style='color: {status_color}; font-weight: bold;'>{project['status']}</span>", unsafe_allow_html=True)
            
            if project.get('github'):
                st.link_button("View on GitHub", project['github'], use_container_width=True)
            
            if project.get('demo'):
                st.link_button("Live Demo", project['demo'], use_container_width=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Skills Matrix - NO PROFICIENCY BARS
st.markdown('<div class="section-header">SKILLS MATRIX</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <p>Below is a comprehensive overview of my technical skills developed through coursework and projects:</p>
    </div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(4)

for idx, skill in enumerate(config.SKILLS):
    with cols[idx % 4]:
        st.markdown(f"""
        <div class="skill-card">
            <h3>{skill['name']}</h3>
            <div class="skill-level">{skill['level']}</div>
        </div>
        """, unsafe_allow_html=True)