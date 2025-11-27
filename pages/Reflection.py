"""
Reflection Page
Video presentation and 3,000-word blog post about the program experience
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
import config

set_page_config(page_title="Reflection", page_icon="📝")
load_css()

render_header("📝 Program Reflection", "My Journey Through the MS in Applied Data Science")

# Video Section
st.markdown("## 🎥 Video Presentation")

st.markdown(f"""
**Duration:** {config.VIDEO_INFO['duration']}  
**Topics Covered:**
""")

for topic in config.VIDEO_INFO['topics_covered']:
    st.markdown(f"- {topic}")

st.markdown("<br>", unsafe_allow_html=True)

if config.VIDEO_INFO['youtube_url']:
    # Embed YouTube video
    st.video(config.VIDEO_INFO['youtube_url'])
else:
    # Placeholder
    render_info_box(
        """
        <strong>📹 Video Coming Soon!</strong><br>
        The video presentation is currently being recorded and edited. 
        It will be uploaded and embedded here once complete.
        <br><br>
        <strong>What to expect:</strong><br>
        • Overview of my MS ADS program experience<br>
        • Key learnings and insights gained<br>
        • Highlights from favorite courses and projects<br>
        • Career goals and future directions<br>
        • Advice for future data science students
        """,
        box_type="info"
    )

st.markdown("<hr>", unsafe_allow_html=True)

# Blog Post Section
st.markdown(f"## ✍️ {config.BLOG_INFO['title']}")

st.markdown(f"*Target word count: ~{config.BLOG_INFO['word_count_target']} words*")

st.markdown("<br>", unsafe_allow_html=True)

# Table of Contents
with st.expander("📑 Table of Contents", expanded=True):
    st.markdown("""
    1. [Introduction: Setting the Stage](#introduction)
    2. [What I Expected to Learn](#expectations)
    3. [What I Actually Learned](#actual-learning)
    4. [Achieving Learning Outcomes](#learning-outcomes)
    5. [Key Projects Deep Dive](#projects-deep-dive)
    6. [Beyond the Classroom](#beyond-classroom)
    7. [Favorite Classes and Experiences](#favorite-classes)
    8. [Biggest Surprises](#surprises)
    9. [Looking Forward](#looking-forward)
    10. [Conclusion](#conclusion)
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Blog Post Content - Section by Section

# Section 1: Introduction
st.markdown("### <a name='introduction'></a>1. Introduction: Setting the Stage")

st.markdown(f"""
*[Write your introduction here - approximately 200-300 words]*

**Suggested content:**
- Brief background on why you chose the MS ADS program
- Your state of mind when starting the program
- Initial career goals and motivations
- What made Syracuse University's program stand out

**Example opening:**

> When I enrolled in the MS in Applied Data Science program at {config.PROGRAM_INFO['university']} 
in [Month/Year], I was at a crossroads in my career. With a background in electronics engineering 
and experience in hardware research at DRDO, I had developed a fascination with data-driven 
systems but lacked the comprehensive training needed to build robust ML applications. The 
program promised to bridge this gap, offering...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Section 2: Expectations
st.markdown("### <a name='expectations'></a>2. What I Expected to Learn")

st.markdown("""
*[Approximately 300-400 words]*

**Topics to cover:**
- Technical skills you expected to develop (ML, programming, statistics, etc.)
- Career outcomes you hoped for
- Misconceptions or assumptions you had about data science
- Specific areas you wanted to focus on

**Guiding questions:**
- What did you think data science work would be like?
- What skills did you think were most important?
- Were you focused more on theory or application?
- Did you have specific career goals (industry, research, PhD)?

**Placeholder text:**

> Coming into the program, I expected to primarily learn about machine learning algorithms 
and statistical modeling. My experience at Continental and Cirruslabs had exposed me to 
production systems, but I wanted to deepen my theoretical understanding and learn how to...

> I assumed that data science was mainly about building ML models and analyzing data. 
I didn't fully appreciate the importance of...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Section 3: What I Actually Learned
st.markdown("### <a name='actual-learning'></a>3. What I Actually Learned")

st.markdown("""
*[Approximately 400-500 words]*

**Topics to cover:**
- Technical skills actually gained
- Non-technical skills (communication, collaboration, project management)
- Unexpected areas of growth
- How your understanding of data science evolved
- Real-world applications vs. theory

**Structure suggestion:**
1. **Technical Growth:** Advanced ML, systems engineering, research methodology
2. **Soft Skills:** Communication, teamwork, presentation skills
3. **Mindset Shifts:** How you think about problems differently now
4. **Interdisciplinary Learning:** Connections between areas you didn't expect

**Placeholder text:**

> The program exceeded my expectations in ways I hadn't anticipated. Yes, I learned advanced 
machine learning techniques and statistical methods, but more importantly, I learned how to...

> One of the most valuable lessons was understanding that data science isn't just about 
algorithms—it's about...

> The focus on end-to-end systems thinking, from data collection and engineering through 
model deployment and monitoring, gave me a holistic perspective that...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Section 4: Learning Outcomes Achievement
st.markdown("### <a name='learning-outcomes'></a>4. Achieving the Program Learning Outcomes")

st.markdown(f"""
*[Approximately 600-800 words - one of the longest sections]*

The MS ADS program defines {len(config.PROGRAM_INFO['learning_outcomes'])} key learning outcomes. 
Here, I reflect on how I achieved each one through coursework, projects, and practical experience.
""")

for i, outcome in enumerate(config.PROGRAM_INFO['learning_outcomes'], 1):
    st.markdown(f"#### Learning Outcome {i}: {outcome['outcome']}")
    
    st.markdown(f"*{outcome['description']}*")
    
    st.markdown(f"""
    **How I achieved this outcome:**
    
    *[Write 100-150 words explaining:]*
    - Which courses contributed to this outcome
    - Specific projects that demonstrated this skill
    - Concrete examples of applying this knowledge
    - How you've grown in this area
    - Evidence of achievement (grades, feedback, outcomes)
    
    **Example projects:** {', '.join(outcome['projects'])}
    
    **Placeholder text:**
    
    > Through courses like [Course Name] and [Course Name], I developed deep expertise in 
    {outcome['outcome'].lower()}. The {outcome['projects'][0]} project was particularly 
    instrumental in demonstrating this outcome because...
    
    > I initially struggled with [specific aspect], but through [specific experience], 
    I developed proficiency in...
    
    ---
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Section 5: Key Projects Deep Dive
st.markdown("### <a name='projects-deep-dive'></a>5. Key Projects: Deep Dive into Learning")

st.markdown("""
*[Approximately 500-700 words total, ~150-200 words per project]*

**Instructions:** Choose 3 projects that were most impactful to your learning. 
For each project, discuss:
- What you learned (technical and non-technical)
- Challenges you faced and how you overcame them
- How it connected to course material
- Real-world applications or implications
- How it influenced your career direction

**Suggested projects based on your resume:**
1. RAG-ception (ML systems, research, LLMs)
2. CapsNet Classifier (deep learning, research, innovation)
3. Aurora Prediction or CuseBus (applied ML, social impact)
""")

for i in range(1, 4):
    st.markdown(f"#### Project {i}: [Project Title]")
    
    st.markdown("""
    **Placeholder text:**
    
    > The [Project Name] project was transformative for my understanding of [topic]. 
    When I started, I thought [assumption], but through the process of [activity], 
    I realized [insight]...
    
    > **Technical Learning:** I mastered [specific skill/tool/concept], which required me to...
    
    > **Challenge & Growth:** The biggest challenge was [specific challenge]. I overcame this by 
    [specific approach], which taught me the importance of...
    
    > **Course Connections:** This project directly applied concepts from [Course Name], 
    specifically [topic]. It helped me understand how [theoretical concept] translates to 
    [practical application]...
    
    > **Career Impact:** This project reinforced my interest in [career direction] and 
    demonstrated that I can [specific capability]...
    
    ---
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# Section 6: Beyond the Classroom
st.markdown("### <a name='beyond-classroom'></a>6. Learning Beyond the Classroom")

st.markdown("""
*[Approximately 300-400 words]*

**Topics to cover:**
- Industry experience (Continental, Cirruslabs, DRDO)
- Research mentorship activities
- Independent projects
- Networking and professional development
- Conferences, workshops, or competitions attended
- Any internships, iConsults, or external projects

**Placeholder text:**

> My learning extended far beyond classroom lectures and assignments. During my time at 
{config.PROGRAM_INFO['university']}, I...

> **Industry Experience:** My previous roles at Continental Automotive and Cirruslabs provided 
valuable context for understanding how ML systems work in production environments. Specifically...

> **Research Mentorship:** Mentoring a high school student on AI fairness research taught me...

> **Independent Exploration:** Outside of coursework, I pursued projects like [project] because 
I was curious about [topic]. This self-directed learning taught me...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Section 7: Favorite Classes
st.markdown("### <a name='favorite-classes'></a>7. Favorite Classes and Memorable Experiences")

st.markdown("""
*[Approximately 300-400 words]*

**What to include:**
- Your favorite class(es) and why
- Specific professors who influenced you
- Memorable lectures, assignments, or discussions
- Classes that challenged you in unexpected ways
- How these classes shaped your interests

**Placeholder text:**

> **Favorite Class: [Course Name]**
> 
> Without a doubt, [Course Name] taught by [Professor Name] was my favorite class. 
> What made it special was...
> 
> The [specific assignment/project] was particularly memorable because...
> 
> **Other Notable Classes:**
> - **[Course Name]:** This class challenged me to...
> - **[Course Name]:** I appreciated how it connected...
> 
> **Most Challenging Class:**
> 
> [Course Name] was the most difficult course I took, but also one of the most rewarding. 
> I struggled with [concept], but through [effort], I eventually...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Section 8: Biggest Surprises
st.markdown("### <a name='surprises'></a>8. Biggest Surprises and Unexpected Insights")

st.markdown("""
*[Approximately 200-300 words]*

**What surprised you about:**
- The program structure or curriculum
- The data science field itself
- Your own interests and strengths
- The job market or career paths
- The role of communication in data science
- The importance of certain skills you undervalued

**Placeholder text:**

> Looking back, several aspects of the program surprised me:
> 
> **Surprise 1: The Importance of [Aspect]**
> 
> I didn't expect [aspect] to be so crucial for data science work. I learned that...
> 
> **Surprise 2: My Interest in [Area]**
> 
> Before the program, I thought I wanted to focus on [area], but I discovered a passion for 
> [different area] through...
> 
> **Surprise 3: [Community/Culture/Resource]**
> 
> I was pleasantly surprised by [unexpected positive aspect of the program or community]...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Section 9: Looking Forward
st.markdown("### <a name='looking-forward'></a>9. Looking Forward: Career Goals and Next Steps")

st.markdown(f"""
*[Approximately 200-300 words]*

**Topics to cover:**
- Immediate career goals (job search, PhD applications, etc.)
- Long-term vision (5-10 years)
- Areas you want to continue learning
- How the program prepared you for these goals
- Your unique value proposition as a data scientist

**Placeholder text:**

> As I prepare to graduate in {config.PROGRAM_INFO['graduation_date']}, I'm excited about 
the opportunities ahead. My immediate goal is to...
> 
> **PhD Applications:**
> 
> I'm currently applying to PhD programs focused on [research area]. The program has prepared 
me for doctoral study by...
> 
> **Career Vision:**
> 
> Long-term, I want to [career goal]. I'm particularly interested in [specific application area] 
because...
> 
> **Continued Learning:**
> 
> Data science is a rapidly evolving field. I plan to continue developing expertise in...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Section 10: Conclusion
st.markdown("### <a name='conclusion'></a>10. Conclusion: Full Circle")

st.markdown("""
*[Approximately 200-300 words]*

**Wrap up with:**
- Summary of your transformation/growth
- Gratitude (professors, peers, family, etc.)
- Advice for future students
- Final reflections on the value of the program

**Placeholder text:**

> The MS in Applied Data Science program at {config.PROGRAM_INFO['university']} has been 
transformative. I entered as someone with engineering experience but limited ML expertise, 
and I'm leaving as...
> 
> **Gratitude:**
> 
> I'm grateful to [specific people/groups] for [specific contributions to your growth]...
> 
> **Advice for Future Students:**
> 
> For those considering or starting the program, my advice is to...
> 
> **Final Thoughts:**
> 
> If I could summarize my experience in one insight, it would be...

""")

st.markdown("<hr>", unsafe_allow_html=True)

# Writing Progress Tracker
st.markdown("## 📊 Writing Progress Tracker")

st.markdown("""
**Use this section to track your blog post progress:**
""")

sections_complete = st.slider(
    "Sections completed:",
    min_value=0,
    max_value=10,
    value=0,
    help="Track how many of the 10 sections you've written"
)

word_count = st.number_input(
    "Current word count:",
    min_value=0,
    max_value=5000,
    value=0,
    step=100,
    help="Track your progress toward the 3,000 word target"
)

progress_pct = min(100, (word_count / config.BLOG_INFO['word_count_target']) * 100)

st.progress(progress_pct / 100)
st.markdown(f"**Progress:** {word_count:,} / {config.BLOG_INFO['word_count_target']:,} words ({progress_pct:.1f}%)")

if progress_pct >= 100:
    st.balloons()
    st.success("🎉 Congratulations! You've reached your word count target!")

st.markdown("<hr>", unsafe_allow_html=True)

# Tips for Writing
with st.expander("💡 Writing Tips & Guidelines"):
    st.markdown("""
    **General Writing Advice:**
    
    1. **Be Authentic:** Write in your own voice. Share genuine experiences and emotions.
    
    2. **Show, Don't Tell:** Instead of saying "I learned a lot," describe specific moments of discovery.
    
    3. **Use Concrete Examples:** Back up general statements with specific project experiences.
    
    4. **Balance Technical and Personal:** Include enough technical detail to be credible, but focus on 
    the learning journey.
    
    5. **Edit Ruthlessly:** First draft should be longer than 3,000 words, then cut to the most impactful content.
    
    **Structure Tips:**
    
    - **Introduction:** Hook readers with a compelling opening about your journey
    - **Body:** Organize by themes (not chronologically) for better flow
    - **Conclusion:** Circle back to your opening to show transformation
    
    **Audience Considerations:**
    
    This blog post will be read by:
    - Potential employers evaluating your communication skills
    - PhD admissions committees assessing your research potential
    - Future ADS students looking for program insights
    - Faculty evaluating your learning outcomes achievement
    
    **Tone:** Professional but personal, reflective but not overly casual
    """)
