from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..schemas.auth import Token
from ..schemas.user import UserCreate, UserResponse, LoginRequest
from ..services.auth_service import register_user, authenticate_user
from ..utils.security import create_access_token
from ..config.settings import settings
from fastapi.security import OAuth2PasswordBearer
from jose import jwt



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


SECRET_KEY = settings.SECRET_KEY

router = APIRouter(tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = register_user(db, user_data)  # Se registra el usuario


        return UserResponse(
            id=user.id,
            email=user.email,
            nombre=user.nombre,
            apellido=user.apellido
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@router.post("/login", response_model=Token)
async def login(
    login_data: LoginRequest,  
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, login_data.username, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )
    
    access_token = create_access_token(
        data={
            "id": user.id,
            "sub": user.email,
            "nombre": user.nombre
        }
    )
    return {"access_token": access_token, "token_type": "bearer"}



#funcion para validar el usuarios, en la api de cursos
@router.get("/validate-token")
def validate_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {
            "id": payload.get("id"),
            "email": payload.get("sub")
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
