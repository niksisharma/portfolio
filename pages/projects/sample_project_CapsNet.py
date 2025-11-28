"""
SAMPLE PROJECT DETAIL PAGE
Copy this template to create detailed pages for each project

To create a new project page:
1. Copy this file
2. Rename it to: pages/projects/ProjectName.py
3. Update the content with your project details
4. Add screenshots/images to assets/images/
5. Link to it from the Projects page
"""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="RAG-ception - Project Details",
    page_icon="🔬",
    layout="wide"
)

# Load CSS
def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Project Header
st.markdown("""
<div class="hero-window">
    <div class="window-titlebar">
        <div class="window-title">PROJECT.EXE - RAG-CEPTION</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>RAG-ception</h1>
        <div class="subtitle">Automated Research Knowledge Management System</div>
        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-label">Status:</span>
                <span class="stat-value">In Progress</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Timeline:</span>
                <span class="stat-value">Oct - Dec 2025</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Team Size:</span>
                <span class="stat-value">1</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Screenshot Gallery
st.markdown('<div class="section-header">SCREENSHOTS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="terminal">
Loading image gallery...
</div>
""", unsafe_allow_html=True)

# Placeholder for images
cols = st.columns(3)
for i in range(3):
    with cols[i]:
        st.markdown("""
        <div class="project-image">
            <div class="project-placeholder">SCREENSHOT</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Project Overview
st.markdown('<div class="section-header">OVERVIEW</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <h3>Problem Statement</h3>
        <p>Research in RAG (Retrieval-Augmented Generation) and LLMs is advancing rapidly, with hundreds of 
        papers published monthly on arXiv. Researchers and practitioners struggle to keep up with the literature, 
        identify key papers, and understand connections between different approaches.</p>
        
        <h3>Solution</h3>
        <p>RAG-ception is an end-to-end ML system that automatically tracks, summarizes, and connects research papers. 
        The system fine-tunes LLMs to generate structured summaries and builds a dynamic knowledge graph to reveal 
        conceptual relationships across 500+ papers.</p>
        
        <h3>Impact</h3>
        <p>This project helps researchers save hours of literature review time, discover relevant papers more efficiently, 
        and understand the evolution of RAG techniques through visual knowledge graphs.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# System Requirements / Tech Stack
st.markdown('<div class="section-header">SYSTEM REQUIREMENTS</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>Technologies</h3>
        </div>
        <div class="project-body">
            <div class="tech-tags">
                <span class="tech-tag">PYTHON</span>
                <span class="tech-tag">PYTORCH</span>
                <span class="tech-tag">LANGCHAIN</span>
                <span class="tech-tag">GRAPHITI</span>
                <span class="tech-tag">CHROMADB</span>
                <span class="tech-tag">STREAMLIT</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-info">
        <div class="project-header">
            <h3>Infrastructure</h3>
        </div>
        <div class="project-body">
            <div class="skill-level">☁️ AWS EC2 (GPU instances)</div>
            <div class="skill-level">💾 Vector Database (ChromaDB)</div>
            <div class="skill-level">📊 Neo4j (Knowledge Graph)</div>
            <div class="skill-level">🐳 Docker Containers</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Architecture
st.markdown('<div class="section-header">ARCHITECTURE</div>', unsafe_allow_html=True)

st.markdown("""
<div class="terminal">
$ cat system_architecture.txt

Pipeline Flow:
1. arXiv API → Fetch papers (daily cron job)
2. PDF Parser → Extract text, figures, tables
3. LLM Fine-tuning → Generate structured summaries
4. Vector DB → Store embeddings for semantic search
5. Knowledge Graph → Build relationship network
6. Streamlit UI → Interactive exploration
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-image">
    <div class="project-placeholder">ARCHITECTURE DIAGRAM</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Key Features
st.markdown('<div class="section-header">KEY FEATURES</div>', unsafe_allow_html=True)

features_cols = st.columns(2)

with features_cols[0]:
    st.markdown("""
    <div class="skill-card">
        <h3>Automated Paper Tracking</h3>
        <div class="skill-level">
            • Daily monitoring of arXiv RAG/LLM papers<br>
            • Automatic classification and tagging<br>
            • Deduplication and quality filtering
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-card">
        <h3>LLM-Powered Summarization</h3>
        <div class="skill-level">
            • Fine-tuned model for research summaries<br>
            • Consistent schema extraction<br>
            • Key findings and methodology highlights
        </div>
    </div>
    """, unsafe_allow_html=True)

with features_cols[1]:
    st.markdown("""
    <div class="skill-card">
        <h3>Knowledge Graph</h3>
        <div class="skill-level">
            • Automatic relationship detection<br>
            • Citation network analysis<br>
            • Concept evolution tracking
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-card">
        <h3>Interactive Search</h3>
        <div class="skill-level">
            • Semantic search across papers<br>
            • Filter by date, venue, authors<br>
            • Visual graph exploration
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Technical Implementation
st.markdown('<div class="section-header">TECHNICAL DEEP DIVE</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Data Pipeline", "Model Training", "Deployment"])

with tab1:
    st.markdown("""
    ### Data Collection & Processing
    
    **Paper Collection:**
    ```python
    # Daily cron job fetches new papers
    papers = arxiv_api.search(
        query="RAG OR retrieval-augmented generation",
        max_results=100,
        sort_by="submittedDate"
    )
    ```
    
    **Text Extraction:**
    - PyMuPDF for PDF parsing
    - Layout analysis for sections
    - Figure/table extraction
    
    **Preprocessing:**
    - Remove boilerplate
    - Section segmentation
    - Reference parsing
    """)

with tab2:
    st.markdown("""
    ### LLM Fine-tuning
    
    **Base Model:** LLaMA 2 7B
    
    **Training Data:**
    - 500 manually annotated paper summaries
    - Structured schema with fields:
      - Problem/Motivation
      - Proposed Method
      - Key Results
      - Limitations
    
    **Training Config:**
    ```python
    training_args = TrainingArguments(
        num_train_epochs=3,
        per_device_train_batch_size=4,
        learning_rate=2e-5,
        fp16=True
    )
    ```
    
    **Performance:**
    - ROUGE-L: 0.42
    - Human eval agreement: 85%
    """)

with tab3:
    st.markdown("""
    ### Deployment Architecture
    
    **Infrastructure:**
    - AWS EC2 g4dn.xlarge (GPU)
    - Docker containers for services
    - Redis for caching
    - PostgreSQL for metadata
    
    **Monitoring:**
    - CloudWatch metrics
    - Error logging
    - Usage analytics
    
    **CI/CD:**
    - GitHub Actions
    - Automated testing
    - Rolling deployments
    """)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Results
st.markdown('<div class="section-header">RESULTS & IMPACT</div>', unsafe_allow_html=True)

results_cols = st.columns(3)

with results_cols[0]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">500+</div>
        <h3>Papers Processed</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[1]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">85%</div>
        <h3>Accuracy</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[2]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">70%</div>
        <h3>Time Saved</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Challenges & Learnings
st.markdown('<div class="section-header">CHALLENGES & LEARNINGS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <h3>Technical Challenges</h3>
        <p><strong>Challenge 1: PDF Parsing Accuracy</strong><br>
        Scientific papers have complex layouts. Initial parsing captured only 60% of content correctly.</p>
        <p><strong>Solution:</strong> Implemented multi-pass parsing with layout analysis and manual validation 
        for training data. Improved to 92% accuracy.</p>
        
        <p><strong>Challenge 2: LLM Hallucinations</strong><br>
        Model sometimes generated plausible but incorrect summaries.</p>
        <p><strong>Solution:</strong> Added citation grounding - every claim must link to source text. 
        Reduced hallucinations by 40%.</p>
        
        <h3>Key Learnings</h3>
        <ul>
            <li>Domain-specific fine-tuning is critical for specialized tasks</li>
            <li>Human-in-the-loop validation improves quality significantly</li>
            <li>Graph databases excel at relationship-heavy data</li>
            <li>Production ML requires extensive monitoring and error handling</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Links and Resources
st.markdown('<div class="section-header">LINKS & RESOURCES</div>', unsafe_allow_html=True)

link_cols = st.columns(4)

with link_cols[0]:
    st.link_button("📂 GitHub Repo", "https://github.com/yourusername/rag-ception", use_container_width=True)

with link_cols[1]:
    st.link_button("🚀 Live Demo", "#", use_container_width=True)

with link_cols[2]:
    st.link_button("📄 Paper", "#", use_container_width=True)

with link_cols[3]:
    st.link_button("📊 Presentation", "#", use_container_width=True)
