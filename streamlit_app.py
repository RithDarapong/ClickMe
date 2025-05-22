import streamlit as st
import streamlit.components.v1 as components

# Page settings
st.set_page_config(page_title="Mission: Impossible", layout="centered")

# Custom CSS for full centering and theme
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: red;
        font-family: 'Courier New', monospace;
    }
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .center-button > button {
        background-color: red;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px 24px;
        transition: 0.3s;
        margin-top: 20px;
    }
    .center-button > button:hover {
        background-color: #a10000;
        transform: scale(1.05);
    }
    .surprise-text {
        font-size: 25px;
        color: lightgreen;
        margin-bottom: 5px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML-based layout for perfect centering
st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.markdown("<h1>Hi Molly!! How are you Today?</h1>", unsafe_allow_html=True)

# Streamlit Button in a styled div
clicked = st.button("Click to Accept the Mission POSSIBLE!", key="center-button", help="Accept the mission")
st.markdown('</div>', unsafe_allow_html=True)

# Display image and play sound only after button is clicked
if clicked:
    # Audio component (auto play on click)
    audio_file_url = "https://orangefreesounds.com/wp-content/uploads/2025/04/Celebration-horn-sound-effect.mp3"
    components.html(f"""
        <audio autoplay>
            <source src="{audio_file_url}" type="audio/mpeg">
        </audio>
    """, height=0)

    # Show message + image
    st.markdown('<div class="surprise-text">🥳 Surprised!! You are invited to join to see the Movie!!</div>', unsafe_allow_html=True)
    st.image("images/pic1.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
