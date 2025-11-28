"""
Portfolio Configuration File
Update this file with your personal information
"""

# Personal Information
PERSONAL_INFO = {
    "name": "Your Name",
    "title": "MS Applied Data Science | Syracuse University",
    "tagline": "Building robust, fair, and human-centered AI/ML systems",
    "email": "your.email@example.com",
    "phone": "+1 (123) 456-7890",
    "location": "Syracuse, NY",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "website": "https://yourwebsite.com"
}

# Stats for Homepage
STATS = {
    "projects": 7,
    "completed": 5,
    "gpa": "3.87",
    "publications": 1
}

# Theme Colors - Option A: Windows 95 Style
COLORS = {
    "bg_beige": "#F4E4C1",
    "bg_tan": "#E8D8B8",
    "bg_darker": "#D4C4A1",
    "primary_teal": "#00A9A5",
    "primary_teal_light": "#00C9C4",
    "accent_orange": "#FF6700",
    "text_dark": "#2B2B2B",
    "text_gray": "#5A5A5A",
    "text_light": "#666666",
    "border_black": "#000000",
    "white": "#FFFFFF"
}

# Skills
SKILLS = [
    {
        "name": "Python",
        "level": "Advanced",
        "percentage": 90
    },
    {
        "name": "PyTorch",
        "level": "Advanced",
        "percentage": 85
    },
    {
        "name": "TensorFlow",
        "level": "Advanced",
        "percentage": 80
    },
    {
        "name": "LangChain / LLMs",
        "level": "Intermediate",
        "percentage": 75
    },
    {
        "name": "SQL",
        "level": "Advanced",
        "percentage": 85
    },
    {
        "name": "AWS / Cloud",
        "level": "Intermediate",
        "percentage": 70
    },
    {
        "name": "Scikit-learn",
        "level": "Advanced",
        "percentage": 85
    },
    {
        "name": "Docker",
        "level": "Intermediate",
        "percentage": 70
    }
]

# Research Interests
INTERESTS = [
    {"icon": "🖥️", "name": "ML Systems"},
    {"icon": "🧠", "name": "NLP & LLMs"},
    {"icon": "⚙️", "name": "MLOps"},
    {"icon": "🤝", "name": "Human-AI"},
    {"icon": "🌍", "name": "Social Impact"},
    {"icon": "🔬", "name": "Research"}
]

# Projects
PROJECTS = [
    {
        "id": "rag-ception",
        "title": "RAG-ception",
        "subtitle": "Automated Research Knowledge Management",
        "date": "Oct 2025 - Dec 2025",
        "status": "In Progress",
        "description": "End-to-end ML system to automatically track, summarize, and connect RAG/LLM research papers from arXiv. Fine-tuning LLMs to generate structured research summaries with consistent schema. Building dynamic knowledge graph using Graphiti API to identify conceptual relationships and citation networks across 500+ papers.",
        "tech_stack": ["Python", "PyTorch", "LangChain", "Graphiti", "ChromaDB", "Streamlit"],
        "image": "placeholder",  # Replace with actual image path
        "github": "https://github.com/yourusername/rag-ception",
        "demo": None,
        "featured": True
    },
    {
        "id": "aurora-prediction",
        "title": "Aurora Prediction",
        "subtitle": "Geomagnetic Activity Forecasting",
        "date": "Fall 2025",
        "status": "In Progress",
        "description": "LSTM-based deep learning model to predict geomagnetic activity (Kp index) for aurora visibility forecasting. Implementing multi-horizon forecasting pipeline predicting Kp index at 1h, 3h, 6h, and 12h intervals using time-series data from solar wind parameters and geomagnetic measurements.",
        "tech_stack": ["TensorFlow", "Keras", "LSTM", "Python", "Time Series"],
        "image": "placeholder",
        "github": "https://github.com/yourusername/aurora-prediction",
        "demo": None,
        "featured": True
    },
    {
        "id": "capsnet",
        "title": "CapsNet Classifier",
        "subtitle": "Advanced Image Classification",
        "date": "Spring 2025",
        "status": "Completed",
        "description": "Re-implemented and extended CapsNet architecture, training on CIFAR-100 (60K images, 100 classes) to investigate pose-aware feature representations. Achieved ~2pp higher top-1 accuracy than ResNet-34 baseline while using ~40% fewer parameters. Proposed Hybrid Capsule + Vision Transformer variant reducing training time by ~30%.",
        "tech_stack": ["PyTorch", "Computer Vision", "Deep Learning", "Python"],
        "image": "placeholder",
        "github": "https://github.com/yourusername/capsnet",
        "demo": None,
        "featured": True
    },
    {
        "id": "airbnb-occupancy",
        "title": "Airbnb Occupancy Prediction",
        "subtitle": "Time Series Forecasting",
        "date": "Fall 2024",
        "status": "Completed",
        "description": "Built machine learning models to predict Airbnb occupancy rates using historical booking data and external factors. Implemented multiple forecasting approaches including ARIMA, Prophet, and LSTM networks.",
        "tech_stack": ["Python", "Prophet", "ARIMA", "LSTM", "Pandas"],
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False
    },
    {
        "id": "cusebus",
        "title": "CuseBus Route Optimization",
        "subtitle": "Operations Research",
        "date": "Spring 2024",
        "status": "Completed",
        "description": "Analyzed Syracuse University bus system data to optimize routes and schedules. Used network analysis and optimization algorithms to improve service efficiency.",
        "tech_stack": ["Python", "NetworkX", "OR-Tools", "Visualization"],
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False
    },
    {
        "id": "energy-forecasting",
        "title": "Energy Consumption Forecasting",
        "subtitle": "Sustainability Analytics",
        "date": "Fall 2024",
        "status": "Completed",
        "description": "Developed predictive models for building energy consumption to support sustainability initiatives. Incorporated weather data, occupancy patterns, and historical usage.",
        "tech_stack": ["Python", "XGBoost", "Feature Engineering", "Time Series"],
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False
    },
    {
        "id": "medical-imaging",
        "title": "Medical Image Analysis",
        "subtitle": "Computer Vision for Healthcare",
        "date": "Spring 2025",
        "status": "In Progress",
        "description": "Developing deep learning models for automated medical image analysis. Focus on segmentation and classification tasks for diagnostic support.",
        "tech_stack": ["PyTorch", "Computer Vision", "U-Net", "Medical Imaging"],
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False
    }
]

