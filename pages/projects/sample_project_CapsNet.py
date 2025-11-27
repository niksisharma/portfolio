"""
Sample Project Page: CapsNet Image Classifier
This is a template - duplicate and modify for other projects
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.helpers import *
import config

set_page_config(page_title="CapsNet Classifier", page_icon="🖼️")
load_css()

# Get project details from config
project = get_project_by_id("capsnet")

if not project:
    st.error("Project not found in configuration")
    st.stop()

# Header
render_header(project['title'], project['category'])

# Status and Date
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    render_tags(project['tags'][:6])

with col2:
    status_color = config.THEME['secondary'] if project['status'] == 'Completed' else config.THEME['accent2']
    st.markdown(f"**Status:** <span style='color: {status_color}; font-weight: 600;'>{project['status']}</span>", 
               unsafe_allow_html=True)

with col3:
    st.markdown(f"**Date:** {project['date']}")

st.markdown("<hr>", unsafe_allow_html=True)

# Quick Links
if project['github'] or project['demo']:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if project['github']:
            st.markdown(f"[💻 View on GitHub]({project['github']})")
    
    with col2:
        if project['demo']:
            st.markdown(f"[🔗 Live Demo]({project['demo']})")
    
    with col3:
        st.markdown("[📧 Contact Me](mailto:" + config.PERSONAL_INFO['email'] + ")")
    
    st.markdown("<hr>", unsafe_allow_html=True)

# Project Overview
st.markdown("## 📋 Project Overview")

st.markdown("""
This project involved re-implementing and extending the Capsule Network (CapsNet) architecture, 
originally proposed by Sabour et al. (2017), to investigate pose-aware feature representations in 
deep learning models.

**Key Highlights:**
- Trained on CIFAR-100 dataset (60,000 images, 100 classes)
- Achieved ~2 percentage points higher top-1 accuracy than ResNet-34 baseline
- Reduced model parameters by ~40% compared to ResNet-34
- Proposed novel Hybrid Capsule + Vision Transformer (CapsViT) variant
- Reduced training time by ~30% through architectural improvements
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Problem Statement
st.markdown("## 🎯 Problem Statement")

st.markdown("""
Traditional Convolutional Neural Networks (CNNs) struggle with:
1. **Spatial relationship understanding**: CNNs use pooling layers that discard precise spatial information
2. **Pose variations**: Limited ability to handle rotations, translations, and other geometric transformations
3. **Parameter efficiency**: Large models require millions of parameters for high accuracy

**Research Question:** Can Capsule Networks provide better pose-aware representations while maintaining 
or improving accuracy with fewer parameters?
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Approach & Methodology
st.markdown("## 🔬 Approach & Methodology")

st.markdown("### Architecture Design")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Original CapsNet Implementation:**
    - Primary capsule layer with 32 channels
    - Dynamic routing between capsules
    - 6×6 dimensional capsule outputs
    - Reconstruction loss for regularization
    """)

with col2:
    st.markdown("""
    **Hybrid CapsViT Extension:**
    - Vision Transformer encoder for initial features
    - Capsule layers for spatial hierarchy
    - Attention-based dynamic routing
    - Multi-scale feature extraction
    """)

st.markdown("### Training Process")

