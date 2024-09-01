import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "AIzaSyDwh-PhJuA8NVKEZ9hFGVzRzXiGA6WJFb0"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    try:
        response = model.generate_content(user_input)
        if response and hasattr(response, 'text'):
            return response.text
        else:
            return "Sorry, I couldn't generate a response. Please try again."
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit interface
st.set_page_config(page_title="Fitness Insight Generator", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        text-align: center; 
        font-size: 2.5rem; 
        color: #FF6347; 
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 1.5rem; 
        color: #4CAF50; 
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .result-box {
        background-color: #F0F8FF;
        border: 2px solid #00CED1;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .chat-box {
        background-color: #FAF0E6;
        border: 2px solid #D2691E;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #333; /* Darker text color */
    }
    </style>
""", unsafe_allow_html=True)

# Center the title
st.markdown("<h1 class='main-title'>💪 Fitness Insight Generator 💪</h1>", unsafe_allow_html=True)
st.write("Powered by Google Generative AI")

# User input form
with st.form(key="user_input_form", clear_on_submit=True):
    st.markdown("<h2 class='section-title'>Enter your fitness details:</h2>", unsafe_allow_html=True)
    
    age = st.number_input("Age", min_value=0, max_value=120, step=1, value=16)
    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, value=60.0)
    height_feet = st.number_input("Height (Feet)", min_value=0, step=1, value=5)
    height_inches = st.number_input("Height (Inches)", min_value=0, max_value=11, step=1, value=8)
    fitness_goals = st.text_input("Your fitness goals", value="Improve endurance and build muscle")
    physical_activity_status = st.selectbox("Physical Activity Status", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"], index=2)

    submit_button = st.form_submit_button("Get Insights")

    if submit_button:
        # Convert height to centimeters
        height = height_feet * 30.48 + height_inches * 2.54

        # Create the input for the chatbot to generate a response
        user_input = f"Age: {age}, Weight: {weight}, Height: {height:.2f} cm, Fitness Goals: {fitness_goals}, Physical Activity Status: {physical_activity_status}"
        response = get_chatbot_response(user_input)

        # Display the response
        st.markdown(f"""
        <div class='result-box'>
            <h2 class='section-title'>Your Fitness Insights:</h2>
            <div class='chat-box'>
                <p>{response}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
