import streamlit as st
import cohere
import os

# Set up Cohere API key
cohere_api_key = "2xTRZXXXXXXXXX"  # Replace with your actual API key
co = cohere.Client(cohere_api_key)

def get_cohere_response(prompt):
    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=500
    )
    return response.generations[0].text.strip()

def main():
    st.title("TalentScout Hiring Assistant")
    st.write("Welcome! Please provide your details to begin the screening process.")
    
    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0, max_value=50)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (e.g., Python, Django, SQL)")
        submit = st.form_submit_button("Submit")
    
    if submit:
        if not name or not email or not phone or not tech_stack:
            st.warning("Please fill all required fields.")
        else:
            st.success("Thank you! Generating technical questions...")
            prompt = f"Generate 3-5 technical interview questions for a candidate skilled in {tech_stack}."
            questions = get_cohere_response(prompt)
            st.write("Here are your technical questions:")
            st.write(questions)
            st.write("Good luck with the interview!")
            
if __name__ == "__main__":
    main()
