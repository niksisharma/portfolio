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
    "location": "Syracuse, NY",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "website": "https://yourwebsite.com"
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
        "date": "Fall 2025",
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
            "papers_processed": "50+",
            "accuracy": "ooo",
            "time_saved": "idk"
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
        "github": "https://github.com/niksisharma/ragception",
        "demo": None,
        "featured": True,
        "course": "IST 688 - Building Human Centered AI Applications"
    },
    {
        "id": "aurora-prediction",
        "title": "Aurora Prediction",
        "subtitle": "LSTM Based Geomagnetic Activity Forecasting",
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
        "github": "https://github.com/niksisharma/aurora-prediction",
        "demo": None,
        "featured": True,
        "course": "IST 699 - Deep Learning in Practice"
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
        "github": "https://github.com/niksisharma/capsNet",
        "demo": None,
        "featured": True,
        "course": "CIS 788 - Artificial Neural Networks"
    },
    {
        "id": "airbnb-occupancy",
        "title": "Airbnb Occupancy Prediction",
        "subtitle": "Time Series Forecasting for Hospitality",
        "date": "Spring 2025",
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
        "github": "https://github.com/niksisharma/airBnB",
        "demo": None,
        "featured": False,
        "course": "IST 707 - Applied Data Science"
    },
    {
        "id": "cusebus",
        "title": "Syracuse University Bus System Optimization",
        "subtitle": "Operations Research for Campus Transit",
        "date": "Fall 2024",
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
        "course": "IST 652 - Data Admin and Database Management Systems"
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
            "heading": "Part 1: Expectations vs. Reality",
            "content": """I came in with realistic expectations: some math, plenty of Python, lots of building projects. What broke me in the first semester wasn't the technical work. It was the writing. Every project needed documentation. Every experiment needed a report explaining methodology, results, interpretation. Every presentation had to tell a story that made sense to people who weren't neck-deep in your code. I came from DevOps where documentation was "comments in the code if you're lucky." Suddenly I was writing 10-page reports about why my model performed the way it did.

But here's the surprise that saved me: I discovered I actually liked the experimentation part more than the engineering part. In my old job, the goal was always "build it once, make it rock-solid, never touch it again." In ML, it's "try fifty things, see what works, throw out forty-nine of them, try fifty more." That iterative, exploratory process felt weirdly freeing.

The biggest myth I believed? More data equals better models, and fancier models equal better results. I spent the first half of my first ML course thinking that if my model wasn't performing well, I just needed more data or a more complex architecture. Then I hit a project where I had tons of data and my model got worse. Noisy labels, duplicate entries, data drift. I tried swapping my simple logistic regression for a deep neural network, and my performance tanked because I was overfitting on a small signal. Some of my best-performing models ended up being embarrassingly simple: linear regressions, decision trees, things I could explain to a non-technical stakeholder in two sentences. I learned to start simple, add complexity only when justified, and spend more time cleaning data than tuning hyperparameters."""
        },
        {
            "heading": "Part 2: Technical Growth Through Projects",
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
            "heading": "Part 3: Favorite Class",
            "content": """My favorite class was Responsible AI, taught by Jasmina Tacheva. It was completely different from everything else I took. Most classes followed the same pattern: learn algorithm, implement algorithm, tune hyperparameters, submit results. Responsible AI didn't work like that. We spent less time coding and more time reading papers, discussing case studies, debating ethical implications. We analyzed real systems (facial recognition, content moderation, hiring algorithms) and tore apart their assumptions. The class felt like a seminar, not a lecture. It was uncomfortable in the best way. You couldn't just be technically correct; you had to think about context, stakeholders, second-order effects.

The assignment that stuck with me was analyzing TikTok's recommendation system, not the algorithm itself, but its social and ethical impact. We had to map out how the system worked, who it affected, what incentives it created, and where things could go wrong. I started thinking it was just clever use of collaborative filtering. By the end, I was looking at feedback loops that amplify extreme content, filter bubbles that narrow worldviews, and psychological manipulation baked into something as casual as scrolling through videos. The moment it clicked was realizing that AI doesn't just exist in research labs. It shapes every interaction people have online, often in ways they don't notice.

The biggest impact? I now ask "should I build this?" before I ask "can I build this?" Every project since Responsible AI, I spend time thinking about potential harms, edge cases, and who might be negatively affected. I don't always have good answers, but at least I'm asking the questions. I also present projects differently now. I used to focus purely on performance: "I got 87% accuracy, here's my confusion matrix." Now I talk about limitations, failure modes, what the model gets wrong and why that matters. Responsible AI made me a more thoughtful engineer. I'd probably still be optimizing metrics without thinking too hard about what happens after deployment. Now I can't unsee that part."""
        },
        {
            "heading": "Part 4: Beyond the Classroom",
            "content": """I didn't do a formal internship, but I ended up mentoring a high school student on an AI bias project through a connection from Jasmina. The student was preparing for the Central New York science fair and had done previous work on AI ethics. We were scoping a project on bias mitigation strategies. The challenge was explaining AI bias without dumbing it down or drowning her in jargon. Every time I tried to explain fairness metrics or mitigation strategies, I realized I didn't understand them as well as I thought. If you can't explain it simply, you don't really get it. Teaching forced me to strip away technical language and find core concepts. Before the program, I would've helped her build something technically flashy. Now I was focused on building something that clearly demonstrated a concept, even if the implementation was simple."""
        },
        {
            "heading": "Part 5: Key Learning Outcomes",
            "content": """When I started, I thought "end-to-end ML" meant having a Jupyter notebook that ran without errors. Now I know it means data collection, cleaning, pipeline design, model training, evaluation across multiple dimensions, deployment strategy, monitoring, and explaining results to people who don't care about your F1 score. RAG-ception needed a data pipeline that could fetch papers from arXiv daily, parse PDFs reliably, handle duplicates, and store embeddings efficiently. Aurora needed multi-horizon evaluation, handling missing sensor data, and thinking about API latency requirements before the model even worked. The model is maybe 20% of the system. The other 80% is everything around it.

I learned to do research by doing it badly first. CapsNet taught me that you can't just read a paper once and start coding. You need to read it three times, check the appendix, find the author's GitHub if it exists, and accept that you'll still be missing details. My process now: reproduce first, innovate later. I don't start from scratch anymore. I find the closest existing work, get their baseline running, and iterate from there. The other skill: documentation. I keep detailed experiment logs now of what I tried, why it failed, what I learned. Research is iterative, and iteration only works if you remember what you've already tried.

I've written more in this program than I did in four years of undergrad. At first, this felt like busy work. Why am I writing ten pages when the code speaks for itself? But the code doesn't speak for itself. Code tells you what you did; writing tells you why you did it and whether it worked. I got better through repetition and necessity. The mentoring experience helped. Responsible AI helped. Now I structure explanations differently: start with the problem, explain why existing approaches fall short, describe what I did, show results, acknowledge limitations. No jargon unless necessary. If I can't explain my work clearly, that's a sign I don't understand it well enough."""
        },
        {
            "heading": "Part 6: Surprises & Challenges",
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
