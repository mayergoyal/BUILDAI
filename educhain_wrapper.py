from archive.qna_engine import generate_mcq
from archive.content_engine import generate_lesson_plan
from dotenv import load_dotenv
load_dotenv()

from dotenv import load_dotenv
load_dotenv()

def get_mcqs(topic: str, count: int = 5):
    return generate_mcq(topic, count)


print("\nLesson Plan:")
def get_lesson_plan(subject: str):
    return generate_lesson_plan(subject)