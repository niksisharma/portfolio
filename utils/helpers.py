"""
Utility functions for the portfolio
"""
import streamlit as st
from pathlib import Path
import sys

# Add parent directory to path to import config
sys.path.append(str(Path(__file__).parent.parent))
import config

def load_css():
    """Load custom CSS"""
    css_file = Path(__file__).parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def set_page_config(page_title=None, page_icon="🎓", layout="wide"):
    """Configure page settings"""
    if page_title is None:
        page_title = config.SEO["page_title"]
    
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout,
        initial_sidebar_state="expanded"
    )

def render_header(title, subtitle=None):
    """Render a consistent page header"""
    st.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p style='font-size: 1.2rem; color: {config.THEME['text_muted']};'>{subtitle}</p>", 
                   unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

def render_project_card(project):
    """Render a project card with consistent styling"""
    # Status badge
    status_color = config.THEME["secondary"] if project["status"] == "Completed" else config.THEME["accent2"]
    
    card_html = f"""
    <div class="project-card">
        <h3>{project["title"]}</h3>
        <p style="color: {config.THEME['text_muted']}; font-size: 0.9rem; margin-bottom: 0.5rem;">
            {project["date"]} | <span style="color: {status_color}; font-weight: 600;">{project["status"]}</span>
        </p>
        <p>{project["short_description"]}</p>
        <div style="margin-top: 1rem;">
    """
    
    # Tags
    for tag in project["tags"][:5]:  # Limit to 5 tags
        card_html += f'<span class="tag">{tag}</span>'
    
    card_html += "</div></div>"
    
    st.markdown(card_html, unsafe_allow_html=True)

def render_tags(tags, max_tags=None):
    """Render tags/badges"""
    if max_tags:
        tags = tags[:max_tags]
    
    tags_html = '<div style="margin: 1rem 0;">'
    for i, tag in enumerate(tags):
        # Cycle through tag styles
        tag_class = ["tag", "tag-secondary", "tag-accent1"][i % 3]
        tags_html += f'<span class="{tag_class}">{tag}</span>'
    tags_html += '</div>'
    
    st.markdown(tags_html, unsafe_allow_html=True)

def render_metric(label, value, icon=None):
    """Render a metric card"""
    metric_html = f"""
    <div class="metric-container">
        <div class="metric-value">{icon if icon else ''} {value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """
    st.markdown(metric_html, unsafe_allow_html=True)

def render_timeline_item(title, organization, dates, highlights):
    """Render a timeline item for experience"""
    timeline_html = f"""
    <div class="timeline-item">
        <h3>{title}</h3>
        <p style="color: {config.THEME['secondary']}; font-weight: 600;">{organization}</p>
        <p style="color: {config.THEME['text_muted']}; font-size: 0.9rem;">{dates}</p>
        <ul>
    """
    
    for highlight in highlights:
        timeline_html += f"<li>{highlight}</li>"
    
    timeline_html += "</ul></div>"
    st.markdown(timeline_html, unsafe_allow_html=True)

def render_social_links():
    """Render social media links"""
    social_html = '<div class="social-links">'
    
    if config.PERSONAL_INFO["linkedin"]:
        social_html += f'<a href="{config.PERSONAL_INFO["linkedin"]}" target="_blank" class="social-link">💼 LinkedIn</a>'
    
    if config.PERSONAL_INFO["github"]:
        social_html += f'<a href="{config.PERSONAL_INFO["github"]}" target="_blank" class="social-link">💻 GitHub</a>'
    
    if config.PERSONAL_INFO["scholar"]:
        social_html += f'<a href="{config.PERSONAL_INFO["scholar"]}" target="_blank" class="social-link">🎓 Scholar</a>'
    
    if config.PERSONAL_INFO["email"]:
        social_html += f'<a href="mailto:{config.PERSONAL_INFO["email"]}" class="social-link">📧 Email</a>'
    
    social_html += '</div>'
    st.markdown(social_html, unsafe_allow_html=True)

def get_project_by_id(project_id):
    """Get project details by ID"""
    for project in config.PROJECTS:
        if project["id"] == project_id:
            return project
    return None

def render_info_box(content, box_type="info"):
    """Render an info/warning/success box"""
    box_class = f"{box_type}-box"
    st.markdown(f'<div class="{box_class}">{content}</div>', unsafe_allow_html=True)

def render_section_header(title, icon=None):
    """Render a section header with optional icon"""
    if icon:
        st.markdown(f"<h2>{icon} {title}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2>{title}</h2>", unsafe_allow_html=True)

def create_download_button(file_path, button_text, file_name):
    """Create a download button for files"""
    try:
        with open(file_path, "rb") as file:
            st.download_button(
                label=button_text,
                data=file,
                file_name=file_name,
                mime="application/octet-stream"
            )
    except FileNotFoundError:
        st.warning(f"File not found: {file_path}")

def render_skill_category(category, skills):
    """Render a skill category with list of skills"""
    st.markdown(f"**{category}:**")
    skills_text = " • ".join(skills)
    st.markdown(f"<p style='color: {config.THEME['text_muted']};'>{skills_text}</p>", 
               unsafe_allow_html=True)
