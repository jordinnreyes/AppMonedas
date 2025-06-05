from sqlalchemy.orm import Session
from ..models.user import User
from ..utils.security import get_password_hash, verify_password
from sqlalchemy.orm import Session, joinedload
from ..models.user import User
from ..utils.security import get_password_hash, verify_password
from ..schemas.user import UserCreate


def register_user(db: Session, user_data: UserCreate):
    # Verifica si el email ya está registrado
    if db.query(User).filter(User.email == user_data.email).first():
        raise ValueError("El email ya está registrado")
    
    
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        nombre=user_data.nombre,
        apellido=user_data.apellido,
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    
    if not user or not verify_password(password, user.hashed_password):
        return None
    
    return user