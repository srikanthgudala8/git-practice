from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
import uuid

app = FastAPI()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CloudTrainingCourses')

class Course(BaseModel):   /adding comments
    title: str
    description: str
    level: str  # e.g., Beginner, Advanced

@app.post("/courses/")
async def create_course(course: Course):
    course_id = str(uuid.uuid4())
    item = {
        'course_id': course_id,
        'title': course.title,
        'description': course.description,
        'level': course.level
    }
    table.put_item(Item=item)
    return {"message": "Course created!", "course_id": course_id}

@app.get("/courses/{course_id}")
async def get_course(course_id: str):
    response = table.get_item(Key={'course_id': course_id})
    if 'Item' not in response:
        raise HTTPException(status_code=404, detail="Course not found")
    return response['Item']
