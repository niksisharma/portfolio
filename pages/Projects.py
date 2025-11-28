import streamlit as st
from pathlib import Path
import config

st.set_page_config(
    page_title="Projects - Portfolio",
    # page_icon="🚀",
    layout="wide"
)

# Load CSS
def load_css():
    css_file = Path(__file__).parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

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

# Load CSS
def load_css():
    css_file = Path(__file__).parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Page Header
st.markdown("""
<div class="hero-window">
    <div class="window-titlebar">
        <div class="window-title">PROJECTS.EXE</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>Project Portfolio</h1>
        <p>A collection of my data science and machine learning projects demonstrating end-to-end ML system development.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Filter options
st.markdown('<div class="section-header">FILTER PROJECTS</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    status_filter = st.selectbox(
        "Status",
        ["All", "Completed", "In Progress"],
        key="status_filter"
    )

with col2:
    # Get unique tech from all projects
    all_tech = set()
    for p in config.PROJECTS:
        all_tech.update(p['tech_stack'])
    tech_filter = st.selectbox(
        "Technology",
        ["All"] + sorted(list(all_tech)),
        key="tech_filter"
    )

with col3:
    show_featured = st.checkbox("Featured Only", value=False)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Filter projects
filtered_projects = config.PROJECTS

if status_filter != "All":
    filtered_projects = [p for p in filtered_projects if p['status'] == status_filter]

if tech_filter != "All":
    filtered_projects = [p for p in filtered_projects if tech_filter in p['tech_stack']]

if show_featured:
    filtered_projects = [p for p in filtered_projects if p.get('featured', False)]

# Display projects
st.markdown(f'<div class="section-header">SHOWING {len(filtered_projects)} PROJECTS</div>', unsafe_allow_html=True)

for project in filtered_projects:
    # Tech stack tags HTML
    tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])
    
    # Featured badge
    featured_badge = '⭐ Featured' if project.get('featured') else ''
    
    st.markdown(f"""
    <div class="project-display">
        <div class="project-image">
            <div class="project-placeholder">IMAGE</div>
        </div>
        <div class="project-info">
            <div class="project-header">
                <h3>{project['title']} {featured_badge}</h3>
                <div class="project-meta">{project['date']} | {project['status']}</div>
            </div>
            <div class="project-body">
                <h4 style="margin-bottom: 0.5rem; color: var(--primary-teal);">{project['subtitle']}</h4>
                <p>{project['description']}</p>
                <div class="tech-label">Built With:</div>
                <div class="tech-tags">
                    {tech_tags}
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
    
    with col1:
        if project.get('github'):
            st.link_button("GitHub", project['github'], use_container_width=True)
        else:
            st.button("GitHub", disabled=True, use_container_width=True)
    
    with col2:
        if project.get('demo'):
            st.link_button("Demo", project['demo'], use_container_width=True)
        else:
            st.button("Demo", disabled=True, use_container_width=True)
    
    with col3:
        # Link to detailed project page
        st.button("Details →", key=f"details_{project['id']}", use_container_width=True)
    
    st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Project Highlights Summary
st.markdown('<div class="section-header">PROJECT HIGHLIGHTS</div>', unsafe_allow_html=True)

highlights_cols = st.columns(3)

with highlights_cols[0]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>🏆 Best Technical</h3>
        </div>
        <div class="project-body">
            <p><strong>CapsNet Classifier</strong></p>
            <p>Most technically sophisticated implementation with novel architecture improvements.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with highlights_cols[1]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>🚀 Most Innovative</h3>
        </div>
        <div class="project-body">
            <p><strong>RAG-ception</strong></p>
            <p>Creative application of RAG systems to solve research paper organization challenges.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with highlights_cols[2]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>🌍 Best Impact</h3>
        </div>
        <div class="project-body">
            <p><strong>Energy Forecasting</strong></p>
            <p>Direct applications to sustainability and environmental conservation efforts.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Technologies Used Across All Projects
st.markdown('<div class="section-header">TECHNOLOGY STACK</div>', unsafe_allow_html=True)

# Count technology usage
tech_count = {}
for project in config.PROJECTS:
    for tech in project['tech_stack']:
        tech_count[tech] = tech_count.get(tech, 0) + 1

# Sort by frequency
sorted_tech = sorted(tech_count.items(), key=lambda x: x[1], reverse=True)

# Display in columns
tech_cols = st.columns(4)
for idx, (tech, count) in enumerate(sorted_tech):
    with tech_cols[idx % 4]:
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon" style="font-size: 2.5rem;">{count}</div>
            <h3>{tech}</h3>
        </div>
        """, unsafe_allow_html=True)
