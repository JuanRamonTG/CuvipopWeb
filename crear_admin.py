#!/usr/bin/env python3
"""
Script para crear un usuario admin en la base de datos de Cuvipop.
Ejecutar desde: python crear_admin.py
"""

import sys
from pathlib import Path

# Agregar el backend al path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

from database import SessionLocal
from models.usuario import Usuario
from security import hash_password

def crear_admin():
    db = SessionLocal()
    
    correo = "admin@cuvipop.com"
    password = "admin123"
    nombre = "Administrador"
    
    # Verificar si ya existe
    existe = db.query(Usuario).filter(Usuario.correo == correo).first()
    if existe:
        print(f"❌ El usuario admin con correo {correo} ya existe.")
        db.close()
        return
    
    # Crear admin
    admin = Usuario(
        nombre=nombre,
        correo=correo,
        password=hash_password(password),
        rol="admin"
    )
    
    db.add(admin)
    db.commit()
    db.refresh(admin)
    db.close()
    
    print("✅ Usuario admin creado exitosamente!")
    print(f"\n📧 Correo: {correo}")
    print(f"🔐 Contraseña: {password}")
    print(f"👤 Rol: admin")
    print(f"📋 ID: {admin.id}")

if __name__ == "__main__":
    crear_admin()
