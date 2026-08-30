from fastapi import APIRouter,HTTPException
from schemas.users import UserRegister, UserLogin
from models.user import User
from utils.security import hash_password,verify_password,create_access_token

router=APIRouter(
    prefix="/auth",
    tags=["Authencation"]
)

@router.post("/register")
async def register(user: UserRegister):
    
    hashed_password=hash_password(user.password)
    new_user=User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=hashed_password
    )
    
    new_user.save()
    
    return {
        "message":"User Registered Successfully ✅",
        "User_id":str(new_user.id)
    }

@router.post("/login")
async def login(user: UserLogin):
    db_user=User.objects(email=user.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found ❌")
    password_valid=verify_password(user.password, db_user.password)
    if not password_valid:
        raise HTTPException(status_code=401, detail="Invalid password ❌")
    access_token=create_access_token(str(db_user.id))
    return {
        "message":"Login Successful ✅",
        "access_token":access_token,
        "token_type":"bearer"
    }