import streamlit as st
from PIL import Image

# ------------------ CONFIGURATION ------------------
st.set_page_config(page_title="Arnob Majumder Portfolio", layout="wide")

# ------------------ SIDEBAR ------------------
with st.sidebar:
    profile_image = Image.open("Arnob Majumder.jpg")  # Replace with your actual profile image
    st.image(profile_image, width=200)

    st.title("Arnob Majumder")
    st.write("📍 Kolkata, India")
    st.write("📧 arnob.majumder24-26@bibs.co.in")
    st.write("📞 +91 8481054446")

    st.markdown("### 🔗 Connect with me")
    st.markdown("""
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://linkedin.com)  <!-- Replace with actual link -->
    """)

# ------------------ MAIN CONTENT ------------------

st.title("💼 Personal Portfolio")

# Summary
st.header("🔍 Summary")
st.write("""
I’m an aspiring Data Analyst with a background in Information Technology and a passion for transforming data into actionable insights. 
Currently pursuing an MBA in Business Analytics & Data Science at BIBS, I have hands-on experience with Python, SQL, and tools like Power BI and Excel. 
I enjoy visualizing trends and crafting compelling stories with data.
""")

# Education
st.header("🎓 Education")
st.write("""
- **PGP + MBA in Business Analytics & Data Science** – Bengal Institute of Business Studies *(2024 - Present)*  
- **B.Tech in Information Technology** – Narula Institute of Technology *(2017 - 2021)* — 68%  
- **Class XII (Science)** – Belgharia High School *(2015 - 2017)* — 64%  
- **Class X (General)** – Belgharia High School *(2015)* — 84.57%
""")

# Experience
st.header("💼 Experience")
st.write("""
**Data Analyst Intern** – Prodigy InfoTech *(April 2024 – May 2024)*  
- Gained hands-on experience in data analysis, interpretation, and visualization as part of a practical internship in Kolkata.
""")

# Skills
st.header("🛠️ Skills")
st.write("""
- **Languages**: Python, SQL  
- **Tools & Technologies**: Power BI, MySQL, Advanced Excel, Pandas, NumPy, Seaborn, Matplotlib  
- **Other Skills**: Data Visualization, Data Analysis, Critical Thinking, Communication, Presentation
""")

# Projects
st.header("🚀 Projects")
st.write("""
**Car Sales Analysis**  
- Created dashboards using Power BI and Excel to analyze sales by brand, type, region, and customer preferences.  
- Helped in policy formulation through data-driven insights.

**Vehicle Parking Management System**  
- Developed a system using Apache Web Server and MySQL to manage parking data.  
- Designed for Windows OS and deployed on Chrome for usability.
""")

# Certifications
st.header("📜 Certifications")
st.write("""
- Machine Learning with Python – IIT Kanpur  
- Student Development Program on ML with Python – IIT Kanpur  
- Data Analysis Using Python – IBM Cognitive AI  
- SQL & Relational Databases 101 – IBM Cognitive AI  
- Data Science Methodology – IBM Cognitive AI  
- Data Science 101 – IBM Cognitive AI  
- The Joy of Computing Using Python – NPTEL
""")

# Achievements
st.header("🏆 Achievements")
st.write("""
- Finalist in Group Discussion Competition – BIBS  
- Top 3 Best Team in Presentation – Narula Institute of Technology
""")

# Hobbies
st.header("🎨 Hobbies")
st.write("""
In my free time, I enjoy:
- Exploring new tech trends  
- Public speaking and group discussions  
- Watching educational YouTube channels  
- Playing strategy-based games
""")

# Footer
st.markdown("---")
st.write("Made with ❤️ by Arnob Majumder | © 2025")
