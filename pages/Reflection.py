import streamlit as st
from pathlib import Path
import config

st.set_page_config(
    page_title="Reflection - Portfolio",
    page_icon="✍️",
    layout="wide"
)

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
        <div class="window-title">REFLECTION.DOC</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>{title}</h1>
        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-label">Published:</span>
                <span class="stat-value">{date}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Read Time:</span>
                <span class="stat-value">{read_time}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Word Count:</span>
                <span class="stat-value">~3000</span>
            </div>
        </div>
    </div>
</div>
""".format(
    title=config.BLOG_POST['title'],
    date=config.BLOG_POST['date'],
    read_time=config.BLOG_POST['read_time']
), unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Table of Contents
st.markdown('<div class="section-header">TABLE OF CONTENTS</div>', unsafe_allow_html=True)

toc_items = []
for idx, section in enumerate(config.BLOG_POST['sections'], 1):
    toc_items.append(f"{idx}. {section['heading']}")

st.markdown("""
<div class="project-info">
    <div class="project-body">
        {}
    </div>
</div>
""".format('<br>'.join(toc_items)), unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Blog Content
for idx, section in enumerate(config.BLOG_POST['sections'], 1):
    st.markdown(f'<div class="section-header">{idx}. {section["heading"].upper()}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="project-info">
        <div class="project-body">
            {section['content'].replace(chr(10), '<br>')}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Conclusion Section Template
st.markdown('<div class="section-header">CONCLUSION</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <p>As I complete my Master's in Applied Data Science at Syracuse University, I reflect on the incredible 
        journey of growth, learning, and discovery. This portfolio represents not just technical achievements, 
        but a transformation in how I approach problems, design solutions, and think about the role of AI in society.</p>
        
        <p><strong>Key Takeaways:</strong></p>
        <ul>
            <li>Technical excellence must be balanced with ethical considerations</li>
            <li>The best ML systems are built with end-users in mind</li>
            <li>Continuous learning and adaptability are essential in this rapidly evolving field</li>
            <li>Collaboration and communication skills are just as important as coding abilities</li>
        </ul>
        
        <p>Looking ahead, I'm excited to apply these lessons in [YOUR NEXT STEP - PhD program, industry role, etc.], 
        where I hope to continue building AI systems that make a positive impact on the world.</p>
        
        <p>Thank you for taking the time to explore my portfolio. I welcome any questions, feedback, or opportunities 
        to collaborate.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Share Section
st.markdown('<div class="section-header">SHARE THIS POST</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">🔗</div>
        <h3>LinkedIn</h3>
    </div>
    """, unsafe_allow_html=True)
    st.button("Share", key="linkedin", use_container_width=True)

with col2:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">🐦</div>
        <h3>Twitter</h3>
    </div>
    """, unsafe_allow_html=True)
    st.button("Tweet", key="twitter", use_container_width=True)

with col3:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">📧</div>
        <h3>Email</h3>
    </div>
    """, unsafe_allow_html=True)
    st.button("Send", key="email", use_container_width=True)

with col4:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon">📄</div>
        <h3>PDF</h3>
    </div>
    """, unsafe_allow_html=True)
    st.button("Download", key="pdf", use_container_width=True)

# Writing Guide Box
st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

with st.expander("📝 WRITING GUIDE - How to Complete Your 3000-Word Reflection"):
    st.markdown("""
    ### Structure Your Post:
    
    **Introduction (300-400 words)**
    - Hook: Start with a compelling anecdote or question
    - Context: Your background and what brought you to data science
    - Thesis: What this post will explore
    
    **Main Sections (500-700 words each)**
    
    Section 1: Technical Growth
    - Specific examples from your projects
    - Challenges you overcame
    - Skills you developed
    - Compare where you started vs. where you are now
    
    Section 2: Key Learnings
    - Most important lessons from your program
    - Surprising discoveries
    - Misconceptions you had that changed
    - How your perspective evolved
    
    Section 3: Real-World Applications
    - Connect coursework to industry practices
    - Discuss current trends and your take on them
    - Ethical considerations you've learned to think about
    - Where you see the field heading
    
    Section 4: Personal Reflections
    - How this journey changed you
    - Mistakes and what you learned from them
    - Advice for future students
    - Your philosophy on data science/ML
    
    **Conclusion (300-400 words)**
    - Synthesize main points
    - Look to the future
    - Call to action or final thought
    
    ### Tips:
    - Use concrete examples from your projects
    - Include data, metrics, or specific outcomes
    - Be honest about challenges and failures
    - Show growth and learning
    - Connect theory to practice
    - Make it personal but professional
    - Use subheadings to break up text
    - Include visuals if possible
    """)
