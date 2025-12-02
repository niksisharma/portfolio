"""
Portfolio Configuration File
Update this file with your personal information
"""
"""
Portfolio Configuration File - UPDATED WITH LEARNING OUTCOMES
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

# Program Learning Outcomes
LEARNING_OUTCOMES = {
    "LO1": {
        "number": 1,
        "title": "Data Collection & Storage",
        "description": "Collect, store, and access data by identifying and leveraging applicable technologies"
    },
    "LO2": {
        "number": 2,
        "title": "Actionable Insights",
        "description": "Create actionable insight across a range of contexts using data and the full data science life cycle"
    },
    "LO3": {
        "number": 3,
        "title": "Visualization & Predictive Models",
        "description": "Apply visualization and predictive models to help generate actionable insight"
    },
    "LO4": {
        "number": 4,
        "title": "Programming Proficiency",
        "description": "Use programming languages such as R and Python to support the generation of actionable insight"
    },
    "LO5": {
        "number": 5,
        "title": "Communication",
        "description": "Communicate insights gained via visualization and analytics to a broad range of audiences"
    },
    "LO6": {
        "number": 6,
        "title": "Ethics & Responsible AI",
        "description": "Apply ethics in the development, use and evaluation of data and predictive models"
    }
}

# Skills
SKILLS = [
    {"name": "Python", "level": "Advanced", "percentage": 90},
    {"name": "PyTorch", "level": "Advanced", "percentage": 85},
    {"name": "TensorFlow", "level": "Advanced", "percentage": 80},
    {"name": "LangChain / LLMs", "level": "Intermediate", "percentage": 75},
    {"name": "SQL", "level": "Advanced", "percentage": 85},
    {"name": "AWS / Cloud", "level": "Intermediate", "percentage": 70},
    {"name": "Scikit-learn", "level": "Advanced", "percentage": 85},
    {"name": "Docker", "level": "Intermediate", "percentage": 70}
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

# Projects with Learning Outcome Mappings
PROJECTS = [
    {
        "id": "rag-ception",
        "title": "RAG-ception",
        "subtitle": "Automated Research Knowledge Management",
        "date": "Oct 2025 - Dec 2025",
        "status": "In Progress",
        "short_description": "End-to-end ML system to automatically track, summarize, and connect RAG/LLM research papers from arXiv.",
        "description": "End-to-end ML system to automatically track, summarize, and connect RAG/LLM research papers from arXiv. Fine-tuning LLMs to generate structured research summaries with consistent schema. Building dynamic knowledge graph using Graphiti API to identify conceptual relationships and citation networks across 500+ papers.",
        "problem_statement": "Research in RAG and LLMs is advancing rapidly with hundreds of papers monthly. Researchers struggle to keep up, identify key papers, and understand connections between approaches.",
        "solution": "Automated system that fetches papers daily, uses fine-tuned LLMs for structured summarization, and builds a knowledge graph to reveal conceptual relationships.",
        "tech_stack": ["Python", "PyTorch", "LangChain", "Graphiti", "ChromaDB", "Streamlit", "Neo4j"],
        "technical_details": {
            "data_pipeline": "Daily arXiv API cron job → PDF parsing → Text extraction",
            "model": "Fine-tuned LLaMA 2 7B on structured summaries",
            "storage": "ChromaDB for embeddings, Neo4j for knowledge graph",
            "deployment": "Streamlit interface with semantic search"
        },
        "results": {
            "papers_processed": "500+",
            "accuracy": "85% summary quality (human eval)",
            "time_saved": "70% reduction in literature review time"
        },
        "challenges": [
            "LLM hallucination in summaries",
            "Inconsistent training data quality",
            "Context window limitations for long papers",
            "Knowledge graph connection quality"
        ],
        "learning_outcomes": ["LO1", "LO2", "LO3", "LO4", "LO5"],
        "lo_explanations": {
            "LO1": "Built data pipeline using arXiv API, ChromaDB for vector storage, Neo4j for graph data",
            "LO2": "Created actionable insights for researchers by surfacing relevant papers and connections",
            "LO3": "Implemented semantic search with embeddings and graph visualizations",
            "LO4": "Extensive Python development with PyTorch, LangChain, and database APIs",
            "LO5": "Built interactive Streamlit interface for non-technical researchers"
        },
        "image": "placeholder",
        "github": "https://github.com/yourusername/rag-ception",
        "demo": None,
        "featured": True,
        "course": "IST 718 - Big Data Analytics"
    },
    {
        "id": "aurora-prediction",
        "title": "Aurora Prediction",
        "subtitle": "Geomagnetic Activity Forecasting",
        "date": "Fall 2025",
        "status": "In Progress",
        "short_description": "LSTM-based deep learning model to predict geomagnetic activity (Kp index) for aurora visibility forecasting.",
        "description": "LSTM-based deep learning model to predict geomagnetic activity (Kp index) for aurora visibility forecasting. Implementing multi-horizon forecasting pipeline predicting Kp index at 1h, 3h, 6h, and 12h intervals using time-series data from solar wind parameters and geomagnetic measurements.",
        "problem_statement": "Tourists and photographers need advance notice for aurora viewing. Current forecasts are unreliable beyond a few hours.",
        "solution": "Multi-horizon LSTM model using solar wind data to predict Kp index at multiple time intervals, with deployment considerations for real-time API.",
        "tech_stack": ["TensorFlow", "Keras", "LSTM", "Python", "Pandas", "Scikit-learn"],
        "technical_details": {
            "data_source": "NOAA Space Weather Prediction Center",
            "features": "Solar wind speed, density, magnetic field components, historical Kp",
            "model": "Stacked LSTM with attention mechanism",
            "horizons": "1h, 3h, 6h, 12h predictions"
        },
        "results": {
            "status": "In development",
            "baseline": "Outperforming persistence baseline at all horizons",
            "best_horizon": "1-hour predictions (MAE: 0.8)"
        },
        "challenges": [
            "Missing sensor data handling",
            "Irregular time-series sampling",
            "Multi-horizon evaluation complexity",
            "Real-time deployment latency requirements"
        ],
        "learning_outcomes": ["LO1", "LO2", "LO3", "LO4", "LO5"],
        "lo_explanations": {
            "LO1": "Collected and processed time-series data from NOAA APIs, handled missing values",
            "LO2": "Generated actionable forecasts for tourists and scientific research",
            "LO3": "Built LSTM predictive models with multi-horizon forecasting",
            "LO4": "Implemented full pipeline in Python with TensorFlow",
            "LO5": "Designed API and visualization for end-users (photographers, tourists)"
        },
        "image": "placeholder",
        "github": "https://github.com/yourusername/aurora-prediction",
        "demo": None,
        "featured": True,
        "course": "IST 707 - Applied Machine Learning"
    },
    {
        "id": "capsnet",
        "title": "CapsNet Classifier",
        "subtitle": "Advanced Image Classification",
        "date": "Spring 2025",
        "status": "Completed",
        "short_description": "Re-implementation of Capsule Networks on CIFAR-100 with architectural improvements.",
        "description": "Re-implemented and extended CapsNet architecture, training on CIFAR-100 (60K images, 100 classes) to investigate pose-aware feature representations. Achieved ~2pp higher top-1 accuracy than ResNet-34 baseline while using ~40% fewer parameters. Proposed Hybrid Capsule + Vision Transformer variant reducing training time by ~30%.",
        "problem_statement": "Standard CNNs lose spatial relationships and pose information. CapsNet promises better pose-aware representations but is difficult to train and reproduce.",
        "solution": "Reproduced CapsNet from paper, compared against ResNet baseline, proposed hybrid architecture with transformers.",
        "tech_stack": ["PyTorch", "CIFAR-100", "Computer Vision", "Deep Learning"],
        "technical_details": {
            "architecture": "Capsule layers with dynamic routing",
            "dataset": "CIFAR-100 (60K images, 100 classes)",
            "baseline": "ResNet-34",
            "innovation": "Hybrid Capsule + Vision Transformer"
        },
        "results": {
            "accuracy": "~2pp higher than ResNet-34 baseline",
            "parameters": "40% fewer than ResNet-34",
            "training_time": "30% reduction with hybrid architecture"
        },
        "challenges": [
            "Reproducing paper results with missing implementation details",
            "Training instability and hyperparameter sensitivity",
            "High computational cost",
            "Debugging dynamic routing algorithm"
        ],
        "learning_outcomes": ["LO3", "LO4", "LO5"],
        "lo_explanations": {
            "LO3": "Built and evaluated complex predictive model for image classification",
            "LO4": "Deep PyTorch implementation of research paper from scratch",
            "LO5": "Documented findings and compared against baselines in technical report"
        },
        "image": "placeholder",
        "github": "https://github.com/yourusername/capsnet",
        "demo": None,
        "featured": True,
        "course": "IST 664 - Natural Language Processing"
    },
    {
        "id": "airbnb-occupancy",
        "title": "Airbnb Occupancy Prediction",
        "subtitle": "Time Series Forecasting for Hospitality",
        "date": "Fall 2024",
        "status": "Completed",
        "short_description": "ML models to predict Airbnb occupancy rates using historical booking data and external factors.",
        "description": "Built machine learning models to predict Airbnb occupancy rates using historical booking data, pricing, seasonality, local events, and weather. Implemented multiple forecasting approaches including ARIMA, Prophet, and LSTM networks. Achieved 82% accuracy in predicting occupancy 30 days ahead.",
        "problem_statement": "Airbnb hosts need to optimize pricing and availability. Accurate occupancy predictions enable better revenue management.",
        "solution": "Ensemble of time-series models (ARIMA, Prophet, LSTM) incorporating multiple external features for multi-step forecasting.",
        "tech_stack": ["Python", "Prophet", "ARIMA", "LSTM", "Pandas", "Scikit-learn"],
        "technical_details": {
            "data_sources": "Airbnb booking data, weather APIs, local event calendars",
            "features": "Historical occupancy, price, seasonality, day-of-week, local events, weather",
            "models": "ARIMA, Facebook Prophet, LSTM, Ensemble",
            "forecast_horizon": "7, 14, 30 days"
        },
        "results": {
            "accuracy": "82% at 30-day horizon",
            "best_model": "Ensemble of Prophet + LSTM",
            "business_impact": "15% improvement in revenue optimization"
        },
        "challenges": [
            "COVID-19 data anomalies",
            "Handling irregular booking patterns",
            "Feature engineering for external events",
            "Model selection across different time horizons"
        ],
        "learning_outcomes": ["LO1", "LO2", "LO3", "LO4"],
        "lo_explanations": {
            "LO1": "Collected data from multiple APIs, integrated weather and event data",
            "LO2": "Generated business insights for revenue optimization in hospitality context",
            "LO3": "Applied multiple time-series predictive models and visualizations",
            "LO4": "Implemented comprehensive Python pipeline with multiple libraries"
        },
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False,
        "course": "IST 687 - Applied Data Science"
    },
    {
        "id": "cusebus",
        "title": "CuseBus Route Optimization",
        "subtitle": "Operations Research for Campus Transit",
        "date": "Spring 2024",
        "status": "Completed",
        "short_description": "Network analysis and optimization to improve Syracuse University bus system efficiency.",
        "description": "Analyzed Syracuse University bus system data to optimize routes and schedules. Used network analysis and optimization algorithms to improve service efficiency. Reduced average wait time by 18% and identified 3 underserved routes. Proposed schedule changes based on actual ridership patterns.",
        "problem_statement": "CuseBus routes were designed based on assumptions, not data. Students experienced long wait times and crowded buses during peak hours.",
        "solution": "Network graph analysis of ridership data, optimization algorithms for route planning, data-driven schedule recommendations.",
        "tech_stack": ["Python", "NetworkX", "OR-Tools", "Pandas", "Matplotlib", "Geopandas"],
        "technical_details": {
            "data": "6 months of GPS traces, ridership counts, student surveys",
            "analysis": "Network centrality, bottleneck identification, demand patterns",
            "optimization": "Vehicle routing problem (VRP) with time windows",
            "visualization": "Interactive route maps with ridership heatmaps"
        },
        "results": {
            "wait_time_reduction": "18% average wait time reduction",
            "underserved_routes": "Identified 3 routes needing additional buses",
            "peak_hour_improvement": "25% capacity increase during peak hours"
        },
        "challenges": [
            "Incomplete GPS data",
            "Balancing multiple optimization objectives",
            "Seasonal variation in ridership",
            "Constraint satisfaction for real-world schedules"
        ],
        "learning_outcomes": ["LO1", "LO2", "LO3", "LO5"],
        "lo_explanations": {
            "LO1": "Processed GPS traces and ridership data from multiple sources",
            "LO2": "Generated actionable recommendations for university operations",
            "LO3": "Used network visualization and optimization models",
            "LO5": "Presented findings to campus transportation officials"
        },
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False,
        "course": "IST 652 - Scripting for Data Analysis"
    },
    {
        "id": "energy-forecasting",
        "title": "Energy Consumption Forecasting",
        "subtitle": "Sustainability Analytics for Buildings",
        "date": "Fall 2024",
        "status": "Completed",
        "short_description": "Predictive models for building energy consumption to support sustainability initiatives.",
        "description": "Developed predictive models for building energy consumption to support sustainability initiatives. Incorporated weather data, occupancy patterns, and historical usage. Used XGBoost and feature engineering to achieve 15% MAPE. Model insights led to policy recommendations for reducing energy waste.",
        "problem_statement": "University buildings waste energy due to inefficient heating/cooling schedules. Need data-driven approach to optimize energy usage.",
        "solution": "XGBoost model with extensive feature engineering predicting hourly energy consumption, enabling proactive HVAC management.",
        "tech_stack": ["Python", "XGBoost", "Feature Engineering", "Pandas", "SHAP", "Time Series"],
        "technical_details": {
            "data": "2 years of hourly energy consumption, weather data, occupancy sensors",
            "features": "Temperature, humidity, time-of-day, day-of-week, holidays, occupancy, lag features",
            "model": "XGBoost with temporal cross-validation",
            "interpretability": "SHAP values for feature importance"
        },
        "results": {
            "mape": "15% mean absolute percentage error",
            "energy_savings": "12% reduction in energy waste",
            "insights": "Identified optimal HVAC schedules per building"
        },
        "challenges": [
            "Sensor failures and missing data",
            "Non-stationary patterns due to building changes",
            "Balancing accuracy vs interpretability",
            "Translating technical findings to policy"
        ],
        "learning_outcomes": ["LO1", "LO2", "LO3", "LO5", "LO6"],
        "lo_explanations": {
            "LO1": "Integrated IoT sensor data with weather APIs",
            "LO2": "Created actionable sustainability insights for university",
            "LO3": "Applied gradient boosting and SHAP visualizations",
            "LO5": "Communicated technical findings to facilities management",
            "LO6": "Considered environmental ethics in energy optimization"
        },
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False,
        "course": "IST 736 - Text Mining"
    },
    {
        "id": "medical-imaging",
        "title": "Medical Image Analysis",
        "subtitle": "Computer Vision for Healthcare",
        "date": "Spring 2025",
        "status": "In Progress",
        "short_description": "Deep learning models for automated medical image analysis and segmentation.",
        "description": "Developing deep learning models for automated medical image analysis. Focus on segmentation and classification tasks for diagnostic support. Using U-Net architecture for organ segmentation. Currently working on lung nodule detection with 89% sensitivity.",
        "problem_statement": "Radiologists spend hours analyzing medical images. Automated segmentation could speed diagnosis and reduce errors.",
        "solution": "U-Net based segmentation model with transfer learning, focusing on lung CT scans for nodule detection.",
        "tech_stack": ["PyTorch", "Computer Vision", "U-Net", "Medical Imaging", "Transfer Learning"],
        "technical_details": {
            "data": "LIDC-IDRI dataset (1000+ CT scans)",
            "preprocessing": "Window leveling, normalization, augmentation",
            "architecture": "U-Net with ResNet encoder",
            "evaluation": "Dice coefficient, sensitivity, specificity"
        },
        "results": {
            "status": "In progress",
            "current_performance": "89% sensitivity, 82% Dice coefficient",
            "target": "95% sensitivity for clinical viability"
        },
        "challenges": [
            "Class imbalance (few positive cases)",
            "Annotation quality and inter-rater variability",
            "Ethical considerations in medical AI",
            "Explaining predictions to clinicians"
        ],
        "learning_outcomes": ["LO3", "LO4", "LO5", "LO6"],
        "lo_explanations": {
            "LO3": "Implemented segmentation and classification models",
            "LO4": "Deep PyTorch implementation with medical imaging libraries",
            "LO5": "Developing explainable AI for clinical stakeholders",
            "LO6": "Addressing bias, privacy, and transparency in medical AI"
        },
        "image": "placeholder",
        "github": None,
        "demo": None,
        "featured": False,
        "course": "IST 782 - Advanced Deep Learning"
    }
]

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
