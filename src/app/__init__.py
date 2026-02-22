"""
Application factory for simple FastAPI.
"""
from fastapi import FastAPI

def create_app():
    app = FastAPI()

    @app.get('/')
    def hello():
        return {"hello":"world"}

    return app
