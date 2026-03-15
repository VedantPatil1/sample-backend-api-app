"""
Application factory for simple FastAPI.
"""
from fastapi import FastAPI

def create_app():
    app = FastAPI()

    @app.get('/')
    def hello():
        return {"hello":"world"}

    @app.get('/health')
    def health():
        return {"status": "ok"}

    return app
