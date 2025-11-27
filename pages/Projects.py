"""
Projects Page
Showcase all projects with filtering and navigation
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
import config

set_page_config(page_title="Projects", page_icon="🔬")
load_css()

render_header("🔬 Projects Portfolio", "Explore my data science and ML projects")

# Filter Section
st.markdown("### 🔍 Filter Projects")

col1, col2, col3 = st.columns(3)

with col1:
    # Category filter
    categories = list(set([p["category"] for p in config.PROJECTS]))
    selected_category = st.selectbox("Category", ["All"] + categories)

with col2:
    # Status filter
    statuses = list(set([p["status"] for p in config.PROJECTS]))
    selected_status = st.selectbox("Status", ["All"] + statuses)

with col3:
    # Interactive filter
    interactive_filter = st.selectbox("Type", ["All", "Interactive", "Static"])

st.markdown("<hr>", unsafe_allow_html=True)

# Filter projects
filtered_projects = config.PROJECTS.copy()

if selected_category != "All":
    filtered_projects = [p for p in filtered_projects if p["category"] == selected_category]

if selected_status != "All":
    filtered_projects = [p for p in filtered_projects if p["status"] == selected_status]

if interactive_filter == "Interactive":
    filtered_projects = [p for p in filtered_projects if p.get("interactive", False)]
elif interactive_filter == "Static":
    filtered_projects = [p for p in filtered_projects if not p.get("interactive", False)]

# Display results count
st.markdown(f"**Showing {len(filtered_projects)} of {len(config.PROJECTS)} projects**")

st.markdown("<hr>", unsafe_allow_html=True)

# Display projects
if filtered_projects:
    # Featured projects first
    featured = [p for p in filtered_projects if p.get("featured", False)]
    non_featured = [p for p in filtered_projects if not p.get("featured", False)]
    
    if featured:
        st.markdown("### ⭐ Featured Projects")
        for project in featured:
            render_project_card(project)
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if project.get("interactive"):
                    if st.button("🎮 Interactive Demo", key=f"demo_{project['id']}"):
                        st.info(f"Navigate to: Projects → {project['title']} (Interactive)")
            
            with col2:
                if project["github"]:
                    st.markdown(f"[💻 GitHub]({project['github']})")
            
            with col3:
                if st.button("📄 Details", key=f"details_{project['id']}"):
                    st.info(f"Scroll down to find {project['title']} in the project list")
            
            st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<hr>", unsafe_allow_html=True)
    
    # All projects (organized)
    st.markdown("### 📚 All Projects")
    
    # Group by category for display
    categories_display = {}
    for project in non_featured + featured:
        category = project["category"]
        if category not in categories_display:
            categories_display[category] = []
        categories_display[category].append(project)
    
    # Display by category
    for category, projects in categories_display.items():
        st.markdown(f"#### {category}")
        
        for project in projects:
            with st.expander(f"**{project['title']}** - {project['date']}", expanded=False):
                # Project details
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Description:**")
                    st.markdown(project['short_description'])
                    
                    st.markdown(f"**Technologies:**")
                    render_tags(project['tags'])
                
                with col2:
                    # Status
                    status_color = config.THEME['secondary'] if project['status'] == 'Completed' else config.THEME['accent2']
                    st.markdown(f"**Status:** <span style='color: {status_color}; font-weight: 600;'>{project['status']}</span>", 
                               unsafe_allow_html=True)
                    
                    # Interactive badge
                    if project.get('interactive'):
                        st.markdown(f"<span class='tag-accent1'>🎮 Interactive Demo</span>", unsafe_allow_html=True)
                    
                    # Featured badge
                    if project.get('featured'):
                        st.markdown(f"<span class='tag-accent2'>⭐ Featured</span>", unsafe_allow_html=True)
                
                # Action buttons
                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if project.get('interactive'):
                        if st.button("View Interactive Demo", key=f"interactive_{project['id']}_exp"):
                            st.info(f"Interactive demo pages are under construction. Coming soon!")
                
                with col2:
                    if project['github']:
                        st.markdown(f"[View on GitHub →]({project['github']})")
                
                with col3:
                    if st.button("Full Details", key=f"full_{project['id']}_exp"):
                        st.info(f"Detailed project page coming soon!")
        
        st.markdown("<br>", unsafe_allow_html=True)

else:
    st.warning("No projects match the selected filters.")

st.markdown("<hr>", unsafe_allow_html=True)

# Project Stats
st.markdown("### 📊 Portfolio Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_metric("Total Projects", len(config.PROJECTS), "🚀")

with col2:
    completed = len([p for p in config.PROJECTS if p['status'] == 'Completed'])
    render_metric("Completed", completed, "✅")

with col3:
    interactive = len([p for p in config.PROJECTS if p.get('interactive', False)])
    render_metric("Interactive", interactive, "🎮")

with col4:
    featured = len([p for p in config.PROJECTS if p.get('featured', False)])
    render_metric("Featured", featured, "⭐")

st.markdown("<hr>", unsafe_allow_html=True)

# Technologies Used
st.markdown("### 🛠️ Technologies Across Projects")

all_tags = []
for project in config.PROJECTS:
    all_tags.extend(project['tags'])

# Count frequency
from collections import Counter
tag_counts = Counter(all_tags)
top_tags = tag_counts.most_common(15)

st.markdown("**Most frequently used technologies:**")
tag_html = '<div style="margin: 1rem 0;">'
for i, (tag, count) in enumerate(top_tags):
    tag_class = ["tag", "tag-secondary", "tag-accent1"][i % 3]
    tag_html += f'<span class="{tag_class}">{tag} ({count})</span>'
tag_html += '</div>'
st.markdown(tag_html, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Call to Action
render_info_box(
    """
    <strong>🔗 Interested in a specific project?</strong><br>
    Most projects have detailed documentation on GitHub. For questions or collaboration opportunities, 
    feel free to reach out via the contact information in the About section!
    """,
    box_type="info"
)
