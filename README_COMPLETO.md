# 🍦 Cuvipop - Sistema de Gestión de Heladería

Sistema web para venta de helados y snacks con carrito de compras, autenticación y panel de administración.

## ✨ Características

### 👥 Para Usuarios Cliente
- ✅ Ver menú sin necesidad de cuenta
- ✅ Agregar productos al carrito
- ✅ Ver carrito y modificar cantidades
- ✅ Registrarse / Iniciar sesión
- ✅ Realizar pedido con fecha, hora, tipo entrega y método pago
- ✅ Modal de login al intentar pedir sin sesión

### 👨‍💼 Para Administradores
- ✅ Panel admin dedicado (`/static/admin.html`)
- ✅ Gestión de productos (en desarrollo)
- ✅ Ver pedidos (en desarrollo)
- ✅ Ver usuarios (en desarrollo)
- ✅ Reportes (en desarrollo)

---

## 🚀 Inicio Rápido

### 1. Clonar el proyecto
```bash
git clone https://github.com/JuanRamonTG/CuvipopWeb.git
cd CuvipopWeb
```

### 2. Crear entorno virtual
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias
```powershell
pip install -r requirements.txt
```

### 4. Levantar el servidor
```powershell
cd backend
uvicorn main:app --reload
```

El servidor estará en `http://localhost:8000`

---

## 📝 Crear Usuario Admin

**OPCIÓN 1: Vía API (Recomendado)**

Ejecuta en PowerShell:
```powershell
curl -X POST "http://localhost:8000/auth/crear-admin-prueba"
```

O abre en navegador:
```
http://localhost:8000/auth/crear-admin-prueba
```

**OPCIÓN 2: Script Python**

```powershell
python crear_admin.py
```

**Credenciales por defecto:**
- 📧 Email: `admin@cuvipop.com`
- 🔐 Contraseña: `admin123`

Para más detalles, ver [`CREAR_ADMIN.md`](./CREAR_ADMIN.md)

---

## 📂 Estructura del Proyecto

```
CuvipopWeb/
├── backend/
│   ├── main.py              # Aplicación FastAPI
│   ├── database.py          # Conexión a MySQL
│   ├── security.py          # Hash, JWT, tokens
│   ├── dependencies.py      # Dependencias (get_db, get_current_user)
│   ├── models/              # Modelos SQLAlchemy
│   │   ├── usuario.py
│   │   ├── producto.py
│   │   ├── pedido.py
│   │   ├── detalle_pedido.py
│   │   └── ubicacion.py
│   └── routes/              # Rutas FastAPI
│       ├── auth.py          # Registro, login, crear-admin-prueba
│       ├── productos.py     # GET /productos/
│       ├── pedidos.py       # POST /pedidos/
│       ├── usuarios.py
│       └── admin.py
│
├── frontend/
│   ├── index.html           # Página principal
│   ├── menu.html            # Menú de productos
│   ├── carrito.html         # Página del carrito
│   ├── login.html           # Formulario de login
│   ├── registro.html        # Formulario de registro
│   ├── admin.html           # 👨‍💼 Panel admin (NUEVO)
│   └── js/
│       ├── menu.js          # Carga productos
│       ├── carrito.js       # Lógica del carrito
│       ├── cart-indicator.js # Contador global
│       └── auth.js          # Funciones de autenticación
│
├── crear_admin.py           # Script para crear admin
├── CREAR_ADMIN.md           # Guía detallada (NUEVO)
└── README.md                # Este archivo
```

---

## 🔐 Autenticación y Roles

### Flujo de Login
1. Usuario se registra con email y contraseña
2. Sistema guarda password hasheado (bcrypt)
3. Al login, genera JWT token y lo guarda en localStorage
4. Token contiene: email, rol, expiracion

### Roles disponibles
- `cliente`: Usuario normal que compra
- `admin`: Puede acceder a `/static/admin.html` y funciones especiales

### Protección de rutas
- Frontend: `auth.js` verifica `auth_token` en localStorage
- Backend: `dependencies.py` valida JWT en headers

---

## 📡 API Endpoints

### Autenticación
- `POST /auth/registro` - Registrar nuevo usuario
- `POST /auth/login` - Iniciar sesión (devuelve JWT)
- `POST /auth/crear-admin-prueba` - Crear usuario admin (SOLO DESARROLLO)

### Productos
- `GET /productos/` - Listar todos los productos (sin autenticación)

### Pedidos
- `POST /pedidos/` - Crear pedido (requiere: items, total, fecha, hora, tipo_entrega, metodo_pago)

---

## 💾 Base de Datos

**Conexión:**
```
mysql+pymysql://root:@localhost/cuvipopweb_db
```

**Tablas principales:**
- `usuarios` - Clientes y admins
- `productos` - Catálogo
- `pedidos` - Pedidos realizados
- `detalle_pedido` - Ítems de cada pedido

---

## 🎨 Tecnologías

### Backend
- **FastAPI** - Framework web Python
- **SQLAlchemy** - ORM
- **MySQL** - Base de datos
- **JWT** - Autenticación
- **bcrypt** - Hash de contraseñas

### Frontend
- **Bootstrap 5** - Framework CSS
- **Vanilla JavaScript** - Lógica
- **LocalStorage** - Carrito y tokens

---

## ⚙️ Configuración

### Variables de entorno (opcional)
Crear `.env` en la raíz:
```
DATABASE_URL=mysql+pymysql://user:pass@localhost/dbname
SECRET_KEY=tu-clave-secreta
ALGORITHM=HS256
```

### Base de datos
Crear en MySQL:
```sql
CREATE DATABASE cuvipopweb_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Las tablas se crean automáticamente con SQLAlchemy.

---

## 🧪 Testing

### Crear usuario cliente
1. Ir a `http://localhost:8000/static/registro.html`
2. Llenar formulario
3. Se registra automáticamente con rol "cliente"

### Crear usuario admin
Ver sección "Crear Usuario Admin" arriba

### Probar carrito
1. Ir a menú
2. Agregar productos
3. Abrir carrito
4. Sin login: intenta pedir → aparece modal login
5. Con login: puede pedir normalmente

---

## 📋 Próximas Funcionalidades

- [ ] Persistencia de pedidos en BD
- [ ] Dashboard admin con estadísticas
- [ ] Gestión de productos en admin
- [ ] Ver historial de pedidos de usuario
- [ ] Búsqueda y filtros avanzados
- [ ] Métodos de pago reales (Stripe, PayPal)
- [ ] Sistema de notificaciones por email
- [ ] APP móvil
- [ ] Catálogo dinámico desde BD

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-func`)
3. Commit cambios (`git commit -am 'Agrega nueva función'`)
4. Push a la rama (`git push origin feature/nueva-func`)
5. Abre Pull Request

---

## 📄 Licencia

MIT License - Ver LICENSE

---

## 👨‍💻 Autor

Desarrollo: **Juan Ramón**

---

## 📞 Soporte

Para reportar bugs o sugerencias, crear un issue en GitHub.

---

**¡Disfruta de Cuvipop! 🍦**
