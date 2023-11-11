import streamlit as st
import openai

# Function to generate images using OpenAI's DALL-E model
def generate_image(prompt, api_key):
    if not api_key:
        st.error("Please enter your OpenAI API Key.")
        return

    try:
        openai.api_key = api_key
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            n=1,
        )

        image_url = response['data'][0]['url']
        st.image(image_url)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app layout
st.title("OpenAI Image Generator")

# API key input
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# User prompt input
prompt = st.text_area("Enter your prompt for image generation", height=100)

# Generate image button
if st.button("Generate Image"):
    generate_image(prompt, api_key)
