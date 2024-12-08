import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import os

st.set_page_config(
    page_title="EngageVision - Youtube Thumbnail Engager", 
    page_icon="https://img.icons8.com/?size=100&id=WogJuEKB4InH&format=png&color=000000",
)


# Load the trained model
MODEL_PATH = 'thumbnail_model.h5' #your trained thumbnail model

# Ensure the model file exists
if not os.path.exists(MODEL_PATH):
    st.error(f"Model file '{MODEL_PATH}' not found. Please train and save your model first.")
    st.stop()

model = tf.keras.models.load_model(MODEL_PATH)

# Function to preprocess the image
def preprocess_image(image):
    """
    Preprocess the uploaded image to match the model's input requirements.
    - Resize to 224x224
    - Normalize pixel values to [0, 1]
    - Expand dimensions to create a batch
    """
    img = image.resize((224, 224))  # Resize to match model input size
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Streamlit app interface
st.title("YouTube Thumbnail Engagement Checker")
st.write("Upload a YouTube thumbnail image, and the AI will predict whether it's engaging or not.")

# File uploader
uploaded_file = st.file_uploader("Upload a thumbnail (JPG only)", type=["jpg"])

if uploaded_file is not None:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Thumbnail", use_container_width=True)

        # Preprocess the image
        img = preprocess_image(image)

        # Make a prediction
        prediction = model.predict(img)[0][0]

        # Display the result
        if prediction > 0.5:
            st.success("🎉 This thumbnail is likely to be engaging!")
        else:
            st.warning("⚠️ This thumbnail might not be engaging. Try improving it.")

        # Debugging: Show prediction score
        st.write(f"Prediction Score: {prediction:.2f}")
    except Exception as e:
        st.error(f"An error occurred while processing the image: {e}")


# Sidebar with social media icons
st.sidebar.markdown(
    
    """
    # Made with ❤️ from Ved Sharanagate  

    ## Social Handles

    [![GitHub](https://img.icons8.com/?size=40&id=EBCun1ZMi1Jt&format=png&color=000000)](https://github.com/VortexV7)
    -- Github 
    ###
    [![LinkedIn](https://img.icons8.com/?size=40&id=tvG-nQ3s2hZL&format=png&color=000000)](https://www.linkedin.com/in/ved-sharanagate/)
    -- LinkedIn
    ###
    [![Instagram](https://img.icons8.com/?size=40&id=EVUDET6Ig1I5&format=png&color=000000)](https://www.instagram.com/veddd.zip/)
    -- Instagram

    ## Buy Me A Coffee
    [![BuyMeACoffee](https://i.ibb.co/9cRfwt1/bmc-button.png)](https://buymeacoffee.com/veddd.zip)

    """,

    unsafe_allow_html=True,
)	
