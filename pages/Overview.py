import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
import config

st.set_page_config(
    page_title="Overview - Portfolio",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path(__file__).parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Top Navigation
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
        <p>A comprehensive overview of my graduate program learning outcomes and project portfolio demonstrating mastery of data science principles and practices.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Program Learning Outcomes
st.markdown('<div class="section-header">PROGRAM LEARNING OUTCOMES</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <p>The MS in Applied Data Science program at Syracuse University is designed to develop interdisciplinary expertise across technical, analytical, and ethical dimensions of data science. Through coursework and applied projects, I have achieved the following learning outcomes:</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Display each learning outcome
for lo_id, lo in config.LEARNING_OUTCOMES.items():
    st.markdown(f"""
    <div class="skill-card" style="text-align: left; margin-bottom: 1.5rem;">
        <h3 style="margin-bottom: 0.5rem;">Learning Outcome {lo['number']}: {lo['title']}</h3>
        <p style="color: var(--text-dark); margin-top: 0.5rem;">
            {lo['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Learning Outcomes Achievement Matrix
st.markdown('<div class="section-header">HOW I ACHIEVED THE LEARNING OUTCOMES</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <p>The table below maps each project to the specific learning outcomes it demonstrates. Click on any project name to see detailed explanations of how it addresses each learning outcome.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Create matrix showing which projects demonstrate which LOs
st.markdown('<div style="margin-top: 2rem;"></div>', unsafe_allow_html=True)

# Matrix table
matrix_html = """
<div class="project-info">
    <div class="project-body">
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: var(--bg-darker); border-bottom: 3px solid var(--border-black);">
                    <th style="padding: 1rem; text-align: left; border-right: 2px solid var(--border-black);">Project</th>
                    <th style="padding: 1rem; text-align: center; border-right: 2px solid var(--border-black);">LO1</th>
                    <th style="padding: 1rem; text-align: center; border-right: 2px solid var(--border-black);">LO2</th>
                    <th style="padding: 1rem; text-align: center; border-right: 2px solid var(--border-black);">LO3</th>
                    <th style="padding: 1rem; text-align: center; border-right: 2px solid var(--border-black);">LO4</th>
                    <th style="padding: 1rem; text-align: center; border-right: 2px solid var(--border-black);">LO5</th>
                    <th style="padding: 1rem; text-align: center;">LO6</th>
                </tr>
            </thead>
            <tbody>
"""

for project in config.PROJECTS:
    matrix_html += f"""
                <tr style="border-bottom: 2px solid var(--bg-darker);">
                    <td style="padding: 0.8rem; font-weight: bold; border-right: 2px solid var(--border-black);">{project['title']}</td>
    """
    
    for i in range(1, 7):
        lo_id = f"LO{i}"
        if lo_id in project.get('learning_outcomes', []):
            matrix_html += f'<td style="padding: 0.8rem; text-align: center; border-right: 2px solid var(--border-black);"><span style="color: var(--primary-teal); font-size: 1.5rem;">✓</span></td>'
        else:
            matrix_html += f'<td style="padding: 0.8rem; text-align: center; border-right: 2px solid var(--border-black);"><span style="color: var(--text-light);">-</span></td>'
    
    matrix_html += """
                </tr>
    """

matrix_html += """
            </tbody>
        </table>
    </div>
</div>
"""

st.markdown(matrix_html, unsafe_allow_html=True)

# Legend
st.markdown("""
<div class="project-info" style="margin-top: 1rem;">
    <div class="project-body">
        <p style="font-size: 0.9rem; color: var(--text-gray);">
            <strong>Legend:</strong> LO1 = Data Collection & Storage | LO2 = Actionable Insights | LO3 = Visualization & Predictive Models | LO4 = Programming Proficiency | LO5 = Communication | LO6 = Ethics & Responsible AI
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Detailed LO Achievement Explanations
st.markdown('<div class="section-header">DETAILED ACHIEVEMENT EXPLANATIONS</div>', unsafe_allow_html=True)

# For each LO, show which projects demonstrate it and how
for lo_id, lo in config.LEARNING_OUTCOMES.items():
    with st.expander(f"🎯 LO{lo['number']}: {lo['title']}", expanded=False):
        st.markdown(f"**{lo['description']}**")
        st.markdown("---")
        
        # Find all projects that demonstrate this LO
        relevant_projects = [p for p in config.PROJECTS if lo_id in p.get('learning_outcomes', [])]
        
        if relevant_projects:
            st.markdown(f"**Demonstrated in {len(relevant_projects)} project(s):**")
            
            for project in relevant_projects:
                explanation = project['lo_explanations'].get(lo_id, "")
                st.markdown(f"""
                <div class="skill-card" style="text-align: left; margin: 1rem 0;">
                    <h3 style="margin-bottom: 0.5rem;">{project['title']}</h3>
                    <p style="color: var(--text-dark);">✓ {explanation}</p>
                </div>
                """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# High-Level Project Descriptions
st.markdown('<div class="section-header">PROJECT PORTFOLIO OVERVIEW</div>', unsafe_allow_html=True)

# Stats
col1, col2, col3, col4 = st.columns(4)

completed = len([p for p in config.PROJECTS if p['status'] == 'Completed'])
in_progress = len([p for p in config.PROJECTS if p['status'] == 'In Progress'])
featured = len([p for p in config.PROJECTS if p.get('featured', False)])

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
        <div class="interest-icon" style="font-size: 3rem;">{featured}</div>
        <h3>Featured</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Project Catalog with High-Level Descriptions
st.markdown('<div class="section-header">PROJECT CATALOG</div>', unsafe_allow_html=True)

for project in config.PROJECTS:
    with st.expander(f"{'⭐ ' if project.get('featured') else ''}🖥️ {project['title']} - {project['status']}", expanded=False):
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**{project['subtitle']}**")
            st.markdown(f"*{project['date']} | {project.get('course', 'Independent Project')}*")
            st.markdown("")
            st.markdown(project['description'])
            
            # Tech stack
            st.markdown("**Technologies:**")
            tech_badges = " ".join([f"`{tech}`" for tech in project['tech_stack']])
            st.markdown(tech_badges)
        
        with col2:
            st.markdown("**Status**")
            status_color = "#00A9A5" if project['status'] == "Completed" else "#FF6700"
            st.markdown(f"<span style='color: {status_color}; font-weight: bold;'>{project['status']}</span>", unsafe_allow_html=True)
            
            st.markdown("**Learning Outcomes**")
            los = ", ".join(project['learning_outcomes'])
            st.markdown(f"`{los}`")
            
            st.markdown("")
            
            # View detailed page button
            if project.get('id'):
                project_page_name = ''.join(word.capitalize() for word in project['id'].split('-'))
                st.link_button("View Details →", f"/projects/{project_page_name}", use_container_width=True)
            
            if project.get('github'):
                st.link_button("GitHub →", project['github'], use_container_width=True)
            
            if project.get('demo'):
                st.link_button("Live Demo →", project['demo'], use_container_width=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Skills Developed
st.markdown('<div class="section-header">TECHNICAL SKILLS DEVELOPED</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <p>Through coursework and projects, I have developed proficiency across the following technical areas:</p>
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

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="project-info">
    <div class="project-body" style="text-align: center;">
        <h3 style="color: var(--primary-teal); margin-bottom: 1rem;">Explore My Work</h3>
        <p>Visit the Projects page to see detailed implementations, code samples, and results from each project. Read my Reflection blog post for insights on my learning journey through the program.</p>
    </div>
</div>
""", unsafe_allow_html=True)

link_cols = st.columns(3)
with link_cols[0]:
    st.link_button("📂 View All Projects", "/Projects", use_container_width=True)
with link_cols[1]:
    st.link_button("📝 Read Reflection", "/Reflection", use_container_width=True)
with link_cols[2]:
    st.link_button("👤 About Me", "/About", use_container_width=True)