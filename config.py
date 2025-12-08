"""
Portfolio Configuration File
Update this file with your personal information
"""
"""
Portfolio Configuration File - UPDATED WITH LEARNING OUTCOMES
"""

# Personal Information
PERSONAL_INFO = {
    "name": "Nikita Sharma",
    "title": "MS Applied Data Science | Syracuse University",
    "email": "nsharm23@syr.edu",
    "location": "Syracuse, NY",
    "linkedin": "https://linkedin.com/in/niksisharma",
    "github": "https://github.com/niksisharma",
}

# Stats for Homepage
# STATS = {
#     "projects": 7,
#     "completed": 5,
#     "gpa": "3.87",
#     "publications": 1
# }

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
        "official_description": "Collect, store, and access data by identifying and leveraging applicable technologies",
        "my_understanding": "This covers the fundamental skills needed to work with data at scale. It involves sourcing the right data for any application, whether that means finding publicly available datasets, scraping the web, conducting surveys, or synthesizing your own data. It also includes knowing when a simple CSV file will do and when to use relational versus non-relational databases, being familiar with APIs and cloud storage systems. Overall, it is about designing efficient data pipelines."
    },
    "LO2": {
        "number": 2,
        "title": "Actionable Insights",
        "official_description": "Create actionable insight across a range of contexts (e.g. societal, business, political), using data and the full data science life cycle",
        "my_understanding": "This outcome is about being able to generate insights that drive decisions and actions. Actionable means the insight should be specific, timely, and relevant enough for stakeholders to take action. This applies across the entire data science life cycle from problem formulation and data collection to exploratory analysis, modelling, validation, deployment, and monitoring. You need to be able to work across different domains and translate technical findings into recommendations that non-technical stakeholders can easily understand and implement."
    },
    "LO3": {
        "number": 3,
        "title": "Visualization & Predictive Models",
        "official_description": "Apply visualization and predictive models to help generate actionable insight",
        "my_understanding": "This focuses on the two important skills you need to achieve the previous outcome of creating insights. Visualization is about choosing the right visual graphs to make patterns obvious and support your analysis. Predictive modelling requires understanding and implementing various models, knowing the trade-offs between them, knowing how to evaluate performance appropriately, and recognizing when predictions are reliable or not."
    },
    "LO4": {
        "number": 4,
        "title": "Programming Proficiency",
        "official_description": "Use programming languages such as R and Python to support the generation of actionable insight",
        "my_understanding": "This outcome about developing proficiency in the programming languages used in data science, primarily Python and R. It means writing clean, reproducible code, understanding computational complexity, debugging efficiently, and integrating libraries into pipelines. These skills should support creation of visualizations and modelling which can then be converted into actionable insights."
    },
    "LO5": {
        "number": 5,
        "title": "Communication",
        "official_description": "Communicate insights gained via visualization and analytics to a broad range of audiences (including project sponsors and technical team leads)",
        "my_understanding": "This refers to the ability to explain complex methods and results to different audiences by adjusting the level of detail. For project sponsors, the focus is on the business impact and presenting recommendations without technical details. For technical teams, it's about providing the details of methodology, limitations, and results. Communication can take many forms, such as documentation, technical writing, presentations, and even code comments, all of which demonstrate this ability."
    },
    "LO6": {
        "number": 6,
        "title": "Ethics & Responsible AI",
        "official_description": "Apply ethics in the development, use and evaluation of data and predictive models (e.g., fairness, bias, transparency, privacy)",
        "my_understanding": "Ethics in data science means considering who benefits and who is harmed by our models, questioning whether we should build something just because we can, ensuring our models don't perpetuate or amplify societal biases, being transparent about limitations and uncertainties, and protecting privacy."
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
    "subtitle": "Automated Research Knowledge Management System",
    "date": "Fall 2024",
    "short_description": "End-to-end automated system that discovers new RAG papers, processes content, generates structured summaries, and enables intelligent semantic search.",
    "description": "The field of Retrieval-Augmented Generation (RAG) moves incredibly fast and dozens of new research papers appear on arXiv every week, making it difficult for researchers and practitioners to stay current through manual tracking. Our team built RAG-ception to solve this problem: an end-to-end automated system that discovers new RAG papers, processes their content, generates structured summaries, and enables intelligent semantic search through a user-friendly web interface.",
    "problem_statement": "With dozens of new RAG papers appearing on arXiv weekly, researchers and practitioners struggle to stay current through manual tracking. Traditional literature review is time-consuming and misses important developments.",
    "solution": "An automated pipeline that fetches papers from arXiv, processes PDFs, generates embeddings, produces seven-section summaries, and enables semantic search through a Streamlit interface. The entire workflow runs automatically.",
    "tech_stack": ["Python", "OpenAI GPT-4.1-nano", "text-embedding-3-small", "Graphiti API", "PyPDF2", "SQLite", "Streamlit"],
    "my_role": "I took ownership of the paper summarization component from start to finish. Built high-quality fine-tuning dataset by selecting 30 representative RAG papers, manually editing initial summaries for consistency, and formatting into training data. Managed entire fine-tuning process through OpenAI's API across three training rounds, improving structure adherence from ~20% to nearly 100%. Implemented PaperSummarizer class with single/batch processing, quality scoring, and error handling. Collaborated on database schema design and integration into main orchestrator pipeline.",
    "technical_details": {
        "data_pipeline": "Automatic fetching from arXiv cs.CL, cs.LG, cs.AI categories with PDF download and parsing",
        "embeddings": "OpenAI text-embedding-3-small for semantic representations",
        "summarization": "Fine-tuned GPT-4.1-nano producing seven-section summaries (methodology, related work, etc.)",
        "knowledge_graph": "Graphiti API for relationship extraction",
        "storage": "SQLite for papers, summaries, and embeddings",
        "interface": "Streamlit web app for semantic search",
        "processing": "Intelligent text chunking with overlap for better context"
    },
    "results": {
        "fine_tuning_improvement": "Structure adherence improved from 20% to 100%",
        "automation": "Fully automated weekly paper discovery and processing",
        "search_quality": "Semantic search finds relevant papers beyond keyword matching",
        "time_savings": "Multi-hour literature review reduced to minutes"
    },
    "challenges": [
        "Building consistent fine-tuning dataset from diverse academic writing styles",
        "Iterating through multiple training rounds to achieve 100% structure adherence",
        "Handling complex PDF layouts and mathematical equations",
        "Integrating summarization component with team's orchestrator pipeline",
        "Designing quality scoring metrics for summary evaluation"
    ],
    "learning_outcomes": ["LO1", "LO2", "LO4", "LO5", "LO6"],
    "lo_explanations": {
        "LO1": "Pipeline managing full lifecycle from raw PDFs to structured embeddings in SQLite, including schema design for papers, summaries, and embeddings with automated weekly fetching from arXiv",
        "LO2": "Automated literature discovery and summarization helps researchers quickly identify relevant papers and make informed decisions about deeper investigation, transforming hours of manual review into focused interaction",
        "LO4": "Implemented complete summarization pipeline in Python: API integration, model fine-tuning, database operations, error handling, quality scoring, and batch processing capabilities",
        "LO5": "Presented business-focused online demo to class, explaining technical system in accessible terms and demonstrating practical value for researchers",
        "LO6": "Ensured transparency about model limitations, properly attributed authors, designed system to assist rather than replace human judgment in research evaluation"
    },
    "image": "assets/images/rag-ception.png",
    "github": "https://github.com/niksisharma/ragception",
    "demo": None,
    "course": "IST 688 - Building Human Centered AI Applications"
},
    {
        "id": "aurora-prediction",
        "title": "Aurora Prediction",
        "subtitle": "Geomagnetic Activity Forecasting with LSTM",
        "date": "Fall 2024",
        "short_description": "Multi-horizon LSTM forecasting model predicting Kp index at 1, 3, 6, and 12-hour intervals using NASA's space weather data to help aurora enthusiasts and researchers.",
        "description": "Aurora borealis (northern lights) viewing depends on geomagnetic activity, measured by the Kp index (0-9 scale). Aurora enthusiasts often travel long distances hoping to see them, while researchers study them to understand space weather patterns. Current forecasts are unreliable beyond 1-2 hours. This project builds multi-horizon forecasting models that predict Kp index at 1-hour, 3-hour, 6-hour, and 12-hour intervals using solar wind data.",
        "problem_statement": "Aurora viewing depends on geomagnetic activity (Kp index), but current forecasts are unreliable beyond 1-2 hours. Aurora enthusiasts and researchers need reliable multi-hour predictions for trip planning and space weather research.",
        "solution": "LSTM-based time-series forecasting model trained on NASA's OMNI dataset (95,000 hourly records). Selected 16 key features from 55 available measurements, designed multi-output architecture for 1h, 3h, 6h, and 12h predictions.",
        "tech_stack": ["TensorFlow", "Keras", "Python", "Pandas", "NumPy", "Scikit-learn", "Matplotlib"],
        "my_role": "I worked on all aspects of the project. Explored NASA's space weather dataset and selected most relevant features from 55 available measurements, focusing on solar wind properties and magnetic field characteristics. Experimented with LSTM architectures and trained model while monitoring performance across all prediction horizons. Evaluated results, created visualizations showing prediction accuracy and error distributions, and analyzed which features were most important for each forecast horizon. Designed poster presentation for iSchool poster day.",
        "technical_details": {
            "dataset": "NASA OMNI dataset with 95,000 hourly records",
            "feature_engineering": "Selected 16 key variables from 55 measurements, created 24-hour sliding windows",
            "architecture": "LSTM with multi-output prediction heads for 1h, 3h, 6h, 12h horizons",
            "training": "Custom training loops with regularization to prevent overfitting",
            "evaluation": "Multi-horizon evaluation metrics, error distribution analysis, feature importance",
            "visualization": "Time-series plots, prediction accuracy over time, error distributions"
        },
        "results": {
            "data_processed": "95,000 hourly records from NASA OMNI",
            "feature_selection": "16 key variables from 55 measurements",
            "short_term_accuracy": "Good performance for 1-hour predictions",
            "long_term_degradation": "Performance degrades for 12-hour horizon (expected given chaotic nature)",
            "key_finding": "Accurate Kp predictions don't automatically translate to aurora visibility"
        },
        "challenges": [
            "Reducing 55 available measurements to 16 most relevant features",
            "Balancing model complexity with prediction accuracy across different horizons",
            "Understanding why performance degrades at longer horizons (chaotic geomagnetic activity)",
            "Recognizing gap between Kp prediction and actual aurora visibility",
            "Presenting complex time-series forecasting to diverse poster day audience"
        ],
        "learning_outcomes": ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6"],
        "lo_explanations": {
            "LO1": "Processed nearly 95,000 hourly records from NASA's OMNI dataset, performed feature selection reducing 55 measurements to 16 key variables, created properly structured time-series data with 24-hour sliding windows",
            "LO2": "Provided multi-horizon Kp forecasts (1, 3, 6, 12 hours ahead) enabling aurora enthusiasts to plan viewing activities and helping researchers anticipate geomagnetic disturbances, while identifying critical gap between Kp prediction and actual aurora visibility",
            "LO3": "Built and trained LSTM neural network for time-series forecasting, created visualizations showing prediction accuracy over time and error distributions across horizons, analyzed feature importance to understand which space weather measurements drive geomagnetic activity, designed poster presentation",
            "LO4": "Implemented complete deep learning pipeline in Python: data preprocessing, LSTM architecture design, custom training loops with regularization, multi-output prediction heads, comprehensive evaluation metrics",
            "LO5": "Presented project to diverse audience on iSchool poster day, explaining space weather forecasting and LSTM predictions in accessible terms",
            "LO6": "Transparently reported both successes and limitations, acknowledging that accurate Kp predictions don't automatically translate to aurora visibility, identified need for additional factors in practical aurora forecasting"
        },
        "image": "assets/images/aurora-prediction.png",
        "github": "https://github.com/niksisharma/aurora-prediction",
        "demo": None,
        "course": "IST 699 - Deep Learning in Practice"
    },
    {
        "id": "capsnet",
        "title": "Scaling CapsNet Image Classifier",
        "subtitle": "Comparing CNN, ViT, CapsNet, and Hybrid Architectures",
        "date": "Fall 2024",
        "short_description": "Comparative study of four architectures (ResNet-34, ViT-Tiny, CapsNet, Hybrid CapsViT) on CIFAR-100 to find optimal balance of accuracy and efficiency for image classification.",
        "description": "Traditional image recognition systems are good at identifying basic patterns but struggle to understand how different parts of an image relate to each other spatially. Newer approaches called Vision Transformers can capture these complex relationships but need enormous amounts of data and computing power to work well. This creates a practical problem: what's the best approach when working with a moderately-sized dataset like CIFAR-100? Our team compared four different AI architectures to find which offers the best balance of accuracy and efficiency for image classification tasks.",
        "problem_statement": "CNNs lose spatial relationships, Vision Transformers require massive data and compute, and CapsNet is difficult to train. Need to compare architectures on moderate-sized dataset (CIFAR-100) to determine best accuracy-efficiency trade-off.",
        "solution": "Systematic comparison of four architectures: ResNet-34 (baseline CNN), ViT-Tiny (transformer), Capsule Network (spatial relationships), and Hybrid CapsViT (our proposed combination). All trained from scratch on CIFAR-100 with identical settings for fair comparison.",
        "tech_stack": ["PyTorch", "CUDA 12.8", "cuDNN", "CIFAR-100", "ResNet", "Vision Transformer", "Capsule Networks"],
        "my_role": "I was responsible for building and training two of the four models: the traditional CNN baseline (ResNet-34) and the Capsule Network. Monitored training progress, troubleshot issues, and worked closely with teammate to ensure fair experimental comparisons. Helped analyze why different models performed differently and mapped out practical trade-offs between accuracy and efficiency.",
        "technical_details": {
            "dataset": "CIFAR-100: 50,000 training images, 10,000 test images (32×32 resolution, 100 classes)",
            "resnet34": "Traditional deep learning baseline",
            "vit_tiny": "Vision Transformer processing images as patch sequences",
            "capsnet": "Capsule layers with dynamic routing for spatial relationships",
            "hybrid_capsvit": "Proposed combination merging capsule local analysis with transformer global understanding",
            "training": "Identical preprocessing, augmentation, optimization across all models for fair comparison"
        },
        "results": {
            "comparative_analysis": "Mapped accuracy vs efficiency trade-offs across all four architectures",
            "practical_guidance": "Clear recommendations on which approach to use based on constraints",
            "reproducibility": "Successfully reproduced CapsNet despite missing implementation details",
            "baseline_comparison": "Fair evaluation against ResNet-34 standard"
        },
        "challenges": [
            "Reproducing CapsNet results with missing implementation details from paper",
            "Managing training instability and hyperparameter sensitivity",
            "Debugging dynamic routing algorithm",
            "Ensuring fair comparison across different architecture paradigms",
            "Analyzing why each model performed differently on same dataset"
        ],
        "learning_outcomes": ["LO1", "LO2", "LO3", "LO4", "LO5"],
        "lo_explanations": {
            "LO1": "Organized and managed 60,000-image dataset with proper training/testing splits, implemented data preprocessing pipelines for consistent model input",
            "LO2": "Generated actionable guidance for researchers and practitioners on which architecture to choose based on accuracy vs efficiency constraints, mapped out practical trade-offs",
            "LO3": "Built and evaluated four different deep learning models, compared prediction performance, understood strengths and weaknesses of each approach through systematic experimentation",
            "LO4": "Implemented sophisticated AI models in Python, built custom neural network components, designed training loops, applied optimization strategies for best performance from each architecture",
            "LO5": "Presented findings to advanced computer science class with technical focus, wrote conference-style technical paper documenting methodology and results"
        },
        "image": "assets/images/capsnet.png",
        "github": "https://github.com/niksisharma/capsNet",
        "demo": None,
        "course": "CIS 788 - Artificial Neural Networks"
    },
    {
        "id": "airbnb-occupancy",
        "title": "Airbnb Occupancy Prediction",
        "subtitle": "Time Series Forecasting for Hospitality",
        "date": "Spring 2025",
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
        "image": "assets/images/airbnb-occupancy.png",
        "github": "https://github.com/niksisharma/airBnB",
        "demo": None,
        "course": "IST 707 - Applied Data Science"
    },
    {
        "id": "cusebus",
        "title": "Syracuse University Bus System Optimization",
        "subtitle": "Operations Research for Campus Transit",
        "date": "Fall 2024",
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
        "image": "assets/images/cusebus.png",
        "github": "https://github.com/niksisharma/cuseBus",
        "demo": None,
        "course": "IST 652 - Data Admin and Database Management Systems"
    },
    {
        "id": "energy-forecasting",
        "title": "Energy Consumption Forecasting",
        "subtitle": "Sustainability Analytics for Buildings",
        "date": "Fall 2024",
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
        "image": "assets/images/energy-forecasting.png",
        "github": "https://github.com/niksisharma/energy-forecasting",
        "demo": None,
        "course": "IST 687 - Introduction to Data Science"
    },
]

