# import openai
# import streamlit as st
# import speech_recognition as sr
# import pyttsx3

# # Set up OpenAI API key
# openai.api_key = ""

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# # Function to recognize speech
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             st.write(f"You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             st.write("Sorry, I couldn't understand that.")
#             return None
#         except sr.RequestError:
#             st.write("Speech recognition service is down.")
#             return None

# # Function to generate a response using OpenAI
# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     return response.choices[0].text.strip()

# # Function to speak the response
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Streamlit app
# def main():
#     st.title("Voice Chatbot for Autism Children")
#     st.write("Click the button below and speak to the chatbot.")

#     if st.button("Start Chat"):
#         user_input = recognize_speech()
#         if user_input:
#             response = generate_response(user_input)
#             st.write(f"Chatbot: {response}")
#             speak(response)

# if __name__ == "__main__":
#     main()








import openai
import streamlit as st
import speech_recognition as sr
import pyttsx3
import pythoncom

# Set up OpenAI API key
openai.api_key = ""  # Replace with your OpenAI API key

# Initialize text-to-speech engine
def init_engine():
    pythoncom.CoInitialize()  # Initialize COM library
    return pyttsx3.init()

engine = init_engine()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        st.write("Speech recognition service is down.")
        return None
    except OSError:
        st.write("No microphone found. Please check your audio settings.")
        return None

# Function to generate a response using OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Custom CSS for modern interface
def inject_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            color: #333;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 12px;
            padding: 10px 24px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        .stTitle {
            color: #4CAF50;
            font-size: 36px;
            font-weight: bold;
        }
        .stWrite {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Streamlit app
def main():
    # Inject custom CSS
    inject_custom_css()

    # App title and description
    st.title("Voice Chatbot for Autism Children")
    st.markdown("Welcome to the **Voice Chatbot**! Click the button below and speak to the chatbot.")

    # Chatbot interface
    if st.button("Start Chat", key="start_chat"):
        user_input = recognize_speech()
        if user_input:
            response = generate_response(user_input)
            st.markdown(f"**Chatbot:** {response}", unsafe_allow_html=True)
            speak(response)

if __name__ == "__main__":
    main()







