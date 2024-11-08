import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

def main():
    # Page configuration
    st.set_page_config(
        page_title="Hadiadj Aoul Mohammed Yassin - Professional Portfolio",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for professional styling
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        .main {
            font-family: 'Roboto', sans-serif;
            color: #2C3E50;
            background-color: #f5f7fa;
        }
        
        .header-name {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            color: #1a237e;
            margin-bottom: 0.5rem;
            padding: 1rem;
            background: linear-gradient(to right, #e3f2fd, #bbdefb);
            border-radius: 10px;
        }
        
        .header-title {
            font-size: 1.5rem;
            text-align: center;
            color: #37474f;
            margin-bottom: 2rem;
        }
        
        .contact-info {
            background-color: #e3f2fd;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .section-title {
            color: #1a237e;
            font-size: 1.5rem;
            font-weight: 500;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #1a237e;
        }
        
        .experience-box {
            background-color: #e3f2fd;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            color: #1a237e;
        }
        
        .experience-box h3, .experience-box h4 {
            color: #1a237e;
            margin-bottom: 0.5rem;
        }
        
        .experience-box ul {
            color: #2C3E50;
        }
        
        .experience-box li {
            margin-bottom: 0.5rem;
        }
        
        .skill-tag {
            background-color: #1a237e;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.25rem;
            display: inline-block;
            font-size: 0.9rem;
        }
        
        .highlight {
            color: #1a237e;
            font-weight: 500;
        }
        
        .date-range {
            color: #37474f;
            font-style: italic;
        }
        
        .achievement {
            margin-left: 1.5rem;
            margin-bottom: 0.5rem;
            color: #2C3E50;
        }
        
        .download-button {
            background-color: #1a237e;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 5px;
            text-decoration: none;
            margin-top: 1rem;
            display: inline-block;
        }

        /* Override Streamlit's default background */
        .stApp {
            background-color: #f5f7fa;
        }

        /* Make sure links are visible */
        a {
            color: #1a237e;
            text-decoration: underline;
        }

        /* Ensure text in markdown is visible */
        p, li {
            color: #2C3E50;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("<h1 class='header-name'>HADIADJ AOUL MOHAMMED YASSIN</h1>", unsafe_allow_html=True)
    st.markdown("<p class='header-title'>Infograph Designer & CNC Specialist & Python Dev</p>", unsafe_allow_html=True)

    # Contact Information
    contact_cols = st.columns(4)
    with contact_cols[0]:
        st.markdown("🏠 Tlemcen, Algeria")
    with contact_cols[1]:
        st.markdown("📧 hadjadjaoulmohammedyassine@gmail.com")
    with contact_cols[2]:
        st.markdown("📱 +213 659 012 6015")
    with contact_cols[3]:
        st.markdown("🔗 [LinkedIn](#)")

    # Professional Summary
    st.markdown("<h2 class='section-title'>PROFESSIONAL SUMMARY</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='experience-box'>
        Experienced Infograph Designer and CNC Machinist with over 5 years of expertise in furniture design and manufacturing. 
        Skilled in CAD software, CNC operation, and project management. Proven track record of delivering high-quality products 
        while maintaining efficient production workflows. Multilingual professional with strong technical and creative abilities.
        </div>
    """, unsafe_allow_html=True)

    # Core Competencies
    st.markdown("<h2 class='section-title'>CORE COMPETENCIES</h2>", unsafe_allow_html=True)
    competencies = [
        "CAD/CAM Software", "CNC Programming", "Project Management", 
        "Quality Control", "Technical Drawing", "Production Optimization",
        "Customer Relations", "Process Improvement", "Team Leadership"
    ]
    
    comp_cols = st.columns(3)
    for i, comp in enumerate(competencies):
        with comp_cols[i % 3]:
            st.markdown(f"<div class='skill-tag'>{comp}</div>", unsafe_allow_html=True)

    # Professional Experience
    st.markdown("<h2 class='section-title'>PROFESSIONAL EXPERIENCE</h2>", unsafe_allow_html=True)
    
    # Current Position
    st.markdown("""
        <div class='experience-box'>
            <h3 class='highlight'>Infograph Designer & CNC Machinist</h3>
            <p class='date-range'>2021 - Present</p>
            <p><strong>Key Responsibilities & Achievements:</strong></p>
            <ul>
                <li>Designed and implemented 100+ custom furniture projects using Polyboard software</li>
                <li>Reduced production time by 30% through optimized CNC toolpath programming</li>
                <li>Managed end-to-end project workflows for high-value client orders</li>
                <li>Implemented quality control processes reducing defect rate by 25%</li>
                <li>Leading a team of 5 for & Supervising other CNC Programmers</li>
            </ul>
            <p><strong>Technologies:</strong> Polyboard, ArtCam/Aspire, CorelDraw, CNC Programming</p>
        </div>
    """, unsafe_allow_html=True)

    # Previous Positions (Similar format)
    st.markdown("""
        <div class='experience-box'>
            <h3 class='highlight'>Certified Aluminum Joinery Specialist</h3>
            <p class='date-range'>2015 - 2020</p>
            <ul>
                <li>Successfully completed 200+ custom aluminum installations</li>
                <li>Maintained 98% client satisfaction rate</li>
                <li>Led a team of 3 installers for large-scale projects</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Skills Matrix
    st.markdown("<h2 class='section-title'>TECHNICAL SKILLS MATRIX</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
            <div class='experience-box'>
                <h4>Software & Design</h4>
                <ul>
                    <li>Polyboard (Expert)</li>
                    <li>CorelDraw (Expert)</li>
                    <li>ArtCam (Advanced)</li>
                    <li>Aspire (Advanced)</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
            <div class='experience-box'>
                <h4>Technical Skills</h4>
                <ul>
                    <li>CNC Programming & Operation</li>
                    <li>Manufacturing Processes</li>
                    <li>Quality Control Systems</li>
                    <li>Technical Documentation</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
            <div class='experience-box'>
                <h4>Languages</h4>
                <ul>
                    <li>Arabic (Native)</li>
                    <li>English (Fluent)</li>
                    <li>French (Intermediate)</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Education & Certifications
    st.markdown("<h2 class='section-title'>EDUCATION & CERTIFICATIONS</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='experience-box'>
            <ul>
                <li><strong>Bachelor's Degree in English Literature</strong><br>
                    Abu-Bakr Belkaid University, Tlemcen (2011 - 2014)</li>
                <li><strong>Professional Certificate in Aluminum Joinery</strong><br>
                    Vocational Training Center of Sidi Said (2018)</li>
                <li><strong>CNC Programming and Operation Certification</strong><br>
                    Industrial Training Institute (2021)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Professional Development
    st.markdown("<h2 class='section-title'>PERSONAL DEVELOPMENT</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='experience-box'>
            <ul>
                <li>Python Discord/Telegram Bots</li>
                <li>WebScraping</li>
                <li>Judoka</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
