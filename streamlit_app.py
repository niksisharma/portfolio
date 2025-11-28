import streamlit as st
from pathlib import Path
import config

# Page config
st.set_page_config(
    page_title=f"{config.PERSONAL_INFO['name']} - Portfolio",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    css_file = Path(__file__).parent / "assets" / "style.css"
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

# Hero Section with Window Style
st.markdown("""
<div class="hero-window">
    <div class="window-titlebar">
        <div class="window-title">WELCOME.SYS</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>{name}</h1>
        <div class="subtitle">{title}</div>
        <p>{tagline}</p>
        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-label">Projects:</span>
                <span class="stat-value">{projects}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Completed:</span>
                <span class="stat-value">{completed}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">GPA:</span>
                <span class="stat-value">{gpa}</span>
            </div>
        </div>
    </div>
</div>
""".format(
    name=config.PERSONAL_INFO['name'],
    title=config.PERSONAL_INFO['title'],
    tagline=config.PERSONAL_INFO['tagline'],
), unsafe_allow_html=True)

# Pixel Divider
st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Skills Section - NO PROFICIENCY BARS
st.markdown('<div class="section-header">TECHNICAL SKILLS</div>', unsafe_allow_html=True)

# Display skills in 4 columns
cols = st.columns(4)
for idx, skill in enumerate(config.SKILLS):
    with cols[idx % 4]:
        st.markdown(f"""
        <div class="skill-card">
            <h3>{skill['name']}</h3>
        </div>
        """, unsafe_allow_html=True)

# Pixel Divider
st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Research Interests
st.markdown('<div class="section-header">RESEARCH INTERESTS</div>', unsafe_allow_html=True)

cols = st.columns(3)
for idx, interest in enumerate(config.INTERESTS):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon">{interest['icon']}</div>
            <h3>{interest['name']}</h3>
        </div>
        """, unsafe_allow_html=True)

# Pixel Divider
st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Featured Projects
st.markdown('<div class="section-header">FEATURED PROJECTS</div>', unsafe_allow_html=True)

# # Get featured projects
# featured_projects = [p for p in config.PROJECTS if p.get('featured', False)]

# for project in featured_projects[:3]:  
#     # Tech stack tags HTML
#     tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])
    
#     st.markdown(f"""
#     <div class="project-display">
#         <div class="project-image">
#             <div class="project-placeholder">IMAGE</div>
#         </div>
#         <div class="project-info">
#             <div class="project-header">
#                 <h3>{project['title']}</h3>
#                 <div class="project-meta">{project['date']} | {project['status']}</div>
#             </div>
#             <div class="project-body">
#                 <p>{project['description']}</p>
#                 <div class="tech-label">Built With:</div>
#                 <div class="tech-tags">
#                     {tech_tags}
#                 </div>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # View Project button
#     if project.get('github') or project.get('demo'):
#         col1, col2, col3 = st.columns([1, 1, 4])
#         with col1:
#             if project.get('github'):
#                 st.link_button("GitHub →", project['github'], use_container_width=True)
#         with col2:
#             if project.get('demo'):
#                 st.link_button("Demo →", project['demo'], use_container_width=True)

# # Pixel Divider
# st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Quick Links
st.markdown('<div class="section-header">CONNECT</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if config.PERSONAL_INFO.get('email'):
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon">📧</div>
            <h3>Email</h3>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Send Email", f"mailto:{config.PERSONAL_INFO['email']}", use_container_width=True)

with col2:
    if config.PERSONAL_INFO.get('linkedin'):
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon">💼</div>
            <h3>LinkedIn</h3>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Connect", config.PERSONAL_INFO['linkedin'], use_container_width=True)

with col3:
    if config.PERSONAL_INFO.get('github'):
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon">💻</div>
            <h3>GitHub</h3>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Follow", config.PERSONAL_INFO['github'], use_container_width=True)

with col4:
    st.markdown(f"""
    <div class="interest-item">
        <div class="interest-icon">📄</div>
        <h3>Resume</h3>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Download", "#", use_container_width=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding: 2rem; border-top: 2px dashed var(--primary-teal);">
    <p style="color: var(--text-light); font-size: 0.85rem;">
        Built with Streamlit | © 2025 {name}
    </p>
</div>
""".format(name=config.PERSONAL_INFO['name']), unsafe_allow_html=True)