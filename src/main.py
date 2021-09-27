import uvicorn
from app.settings import configs

if __name__ == "__main__":

    uvicorn.run(
        "app.api:app",
        host=configs.APP_HOST,
        port=configs.APP_PORT,
        reload=configs.APP_RELOAD
    )