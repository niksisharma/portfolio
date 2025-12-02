import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
import config

st.set_page_config(
    page_title="CapsNet - Project Details",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

project = next((p for p in config.PROJECTS if p['id'] == 'capsnet'), None)

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

# Learning Outcomes
st.markdown('<div class="section-header">LEARNING OUTCOMES ACHIEVED</div>', unsafe_allow_html=True)

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

# Technical Details
st.markdown('<div class="section-header">TECHNICAL SPECIFICATIONS</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="terminal">
$ cat model_specs.txt

Architecture: {project['technical_details']['architecture']}
Dataset: {project['technical_details']['dataset']}
Baseline: {project['technical_details']['baseline']}
Innovation: {project['technical_details']['innovation']}
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Results
st.markdown('<div class="section-header">RESULTS & PERFORMANCE</div>', unsafe_allow_html=True)

results_cols = st.columns(3)

with results_cols[0]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">+2pp</div>
        <h3>Accuracy Gain</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[1]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">-40%</div>
        <h3>Fewer Parameters</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[2]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">-30%</div>
        <h3>Training Time</h3>
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

# Challenges
st.markdown('<div class="section-header">CHALLENGES & LEARNINGS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <h3 style="color: var(--primary-teal); margin-bottom: 1rem;">Key Lesson: Reproducing Research is Hard</h3>
        <p>This project taught me that paper results are difficult to reproduce. Missing implementation details, hyperparameters that matter more than expected, and computational resources the paper doesn't mention all compound to make reproduction challenging.</p>
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

with st.expander("📄 Capsule Layer Implementation"):
    st.code("""
# Dynamic routing between capsules
import torch
import torch.nn as nn

class CapsuleLayer(nn.Module):
    def __init__(self, num_capsules, num_route_nodes, in_channels, out_channels):
        super(CapsuleLayer, self).__init__()
        
        self.num_route_nodes = num_route_nodes
        self.num_capsules = num_capsules
        
        self.route_weights = nn.Parameter(
            torch.randn(num_capsules, num_route_nodes, 
                       in_channels, out_channels)
        )
    
    def squash(self, tensor, dim=-1):
        squared_norm = (tensor ** 2).sum(dim=dim, keepdim=True)
        scale = squared_norm / (1 + squared_norm)
        return scale * tensor / torch.sqrt(squared_norm)
    
    def forward(self, x):
        # Dynamic routing algorithm
        # ... (routing iterations)
        return self.squash(outputs)
    """, language="python")

with st.expander("📄 Training Configuration"):
    st.code("""
# CapsNet training setup
import torch.optim as optim

model = CapsNet(num_classes=100)
optimizer = optim.Adam(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5)

# Margin loss for capsule network
def capsule_loss(outputs, targets, m_plus=0.9, m_minus=0.1, lambda_=0.5):
    left = F.relu(m_plus - outputs) ** 2
    right = F.relu(outputs - m_minus) ** 2
    
    loss = targets * left + lambda_ * (1 - targets) * right
    return loss.sum(dim=1).mean()
    """, language="python")

with st.expander("📄 Comparison with ResNet"):
    st.code("""
# Performance comparison
results = {
    'CapsNet': {
        'top1_accuracy': 0.692,
        'parameters': '8.2M',
        'training_time': '12h'
    },
    'ResNet-34': {
        'top1_accuracy': 0.672,
        'parameters': '21.3M',
        'training_time': '8h'
    }
}

# CapsNet: +2pp accuracy, -40% parameters, but slower training
# Trade-off: Better accuracy and efficiency vs longer training
    """, language="python")

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Links
st.markdown('<div class="section-header">LINKS & RESOURCES</div>', unsafe_allow_html=True)

link_cols = st.columns(4)

with link_cols[0]:
    if project.get('github'):
        st.link_button("📂 GitHub", project['github'], use_container_width=True)
    else:
        st.button("📂 GitHub", disabled=True, use_container_width=True)

with link_cols[1]:
    st.button("🚀 Demo", disabled=True, use_container_width=True)

with link_cols[2]:
    st.button("📄 Original Paper", disabled=True, use_container_width=True)

with link_cols[3]:
    st.button("📊 Results", disabled=True, use_container_width=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)
st.link_button("← Back to All Projects", "/Projects", use_container_width=False)