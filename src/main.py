import uvicorn
from fastapi import FastAPI
from web.auth_routes import router as auth_router
from web.calendar_routes import router as calendar_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(calendar_router)

if __name__ == "__main__":
  uvicorn.run("main:app", reload=True)