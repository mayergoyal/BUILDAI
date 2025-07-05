from fastapi import FastAPI
from pydantic import BaseModel
from educhain_wrapper import get_mcqs, get_lesson_plan


app = FastAPI(title="EduChain MCP Server")

class MCQRequest(BaseModel):
    topic: str
    count: int = 5

class LessonPlanRequest(BaseModel):
    subject: str

@app.post("/generate_mcqs")
def mcq_tool(data: MCQRequest):
    return {"mcqs": get_mcqs(data.topic, data.count)}

@app.post("/lesson_plan")
def lesson_plan_tool(data: LessonPlanRequest):
    return {"lesson_plan": get_lesson_plan(data.subject)}
