import json
import random
from datetime import datetime, timedelta

# Helper data to generate synthetic course data
course_topics = [
    "Python Programming", "Web Development", "Data Science", "Machine Learning",
    "Digital Marketing", "Graphic Design", "Photography", "Cybersecurity",
    "Blockchain Basics", "Project Management", "Excel Mastery", "Music Production",
    "Artificial Intelligence", "Cloud Computing", "Mobile App Development",
    "Personal Finance", "Entrepreneurship", "Creative Writing", "Yoga & Meditation",
    "Game Development"
]

course_descriptions = [
    "Learn the fundamentals and advanced concepts of {} with practical examples.",
    "Master {} from scratch and become job-ready.",
    "A comprehensive guide to {} including real-world projects.",
    "Step-by-step tutorials on {} for beginners and experts alike.",
    "Boost your career by mastering {} through this course.",
    "Unlock your potential in {} with hands-on exercises.",
    "Deep dive into {} with the latest tools and techniques.",
    "Become proficient in {} with this intensive course.",
    "Everything you need to know about {} in one place.",
    "Transform your skills in {} with this expert-led course."
]

thumbnail_urls = [
    "https://via.placeholder.com/320x180.png?text=Course+Image+1",
    "https://via.placeholder.com/320x180.png?text=Course+Image+2",
    "https://via.placeholder.com/320x180.png?text=Course+Image+3",
    "https://via.placeholder.com/320x180.png?text=Course+Image+4",
    "https://via.placeholder.com/320x180.png?text=Course+Image+5",
]

base_udemy_url = "https://www.udemy.com/course/"

def random_expiration_date():
    # Randomly assign expiration date or "N/A"
    if random.random() < 0.7:
        # 70% chance coupon expires
        days_from_now = random.randint(5, 90)
        return (datetime.now() + timedelta(days=days_from_now)).strftime("%Y-%m-%d")
    else:
        return "N/A"

def generate_course(i):
    topic = random.choice(course_topics)
    title = f"{topic} Mastery Volume {random.randint(1, 10)}"
    description = random.choice(course_descriptions).format(topic)
    thumbnail = random.choice(thumbnail_urls)
    enroll_url = base_udemy_url + f"{topic.lower().replace(' ', '-')}-mastery-vol-{random.randint(1,10)}"
    expiration = random_expiration_date()
    return {
        "id": i,
        "title": title,
        "description": description,
        "thumbnail": thumbnail,
        "enroll_url": enroll_url,
        "expiration": expiration
    }

# Generate 3000 courses
courses = [generate_course(i) for i in range(1, 3001)]

# Save to JSON file
json_file_path = "courses.json"
with open(json_file_path, "w", encoding="utf-8") as f:
    json.dump(courses, f, indent=2)

print(f"Generated {len(courses)} courses and saved to {json_file_path}")
