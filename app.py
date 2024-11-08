import streamlit as st
import streamlit.components.v1 as components

def main():
    # Page configuration
    st.set_page_config(
        page_title="Hadiadj Aoul Mohammed Yassin - CV",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .section {
            margin-bottom: 2rem;
        }
        .section-title {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
        }
        .contact-info {
            text-align: center;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='header'>HADIADJ AOUL MOHAMMED YASSIN</h1>", unsafe_allow_html=True)
    
    # Contact Information
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("📍 Tlemcen, Tlemcen, Algeria")
    with col2:
        st.markdown("📧 hadjadjaoulmohammedyassine@gmail.com")
    with col3:
        st.markdown("📱 +213 659 012 6015")

    # Professional Experience
    st.markdown("<h2 class='section-title'>PROFESSIONAL EXPERIENCE</h2>", unsafe_allow_html=True)
    
    with st.expander("Infograph Designer & CNC Machinist (2021 - Present)", expanded=True):
        st.markdown("""
        - Design and implement furniture projects using Polyboard CAD software
        - Create and optimize CNC toolpaths using ArtCam/Aspire
        - Organize production layouts and technical drawings with CorelDraw
        - Manage complete project workflow from design to final production
        - Operate CNC machinery for precise wood processing
        - Ensure quality control of finished products
        """)

    with st.expander("Sales Associate | Gaming Shop (2020 - 2021)", expanded=True):
        st.markdown("""
        - Provided customer service and product recommendations
        - Managed inventory and store displays
        - Processed sales transactions and maintained store organization
        - Built strong relationships with customers and increased repeat business
        """)

    with st.expander("Certified Aluminum Joinery Specialist (2015 - 2020)", expanded=True):
        st.markdown("""
        - Fabricated and installed aluminum frames and structures
        - Performed measurements and calculations for custom installations
        - Managed project timelines and client requirements
        - Ensured quality control and safety standards
        - Applied technical certification knowledge to complex installations
        """)

    # Education & Certifications
    st.markdown("<h2 class='section-title'>EDUCATION & CERTIFICATIONS</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Bachelor's Degree in English Literature**  
      Abu-Bakr Belkaid University, Tlemcen | 2011 - 2014
    - **Professional Certificate in Aluminum Joinery**  
      Vocational Training Center of Sidi Said | 2018
    - **Baccalauréat** | 2011
    """)

    # Skills
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h2 class='section-title'>TECHNICAL SKILLS</h2>", unsafe_allow_html=True)
        st.markdown("""
        **CAD Software**
        - Polyboard
        - CorelDraw
        - ArtCam/Aspire

        **Technical**
        - CNC Machine Operation
        - Python Programming
        - Manufacturing Processes

        **Professional**
        - Quality Control
        - Technical Drawing
        - Inventory Management
        """)

    with col2:
        st.markdown("<h2 class='section-title'>ADDITIONAL SKILLS</h2>", unsafe_allow_html=True)
        st.markdown("""
        - Bilingual: Arabic, English, French
        - Problem Solving
        - Customer Service
        - Project Management
        - Attention to Detail
        """)

    # Extracurricular Activities
    st.markdown("<h2 class='section-title'>EXTRACURRICULAR ACTIVITIES</h2>", unsafe_allow_html=True)
    st.markdown("""
    - Judo Training and Competition (2016-2020)
    - Self-taught Python Developer
    - Active participation in manufacturing technology workshops
    """)

if __name__ == "__main__":
    main()