st.markdown("""
1. **Data Preprocessing:**
   - CIFAR-100 dataset (32×32 RGB images, 100 classes)
   - Data augmentation: random crops, horizontal flips, color jittering
   - Normalization using ImageNet statistics

2. **Training Configuration:**
   - Optimizer: Adam (lr=0.001, with ReduceLROnPlateau)
   - Batch size: 128
   - Epochs: 100 with early stopping
   - Loss function: Margin loss + reconstruction loss (weighted 0.5)

3. **Evaluation:**
   - Top-1 and Top-5 accuracy on test set
   - Parameter count comparison
   - Inference time benchmarking
   - Ablation studies on routing iterations
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Results
st.markdown("## 📊 Results")

# Create metrics
col1, col2, col3 = st.columns(3)

with col1:
    render_metric("Top-1 Accuracy", "72.4%", "🎯")
    st.caption("vs. ResNet-34: 70.2%")

with col2:
    render_metric("Parameters", "4.2M", "⚙️")
    st.caption("vs. ResNet-34: 7.1M (40% reduction)")

with col3:
    render_metric("Training Time", "8.5 hrs", "⏱️")
    st.caption("CapsViT: 6 hrs (30% faster)")

st.markdown("### Key Findings")

st.markdown("""
1. **Improved Accuracy:** CapsNet achieved ~2pp higher accuracy than ResNet-34 on CIFAR-100
2. **Parameter Efficiency:** Required 40% fewer parameters while maintaining competitive performance
3. **Pose Awareness:** Better handling of rotated and translated objects (confirmed through adversarial testing)
4. **Hybrid Architecture:** CapsViT variant reduced training time while maintaining accuracy gains

**Limitations Identified:**
- Higher computational cost per iteration due to dynamic routing
- More sensitive to hyperparameter choices
- Requires more careful initialization than standard CNNs
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Technologies & Tools
st.markdown("## 🛠️ Technologies & Tools")

col1, col2 = st.columns(2)

with col1:
    render_skill_category("Core Technologies", [
        "Python 3.9",
        "PyTorch 2.0",
        "NumPy",
        "Matplotlib"
    ])
    
    render_skill_category("Model Architecture", [
        "Capsule Networks",
        "Vision Transformers",
        "Dynamic Routing",
        "Attention Mechanisms"
    ])

with col2:
    render_skill_category("Experiment Tracking", [
        "Weights & Biases",
        "TensorBoard",
        "MLflow"
    ])
    
    render_skill_category("Deployment", [
        "ONNX Export",
        "Model Optimization",
        "GPU Acceleration"
    ])

st.markdown("<hr>", unsafe_allow_html=True)

# Learning Outcomes
st.markdown("## 🎓 Learning Outcomes Demonstrated")

outcomes = [
    {
        "outcome": "Advanced Machine Learning & Deep Learning",
        "description": "Implemented state-of-the-art neural network architecture from research papers, " +
                      "demonstrating understanding of advanced concepts like dynamic routing and capsule representations."
    },
    {
        "outcome": "Research & Problem-Solving",
        "description": "Conducted systematic experiments, ablation studies, and comparative analysis. " +
                      "Proposed novel hybrid architecture based on empirical findings."
    },
    {
        "outcome": "Technical Communication",
        "description": "Documented implementation details, results, and limitations. Presented findings " +
                      "to peers with clear visualizations and explanations."
    },
]

for outcome in outcomes:
    st.markdown(f"**{outcome['outcome']}**")
    st.markdown(outcome['description'])
    st.markdown("")

st.markdown("<hr>", unsafe_allow_html=True)

# Challenges & Solutions
st.markdown("## 💡 Challenges & Solutions")

challenges = [
    {
        "challenge": "Dynamic Routing Instability",
        "solution": "Implemented careful initialization and gradient clipping. Added routing coefficient regularization."
    },
    {
        "challenge": "Memory Constraints",
        "solution": "Used gradient accumulation and mixed precision training. Optimized batch sizes for available GPU memory."
    },
    {
        "challenge": "Slow Convergence",
        "solution": "Implemented learning rate scheduling and warm-up. Added batch normalization to capsule layers."
    },
]

for i, item in enumerate(challenges, 1):
    st.markdown(f"**Challenge {i}: {item['challenge']}**")
    st.markdown(f"*Solution:* {item['solution']}")
    st.markdown("")

st.markdown("<hr>", unsafe_allow_html=True)

# Future Work
st.markdown("## 🚀 Future Directions")

st.markdown("""
Potential extensions and improvements:
1. **Scale to larger datasets:** Apply to ImageNet-1K for more comprehensive evaluation
2. **Architecture search:** Use NAS to optimize capsule dimensions and routing iterations
3. **Multi-task learning:** Extend for simultaneous classification and pose estimation
4. **Efficiency improvements:** Explore quantization and pruning for deployment
5. **Theoretical analysis:** Investigate why capsule networks work better for certain data distributions
""")

st.markdown("<hr>", unsafe_allow_html=True)

# References
st.markdown("## 📚 References")

st.markdown("""
1. Sabour, S., Frosst, N., & Hinton, G. E. (2017). "Dynamic Routing Between Capsules." *NeurIPS*.
2. Krizhevsky, A. (2009). "Learning Multiple Layers of Features from Tiny Images." *Technical Report*.
3. He, K., et al. (2016). "Deep Residual Learning for Image Recognition." *CVPR*.
4. Dosovitskiy, A., et al. (2021). "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale." *ICLR*.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Contact & Collaboration
st.markdown("## 📬 Questions or Collaboration?")

st.markdown(f"""
Interested in this project or want to discuss CapsNet architectures? Feel free to reach out!

- **Email:** {config.PERSONAL_INFO['email']}
- **GitHub:** {config.PERSONAL_INFO['github']}
- **LinkedIn:** {config.PERSONAL_INFO['linkedin']}
""")

# Navigation hint
render_info_box(
    """
    <strong>📂 Explore More Projects:</strong><br>
    Check out my other projects in the Projects section, including ML systems, 
    time-series forecasting, and real-world applications!
    """,
    box_type="info"
)
