from flask import Flask, render_template, request, redirect, url_for, session, flash  # type: ignore[import]
from env.conexion import get_conexion

app = Flask(__name__)
app.secret_key = "cambia-esto-por-una-clave-segura"  # necesario para usar session/flash


# ─── DECORADOR PARA VERIFICAR SESIÓN ──────────────────────────────────
def login_requerido(f):
    """Decorador para proteger rutas que requieren autenticación"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id'):
            flash("Debes iniciar sesión para acceder a esta página", "error")
            return redirect(url_for("inicio"))
        return f(*args, **kwargs)
    return decorated_function


# ─── RUTAS PRINCIPALES ──────────────────────────────────────────────────
@app.route("/")
def inicio():
    """Página de inicio - muestra el carrusel y productos destacados"""
    # Si el usuario ya está logueado, redirigir al admin panel
    if session.get('user_id'):
        return redirect(url_for("admin_panel"))
    return render_template("index1.html")


@app.route("/admin")
@login_requerido
def admin_panel():
    """Panel de administración - solo para usuarios autenticados"""
    conexion = get_conexion()
    cursor = None
    productos = []
    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT codigo, nombre, precio, categoria FROM productos")
            productos = cursor.fetchall()
    except Exception as e:
        print(f"Error al consultar productos: {e}")
    finally:
        if cursor:
            cursor.close()
    return render_template("admin_panel.html", usuario=session.get('nombre'), productos=productos)


@app.route("/productos")
def productos():
    """
    Página de productos - COMPORTAMIENTO DUAL:
    - Usuarios NO logueados: ven el catálogo público (catalogo.html)
    - Usuarios logueados: ven el panel de administración de productos (productos_admin.html)
    """
    if session.get('user_id'):
        # Usuario autenticado: muestra versión admin con opciones de gestión
        conexion = get_conexion()
        cursor = None
        productos = []
        try:
            if conexion and conexion.is_connected():
                cursor = conexion.cursor(dictionary=True)
                cursor.execute("SELECT codigo, nombre, precio, categoria FROM productos")
                productos = cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar productos: {e}")
        finally:
            if cursor:
                cursor.close()
        return render_template("productos_admin.html", usuario=session.get('nombre'), productos=productos)
    else:
        # Usuario no autenticado: muestra catálogo público
        return render_template("catalogo.html")


@app.route("/contacto")
def contacto():
    """Página de contacto - pública"""
    return render_template("contacto.html")


@app.route("/nosotros")
def nosotros():
    """Página sobre nosotros - pública"""
    return render_template("nosotros.html")


@app.route("/servicios")
def servicios():
    """Página de servicios - pública"""
    return render_template("servicios.html")


@app.route("/catalogo")
def catalogo():
    """Catálogo público de productos - accesible para todos"""
    conexion = get_conexion()
    cursor = None
    productos = []
    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT codigo, nombre, precio, categoria FROM productos")
            productos = cursor.fetchall()
    except Exception as e:
        print(f"Error al consultar productos: {e}")
    finally:
        if cursor:
            cursor.close()
    return render_template("catalogo.html", productos=productos)


@app.route("/registro_producto")
@login_requerido
def registro_producto():
    """Formulario para registrar productos - requiere autenticación"""
    return render_template("registro_producto.html")


@app.route("/guardar_producto", methods=["POST"])
@login_requerido
def guardar_producto():
    """Guardar producto en la base de datos"""
    codigo = request.form.get("codigo")
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")

    # Validación básica
    if not all([codigo, nombre, precio, categoria]):
        flash("Todos los campos del producto son obligatorios", "error")
        return redirect(url_for("registro_producto"))

    conexion = get_conexion()
    cursor = None
    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            sql = "INSERT INTO productos (codigo, nombre, precio, categoria) VALUES (%s, %s, %s, %s)"
            valores = (codigo, nombre, precio, categoria)
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            # Obtener todos los productos con cursor diccionario
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT codigo, nombre, precio, categoria FROM productos")
            productos = cursor.fetchall()
            return render_template("respuesta.html",
                                   codigo=codigo,
                                   nombre=nombre,
                                   precio=precio,
                                   categoria=categoria,
                                   productos=productos)
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")
        flash("Error al guardar el producto", "error")
    finally:
        if cursor:
            cursor.close()

    return redirect(url_for("registro_producto"))


# ─── EDITAR PRODUCTO ────────────────────────────────────────────────────────
@app.route("/editar_producto/<codigo>")
@login_requerido
def editar_producto(codigo):
    """Mostrar formulario para editar un producto existente"""
    conexion = get_conexion()
    cursor = None
    producto = None
    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(dictionary=True, buffered=True)
            cursor.execute("SELECT codigo, nombre, precio, categoria FROM productos WHERE codigo = %s", (codigo,))
            producto = cursor.fetchone()
    except Exception as e:
        print(f"Error al obtener producto: {e}")
        flash("Error al cargar datos del producto", "error")
    finally:
        if cursor:
            cursor.close()
    if not producto:
        flash("Producto no encontrado", "error")
        return redirect(url_for('productos'))
    return render_template('editar_producto.html', producto=producto)

# ─── ACTUALIZAR PRODUCTO ───────────────────────────────────────────────────
@app.route("/actualizar_producto", methods=["POST"])
@login_requerido
def actualizar_producto():
    """Actualizar los datos de un producto existente"""
    codigo = request.form.get("codigo")
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")

    if not all([codigo, nombre, precio, categoria]):
        flash("Todos los campos son obligatorios", "error")
        return redirect(url_for('productos'))

    conexion = get_conexion()
    cursor = None
    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            sql = "UPDATE productos SET nombre=%s, precio=%s, categoria=%s WHERE codigo=%s"
            valores = (nombre, precio, categoria, codigo)
            cursor.execute(sql, valores)
            conexion.commit()
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        flash("Error al actualizar el producto", "error")
    finally:
        if cursor:
            cursor.close()
    return redirect(url_for('productos'))

# ─── ELIMINAR PRODUCTO ──────────────────────────────────────────────────────
@app.route("/eliminar_producto/<codigo>", methods=["POST"])
@login_requerido
def eliminar_producto(codigo):
    """Eliminar un producto de la base de datos"""
    # Validar que se recibió un código válido
    if not codigo:
        flash("Código de producto no especificado", "error")
        return redirect(url_for('productos'))
    conexion = get_conexion()
    cursor = None
    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            # Uso LIMIT 1 como medida extra de seguridad
            sql = "DELETE FROM productos WHERE codigo = %s LIMIT 1"
            cursor.execute(sql, (codigo,))
            conexion.commit()
            flash("Producto eliminado correctamente", "success")
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        flash("Error al eliminar el producto", "error")
    finally:
        if cursor:
            cursor.close()
    return redirect(url_for('productos'))

# ─── REGISTRO DE USUARIO ──────────────────────────────────────────────────
@app.route("/registro", methods=["POST"])
def registro():
    """Registrar un nuevo usuario"""
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    password = request.form.get("password")

    # Validación de campos
    if not nombre or not email or not password:
        flash("Todos los campos son obligatorios", "error")
        return redirect(url_for("inicio"))

    if len(password) < 6:
        flash("La contraseña debe tener al menos 6 caracteres", "error")
        return redirect(url_for("inicio"))

    conexion = get_conexion()
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
            (nombre, email, password)  # Recomendado: hashear la contraseña
        )
        conexion.commit()
        flash("Cuenta creada con éxito, ya puedes iniciar sesión", "success")
    except Exception as e:
        if hasattr(e, 'errno') and e.errno == 1062:  # email duplicado (UNIQUE constraint)
            flash("Ese correo ya está registrado", "error")
        else:
            print(f"Error al registrar usuario: {e}")
            flash("Ocurrió un error al crear la cuenta", "error")
    finally:
        if cursor:
            cursor.close()

    return redirect(url_for("inicio"))


# ─── LOGIN ─────────────────────────────────────────────────────────────────
@app.route("/login", methods=["POST"])
def login():
    """Iniciar sesión de usuario"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        flash("Correo y contraseña son obligatorios", "error")
        return redirect(url_for("inicio"))

    conexion = get_conexion()
    cursor = None
    usuario = None
    try:
        cursor = conexion.cursor(dictionary=True, buffered=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
    except Exception as e:
        print(f"Error al consultar usuario: {e}")
        flash("Error al intentar iniciar sesión", "error")
    finally:
        if cursor:
            cursor.close()

    # Verificar credenciales
    if usuario and usuario["password"] == password:
        session["user_id"] = usuario["id"]
        session["nombre"] = usuario["nombre"]
        session["email"] = usuario["email"]
        flash(f"¡Bienvenido, {usuario['nombre']}!", "success")
        # Redirigir al panel de administración
        return redirect(url_for("admin_panel"))

    flash("Correo o contraseña incorrectos", "error")
    return redirect(url_for("inicio"))


@app.route("/logout")
def logout():
    """Cerrar sesión"""
    session.clear()
    flash("Sesión cerrada correctamente", "success")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)