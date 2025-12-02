# pages/projects/RAGception.py

import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
import config

st.set_page_config(
    page_title="RAG-ception - Project Details",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Get project data
project = next((p for p in config.PROJECTS if p['id'] == 'rag-ception'), None)

# Top Navigation
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

# Project Header
st.markdown(f"""
<div class="hero-window">
    <div class="window-titlebar">
        <div class="window-title">PROJECT.EXE - {project['title'].upper()}</div>
        <div class="window-buttons">
            <div class="window-btn"></div>
            <div class="window-btn"></div>
            <div class="window-btn"></div>
        </div>
    </div>
    <div class="window-content">
        <h1>{project['title']}</h1>
        <div class="subtitle">{project['subtitle']}</div>
        <p>{project['short_description']}</p>
        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-label">Status:</span>
                <span class="stat-value">{project['status']}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Timeline:</span>
                <span class="stat-value">{project['date']}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Course:</span>
                <span class="stat-value">{project.get('course', 'Independent')}</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Learning Outcomes Achieved
st.markdown('<div class="section-header">LEARNING OUTCOMES ACHIEVED</div>', unsafe_allow_html=True)

# Display learning outcomes this project addresses
lo_cols = st.columns(len(project['learning_outcomes']))
for idx, lo_id in enumerate(project['learning_outcomes']):
    lo = config.LEARNING_OUTCOMES[lo_id]
    with lo_cols[idx]:
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon" style="font-size: 3rem;">{lo['number']}</div>
            <h3>LO{lo['number']}</h3>
        </div>
        """, unsafe_allow_html=True)

# Detailed explanations
st.markdown("""
<div class="project-info" style="margin-top: 2rem;">
    <div class="project-body">
        <h3 style="color: var(--primary-teal);">How This Project Demonstrates Learning Outcomes:</h3>
    </div>
</div>
""", unsafe_allow_html=True)

for lo_id in project['learning_outcomes']:
    lo = config.LEARNING_OUTCOMES[lo_id]
    explanation = project['lo_explanations'][lo_id]
    
    st.markdown(f"""
    <div class="skill-card" style="text-align: left; margin-bottom: 1rem;">
        <h3 style="margin-bottom: 0.5rem;">LO{lo['number']}: {lo['title']}</h3>
        <div class="skill-level" style="color: var(--text-gray); font-size: 0.9rem; margin-bottom: 0.5rem;">
            {lo['description']}
        </div>
        <p style="color: var(--text-dark); margin-top: 0.5rem;">
            ✓ {explanation}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Screenshot Gallery
st.markdown('<div class="section-header">SCREENSHOTS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="terminal">
$ ls images/
Loading project screenshots...
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for i in range(3):
    with cols[i]:
        st.markdown("""
        <div class="project-image">
            <div class="project-placeholder">SCREENSHOT</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Problem & Solution
st.markdown('<div class="section-header">PROBLEM & SOLUTION</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="project-info">
        <div class="project-header">
            <h3>Problem Statement</h3>
        </div>
        <div class="project-body">
            <p>{project['problem_statement']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="project-info">
        <div class="project-header">
            <h3>Solution Approach</h3>
        </div>
        <div class="project-body">
            <p>{project['solution']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Technical Architecture
st.markdown('<div class="section-header">TECHNICAL ARCHITECTURE</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="terminal">
$ cat system_architecture.txt

Data Pipeline:
{project['technical_details']['data_pipeline']}

Model:
{project['technical_details']['model']}

Storage:
{project['technical_details']['storage']}

Deployment:
{project['technical_details']['deployment']}
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-image" style="margin-top: 2rem;">
    <div class="project-placeholder">ARCHITECTURE DIAGRAM</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Tech Stack
st.markdown('<div class="section-header">TECHNOLOGIES USED</div>', unsafe_allow_html=True)

tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])

st.markdown(f"""
<div class="project-info">
    <div class="project-body">
        <div class="tech-tags">
            {tech_tags}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Results & Impact
st.markdown('<div class="section-header">RESULTS & IMPACT</div>', unsafe_allow_html=True)

results_cols = st.columns(3)

results_list = list(project['results'].items())
for idx, (key, value) in enumerate(results_list):
    with results_cols[idx % 3]:
        st.markdown(f"""
        <div class="interest-item">
            <div class="interest-icon" style="font-size: 3rem;">{value}</div>
            <h3>{key.replace('_', ' ').title()}</h3>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Challenges & Learnings
st.markdown('<div class="section-header">CHALLENGES & LEARNINGS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <h3 style="color: var(--primary-teal); margin-bottom: 1rem;">Technical Challenges</h3>
    </div>
</div>
""", unsafe_allow_html=True)

for idx, challenge in enumerate(project['challenges'], 1):
    st.markdown(f"""
    <div class="skill-card" style="text-align: left; margin-bottom: 1rem;">
        <h3 style="margin-bottom: 0.5rem;">Challenge {idx}</h3>
        <p style="color: var(--text-dark);">{challenge}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Code Samples
st.markdown('<div class="section-header">CODE SAMPLES</div>', unsafe_allow_html=True)

with st.expander("📄 Data Pipeline Implementation"):
    st.code("""
# Daily arXiv paper fetching
import arxiv

def fetch_rag_papers(max_results=100):
    search = arxiv.Search(
        query="RAG OR retrieval-augmented generation",
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'authors': [a.name for a in result.authors],
            'abstract': result.summary,
            'pdf_url': result.pdf_url,
            'published': result.published
        })
    
    return papers
    """, language="python")

with st.expander("📄 LLM Fine-tuning Setup"):
    st.code("""
# Fine-tuning setup for structured summaries
from transformers import AutoModelForCausalLM, TrainingArguments

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")

training_args = TrainingArguments(
    output_dir="./rag-summarizer",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    learning_rate=2e-5,
    fp16=True,
    logging_steps=100
)

# Training on structured summary dataset
# Schema: {problem, method, results, limitations}
    """, language="python")

with st.expander("📄 Knowledge Graph Construction"):
    st.code("""
# Building relationships in Neo4j
from neo4j import GraphDatabase

def add_paper_relationship(tx, paper1_id, paper2_id, rel_type):
    query = '''
    MATCH (p1:Paper {id: $paper1_id})
    MATCH (p2:Paper {id: $paper2_id})
    CREATE (p1)-[r:RELATED_TO {type: $rel_type}]->(p2)
    RETURN r
    '''
    result = tx.run(query, 
                   paper1_id=paper1_id,
                   paper2_id=paper2_id,
                   rel_type=rel_type)
    return result
    """, language="python")

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Links and Resources
st.markdown('<div class="section-header">LINKS & RESOURCES</div>', unsafe_allow_html=True)

link_cols = st.columns(4)

with link_cols[0]:
    if project.get('github'):
        st.link_button("📂 GitHub", project['github'], use_container_width=True)
    else:
        st.button("📂 GitHub", disabled=True, use_container_width=True)

with link_cols[1]:
    if project.get('demo'):
        st.link_button("🚀 Demo", project['demo'], use_container_width=True)
    else:
        st.button("🚀 Demo", disabled=True, use_container_width=True)

with link_cols[2]:
    st.button("📄 Paper", disabled=True, use_container_width=True)

with link_cols[3]:
    st.button("📊 Slides", disabled=True, use_container_width=True)

# Back to projects
st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)
st.link_button("← Back to All Projects", "/Projects", use_container_width=False)