from datetime import datetime

from fastapi import APIRouter, Depends
from starlette.responses import Response
from sqlalchemy.orm import Session

from app.database.conn import db
from app.database.schema import Users

router = APIRouter()

@router.get("/")
async def index(session: Session = Depends(db.session)):
    """
    ELB 상태 체크용 api

    Args:
        session (Session, optional): _description_. Defaults to Depends(db.session).

    Returns:
        _type_: _description_
    """
    Users().create(session=session, auto_commit=True, name="코알라")
    curr_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {curr_time.strftime('%Y-%m-%d %H:%M:%S')}) ")

