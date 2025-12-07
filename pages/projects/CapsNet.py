import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
import config

PROJECT_ID = 'capsnet'

st.set_page_config(
    page_title="Scaling CapsNet Image Classifier - Project Details",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

project = next((p for p in config.PROJECTS if p['id'] == PROJECT_ID), None)

if not project:
    st.error(f"Project with ID '{PROJECT_ID}' not found in config.PROJECTS")
    st.stop()

# Top Navigation
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

# Project Header
st.markdown(f"""
<div style="text-align: center; margin: 3rem 0 2rem 0;">
    <h1>{project['title']}</h1>
    <p style="font-size: 1.3rem; color: var(--text-secondary); margin-top: 1rem;">
        {project['subtitle']}
    </p>
    <div style="margin-top: 1.5rem; font-size: 1.05rem; color: var(--text-tertiary);">
        {project['date']} | {project['status']} | {project.get('course', 'Independent Project')}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Overview
st.markdown('<div class="section-header">Overview</div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="background: rgba(255, 255, 255, 0.5); padding: 2rem; border-radius: 12px; border: 1px solid rgba(168, 216, 234, 0.3); margin-bottom: 2rem;">
    <p style="font-size: 1.15rem; line-height: 1.9;">{project.get('description', project['short_description'])}</p>
</div>
""", unsafe_allow_html=True)

# Problem & Solution
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h3 style="color: var(--text-primary); margin-bottom: 1rem;">Problem Statement</h3>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.5); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--accent-rose);">
        <p style="font-size: 1.05rem; line-height: 1.8;">{project.get('problem_statement', 'Problem statement not available.')}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<h3 style="color: var(--text-primary); margin-bottom: 1rem;">Solution</h3>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.5); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--accent-sage);">
        <p style="font-size: 1.05rem; line-height: 1.8;">{project.get('solution', 'Solution details not available.')}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Tech Stack
st.markdown('<div class="section-header">Technologies Used</div>', unsafe_allow_html=True)
tech_tags_html = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])
st.markdown(f'<div class="tech-tags">{tech_tags_html}</div>', unsafe_allow_html=True)

st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# My Role (if available)
if project.get('my_role'):
    st.markdown('<div class="section-header">My Role</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.5); padding: 2rem; border-radius: 12px; border: 1px solid rgba(168, 216, 234, 0.3); margin-bottom: 2rem;">
        <p style="font-size: 1.1rem; line-height: 1.9;">{project['my_role']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Technical Details (if available)
if project.get('technical_details'):
    st.markdown('<div class="section-header">Technical Details</div>', unsafe_allow_html=True)
    for key, value in project['technical_details'].items():
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.4); padding: 1.25rem; border-radius: 8px; margin-bottom: 1rem; border-left: 3px solid var(--primary-sky);">
            <h4 style="color: var(--text-primary); margin-bottom: 0.5rem; text-transform: capitalize;">{key.replace('_', ' ')}</h4>
            <p style="font-size: 1.05rem; line-height: 1.7; margin: 0;">{value}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Results (if available)
if project.get('results'):
    st.markdown('<div class="section-header">Results & Impact</div>', unsafe_allow_html=True)
    results_cols = st.columns(2)
    for idx, (key, value) in enumerate(project['results'].items()):
        with results_cols[idx % 2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, rgba(168, 216, 234, 0.2), rgba(184, 212, 186, 0.2)); padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem; text-align: center;">
                <h4 style="color: var(--text-primary); margin-bottom: 0.5rem; text-transform: capitalize;">{key.replace('_', ' ')}</h4>
                <p style="font-size: 1.1rem; font-weight: 600; color: var(--primary-sky-dark); margin: 0;">{value}</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Challenges (if available)
if project.get('challenges'):
    st.markdown('<div class="section-header">Challenges</div>', unsafe_allow_html=True)
    for idx, challenge in enumerate(project['challenges'], 1):
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.4); padding: 1.25rem; border-radius: 8px; margin-bottom: 1rem;">
            <p style="font-size: 1.05rem; line-height: 1.8; margin: 0;"><strong style="color: var(--accent-rose-dark);">{idx}.</strong> {challenge}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Learning Outcomes
st.markdown('<div class="section-header">Learning Outcomes Demonstrated</div>', unsafe_allow_html=True)

for lo_id in project['learning_outcomes']:
    lo = config.LEARNING_OUTCOMES[lo_id]
    explanation = project.get('lo_explanations', {}).get(lo_id, 'Explanation not available.')

    st.markdown(f"""
    <div style="background: rgba(184, 212, 186, 0.2); padding: 1.75rem; border-radius: 12px; margin-bottom: 1.5rem; border-left: 4px solid var(--accent-sage);">
        <div style="display: flex; align-items: baseline; gap: 1rem; margin-bottom: 0.75rem;">
            <span style="color: var(--accent-sage-dark); font-weight: 700; font-size: 1.1rem;">LO{lo['number']}</span>
            <h3 style="margin: 0; font-size: 1.4rem; color: var(--text-primary);">{lo['title']}</h3>
        </div>
        <p style="font-size: 0.95rem; color: var(--text-tertiary); font-style: italic; margin-bottom: 1rem;">"{lo['official_description']}"</p>
        <p style="font-size: 1.05rem; line-height: 1.8; margin: 0;"><strong>How this project demonstrates it:</strong> {explanation}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider-gradient"></div>', unsafe_allow_html=True)

# Links
st.markdown('<div class="section-header">Links & Resources</div>', unsafe_allow_html=True)

link_cols = st.columns(3)

with link_cols[0]:
    if project.get('github'):
        st.link_button("View GitHub Repository", project['github'], use_container_width=True)

with link_cols[1]:
    if project.get('demo'):
        st.link_button("Live Demo", project['demo'], use_container_width=True)

with link_cols[2]:
    st.link_button("Back to All Projects", "/Projects", use_container_width=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 4rem; padding: 2rem;">
    <div class="divider" style="margin-bottom: 2rem;"></div>
    <p style="color: var(--text-tertiary); font-size: 0.9rem;">
        MS Applied Data Science Portfolio | Syracuse University | © 2025 {config.PERSONAL_INFO['name']}
    </p>
</div>
""", unsafe_allow_html=True)
