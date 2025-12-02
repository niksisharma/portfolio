import streamlit as st
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
import config

st.set_page_config(
    page_title="CuseBus - Project Details",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path(__file__).parent.parent.parent / "assets" / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

project = next((p for p in config.PROJECTS if p['id'] == 'cusebus'), None)

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
st.markdown('<div class="section-header">TECHNICAL APPROACH</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="terminal">
$ cat analysis_methodology.txt

Data: {project['technical_details']['data']}
Analysis: {project['technical_details']['analysis']}
Optimization: {project['technical_details']['optimization']}
Visualization: {project['technical_details']['visualization']}
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

# Results
st.markdown('<div class="section-header">RESULTS & IMPACT</div>', unsafe_allow_html=True)

results_cols = st.columns(3)

with results_cols[0]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">-18%</div>
        <h3>Wait Time Reduction</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[1]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">3</div>
        <h3>Underserved Routes</h3>
    </div>
    """, unsafe_allow_html=True)

with results_cols[2]:
    st.markdown("""
    <div class="interest-item">
        <div class="interest-icon" style="font-size: 3rem;">+25%</div>
        <h3>Peak Hour Capacity</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Recommendations
st.markdown('<div class="section-header">KEY RECOMMENDATIONS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-info">
    <div class="project-body">
        <h3 style="color: var(--primary-teal); margin-bottom: 1rem;">Data-Driven Operations Improvements</h3>
    </div>
</div>
""", unsafe_allow_html=True)

rec_cols = st.columns(3)

with rec_cols[0]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Route Adjustments</h3>
        <p style="color: var(--text-dark);">Identified 3 routes needing additional buses during peak hours</p>
    </div>
    """, unsafe_allow_html=True)

with rec_cols[1]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Schedule Optimization</h3>
        <p style="color: var(--text-dark);">Proposed staggered schedules based on actual ridership patterns</p>
    </div>
    """, unsafe_allow_html=True)

with rec_cols[2]:
    st.markdown("""
    <div class="skill-card" style="text-align: left;">
        <h3>Bottleneck Resolution</h3>
        <p style="color: var(--text-dark);">Network analysis revealed key transfer points causing delays</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Challenges
st.markdown('<div class="section-header">CHALLENGES & LEARNINGS</div>', unsafe_allow_html=True)

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

with st.expander("📄 Network Graph Construction"):
    st.code("""
# Building bus route network
import networkx as nx
import pandas as pd

def build_route_network(gps_data):
    G = nx.DiGraph()
    
    # Add stops as nodes
    for stop in stops_df.itertuples():
        G.add_node(stop.stop_id, 
                  pos=(stop.lat, stop.lon),
                  name=stop.stop_name)
    
    # Add routes as edges with ridership weights
    for route in routes_df.itertuples():
        G.add_edge(route.from_stop, route.to_stop,
                  route_id=route.route_id,
                  ridership=route.avg_ridership,
                  travel_time=route.avg_time)
    
    return G
    """, language="python")

with st.expander("📄 Bottleneck Analysis"):
    st.code("""
# Identifying network bottlenecks using centrality
import networkx as nx

def analyze_bottlenecks(G):
    # Betweenness centrality identifies critical transfer points
    betweenness = nx.betweenness_centrality(G, weight='travel_time')
    
    # Degree centrality shows connectivity
    degree = nx.degree_centrality(G)
    
    # Find stops with high betweenness but low capacity
    bottlenecks = []
    for node in G.nodes():
        if betweenness[node] > 0.1 and capacity[node] < ridership[node]:
            bottlenecks.append({
                'stop': node,
                'betweenness': betweenness[node],
                'overcapacity': ridership[node] / capacity[node]
            })
    
    return pd.DataFrame(bottlenecks).sort_values('betweenness', ascending=False)
    """, language="python")

with st.expander("📄 Route Optimization (VRP)"):
    st.code("""
# Vehicle Routing Problem with time windows
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def optimize_routes(distance_matrix, demand, time_windows):
    # Create routing model
    manager = pywrapcp.RoutingIndexManager(
        len(distance_matrix), 
        num_vehicles=5, 
        depot=0
    )
    routing = pywrapcp.RoutingModel(manager)
    
    # Add time window constraints
    time = 'Time'
    routing.AddDimension(
        transit_callback_index,
        30,  # allow 30min waiting
        180,  # maximum route time
        False,
        time
    )
    
    # Solve
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    solution = routing.SolveWithParameters(search_parameters)
    
    return extract_routes(solution, manager, routing)
    """, language="python")

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)

# Links
st.markdown('<div class="section-header">LINKS & RESOURCES</div>', unsafe_allow_html=True)

link_cols = st.columns(4)
for i in range(4):
    with link_cols[i]:
        st.button(["📂 GitHub", "🗺️ Map Viz", "📄 Report", "📊 Presentation"][i], 
                 disabled=True, use_container_width=True)

st.markdown('<div class="pixel-divider"></div>', unsafe_allow_html=True)
st.link_button("← Back to All Projects", "/Projects", use_container_width=False)