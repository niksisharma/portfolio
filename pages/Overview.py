import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import config

st.set_page_config(
    page_title=f"Overview - {config.PERSONAL_INFO['name']}",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
    <h1>Portfolio Overview</h1>
    <p style="font-size: 1.2rem; color: var(--text-secondary); margin-top: 1rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        A comprehensive overview of my graduate program learning outcomes and project portfolio demonstrating mastery of data science principles and practices.
    </p>
</div>
""", unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Program Learning Outcomes
st.markdown('<div class="section-header">Program Learning Outcomes</div>', unsafe_allow_html=True)

st.markdown("""
<div style="max-width: 900px; margin: 0 auto 2rem auto;">
    <p style="font-size: 1.05rem; color: var(--text-secondary); line-height: 1.8; text-align: center;">
        The MS in Applied Data Science program at Syracuse University is designed to develop interdisciplinary expertise across technical, analytical, and ethical dimensions of data science. Through coursework and applied projects, I have achieved the following learning outcomes:
    </p>
</div>
""", unsafe_allow_html=True)

# Display each learning outcome with clean, readable style
for lo_id, lo in config.LEARNING_OUTCOMES.items():
    st.markdown(f"""
    <div style="margin-bottom: 2.5rem;">
        <div style="display: flex; align-items: baseline; gap: 1rem; margin-bottom: 0.75rem;">
            <span style="color: var(--primary-sky-dark); font-weight: 600; font-size: 0.9rem; letter-spacing: 0.05em;">LO{lo['number']}</span>
            <h3 style="margin: 0; font-size: 1.5rem; font-weight: 600; color: var(--text-primary);">
                {lo['title']}
            </h3>
        </div>
        <p style="color: var(--text-secondary); margin: 0 0 0.5rem 3.5rem; font-size: 0.95rem; line-height: 1.6; font-style: italic;">
            "{lo['official_description']}"
        </p>
        <p style="color: var(--text-primary); margin: 0.75rem 0 0 3.5rem; font-size: 1.05rem; line-height: 1.85;">
            <strong>My Understanding:</strong> {lo['my_understanding']}
        </p>
    </div>
    """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Learning Outcomes Achievement Matrix
st.markdown('<div class="section-header">Learning Outcome Achievement Matrix</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="margin-bottom: 2rem;">
    <div class="card-body">
        <p>The table below maps each project to the specific learning outcomes it demonstrates. This matrix shows how my project portfolio comprehensively addresses all program learning outcomes.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Matrix table with enhanced visibility
st.markdown("""
<div style="background: #FFFFFF; border: 2px solid #BDBDBD; border-radius: 12px; padding: 2rem; margin: 2rem auto; max-width: 1200px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <table style="width: 100%; border-collapse: separate; border-spacing: 0; background: #FFFFFF;">
        <thead>
            <tr style="background: linear-gradient(135deg, #E3F2FD 0%, #E8F5E9 100%);">
                <th style="padding: 1.2rem 1rem; text-align: left; border-right: 2px solid #BDBDBD; border-bottom: 2px solid #2196F3; font-weight: 700; color: #1565C0; font-size: 1rem;">Project</th>
                <th style="padding: 1.2rem 1rem; text-align: center; border-right: 2px solid #BDBDBD; border-bottom: 2px solid #2196F3; font-weight: 700; color: #1565C0; font-size: 1rem;">LO1</th>
                <th style="padding: 1.2rem 1rem; text-align: center; border-right: 2px solid #BDBDBD; border-bottom: 2px solid #2196F3; font-weight: 700; color: #1565C0; font-size: 1rem;">LO2</th>
                <th style="padding: 1.2rem 1rem; text-align: center; border-right: 2px solid #BDBDBD; border-bottom: 2px solid #2196F3; font-weight: 700; color: #1565C0; font-size: 1rem;">LO3</th>
                <th style="padding: 1.2rem 1rem; text-align: center; border-right: 2px solid #BDBDBD; border-bottom: 2px solid #2196F3; font-weight: 700; color: #1565C0; font-size: 1rem;">LO4</th>
                <th style="padding: 1.2rem 1rem; text-align: center; border-right: 2px solid #BDBDBD; border-bottom: 2px solid #2196F3; font-weight: 700; color: #1565C0; font-size: 1rem;">LO5</th>
                <th style="padding: 1.2rem 1rem; text-align: center; border-bottom: 2px solid #2196F3; font-weight: 700; color: #1565C0; font-size: 1rem;">LO6</th>
            </tr>
        </thead>
        <tbody>
""", unsafe_allow_html=True)

# Build table rows
for project in config.PROJECTS:
    # Start row
    row_html = f'<tr style="background: #FFFFFF;"><td style="padding: 1rem; font-weight: 600; border-right: 2px solid #BDBDBD; border-bottom: 1px solid #E0E0E0; color: #212121; font-size: 0.95rem;">{project["title"]}</td>'

    # Add cells for each LO
    for i in range(1, 7):
        lo_id = f"LO{i}"
        border_right = 'border-right: 2px solid #BDBDBD;' if i < 6 else ''
        if lo_id in project.get('learning_outcomes', []):
            row_html += f'<td style="padding: 1rem; text-align: center; {border_right} border-bottom: 1px solid #E0E0E0; background: #FFFFFF;"><span style="color: #388E3C; font-size: 1.5rem; font-weight: bold;">✓</span></td>'
        else:
            row_html += f'<td style="padding: 1rem; text-align: center; {border_right} border-bottom: 1px solid #E0E0E0; background: #FFFFFF;"><span style="color: #BDBDBD; font-size: 1.2rem;">—</span></td>'

    # Close row and render
    row_html += '</tr>'
    st.markdown(row_html, unsafe_allow_html=True)

# Close table
st.markdown("""
        </tbody>
    </table>
</div>
</div>
""", unsafe_allow_html=True)

# Legend
st.markdown("""
<div class="card" style="margin-top: 1rem; background: var(--bg-light-gray);">
    <div class="card-body">
        <p style="font-size: 0.9rem; color: var(--text-tertiary); margin: 0;">
            <strong>Legend:</strong> LO1 = Data Collection & Storage | LO2 = Actionable Insights | LO3 = Visualization & Predictive Models | LO4 = Programming Proficiency | LO5 = Communication | LO6 = Ethics & Responsible AI
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Detailed LO Achievement Explanations
st.markdown('<div class="section-header">How I Achieved Each Learning Outcome</div>', unsafe_allow_html=True)

# For each LO, show which projects demonstrate it and how
for lo_id, lo in config.LEARNING_OUTCOMES.items():
    with st.expander(f"🎯 LO{lo['number']}: {lo['title']}", expanded=False):
        st.markdown(f"**{lo['official_description']}**")
        st.markdown("---")

        # Find all projects that demonstrate this LO
        relevant_projects = [p for p in config.PROJECTS if lo_id in p.get('learning_outcomes', [])]

        if relevant_projects:
            st.markdown(f"**Demonstrated in {len(relevant_projects)} project(s):**")

            for project in relevant_projects:
                explanation = project['lo_explanations'].get(lo_id, "")
                st.markdown(f"""
                <div class="card" style="margin: 1rem 0;">
                    <div class="card-header">
                        <h4 style="margin: 0; font-size: 1.1rem;">{project['title']}</h4>
                    </div>
                    <div class="card-body">
                        <p style="margin: 0;">✓ {explanation}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# High-Level Project Descriptions
st.markdown('<div class="section-header">Project Portfolio</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="margin-bottom: 2rem;">
    <div class="card-body">
        <p>Below are high-level descriptions of all projects in my portfolio. Each project demonstrates multiple learning outcomes and showcases different aspects of the data science lifecycle.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Project Catalog with High-Level Descriptions
for project in config.PROJECTS:
    with st.expander(f"{'⭐ ' if project.get('featured') else ''}💻 {project['title']} — {project['status']}", expanded=False):

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"### {project['subtitle']}")
            st.markdown(f"*{project['date']} | {project.get('course', 'Independent Project')}*")
            st.markdown("")
            st.markdown(project['description'])

            # Tech stack
            st.markdown("**Technologies:**")
            tech_tags_html = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])
            st.markdown(f'<div class="tech-tags">{tech_tags_html}</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("**Status**")
            status_color = "var(--accent-sage-dark)" if project['status'] == "Completed" else "var(--accent-rose-dark)"
            st.markdown(f"<span style='color: {status_color}; font-weight: 600;'>{project['status']}</span>", unsafe_allow_html=True)

            st.markdown("**Learning Outcomes**")
            los_badges = ''.join([f'<span class="lo-badge">{lo}</span>' for lo in project['learning_outcomes']])
            st.markdown(f'<div>{los_badges}</div>', unsafe_allow_html=True)

            st.markdown("")

            # View detailed page button
            if project.get('id'):
                project_page_name = ''.join(word.capitalize() for word in project['id'].split('-'))
                st.link_button("View Details →", f"/projects/{project_page_name}", use_container_width=True)

            if project.get('github'):
                st.link_button("GitHub →", project['github'], use_container_width=True)

            if project.get('demo'):
                st.link_button("Live Demo →", project['demo'], use_container_width=True)

# Gradient Divider
st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="card" style="background: linear-gradient(135deg, var(--primary-sky-light), var(--accent-sage-light));">
    <div class="card-body" style="text-align: center;">
        <h3 style="margin-bottom: 1rem;">Explore My Work</h3>
        <p>Visit the Projects page to see detailed implementations, code samples, and results. Read my Reflection for insights on my learning journey through the program.</p>
    </div>
</div>
""", unsafe_allow_html=True)

link_cols = st.columns(3)
with link_cols[0]:
    st.link_button("📂 View All Projects", "/Projects", use_container_width=True)
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
