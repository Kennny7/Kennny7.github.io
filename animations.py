import json
from typing import Dict
import streamlit as st

def load_lottie_animation(file_path: str) -> Dict:
    """
    Loads a local Lottie JSON file and returns it as a dictionary
    for rendering via streamlit-lottie.
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

def display_lottie_animation(lottie_dict: Dict, height: int = 300) -> None:
    """
    Displays the Lottie animation in a Streamlit app using the streamlit-lottie component.
    To use this, you need to install 'streamlit-lottie' via:
        pip install streamlit-lottie
    Then import and call st_lottie function:
        from streamlit_lottie import st_lottie
    """
    try:
        from streamlit_lottie import st_lottie
        st_lottie(lottie_dict, height=height, key=None)
    except ImportError:
        st.error("Please install 'streamlit-lottie' to display animations (pip install streamlit-lottie).")


# For downloading more such animations, you can visit this link: https://lottiefiles.com