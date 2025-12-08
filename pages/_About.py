import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import config

st.set_page_config(
    page_title=f"About - {config.PERSONAL_INFO['name']}",
    page_icon="👤",
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
    <h1>About Me</h1>
    <p style="font-size: 1.2rem; color: var(--text-secondary); margin-top: 1rem;">
        Learn more about my background, education, and professional experience
    </p>
</div>
""", unsafe_allow_html=True)

# Bio Section with Profile
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="section-header">Biography</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card">
        <div class="card-body">
            {config.ABOUT_ME['bio'].replace(chr(10), '<br><br>')}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="profile-image-placeholder">
        <span>👤</span>
    </div>
    """, unsafe_allow_html=True)

    # Quick Facts
    st.markdown(f"""
    <div class="card" style="margin-top: 1rem;">
        <div class="card-header">
            <h3>Quick Facts</h3>
        </div>
        <div class="card-body">
            <p><strong>📍 Location:</strong> {config.PERSONAL_INFO['location']}</p>
            <p><strong>🎓 Degree:</strong> MS Applied Data Science</p>
            <p><strong>📊 GPA:</strong> 3.88/4.0</p>
            <p><strong>🚀 Projects:</strong> {len(config.PROJECTS)}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Education
st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

for edu in config.ABOUT_ME['education']:
    st.markdown(f"""
    <div class="card">
        <div class="card-header">
            <h3>{edu['degree']}</h3>
        </div>
        <div class="card-body">
            <p><strong>{edu['school']}</strong> | {edu['location']}</p>
            <p><strong>Graduation:</strong> {edu['date']}</p>
            <p><strong>GPA:</strong> {edu['gpa']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Professional Experience
st.markdown('<div class="section-header">Professional Experience</div>', unsafe_allow_html=True)

for exp in config.ABOUT_ME['experience']:
    st.markdown(f"""
    <div class="card">
        <div class="timeline-item" style="border-left: 3px solid var(--primary-sky); padding-left: 2rem;">
            <div class="timeline-header">
                <h3>{exp['title']}</h3>
            </div>
            <div class="timeline-meta">
                <p><strong>{exp['company']}</strong> | {exp['location']} | {exp['date']}</p>
            </div>
            <div class="card-body">
                <ul style="line-height: 1.8; color: var(--text-secondary);">
    """, unsafe_allow_html=True)

    for item in exp['description']:
        st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)

    st.markdown("""
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Technical Expertise
st.markdown('<div class="section-header">Technical Expertise</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="card-body">
        <p>Throughout my graduate program, I've developed proficiency across a range of technical domains:</p>
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

# Contact Section
st.markdown('<div class="section-header">Get In Touch</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="card" style="background: linear-gradient(135deg, var(--primary-sky-light), var(--accent-sage-light));">
    <div class="card-body" style="text-align: center;">
        <h3>Let's Connect</h3>
        <p style="margin-top: 1rem;">I'm always interested in discussing data science, machine learning, and potential collaboration opportunities.</p>
    </div>
</div>
""", unsafe_allow_html=True)

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
        <div class="interest-icon">🌐</div>
        <h3>Website</h3>
    </div>
    """, unsafe_allow_html=True)
    if config.PERSONAL_INFO.get('website'):
        st.link_button("Visit", config.PERSONAL_INFO['website'], use_container_width=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 4rem; padding: 2rem;">
    <div class="divider" style="margin-bottom: 2rem;"></div>
    <p style="color: var(--text-tertiary); font-size: 0.9rem;">
        MS Applied Data Science Portfolio | Syracuse University | © 2025 {config.PERSONAL_INFO['name']}
    </p>
</div>
""", unsafe_allow_html=True)
