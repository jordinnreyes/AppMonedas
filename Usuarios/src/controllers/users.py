from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..models.user import User
from ..db.database import get_db
from ..schemas.user import UserResponse
from ..utils.dependencies import get_authenticated_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
async def read_current_user(
    current_user: User = Depends(get_authenticated_user),
    db: Session = Depends(get_db)
):

    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        nombre=current_user.nombre,
        apellido=current_user.apellido
    )

@router.get("/{usuario_id}", response_model=UserResponse)
def get_user_by_id(usuario_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == usuario_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return UserResponse(
        id=user.id,
        email=user.email,
        nombre=user.nombre,
        apellido=user.apellido
    )