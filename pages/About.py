"""
About Page
Personal information, skills, experience, and contact
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
import config

set_page_config(page_title="About Me", page_icon="👤")
load_css()

render_header("👤 About Me", "Data Science Graduate | ML Researcher | Systems Engineer")

# Profile Image and Introduction
col1, col2 = st.columns([1, 2])

with col1:
    # Profile image if available
    if config.PERSONAL_INFO["profile_image"]:
        try:
            profile_path = Path(__file__).parent.parent / "assets" / "images" / config.PERSONAL_INFO["profile_image"]
            if profile_path.exists():
                st.image(str(profile_path), width=250, output_format="auto")
        except:
            st.markdown("📸 *Add your profile image to `assets/images/`*")
    
    st.markdown("### Quick Facts")
    st.markdown(f"""
    **Location:** {config.PERSONAL_INFO['location']}  
    **Email:** {config.PERSONAL_INFO['email']}  
    **GPA:** {config.PROGRAM_INFO['gpa']}
    """)
    
    render_social_links()

with col2:
    st.markdown("### Who I Am")
    st.markdown(config.PERSONAL_INFO['bio'])
    
    st.markdown("### Education")
    st.markdown(f"""
    **{config.PROGRAM_INFO['program_name']}**  
    {config.PROGRAM_INFO['university']} | {config.PROGRAM_INFO['graduation_date']}  
    GPA: {config.PROGRAM_INFO['gpa']}
    
    **Bachelor of Engineering in Electronics and Communication**  
    Nitte Meenakshi Institute of Technology, Bengaluru, India | Aug 2022
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Technical Skills
st.markdown("## 🛠️ Technical Skills")

# Create skill columns
col1, col2 = st.columns(2)

skills_list = list(config.SKILLS.items())
mid_point = len(skills_list) // 2

with col1:
    for category, skills in skills_list[:mid_point]:
        render_skill_category(category, skills)
        st.markdown("<br>", unsafe_allow_html=True)

with col2:
    for category, skills in skills_list[mid_point:]:
        render_skill_category(category, skills)
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Experience Timeline
st.markdown("## 💼 Professional Experience")

st.markdown("### Industry & Research Roles")

for exp in config.EXPERIENCE:
    render_timeline_item(
        title=exp['title'],
        organization=f"{exp['organization']} | {exp['location']}",
        dates=exp['dates'],
        highlights=exp['highlights']
    )
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Leadership & Service
st.markdown("## 🌟 Leadership & Service")

