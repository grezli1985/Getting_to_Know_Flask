from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# project.lecture.lesson_05.main_01:app --reload   Запуск приложения
