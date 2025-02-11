import base64
import streamlit as st
from skills_data import get_skills_data
from projects_data import get_projects_data
from animations import load_lottie_animation, display_lottie_animation
from typing import List, Dict

# Set page config
st.set_page_config(
    page_title="My Portfolio",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="auto"
)

def load_local_css(css_file_path: str) -> None:
    """Loads a local CSS file into Streamlit."""
    with open(css_file_path, "r", encoding="utf-8") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

def create_hero_section(name: str, title: str, personal_statement: str, headshot_path: str) -> None:
    """Displays a hero section with a name, title, personal statement, and a responsive headshot."""
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"## {name}")
        st.markdown(f"### {title}")
        st.write(personal_statement)
    with col2:
        # Ensure the image is responsive by using 'use_column_width' in st.image
        st.image(headshot_path, use_container_width=True)

def create_about_section(about_text: str, skills_with_icons: Dict[str, str]) -> None:
    """Displays an 'About Me' section with text and skill icons."""
    st.markdown("## About Me")
    st.write(about_text)

    # Skill icons in a horizontal layout
    icon_cols = st.columns(len(skills_with_icons))
    for (skill, icon), col in zip(skills_with_icons.items(), icon_cols):
        col.markdown(f"### <center>{icon}</center>", unsafe_allow_html=True)
        col.markdown(f"<center>{skill}</center>", unsafe_allow_html=True)

def create_projects_section(projects: List[Dict[str, str]]) -> None:
    """
    Displays a projects section in a grid layout.
    Each project dict has keys: 'title', 'description', 'image_path', 'demo_link', 'github_link'.
    """
    st.markdown("## Projects")
    # Build a grid using columns
    num_cols = 3  # You can adjust for responsive design
    rows = [projects[idx:idx + num_cols] for idx in range(0, len(projects), num_cols)]

    for row in rows:
        cols = st.columns(len(row))
        for project, col in zip(row, cols):
            with col.expander(project["title"]):
                st.image(project["image_path"], use_container_width=True)
                st.write(project["description"])
                st.markdown(f"[Live Demo]({project['demo_link']})" + " | " +
                            f"[GitHub]({project['github_link']})")

def create_skills_section(skills: Dict[str, int]) -> None:
    """
    Displays a skills section with progress bars or some form of visual representation.
    Dictionary keys are skill names, and values are proficiency percentages (0-100).
    """
    st.markdown("## Technical Skills")
    for skill, proficiency in skills.items():
        st.write(f"**{skill}**")
        st.progress(proficiency)

def create_contact_section(email: str, linkedin_url: str, other_links: Dict[str, str]) -> None:
    """Displays a contact section with basic details, plus optional additional links."""
    st.markdown("## Contact")
    st.write(f"**Email:** {email}")
    st.write(f"**LinkedIn:** {linkedin_url}")
    for link_name, link_url in other_links.items():
        st.write(f"**{link_name}:** {link_url}")

@st.cache_data
def encode_image_to_base64(image_path: str) -> str:
    """Encodes an image file as Base64 for potential inline usage."""
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

def main() -> None:
    """Main function that orchestrates the Streamlit portfolio layout."""
    # Load external CSS
    load_local_css("style.css")

    # Animations
    # lottie_dict = load_lottie_animation("assets/lottie.json")
    # display_lottie_animation(lottie_dict, height=300)

    # Hero Section
    create_hero_section(
        name="Khushal Pareta",
        title="Big Data & Machine Learning Enthusiast",
        personal_statement=(
            "Passionate and results-driven Computer Science graduate with strong expertise in advanced Python, SQL, "
            "and Big Data technologies (Hadoop, PySpark, Kafka, Hive, HBase). Proven ability to develop innovative "
            "solutions in computer vision, real-time analytics, and public safety, leveraging frameworks like Flask "
            "and containerization with Docker to build scalable, high-performance applications."
        ),
        headshot_path="assets/headshot.png"  # Replace with your actual image path
    )

    # About Section
    create_about_section(
        about_text=(
            "I blend academic excellence with a collaborative approach to solving complex problems. Having completed "
            "the rigorous PG DBDA course, I've honed practical skills in Python, SQL, and Big Data frameworks. "
            "My experience spans machine learning, anomaly detection, and building real-time data pipelines—"
            "all aimed at creating impactful, tech-driven solutions for real-world challenges."
        ),
        skills_with_icons={
                    "Big Data & Distributed Systems": "🐘",
                    "Real-Time Analytics & Kafka Streams": "📡",
                    "Machine Learning & Anomaly Detection": "🤖",
                    "Containerization (Docker) & DevOps Fundamentals": "🐳",
                    "Cloud Deployments (Azure/AWS)": "☁️"
        }
    )

    # Projects Section
    projects_data = get_projects_data()
    create_projects_section(projects_data)

    # Skills Section
    skills_data = get_skills_data()
    create_skills_section(skills_data)

    # Contact Section
    other_links_data = {
        "GitHub": "https://github.com/Kennny7",
        "Phone": "+91-9024211417"
    }
    create_contact_section(
        email="khushalpareta9@gmail.com",
        linkedin_url="https://www.linkedin.com/in/khushal-pareta-704355338",
        other_links=other_links_data
    )

if __name__ == "__main__":
    main()
