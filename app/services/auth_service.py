from app.core.security import verify_password, create_access_token
from app.models.usuario import Usuario

def autenticar_usuario(db, email, password):
    user = db.query(Usuario).filter(Usuario.email == email).first()

    if not user:
        return "USER_NOT_FOUND"

    if not verify_password(password, user.password):
        return "INVALID_PASSWORD"

    token = create_access_token({"sub": user.email})
    return token
