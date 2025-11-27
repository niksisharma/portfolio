"""
Portfolio Configuration File
Update this file with your personal information and preferences
"""

# ==================== PERSONAL INFORMATION ====================
PERSONAL_INFO = {
    "name": "Your Name",
    "title": "MS in Applied Data Science Candidate",
    "tagline": "From Hardware to Human-Centered AI",
    "email": "your.email@example.com",
    "phone": "(XXX) XXX-XXXX",
    "location": "Syracuse, NY",
    
    # Social Links
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "scholar": "",  # Optional: Google Scholar
    "twitter": "",  # Optional
    
    # About Me (short bio for homepage)
    "bio": """
    Building robust, fair, and human-centered AI/ML systems at the intersection of machine learning, 
    human-computer interaction, and responsible AI. Focused on developing scalable ML systems for 
    social impact applications including healthcare, accessibility, and scientific forecasting.
    """,
    
    # Profile image (place in assets/images/)
    "profile_image": "profile.jpg",  # or None if not using
}

# ==================== THEME & STYLING ====================
THEME = {
    # Main colors
    "background": "#1A1A2E",
    "primary": "#BB86FC",      # Soft Purple/Lavender
    "secondary": "#03DAC6",     # Mint/Teal
    "accent1": "#FF6B9D",       # Coral/Salmon
    "accent2": "#FFD93D",       # Soft Yellow
    "text": "#E8E8E8",          # Off-white
    "text_muted": "#A0A0A0",    # Gray
    
    # Fonts
    "font_family": "'Inter', 'Segoe UI', sans-serif",
    "heading_font": "'Poppins', 'Inter', sans-serif",
}

# ==================== PROGRAM INFORMATION ====================
PROGRAM_INFO = {
    "program_name": "Master of Science in Applied Data Science",
    "university": "Syracuse University",
    "graduation_date": "December 2025",
    "gpa": "3.875/4.0",
    
    # Program Learning Outcomes - UPDATE THESE WITH YOUR ACTUAL OUTCOMES
    "learning_outcomes": [
        {
            "outcome": "Advanced Machine Learning & Deep Learning",
            "description": "Develop expertise in modern ML/DL architectures and their applications",
            "projects": ["CapsNet Image Classifier", "Aurora Prediction", "Airbnb Occupancy"],
        },
        {
            "outcome": "ML Systems & Infrastructure",
            "description": "Design and deploy scalable, production-ready ML systems",
            "projects": ["RAG-ception", "Aurora Prediction"],
        },
        {
            "outcome": "Data Engineering & Management",
            "description": "Build robust data pipelines and databases for ML applications",
            "projects": ["CuseBus Platform", "Energy Forecasting"],
        },
        {
            "outcome": "Applied Research & Problem-Solving",
            "description": "Conduct rigorous research and develop novel solutions to real-world problems",
            "projects": ["RAG-ception", "CapsNet", "Medical Imaging"],
        },
        {
            "outcome": "Communication & Collaboration",
            "description": "Effectively communicate technical findings to diverse audiences",
            "projects": ["All projects include documentation and presentations"],
        },
    ]
}

# ==================== PROJECTS CONFIGURATION ====================
PROJECTS = [
    {
        "id": "rag_ception",
        "title": "RAG-ception: Automated Research Knowledge Management",
        "category": "ML Systems & Infrastructure",
        "tags": ["LLMs", "RAG", "Knowledge Graphs", "NLP", "Research Tools"],
        "status": "In Progress",
        "date": "Oct 2025 - Dec 2025",
        "github": "https://github.com/yourusername/rag-ception",
        "demo": None,  # Will be internal interactive page
        "thumbnail": "rag_ception_thumb.jpg",
        "short_description": "End-to-end ML system to automatically track, summarize, and connect RAG/LLM research papers from arXiv",
        "featured": True,
        "interactive": True,
    },
    {
        "id": "aurora_prediction",
        "title": "Aurora Prediction: Geomagnetic Activity Forecasting",
        "category": "ML Systems & Infrastructure",
        "tags": ["LSTM", "Time Series", "Deep Learning", "Forecasting", "Scientific ML"],
        "status": "In Progress",
        "date": "Fall 2025",
        "github": "https://github.com/yourusername/aurora-prediction",
        "demo": None,
        "thumbnail": "aurora_thumb.jpg",
        "short_description": "LSTM-based deep learning model to predict geomagnetic activity (Kp index) for aurora visibility forecasting",
        "featured": True,
        "interactive": True,
    },
    {
        "id": "capsnet",
        "title": "Capsule Network Image Classifier (CapsNet & Hybrid CapsViT)",
        "category": "Applied Machine Learning",
        "tags": ["Computer Vision", "Deep Learning", "PyTorch", "CapsNet", "ViT"],
        "status": "Completed",
        "date": "Spring 2025",
        "github": "https://github.com/yourusername/capsnet-classifier",
        "demo": None,
        "thumbnail": "capsnet_thumb.jpg",
        "short_description": "Re-implemented and extended CapsNet architecture, achieving ~2pp higher accuracy than ResNet-34 with ~40% fewer parameters",
        "featured": True,
        "interactive": False,
    },
    {
        "id": "airbnb",
        "title": "Airbnb Occupancy Prediction & Revenue Optimization",
        "category": "Applied Machine Learning",
        "tags": ["Neural Networks", "Regression", "Feature Engineering", "TensorFlow"],
        "status": "Completed",
        "date": "Spring 2025",
        "github": "https://github.com/yourusername/airbnb-prediction",
        "demo": None,
        "thumbnail": "airbnb_thumb.jpg",
        "short_description": "Deep neural network for occupancy rate prediction across 25K+ multi-city Airbnb listings",
        "featured": False,
        "interactive": False,
    },
    {
        "id": "cusebus",
        "title": "CuseBus: Intelligent Transit Planning Platform",
        "category": "Domain-Specific Applications",
        "tags": ["Database Design", "Web Development", "Data Integration", "Transit"],
        "status": "In Progress",
        "date": "Fall 2025",
        "github": "https://github.com/yourusername/cusebus",
        "demo": None,
        "thumbnail": "cusebus_thumb.jpg",
        "short_description": "Centralized platform to optimize student commute planning using Centro buses and Syracuse trolleys",
        "featured": False,
        "interactive": False,
    },
    {
        "id": "energy_forecasting",
        "title": "Energy Demand Forecasting for Utility Company",
        "category": "Domain-Specific Applications",
        "tags": ["Time Series", "R", "Shiny", "Statistical Modeling", "Forecasting"],
        "status": "Completed",
        "date": "Spring 2025",
        "github": None,
        "demo": None,
        "thumbnail": "energy_thumb.jpg",
        "short_description": "Predictive models to forecast peak electricity demand for South Carolina residential properties",
        "featured": False,
        "interactive": False,
    },
    {
        "id": "medical_imaging",
        "title": "Medical Imaging: Automated Fracture Detection",
        "category": "Domain-Specific Applications",
        "tags": ["Medical Imaging", "Computer Vision", "ML", "Healthcare"],
        "status": "Completed",
        "date": "May 2022 - Jul 2023",
        "github": None,
        "demo": None,
        "thumbnail": "medical_thumb.jpg",
        "short_description": "ML model for automated fracture detection from 3000+ CT scans",
        "featured": False,
        "interactive": False,
    },
]

