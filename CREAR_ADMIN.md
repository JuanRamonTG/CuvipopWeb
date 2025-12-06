# 🛠️ Guía: Crear Usuario Admin en Cuvipop

Hay **2 formas** de crear un usuario admin:

---

## Opción 1: Llamar a la API de prueba (RECOMENDADO)

Esta es la forma más rápida.

### Pasos:

1. **Asegúrate de que el backend esté corriendo:**
   ```powershell
   cd C:\Users\Mar\Pictures\parcial\Parcail3ProyectoWeb\CuvipopWeb\backend
   uvicorn main:app --reload
   ```

2. **En otra terminal, ejecuta:**
   ```powershell
   curl -X POST "http://localhost:8000/auth/crear-admin-prueba"
   ```

   O abre en el navegador:
   ```
   http://localhost:8000/auth/crear-admin-prueba
   ```

3. **Verás una respuesta como:**
   ```json
   {
     "mensaje": "✅ Usuario admin creado correctamente",
     "usuario": {
       "id": 1,
       "nombre": "Administrador",
       "correo": "admin@cuvipop.com",
       "rol": "admin"
     },
     "credenciales": {
       "correo": "admin@cuvipop.com",
       "password": "admin123"
     }
   }
   ```

4. **Usa estas credenciales para login:**
   - 📧 Email: `admin@cuvipop.com`
   - 🔐 Contraseña: `admin123`

---

## Opción 2: Script Python directo (alternativa)

Si prefieres no usar la API:

1. **Abre PowerShell y navega al proyecto:**
   ```powershell
   cd C:\Users\Mar\Pictures\parcial\Parcail3ProyectoWeb\CuvipopWeb
   ```

2. **Activa el entorno virtual (si no lo está):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. **Ejecuta el script:**
   ```powershell
   python crear_admin.py
   ```

4. **Verás:**
   ```
   ✅ Usuario admin creado exitosamente!

   📧 Correo: admin@cuvipop.com
   🔐 Contraseña: admin123
   👤 Rol: admin
   📋 ID: 1
   ```

---

## ✅ Verificar que el admin fue creado

**En la base de datos:**
```sql
SELECT id, nombre, correo, rol FROM usuarios WHERE rol = 'admin';
```

**O prueba haciendo login:**
1. Abre `http://localhost:8000/static/login.html`
2. Ingresa:
   - Email: `admin@cuvipop.com`
   - Contraseña: `admin123`
3. Si ves que redirige a admin.html, ¡el admin está creado! ✅

---

## 🔍 Panel Admin (próximo paso)

Una vez tengas el admin creado, puedes acceder a `http://localhost:8000/static/admin.html` para:
- Ver pedidos
- Gestionar productos
- Ver usuarios
- (Funcionalidades por implementar)

---

## ⚠️ Nota de seguridad

La ruta `/auth/crear-admin-prueba` es **SOLO PARA DESARROLLO**. 

En producción, deberías:
1. ✅ Eliminar esta ruta
2. ✅ O protegerla con autenticación de super-admin
3. ✅ Usar contraseñas más seguras

