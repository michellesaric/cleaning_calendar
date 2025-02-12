from fastapi import APIRouter

router = APIRouter()

@router.get("/register")
def register_user():
  return "Time to register a user(not supposed to be a get method)"

@router.get("/login")
def login_user():
  return "This isn't supposted to be a get method, but it's okay for now, login the user"
