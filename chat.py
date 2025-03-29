import streamlit as st
import cohere
import time

# Set Cohere API Key
COHERE_API_KEY = "2xTRZVraYBDx8GILR5d8CuTtwvyWnsiHayzM1TH5"
co = cohere.Client(COHERE_API_KEY)

# AI Response Function
def get_cohere_response(prompt):
    """Fetch response from Cohere API."""
    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=300
    )
    return response.generations[0].text.strip()

# Page Styling
st.markdown("""
    <style>
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        @keyframes slideUp {
            from {transform: translateY(20px); opacity: 0;}
            to {transform: translateY(0); opacity: 1;}
        }
        .title {
            font-size: 38px;
            font-weight: bold;
            text-align: center;
            color: #FF4B4B;
            animation: fadeIn 2s ease-in-out;
        }
        .subtext {
            font-size: 18px;
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        
        .contact-section {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-top: 40px;
            animation: fadeIn 2s ease-in-out;
        }
        .name {
            font-size: 24px;
            color: #FF4B4B;
            font-weight: bold;
        }
        .link, .email {
            font-size: 18px;
            color: #007BFF;
            text-decoration: none;
            font-weight: bold;
        }
        .link:hover, .email:hover {
            color: #FF4B4B;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<div class="title">🚀 AI TalentScout Hiring Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">AI-powered tool to generate customized interview questions based on your tech skills.</div>', unsafe_allow_html=True)

# Form Section
with st.form("candidate_form"):
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    name = st.text_input("📌 Full Name")
    email = st.text_input("📧 Email Address")
    phone = st.text_input("📞 Phone Number")
    experience = st.number_input("💼 Years of Experience", min_value=0, max_value=50)
    position = st.text_input("🎯 Desired Position(s)")
    location = st.text_input("📍 Current Location")
    tech_stack = st.text_area("🛠️ Tech Stack (e.g., Python, Django, SQL)")

    submit = st.form_submit_button("🚀 Generate Questions")

st.markdown('</div>', unsafe_allow_html=True)

if submit:
    if not name or not email or not phone or not tech_stack:
        st.warning("⚠️ Please fill all required fields.")
    else:
        processing_message = st.empty()  # Create an empty placeholder
        processing_message.success("✅ Processing... Please wait.")  
        time.sleep(2)  

        st.write("### 🎓 AI-Generated Technical Questions:")
        prompt = f"Generate 3-5 advanced interview questions for a candidate skilled in {tech_stack}."
        questions = get_cohere_response(prompt)
        st.write(questions)
        st.write("📢 Good luck with the interview! 🚀")

        processing_message.empty()  # Clear the processing message

# Contact Section
st.markdown("""
    <div class="contact-section">
        <p class="name">👨‍💻 Nikhil Sukthe</p>
        <p>🌐 <a class="link" href="https://nikhilsukthe.vercel.app/" target="_blank">My Portfolio</a></p>
        <p>📧 <a class="email" href="mailto:sukthenikhil@gmail.com">sukthenikhil@gmail.com</a></p>
    </div>
""", unsafe_allow_html=True)
