"""
Overview Page
Program learning outcomes and portfolio overview
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
import config

set_page_config(page_title="Overview", page_icon="📚")
load_css()

render_header("📚 Portfolio Overview", "MS in Applied Data Science Program")

# Program Description
st.markdown("<h2>🎓 Program Information</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    **Program:** {config.PROGRAM_INFO['program_name']}  
    **University:** {config.PROGRAM_INFO['university']}  
    **Graduation:** {config.PROGRAM_INFO['graduation_date']}  
    **GPA:** {config.PROGRAM_INFO['gpa']}
    
    The MS in Applied Data Science program provides comprehensive training in modern data science 
    methodologies, machine learning systems, and real-world applications. Through rigorous coursework 
    and hands-on projects, students develop expertise in:
    
    - Advanced machine learning and deep learning architectures
    - ML systems engineering and deployment
    - Data engineering and infrastructure
    - Statistical modeling and analysis
    - Applied research and problem-solving
    - Professional communication and collaboration
    """)

with col2:
    render_info_box(
        f"""
        <strong>Portfolio Highlights:</strong><br>
        • {len(config.PROJECTS)} Major Projects<br>
        • {len([p for p in config.PROJECTS if p['status'] == 'Completed'])} Completed<br>
        • {len([p for p in config.PROJECTS if p.get('interactive', False)])} Interactive Demos<br>
        • Multiple Industry Experiences
        """,
        box_type="info"
    )

st.markdown("<hr>", unsafe_allow_html=True)

# Learning Outcomes
st.markdown("<h2>🎯 Program Learning Outcomes</h2>", unsafe_allow_html=True)

st.markdown("""
Below are the key learning outcomes of the MS in Applied Data Science program, along with 
specific projects that demonstrate achievement of each outcome.
""")

for i, outcome in enumerate(config.PROGRAM_INFO["learning_outcomes"], 1):
    with st.expander(f"**Learning Outcome {i}: {outcome['outcome']}**", expanded=False):
        st.markdown(f"**Description:** {outcome['description']}")
        
        st.markdown("**Projects demonstrating this outcome:**")
        for project_title in outcome['projects']:
            # Find the actual project
            project = next((p for p in config.PROJECTS if p['title'] == project_title), None)
            if project:
                st.markdown(f"- **{project_title}** ({project['date']})")
            else:
                st.markdown(f"- {project_title}")
        
        st.markdown("---")
        st.markdown("*Detailed explanation of how this outcome was achieved can be found in the Reflection section.*")

st.markdown("<hr>", unsafe_allow_html=True)

# Projects Overview by Category
st.markdown("<h2>📂 Projects by Category</h2>", unsafe_allow_html=True)

# Group projects by category
categories = {}
for project in config.PROJECTS:
    category = project.get("category", "Other")
    if category not in categories:
        categories[category] = []
    categories[category].append(project)

# Display projects by category
for category, projects in categories.items():
    st.markdown(f"### {category}")
    
    for project in projects:
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown(f"**{project['title']}**")
            st.markdown(f"<p style='color: {config.THEME['text_muted']}; font-size: 0.9rem;'>{project['short_description']}</p>", 
                       unsafe_allow_html=True)
        
        with col2:
            status_color = config.THEME['secondary'] if project['status'] == 'Completed' else config.THEME['accent2']
            st.markdown(f"<p style='color: {status_color}; font-weight: 600;'>{project['status']}</p>", 
                       unsafe_allow_html=True)
        
        with col3:
            if st.button("View", key=f"view_{project['id']}"):
                st.info(f"Navigate to Projects page → {project['title']}")
        
        st.markdown("---")

st.markdown("<hr>", unsafe_allow_html=True)

# How Learning Outcomes Were Achieved
st.markdown("<h2>🔗 Mapping: Projects ↔ Learning Outcomes</h2>", unsafe_allow_html=True)

st.markdown("""
This section provides a high-level overview of how specific projects contributed to achieving 
the program learning outcomes. For detailed explanations and reflections, please see the 
**Reflection** page.
""")

# Create a simple table/matrix
st.markdown("### Key Projects and Their Learning Outcome Contributions")

# Example format - you can customize this
project_outcome_map = {
    "RAG-ception": ["Advanced ML/DL", "ML Systems", "Research & Problem-Solving"],
    "Aurora Prediction": ["Advanced ML/DL", "ML Systems", "Data Engineering"],
    "CapsNet Classifier": ["Advanced ML/DL", "Research & Problem-Solving"],
    "Airbnb Prediction": ["Advanced ML/DL", "Data Engineering"],
    "CuseBus Platform": ["Data Engineering", "ML Systems"],
}

for project_name, outcomes in project_outcome_map.items():
    st.markdown(f"**{project_name}**")
    st.markdown(f"*Outcomes addressed:* {', '.join(outcomes)}")
    st.markdown("")

render_info_box(
    """
    <strong>💡 Note:</strong> The detailed narrative of how each project contributed to my learning, 
    including challenges faced and insights gained, is available in the <strong>Reflection</strong> section.
    """,
    box_type="info"
)

st.markdown("<hr>", unsafe_allow_html=True)

# Additional Context
st.markdown("<h2>📋 Additional Information</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏢 Industry Experience")
    st.markdown("""
    - **Continental Automotive** - DevOps Engineer (1 year)
    - **Cirruslabs** - Software Developer & ML Research Engineer (1+ year)
    - **DRDO** - Research Intern (10 months)
    """)

with col2:
    st.markdown("### 📚 Key Competencies Developed")
    st.markdown("""
    - ML/AI system design and deployment
    - Research methodology and publication
    - Cross-functional team collaboration
    - Technical communication and documentation
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Navigation hint
st.markdown("### 🗺️ Navigate This Portfolio")
st.markdown("""
- **Projects**: Detailed descriptions and demos of each project
- **Reflection**: In-depth blog post and video about my program experience
- **About**: Personal background, skills, and contact information

Use the sidebar to navigate between sections!
""")
