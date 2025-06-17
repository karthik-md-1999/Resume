# resume_app.py

import streamlit as st

# ----- HEADER -----
st.set_page_config(page_title="Karthik M D - Resume", layout="wide")

# ----- TITLE -----
st.title("💼 Karthik M D")
st.markdown("""
📍 Banglore | 📧 [karthikmd1445@gmail.com](mailto:karthikmd1445@gmail.com) | 📞 9972715937  
🔗 [LinkedIn](https://linkedin.com/in/Karthik%20M%20D) | 🐙 [GitHub](https://github.com/karthik-md-1999)
""")

# ----- SUMMARY -----
st.header("🧾 Summary")
st.write("""
Highly passionate and motivated individual with a proven ability to develop complex designs and resolve software issues. 
Looking for a challenging role to leverage my skills and contribute to organizational growth.
""")

# ----- SKILLS -----
st.header("🛠️ Skills")
st.markdown("""
- **Languages:** Python, JavaScript, SQL, Basic Java  
- **Technologies & Tools:** Node.js, Flask, Docker, MySQL, Express, Machine Learning, Data Visualization  
- **NLP:** Strong knowledge of text preprocessing, tokenization, embeddings, basic NLP libraries
""")

# ----- EDUCATION -----
st.header("🎓 Education")
st.markdown("""
**Siddaganga Institute Of Technology**  
_MCA, Feb 2022 – Sept 2023_  
- CGPA: 8.9/10  
- Coursework: Computer Applications, OOP, Databases, Machine Learning
""")

# ----- EXPERIENCE -----
st.header("💼 Experience")

st.subheader("Member of Technical Staff, Graylinx Pvt Ltd")
st.caption("June 2023 – Present")
st.markdown("""
- Developed FDD systems for chillers and AHUs using Python.
- Built RESTful APIs with Flask & Node.js.
- Implemented ML algorithms for fault analysis and prediction.
- Used Docker, MySQL, MongoDB for containerization and data management.
- Automated monthly SQL dumps, DAG tasks and database transfers.

**Key Highlights:** Reinforcement learning for optimizing chiller plant operations.
""")

st.subheader("Software Engineer Intern, Polynomial AI India Pvt Ltd")
st.caption("Feb 2023 – Mar 2023")
st.markdown("""
- Developed scalable backend systems using Django and Node.js.
- Focused on robust API design and backend integration.
""")

# ----- CERTIFICATIONS -----
st.header("📜 Certifications")
st.markdown("""
- NPTEL: Programming in Java  
- Internship Completion Certificate – Polynomial AI
""")
