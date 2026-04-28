from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.core.security import hash_password

def crear_usuario_si_no_existe(db: Session, email, nombre, password, rol):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()

    if usuario:
        print(f"⚠️ {rol} ya existe: {email}")
        return

    nuevo = Usuario(
        nombre=nombre,
        email=email,
        telefono="00000000",
        password=hash_password(password),
        rol=rol,
        activo=True
    )

    db.add(nuevo)
    db.commit()
    print(f"✅ {rol.upper()} creado: {email}")


def crear_usuarios_iniciales(db: Session):
    crear_usuario_si_no_existe(
        db,
        email="admin@gmail.com",
        nombre="Administrador",
        password=hash_password(123456),
        rol="administrador"
    )

    crear_usuario_si_no_existe(
        db,
        email="user@gmail.com",
        nombre="Cliente Demo",
        password=hash_password(123456),
        rol="cliente"
    )

    crear_usuario_si_no_existe(
        db,
        email="taller@gmail.com",
        nombre="Taller Demo",
        password=hash_password(123456),
        rol="taller"
    )

    crear_usuario_si_no_existe(
        db,
        email="tecnico@gmail.com",
        nombre="Técnico Demo",
        password=hash_password(123456),
        rol="tecnico"
    )