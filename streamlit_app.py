"""
Portfolio Home Page
Main entry point for the portfolio website
"""
import streamlit as st
from pathlib import Path
import sys

# Add utils to path
sys.path.append(str(Path(__file__).parent))
from utils.helpers import *
import config

# Page configuration
set_page_config(page_title=f"{config.PERSONAL_INFO['name']} - Portfolio", page_icon="🏠")
load_css()

# Hero Section
st.markdown(f"""
<div class="hero">
    <h1>{config.PERSONAL_INFO['name']}</h1>
    <p style="font-size: 1.5rem; color: {config.THEME['primary']}; font-weight: 600;">
        {config.PERSONAL_INFO['tagline']}
    </p>
    <p style="font-size: 1.1rem; color: {config.THEME['text']}; max-width: 700px; margin: 1.5rem auto;">
        {config.PERSONAL_INFO['title']} | {config.PROGRAM_INFO['university']}
    </p>
</div>
""", unsafe_allow_html=True)

# Profile image (if provided)
if config.PERSONAL_INFO["profile_image"]:
    try:
        profile_path = Path(__file__).parent / "assets" / "images" / config.PERSONAL_INFO["profile_image"]
        if profile_path.exists():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(str(profile_path), width=250, output_format="auto")
    except:
        pass

# Social Links
render_social_links()

st.markdown("<hr>", unsafe_allow_html=True)

# About Section
st.markdown("<h2>👋 About Me</h2>", unsafe_allow_html=True)
st.markdown(config.PERSONAL_INFO['bio'])

st.markdown("<hr>", unsafe_allow_html=True)

# Quick Stats
st.markdown("<h2>📊 At a Glance</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_metric("Projects", str(len(config.PROJECTS)), "🚀")

with col2:
    completed_projects = len([p for p in config.PROJECTS if p["status"] == "Completed"])
    render_metric("Completed", str(completed_projects), "✅")

with col3:
    render_metric("GPA", config.PROGRAM_INFO["gpa"], "🎓")

with col4:
    publications = 1  # Update based on your actual publications
    render_metric("Publications", str(publications), "📄")

st.markdown("<hr>", unsafe_allow_html=True)

# Featured Projects
st.markdown("<h2>⭐ Featured Projects</h2>", unsafe_allow_html=True)

featured_projects = [p for p in config.PROJECTS if p.get("featured", False)]

if featured_projects:
    for project in featured_projects:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            render_project_card(project)
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"View Details", key=f"btn_{project['id']}"):
                st.info(f"Navigate to Projects page and select {project['title']}")
            
            if project["github"]:
                st.markdown(f"[GitHub →]({project['github']})")
else:
    st.info("Featured projects will appear here once configured.")

st.markdown("<hr>", unsafe_allow_html=True)

# Research Interests
st.markdown("<h2>🔬 Research Interests</h2>", unsafe_allow_html=True)

interests = [
    "**Machine Learning Systems:** Building scalable, production-ready ML infrastructure",
    "**Responsible AI:** Developing fair, transparent, and human-centered AI systems",
    "**Social Impact Applications:** ML for healthcare, accessibility, and scientific forecasting",
    "**Human-Computer Interaction:** Bridging ML research and real-world deployment",
]

for interest in interests:
    st.markdown(f"- {interest}")

st.markdown("<hr>", unsafe_allow_html=True)

# Call to Action
st.markdown("<h2>📬 Let's Connect</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    I'm currently seeking opportunities in:
    - **PhD Programs** in ML/AI/HCI
    - **Research Positions** in AI systems
    - **ML Engineering** roles with social impact
    """)

with col2:
    st.markdown(f"""
    **Get in touch:**
    - 📧 Email: {config.PERSONAL_INFO['email']}
    - 💼 LinkedIn: [Profile]({config.PERSONAL_INFO['linkedin']})
    - 💻 GitHub: [Profile]({config.PERSONAL_INFO['github']})
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div style="text-align: center; color: {config.THEME['text_muted']}; padding: 2rem;">
    <p>Built with Streamlit • {config.PROGRAM_INFO['university']} • {config.PROGRAM_INFO['graduation_date']}</p>
    <p style="font-size: 0.85rem;">Last updated: November 2025</p>
</div>
""", unsafe_allow_html=True)
