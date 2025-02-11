from typing import Dict

def get_skills_data() -> Dict[str, int]:
    """
    Returns a dictionary of skill names (keys) and proficiency percentages (values).
    Percentages should range from 0 to 100.
    """

    return {
        "Python": 75,
        "SQL": 65,
        "Hadoop": 50,
        "PySpark": 70,
        "Kafka": 60,
        "Hive": 65,
        "HBase": 50,
        "Docker": 70,
        "OpenCV": 60,
        # You can adjust or remove any entries as needed
    }