# Learning Outcomes (for Overview page)
LEARNING_OUTCOMES = """
Throughout my MS in Applied Data Science program at Syracuse University, I have developed comprehensive skills across the entire machine learning lifecycle:

**Technical Foundations:**
- Advanced machine learning algorithms and deep learning architectures
- Statistical modeling and experimental design
- Big data processing and distributed computing
- Cloud-based ML deployment and MLOps practices

**Applied Skills:**
- End-to-end ML project development from problem formulation to deployment
- Working with diverse data types: text, images, time series, graphs
- Model interpretability and fairness considerations
- Production ML systems and monitoring

**Research & Communication:**
- Critical evaluation of ML research papers
- Technical writing and documentation
- Presenting complex technical concepts to diverse audiences
- Collaborative development using version control and agile practices
"""

# Blog Post Sections (for Reflection page)
BLOG_POST = {
    "title": "Building AI Systems for Social Impact: Lessons from My Graduate Journey",
    "date": "December 2025",
    "read_time": "15 min read",
    "sections": [
        {
            "heading": "Introduction",
            "content": """
            Write your introduction here. This should hook the reader and outline what they'll learn.
            Talk about your journey, what motivated you, and what this post will cover.
            """
        },
        {
            "heading": "Section 1: Your First Main Point",
            "content": """
            Expand on your first main idea. Include:
            - Specific examples from your projects
            - Challenges you faced
            - What you learned
            - How it changed your perspective
            """
        },
        {
            "heading": "Section 2: Your Second Main Point",
            "content": """
            Continue developing your narrative. Connect to:
            - Technical concepts you learned
            - Real-world applications
            - Industry trends
            - Future implications
            """
        },
        # Add more sections as needed
    ]
}

# About Me
ABOUT_ME = {
    "bio": """
    I am a Master's student in Applied Data Science at Syracuse University, passionate about building 
    fair, robust, and human-centered AI/ML systems. My work focuses on the intersection of machine learning, 
    natural language processing, and responsible AI.
    
    With a background in [YOUR BACKGROUND], I bring [YOUR UNIQUE PERSPECTIVE] to data science challenges. 
    I'm particularly interested in developing ML systems that create positive social impact while maintaining 
    ethical standards and fairness.
    """,
    "education": [
        {
            "degree": "MS in Applied Data Science",
            "school": "Syracuse University",
            "location": "Syracuse, NY",
            "date": "Expected Dec 2025",
            "gpa": "3.87/4.0"
        },
        {
            "degree": "BS in [Your Major]",
            "school": "[Your University]",
            "location": "[Location]",
            "date": "[Graduation Date]",
            "gpa": "[Your GPA]"
        }
    ],
    "experience": [
        {
            "title": "[Your Role]",
            "company": "[Company Name]",
            "location": "[Location]",
            "date": "[Dates]",
            "description": [
                "Achievement or responsibility 1",
                "Achievement or responsibility 2",
                "Achievement or responsibility 3"
            ]
        }
    ]
}
