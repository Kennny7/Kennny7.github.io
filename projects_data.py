from typing import List, Dict

def get_projects_data() -> List[Dict[str, str]]:
    """
    Returns a list of dictionaries containing project details.
    Each project dictionary has the following keys:
      - title
      - description
      - image_path
      - demo_link
      - github_link

    (Optional Enhancement) 
    You can also include additional keys like 'technologies'
    if you want to store more project data. This won't affect
    the existing main code since it doesn't reference them,
    but will be available if you choose to display them later.
    """

    return [
        {
            "title": "Maskify: Computer Vision-Based Mask Detection",
            "description": (
                "Developed an automated solution to detect mask usage in real-time using Python, OpenCV, "
                "and Convolutional Neural Networks (CNNs). The system helps public authorities ensure mask "
                "compliance, especially during health crises."
            ),
            "image_path": "assets/maskify.png",  # Replace with actual path to your project image
            "demo_link": "https://example.com/maskify_demo",  # Replace with a real link if available
            "github_link": "https://github.com/Kennny7/Maskify",

            # Optional additional field
            "technologies": ["Python", "OpenCV", "CNN", "Deep Learning"]
        },
        {
            "title": "Smart City Surveillance System",
            "description": (
                "Engineered a real-time surveillance solution leveraging anomaly detection and distributed "
                "data pipelines with Kafka, PySpark, and Docker. The system proactively flags abnormal patterns "
                "in urban environments, enhancing public safety."
            ),
            "image_path": "assets/smart_city.png",  # Replace with actual path to your project image
            "demo_link": "https://example.com/smartcity_demo",  # Replace with a real link if available
            "github_link": "https://github.com/Kennny7/SmartCity-Surveillance",

            # Optional additional field
            "technologies": ["Deep Learning", "Kafka", "PySpark", "Docker"]
        },
        {
            "title": "Crime Detection & Prediction System",
            "description": (
                "Leveraged Python, SQL, Deep Learning, Apache Kafka, and PySpark to build a real-time crime "
                "detection and prediction system on Azure cloud. Designed robust data models and streaming "
                "pipelines for proactive law enforcement strategies."
            ),
            "image_path": "assets/crime_detection.png",  # Replace with actual path to your project image
            "demo_link": "https://example.com/crimedetection_demo",  # Replace with a real link if available
            "github_link": "https://github.com/Kennny7/Crime-Detection-System",

            # Optional additional field
            "technologies": ["Python", "SQL", "Deep Learning", "Kafka", "PySpark", "Azure"]
        }
    ]
