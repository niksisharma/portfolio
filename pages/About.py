import streamlit as st
from pathlib import Path
import config

st.set_page_config(
    page_title="About - Portfolio",
    # page_icon="👤",
    layout="wide"
)

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
        <div class="window-title">ABOUT.ME</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>About Me</h1>
        <p>Get to know more about my background, education, and professional experience.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Bio Section
st.markdown('<div class="section-header">BIOGRAPHY</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <div class="project-info">
        <div class="project-body">
            {config.ABOUT_ME['bio'].replace(chr(10), '<br><br>')}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 8rem;">👤</div>
        <h3>Your Photo Here</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Facts
    st.markdown(f"""
    <div class="skill-card">
        <h3>Quick Facts</h3>
        <div class="skill-level">📍 {config.PERSONAL_INFO['location']}</div>
        <div class="skill-level">🎓 MS Applied Data Science</div>
        <div class="skill-level">📊 GPA: {config.STATS['gpa']}</div>
        <div class="skill-level">🚀 {config.STATS['projects']} Projects</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Education
st.markdown('<div class="section-header">EDUCATION</div>', unsafe_allow_html=True)

for edu in config.ABOUT_ME['education']:
    st.markdown(f"""
    <div class="project-info">
        <div class="project-header">
            <h3>{edu['degree']}</h3>
            <div class="project-meta">{edu['school']} | {edu['location']}</div>
        </div>
        <div class="project-body">
            <div class="stats-bar">
                <div class="stat-item">
                    <span class="stat-label">Graduation:</span>
                    <span class="stat-value">{edu['date']}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">GPA:</span>
                    <span class="stat-value">{edu['gpa']}</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Experience
st.markdown('<div class="section-header">EXPERIENCE</div>', unsafe_allow_html=True)

for exp in config.ABOUT_ME['experience']:
    responsibilities = '<br>'.join([f"• {item}" for item in exp['description']])
    
    st.markdown(f"""
    <div class="project-info">
        <div class="project-header">
            <h3>{exp['title']}</h3>
            <div class="project-meta">{exp['company']} | {exp['location']} | {exp['date']}</div>
        </div>
        <div class="project-body">
            {responsibilities}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Skills Overview
st.markdown('<div class="section-header">TECHNICAL EXPERTISE</div>', unsafe_allow_html=True)

cols = st.columns(3)

skills_by_category = {
    "Languages & Frameworks": ["Python", "PyTorch", "TensorFlow"],
    "Data & Cloud": ["SQL", "AWS / Cloud", "Docker"],
    "Specialized": ["LangChain / LLMs", "Scikit-learn"]
}

for idx, (category, skills) in enumerate(skills_by_category.items()):
    with cols[idx]:
        st.markdown(f"""
        <div class="project-info">
            <div class="project-header">
                <h3>{category}</h3>
            </div>
            <div class="project-body">
        """, unsafe_allow_html=True)
        
        for skill_name in skills:
            skill = next((s for s in config.SKILLS if s['name'] == skill_name), None)
            if skill:
                st.markdown(f"""
                <div class="skill-level">✓ {skill['name']} ({skill['level']})</div>
                """, unsafe_allow_html=True)
        
        st.markdown("""
            </div>
        </div>
        """, unsafe_allow_html=True)

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

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Contact Information
st.markdown('<div class="section-header">GET IN TOUCH</div>', unsafe_allow_html=True)

contact_cols = st.columns(2)

with contact_cols[0]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>Contact Information</h3>
        </div>
        <div class="project-body">
            <div class="skill-level">📧 Email: {email}</div>
            <div class="skill-level">📱 Phone: {phone}</div>
            <div class="skill-level">📍 Location: {location}</div>
        </div>
    </div>
    """.format(
        email=config.PERSONAL_INFO['email'],
        phone=config.PERSONAL_INFO['phone'],
        location=config.PERSONAL_INFO['location']
    ), unsafe_allow_html=True)

with contact_cols[1]:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>Online Presence</h3>
        </div>
        <div class="project-body">
            <div class="skill-level">💼 LinkedIn: <a href="{linkedin}" target="_blank">Connect</a></div>
            <div class="skill-level">💻 GitHub: <a href="{github}" target="_blank">Follow</a></div>
            <div class="skill-level">🌐 Website: <a href="{website}" target="_blank">Visit</a></div>
        </div>
    </div>
    """.format(
        linkedin=config.PERSONAL_INFO['linkedin'],
        github=config.PERSONAL_INFO['github'],
        website=config.PERSONAL_INFO['website']
    ), unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Download Resume
st.markdown('<div class="section-header">RESUME</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 4rem;">📄</div>
        <h3>Download My Resume</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.download_button(
        label="Download Resume (PDF)",
        data=b"Your resume PDF content here",  # Replace with actual resume file
        file_name="YourName_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# Fun Facts Section
st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

with st.expander("🎮 FUN FACTS & INTERESTS"):
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
        **Hobbies:**
        - 🎵 Music
        - 📚 Reading
        - 🏃 Running
        - 🎮 Gaming
        """)
    
    with cols[1]:
        st.markdown("""
        **Favorite Tools:**
        - 💻 VS Code
        - 🐍 Python
        - 📊 Jupyter
        - ☁️ AWS
        """)
    
    with cols[2]:
        st.markdown("""
        **Currently Learning:**
        - 🤖 Advanced LLMs
        - ☸️ Kubernetes
        - 🔧 MLOps Best Practices
        - 📈 Causal Inference
        """)
