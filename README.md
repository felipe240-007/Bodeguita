# 📚 Bodeguita — Sistema de Inventario · Librería "El Gran Poeta"

Sistema de gestión de inventario desarrollado en Python con arquitectura MVC.
Permite controlar el stock y los movimientos de productos entre bodegas de la librería.

---

## 🛠️ Tecnologías

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.13 |
| Interfaz gráfica | Tkinter (incluido en Python) |
| Base de datos | MySQL |
| Conector BD | `mysql-connector-python` |

---

## 📂 Estructura del Proyecto

```
bodeguita/
│
├── src/                    # Código fuente (arquitectura MVC)
│   ├── models/             # Lógica de datos y conexión a MySQL
│   ├── views/              # Interfaces gráficas con Tkinter
│   └── controllers/        # Lógica de negocio
│
├── bd/                     # Scripts SQL (creación y configuración de la BD)
├── docs/                   # Documentación, diagramas y manuales
│
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── .env.example            # Plantilla de variables de entorno
├── .env                    # Variables de entorno reales (NO subir al repo)
└── .gitignore
```

---

## ⚙️ Instalación — Paso a Paso

### Prerrequisitos

Antes de comenzar asegúrate de tener instalado:

- [Python 3.13+](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) (o acceso a una instancia MySQL)
- [Git](https://git-scm.com/)

---

### 1. Clonar el repositorio

```bash
git clone https://github.com/felipe240-007/bodeguita.git
cd bodeguita
```

---

### 2. Crear y activar el entorno virtual

Es **muy recomendable** usar un entorno virtual para aislar las dependencias.

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```


> Una vez activo, verás `(venv)` al inicio de tu terminal.

---

### 3. Instalar los requisitos

Con el entorno virtual activo, instala todas las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar las variables de entorno (`.env`)

El proyecto usa un archivo `.env` para manejar credenciales de forma segura.

**4.1** Copia el archivo de ejemplo:

```bash
# Windows (PowerShell)
Copy-Item .env.example .env
```

**4.2** Abre el archivo `.env` con tu editor y completa tus datos reales:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=bodeguita
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contraseña_mysql
```

> ⚠️ **Importante:** El archivo `.env` está incluido en `.gitignore` y **nunca debe subirse al repositorio**. Contiene información sensible.

---


### 5. Ejecutar la aplicación

Con todo configurado, inicia la aplicación desde la raíz del proyecto:

```bash
python main.py
```

---

## ✅ Resumen rápido

```bash
git clone <url-del-repositorio> && cd bodeguita
python -m venv venv && .\venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
cp .env.example .env          # Luego editar .env con tus datos
python main.py
```

---

## 🤝 Contribuir

1. Crea una rama desde `main`: `git checkout -b feature/mi-feature`
2. Realiza tus cambios y haz commit: `git commit -m "feat: descripción"`
3. Sube tu rama: `git push origin feature/mi-feature`
4. Abre un Pull Request

---