st.markdown("""
### Research Mentorship
**Research Mentor - AI Fairness & Ethics** | Syracuse University | 2025 - Present

- Mentoring high school student on independent research examining bias in large language models
- Advising on development of novel bias measurement methodology to compare LLM outputs
- Supporting CNY Science and Engineering Fair research projects focused on bias detection
- Providing guidance on research design, experimental protocols, and scientific communication

### Additional Leadership
- **Certified Scrum Master (CSM):** Trained 30+ interns in Agile and Scrum methodologies
- **Team Lead:** Managed 4-member research team at DRDO, coordinating experimental design
- **Women in Technology Club:** Active member promoting STEM outreach and diversity
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Publications & Recognition
st.markdown("## 📄 Publications & Recognition")

st.markdown("""
### Peer-Reviewed Publications
1. **[Your Name]**, [Co-authors]. "Performance Characterization of High-Accuracy Direction-Finding 
in Electronic-Warfare Systems." *IEEE International Conference on Microwave and Photonics (MAPCON)*, 
2022. DOI: 10.1109/MAPCON56011.2022.10047012

### Presentations
- IEEE MAPCON 2022 - Direction Finding in Electronic Warfare Systems
- 3 University Presentations - Research findings on direction-finding algorithms

### Certifications
- Certified Scrum Master (CSM)
- [Add any other relevant certifications]
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Research Interests
st.markdown("## 🔬 Research Interests")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Primary Areas
    - **Machine Learning Systems:** Building robust, scalable ML infrastructure
    - **Responsible AI:** Fair, transparent, and human-centered AI systems
    - **Human-Computer Interaction:** Bridging ML research and deployment
    """)

with col2:
    st.markdown("""
    ### Application Domains
    - **Healthcare:** Medical imaging, diagnostic systems
    - **Accessibility:** Assistive technologies
    - **Scientific Computing:** Forecasting, simulation
    - **Social Impact:** ML for underserved communities
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Career Goals
st.markdown("## 🎯 Career Goals")

st.markdown(f"""
### Immediate Goals ({config.PROGRAM_INFO['graduation_date']})
- **PhD Programs:** Applying to doctoral programs in ML/AI/HCI
- **Research Positions:** Seeking research roles in AI systems and responsible AI
- **ML Engineering:** Interested in ML systems roles with social impact focus

### Long-Term Vision
Building a career at the intersection of ML research and real-world impact, with focus on:
- Developing fair and robust AI systems
- Bridging academic research and practical deployment
- Contributing to ML applications that address societal challenges
- Mentoring the next generation of data scientists and ML researchers
""")

st.markdown("<hr>", unsafe_allow_html=True)

# What I'm Currently Learning
st.markdown("## 📚 Currently Exploring")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Technical Skills**
    - Advanced RAG systems
    - LLM fine-tuning techniques
    - Causal inference methods
    """)

with col2:
    st.markdown("""
    **Research Areas**
    - AI fairness & bias detection
    - Knowledge graph construction
    - Multi-modal learning
    """)

with col3:
    st.markdown("""
    **Tools & Frameworks**
    - Graphiti API
    - Advanced PyTorch techniques
    - MLOps best practices
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Personal Interests (Optional)
st.markdown("## 🎨 Beyond Data Science")

st.markdown("""
*Optional: Add a brief section about personal interests, hobbies, or activities that show 
you're a well-rounded individual. This helps make you more memorable and relatable.*

**Example:**
- 🏃 Running and fitness enthusiast
- 📚 Avid reader of sci-fi and technology books
- ✈️ Love traveling and experiencing new cultures
- 🎮 Gaming and game AI research
- 🍳 Cooking and experimenting with recipes
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Contact Section
st.markdown("## 📬 Let's Connect!")

st.markdown(f"""
I'm always interested in discussing:
- **PhD programs and research opportunities**
- **ML systems and responsible AI**
- **Collaboration on open-source projects**
- **Speaking or presentation opportunities**
- **Career advice and mentorship**

### Get in Touch

**Prefer Email?**  
📧 {config.PERSONAL_INFO['email']}

**Connect Professionally:**  
💼 [LinkedIn]({config.PERSONAL_INFO['linkedin']})  
💻 [GitHub]({config.PERSONAL_INFO['github']})

**Based in:** {config.PERSONAL_INFO['location']}
""")

# Contact Form (if enabled)
if config.CONTACT_FORM['enabled']:
    st.markdown("### 📝 Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.info("Contact form functionality requires backend integration. " +
                   f"For now, please email directly: {config.PERSONAL_INFO['email']}")

st.markdown("<hr>", unsafe_allow_html=True)

# Download Resume
st.markdown("## 📄 Download My Resume")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
    **Academic Resume**  
    *For PhD applications*
    """)
    # create_download_button("assets/resume_academic.pdf", "Download Academic Resume", "resume_academic.pdf")
    st.button("Download PDF (Add file to assets/)")

with col2:
    st.markdown("""
    **Industry Resume**  
    *For job applications*
    """)
    # create_download_button("assets/resume_industry.pdf", "Download Industry Resume", "resume_industry.pdf")
    st.button("Download PDF (Add file to assets/) ", key="industry")

with col3:
    st.markdown("""
    **Full CV**  
    *Complete academic record*
    """)
    # create_download_button("assets/cv_full.pdf", "Download Full CV", "cv_full.pdf")
    st.button("Download PDF (Add file to assets/)  ", key="cv")

st.markdown("<hr>", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div style="text-align: center; color: {config.THEME['text_muted']}; padding: 2rem;">
    <p>Thank you for visiting my portfolio!</p>
    <p style="font-size: 0.85rem;">
        Built with ❤️ using Streamlit | Last updated: November 2025
    </p>
    <p style="font-size: 0.85rem;">
        {config.PROGRAM_INFO['university']} | {config.PROGRAM_INFO['program_name']}
    </p>
</div>
""", unsafe_allow_html=True)