# ==================== VIDEO & BLOG CONFIGURATION ====================
VIDEO_INFO = {
    "youtube_url": None,  # Add your YouTube URL here (can be unlisted)
    "duration": "1-2 minutes",
    "topics_covered": [
        "Overview of MS ADS program",
        "Key learnings and takeaways",
        "Favorite experiences",
        "Career goals and next steps"
    ]
}

BLOG_INFO = {
    "title": "Reflecting on My Journey Through the MS in Applied Data Science Program",
    "word_count_target": 3000,
    "sections": [
        "What I Expected to Learn",
        "What I Actually Learned",
        "Learning Outcomes Achievement",
        "Key Projects and Their Impact",
        "Outside the Classroom",
        "Favorite Classes and Experiences",
        "Biggest Surprises",
        "Looking Forward"
    ]
}

# ==================== SKILLS ====================
SKILLS = {
    "Programming Languages": ["Python", "R", "JavaScript", "Java", "C++", "SQL", "MATLAB"],
    "ML/AI Frameworks": ["PyTorch", "TensorFlow", "Keras", "scikit-learn", "Hugging Face", "LangChain"],
    "Data Science": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Statistical Modeling"],
    "NLP & LLMs": ["Sentence Transformers", "Word Embeddings", "Fine-tuning", "RAG Systems"],
    "ML Engineering": ["Model Deployment", "MLOps", "Experiment Tracking", "Hyperparameter Tuning"],
    "Databases": ["MySQL", "PostgreSQL", "ChromaDB", "ETL Pipelines"],
    "DevOps & Cloud": ["AWS", "Azure", "Docker", "Jenkins", "CI/CD", "Git/GitHub"],
    "Visualization": ["Power BI", "Tableau", "Streamlit", "Shiny"],
}

# ==================== EXPERIENCE ====================
EXPERIENCE = [
    {
        "title": "Research Intern",
        "organization": "Defence Research and Development Organisation (DRDO)",
        "location": "Bengaluru, India",
        "dates": "Sep 2021 - Jul 2022",
        "type": "Research",
        "highlights": [
            "Designed two novel direction-finding algorithms for airborne electronic warfare systems",
            "Improved target localization accuracy by 15% over baseline methods",
            "Led 4-member research team through systematic experimental design",
            "Published research at IEEE MAPCON 2022"
        ]
    },
    {
        "title": "DevOps Engineer",
        "organization": "Continental Automotive",
        "location": "Bengaluru, India",
        "dates": "Jul 2023 - Jul 2024",
        "type": "Industry",
        "highlights": [
            "Designed automated unit testing framework reducing manual QA effort by 40%",
            "Built Power BI dashboard for 1000+ JSON files",
            "Architected Jenkins CI/CD pipelines achieving 95% uptime"
        ]
    },
    {
        "title": "Software Developer & ML Research Engineer",
        "organization": "Cirruslabs Pvt. Ltd.",
        "location": "Bengaluru, India",
        "dates": "May 2022 - Jul 2023",
        "type": "Industry",
        "highlights": [
            "Led medical imaging research analyzing 3000+ CT scans",
            "Developed 80+ REST APIs for production applications",
            "Served as Scrum Master for 6-member team"
        ]
    },
]

# ==================== CONTACT PREFERENCES ====================
CONTACT_FORM = {
    "enabled": False,  # Set to True if you want a contact form
    "email_service": None,  # e.g., "formspree", "emailjs", etc.
}

# ==================== ANALYTICS ====================
ANALYTICS = {
    "google_analytics_id": None,  # Add your GA4 ID if you want tracking
}

# ==================== SEO ====================
SEO = {
    "page_title": "Your Name - Data Science Portfolio",
    "page_description": "MS in Applied Data Science portfolio showcasing ML systems, research projects, and AI applications",
    "keywords": ["data science", "machine learning", "AI", "portfolio", "research"],
}