# Blog Post / Reflection
BLOG_POST = {
    "title": "Reflection on My MS Applied Data Science Journey",
    "date": "December 2025",
    "read_time": "15 min read",
    "sections": [
        {
            "heading": "Introduction",
            "content": """Early in the program, I was working through a routine lab exercise, building a binary classifier. I'd gotten the accuracy up to 85%, which felt pretty good for a Tuesday afternoon. Someone asked something pretty straightforward: "Which 15% is it getting wrong, and what happens to those people?" It wasn't some dramatic revelation, but it did make me look at my confusion matrix differently. I'd been treating the error rate as just a metric to improve, but the question made me think about actual consequences. Are these people being denied something? Getting flagged incorrectly? It's a simple question, but it stuck with me. It's something I think about every time I build a model.

I came to Syracuse's MS in Applied Data Science program from an odd angle. My undergrad was in electronics engineering, and I'd spent a few years in software engineering and DevOps. There was some data work sprinkled in, enough to make me curious but not enough to really understand what I was doing. I chose this program because I wanted a career switch, maybe PhD prep down the line, and honestly, because ML seemed like where the interesting problems were. I didn't have a specific area in mind when I started, just a vague sense that I wanted to understand how to build systems that actually worked with data, not just around it.

This is my honest take on what I actually learned over the past two years: the technical skills, the perspective shifts, the surprises, and the gaps between expectation and reality. I'll walk through the projects that taught me the most, the class that changed how I think, and the moments where I realized I'd been approaching problems completely wrong. If you're considering grad school in data science or you're in the middle of it wondering if you're learning the "right" things, this is for you."""
        },
        {
            "heading": "Expectations vs. Reality",
            "content": """I came in with realistic expectations: some math, plenty of Python, lots of building projects. What broke me in the first semester wasn't the technical work. It was the writing. Every project needed documentation. Every experiment needed a report explaining methodology, results, interpretation. Every presentation had to tell a story that made sense to people who weren't neck-deep in your code. I came from DevOps where documentation was "comments in the code if you're lucky." Suddenly I was writing 10-page reports about why my model performed the way it did.

But here's the surprise that saved me: I discovered I actually liked the experimentation part more than the engineering part. In my old job, the goal was always "build it once, make it rock-solid, never touch it again." In ML, it's "try fifty things, see what works, throw out forty-nine of them, try fifty more." That iterative, exploratory process felt weirdly freeing.

The biggest myth I believed? More data equals better models, and fancier models equal better results. I spent the first half of my first ML course thinking that if my model wasn't performing well, I just needed more data or a more complex architecture. Then I hit a project where I had tons of data and my model got worse. Noisy labels, duplicate entries, data drift. I tried swapping my simple logistic regression for a deep neural network, and my performance tanked because I was overfitting on a small signal. Some of my best-performing models ended up being embarrassingly simple: linear regressions, decision trees, things I could explain to a non-technical stakeholder in two sentences. I learned to start simple, add complexity only when justified, and spend more time cleaning data than tuning hyperparameters."""
        },
        {
            "heading": "Technical Growth Through Projects",
            "content": """By second year, I was drowning in research papers. Every project started the same way: read twenty papers, take notes, forget which paper said what, re-read three of them because I couldn't remember key differences. I needed a system to organize research, not just store PDFs but actually understand connections between papers and surface relevant work when I needed it. That's how RAG-ception started: a system that uses RAG to manage RAG research.

My first approach was embarrassingly naive. I threw papers at an off-the-shelf LLM and asked it to summarize them. The summaries were fluent, coherent, and completely useless. The model would hallucinate details or write summaries so generic they could apply to anything. The breakthrough came when I realized I needed to fine-tune the summarization model on actual research paper summaries with a consistent schema: extract problem statement, proposed method, key results, limitations. That structure forced the model to stay grounded.

Here's what almost killed the project: my fine-tuning worked, but outputs were wildly inconsistent. Some summaries were detailed and useful. Others were vague one-liners. I checked my loss curves, my evaluation metrics. Everything looked fine. I was going insane until I actually read through my training data. Turns out I'd scraped summaries from different sources: some were detailed abstracts, some were Twitter-length announcements, some were related work sections. I was training the model to be inconsistent because my training data was inconsistent. Once I cleaned that up, everything clicked. Your model can only be as good as your data, and "more data" doesn't help if half of it is teaching the model the wrong thing.

CapsNet was different. I chose it because the architecture genuinely fascinated me: the idea that you could encode pose and spatial relationships directly into the network structure. The paper made bold claims about how capsule networks would solve fundamental problems with CNNs. I wanted to see if that was real or hype.

The challenge wasn't the math. The challenge was that the paper leaves out implementation details that matter enormously. What initialization scheme? What learning rate schedule? How exactly do you handle routing iterations during training versus inference? I'd change one hyperparameter and my accuracy would swing by 10 points. I spent weeks debugging, re-reading the paper, finding blog posts from people who'd tried to reproduce it. Eventually I got it working: about 2 percentage points higher top-1 accuracy than a ResNet-34 baseline on CIFAR-100, using about 40% fewer parameters. On paper, that's a win. In practice, it taught me that paper results are really hard to reproduce.

Here's what CapsNet really taught me: reproducing research is harder than doing the research in the first place. When you're the first person trying something, you can pivot, adjust, redefine success. When you're trying to match someone else's numbers, you're stuck. And the 2pp improvement I got? It came at a massive computational cost. I learned to read papers with a more skeptical eye. "State of the art" often means "state of the art under very specific conditions with a lot of hyperparameter tuning that we didn't mention."

Aurora prediction started as "this seems cool" and evolved into something I cared about. The basic idea: predict geomagnetic activity (Kp index) using solar wind data to forecast when auroras will be visible. Photographers and tourists travel to places like Iceland or Alaska hoping to see the northern lights with maybe a 24-hour window to plan. If I could build a model that predicts Kp index at 1-hour, 3-hour, 6-hour, and 12-hour horizons, that's actually useful to people.

Time-series forecasting is its own beast. I'd done plenty of ML before, but temporal dependencies change everything. You can't just report "85% accuracy" and call it done. A model that's great at 1-hour predictions might be terrible at 12-hour predictions. I needed to evaluate performance at each time horizon separately because they're fundamentally different problems. Short-term forecasts can lean heavily on recent data; long-term forecasts need to capture underlying patterns.

The project is still in progress, but I'm already thinking about deployment. How would this work as an API? What's the acceptable latency? What happens when real-time solar wind data is missing or delayed? In ML, I'm learning you have to think about deployment from day one, because it changes how you build the model."""
        },
        {
            "heading": "Favorite Class",
            "content": """My favorite class was Responsible AI, taught by Jasmina Tacheva. It was completely different from everything else I took. Most classes followed the same pattern: learn algorithm, implement algorithm, tune hyperparameters, submit results. Responsible AI didn't work like that. We spent less time coding and more time reading papers, discussing case studies, debating ethical implications. We analyzed real systems (facial recognition, content moderation, hiring algorithms) and tore apart their assumptions. The class felt like a seminar, not a lecture. It was uncomfortable in the best way. You couldn't just be technically correct; you had to think about context, stakeholders, second-order effects.

The assignment that stuck with me was analyzing TikTok's recommendation system, not the algorithm itself, but its social and ethical impact. We had to map out how the system worked, who it affected, what incentives it created, and where things could go wrong. I started thinking it was just clever use of collaborative filtering. By the end, I was looking at feedback loops that amplify extreme content, filter bubbles that narrow worldviews, and psychological manipulation baked into something as casual as scrolling through videos. The moment it clicked was realizing that AI doesn't just exist in research labs. It shapes every interaction people have online, often in ways they don't notice.

The biggest impact? I now ask "should I build this?" before I ask "can I build this?" Every project since Responsible AI, I spend time thinking about potential harms, edge cases, and who might be negatively affected. I don't always have good answers, but at least I'm asking the questions. I also present projects differently now. I used to focus purely on performance: "I got 87% accuracy, here's my confusion matrix." Now I talk about limitations, failure modes, what the model gets wrong and why that matters. Responsible AI made me a more thoughtful engineer. I'd probably still be optimizing metrics without thinking too hard about what happens after deployment. Now I can't unsee that part."""
        },
        {
            "heading": "Beyond the Classroom",
            "content": """I didn't do a formal internship, but I ended up mentoring a high school student on an AI bias project through a connection from Jasmina. The student was preparing for the Central New York science fair and had done previous work on AI ethics. We were scoping a project on bias mitigation strategies. The challenge was explaining AI bias without dumbing it down or drowning her in jargon. Every time I tried to explain fairness metrics or mitigation strategies, I realized I didn't understand them as well as I thought. If you can't explain it simply, you don't really get it. Teaching forced me to strip away technical language and find core concepts. Before the program, I would've helped her build something technically flashy. Now I was focused on building something that clearly demonstrated a concept, even if the implementation was simple."""
        },
        {
            "heading": "Key Learning Outcomes",
            "content": """When I started, I thought "end-to-end ML" meant having a Jupyter notebook that ran without errors. Now I know it means data collection, cleaning, pipeline design, model training, evaluation across multiple dimensions, deployment strategy, monitoring, and explaining results to people who don't care about your F1 score. RAG-ception needed a data pipeline that could fetch papers from arXiv daily, parse PDFs reliably, handle duplicates, and store embeddings efficiently. Aurora needed multi-horizon evaluation, handling missing sensor data, and thinking about API latency requirements before the model even worked. The model is maybe 20% of the system. The other 80% is everything around it.

I learned to do research by doing it badly first. CapsNet taught me that you can't just read a paper once and start coding. You need to read it three times, check the appendix, find the author's GitHub if it exists, and accept that you'll still be missing details. My process now: reproduce first, innovate later. I don't start from scratch anymore. I find the closest existing work, get their baseline running, and iterate from there. The other skill: documentation. I keep detailed experiment logs now of what I tried, why it failed, what I learned. Research is iterative, and iteration only works if you remember what you've already tried.

I've written more in this program than I did in four years of undergrad. At first, this felt like busy work. Why am I writing ten pages when the code speaks for itself? But the code doesn't speak for itself. Code tells you what you did; writing tells you why you did it and whether it worked. I got better through repetition and necessity. The mentoring experience helped. Responsible AI helped. Now I structure explanations differently: start with the problem, explain why existing approaches fall short, describe what I did, show results, acknowledge limitations. No jargon unless necessary. If I can't explain my work clearly, that's a sign I don't understand it well enough."""
        },
        {
            "heading": "Surprises & Challenges",
            "content": """The hardest moment? Right now. I'm writing this reflection while juggling three unfinished projects, a blog post requirement, and the reality that I graduate in two weeks. The challenge isn't any single technical concept. It's that I underestimated how long everything would take. I thought I could finish Aurora prediction in a month. It's been three. Every project expands to fill more time than you budget for because there's always one more experiment to run, one more bug to fix. The lesson I'm learning in real time: scope management is a skill, and I don't have it yet.

Here's what surprised me: I genuinely love the experimentation part of ML. I thought it would be tedious. But there's something deeply satisfying about the scientific method at this scale. Every failed experiment tells you something. Every hyperparameter sweep narrows the search space. You're not just guessing; you're systematically exploring a problem space, and every result (good or bad) is information. Coming from DevOps where the goal was "make it work once and never touch it again," this iterative process felt chaotic at first. Now it feels like solving a puzzle where you get immediate feedback.

What got me through: study groups and brute force persistence. There were nights where I'd be stuck on something for hours, throw it in the group chat, and someone would spot the issue in five minutes. I also learned that some problems don't have clever solutions. You just have to sit there and try things until one works. If I could give advice to myself two years ago: start projects earlier than you think you need to, because everything takes twice as long as you expect. And when you're in the middle of a deadline crunch, convinced you're not going to make it? You've got this."""
        },
        {
            "heading": "Conclusion: Looking Forward",
            "content": """The technical skills I'm taking aren't just about knowing PyTorch or TensorFlow. They're about how to approach problems systematically. I know how to read a research paper and actually implement it. I know how to debug a model that's not converging by checking data distributions, loss curves, gradient flows. I know how to build pipelines that don't break when data changes. But honestly, the non-technical skill matters more: communication. Being able to explain what I built, why it matters, what could go wrong, and what the limitations are. That's what makes the difference between a demo that impresses your professor and a system someone might actually use.

I'm more cautious about AI than I was when I started, but also more impressed by what it can actually do. I've seen it work (really work) on problems I didn't think were solvable. These things feel like magic until you build them, and then they feel like applied statistics with really good engineering. But I'm also warier now. I've seen how easy it is to build something that works on a test set and fails in the real world. I've seen how a 15% error rate isn't just a number. It's people being affected by your system's failures. I'm less optimistic about AI solving everything, but more convinced that if we build it carefully, if we ask the right questions and design for humans (not just accuracy), it can actually help.

I'm applying to both PhD programs and industry roles. PhD programs in human-centered AI and responsible ML interest me. I want to dig deeper into how we build systems that account for their impact, not just their performance. But I'm also drawn to industry roles where I'd work on production ML systems, because deployment is where the real challenges live. Two years ago I didn't know what I wanted. Now I have options and the skills to execute on whichever one I choose.

If you're starting this program: start messy and iterate later. Don't wait for the perfect plan. Build something that runs, even if it's ugly, and improve it from there. Take the classes that scare you a little, the ones outside your comfort zone. And document everything as you go. Your future self will not remember why you made that design choice at 2am three weeks ago.

I came into this program wanting technical skills. I'm leaving with those, but also with a completely different way of thinking about problems. I don't just ask "can I build this?" I ask "should I build this? Who does it affect? What happens when it fails?" That shift didn't come from one class or one project. It came from two years of building things, watching them break, fixing them, and realizing that the technical part is only half the problem. I'm not saying I've figured it all out. I'm still learning, still making mistakes, still underestimating how long things take. But I'm equipped now to keep learning, to keep building, and to keep asking the questions that matter."""
        }
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
            "gpa": "3.88/4.0"
        },
        {
            "degree": "BE in Electronics and Communication Engineering",
            "school": "[Your University]",
            "location": "[Location]",
            "date": "August 2022",
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
