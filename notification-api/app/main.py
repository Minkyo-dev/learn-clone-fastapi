import uvicorn
from typing import Optional
from fastapi import FastAPI
from dataclasses import asdict
from app.common.config import conf
from app.database.conn import db
from app.routes import index

app = FastAPI()

def create_app():
    """
    app 함수 실행
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)


    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의
    app.include_router(index.router)

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
