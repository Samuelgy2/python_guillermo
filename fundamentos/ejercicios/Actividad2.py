import re

#  Clase Usuario

class Usuario:
    ROLES_VALIDOS = ["Administrador", "Aprendiz", "Instructor"]

    def __init__(self, documento, nombre, correo, rol, estado="Activo"):
        self.documento = documento
        self.nombre    = nombre
        self.correo    = correo
        self.rol       = rol
        self.estado    = estado

    def __str__(self):
        return (f"  Documento : {self.documento}\n"
                f"  Nombre    : {self.nombre}\n"
                f"  Correo    : {self.correo}\n"
                f"  Rol       : {self.rol}\n"
                f"  Estado    : {self.estado}")



#  Clase SistemaUsuarios

class SistemaUsuarios:

    def __init__(self):
        self.usuarios = []

    # helpers de validación 
    def _correo_valido(self, correo):
        return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', correo))

    def _doc_existente(self, documento):
        return any(u.documento == documento for u in self.usuarios)

    def _correo_existente(self, correo, excluir_doc=None):
        return any(u.correo == correo and u.documento != excluir_doc
                   for u in self.usuarios)

    def _mostrar_roles(self):
        for i, r in enumerate(Usuario.ROLES_VALIDOS, 1):
            print(f"  {i}. {r}")

    def _input_no_vacio(self, mensaje):
        while True:
            valor = input(mensaje).strip()
            if valor:
                return valor
            print("  ✗ El campo no puede estar vacío.")

    def _seleccionar_rol(self):
        self._mostrar_roles()
        while True:
            opcion = input("  Elige el número del rol: ").strip()
            if opcion.isdigit() and 1 <= int(opcion) <= len(Usuario.ROLES_VALIDOS):
                return Usuario.ROLES_VALIDOS[int(opcion) - 1]
            print("  ✗ Opción inválida.")

    # Registrar usuario 
    def registrar_usuario(self):
        print("\n── REGISTRAR USUARIO ──")

        documento = self._input_no_vacio("  Documento : ")
        if self._doc_existente(documento):
            print("  ✗ Ya existe un usuario con ese documento.")
            return

        nombre = self._input_no_vacio("  Nombre    : ")

        correo = self._input_no_vacio("  Correo    : ")
        if not self._correo_valido(correo):
            print("  ✗ Correo inválido.")
            return
        if self._correo_existente(correo):
            print("  ✗ Ese correo ya está registrado.")
            return

        print("  Rol:")
        rol = self._seleccionar_rol()

        usuario = Usuario(documento, nombre, correo, rol)
        self.usuarios.append(usuario)
        print(f"  ✓ Usuario '{nombre}' registrado correctamente.")

    # Mostrar usuarios 
    def mostrar_usuarios(self):
        print("\n── LISTA DE USUARIOS ──")
        if not self.usuarios:
            print("  No hay usuarios registrados.")
            return
        for i, u in enumerate(self.usuarios, 1):
            print(f"\n  [{i}]")
            print(u)

    # Buscar usuario 
    def buscar_usuario(self):
        print("\n── BUSCAR USUARIO ──")
        print("  1. Por documento")
        print("  2. Por correo")
        op = input("  Opción: ").strip()

        if op == "1":
            doc = self._input_no_vacio("  Documento: ")
            resultado = next((u for u in self.usuarios if u.documento == doc), None)
        elif op == "2":
            correo = self._input_no_vacio("  Correo: ")
            resultado = next((u for u in self.usuarios if u.correo == correo), None)
        else:
            print("  ✗ Opción inválida.")
            return

        if resultado:
            print("\n  Usuario encontrado:")
            print(resultado)
        else:
            print("  ✗ No se encontró el usuario.")

    # Actualizar usuario
    def actualizar_usuario(self):
        print("\n── ACTUALIZAR USUARIO ──")
        doc = self._input_no_vacio("  Documento del usuario a actualizar: ")
        usuario = next((u for u in self.usuarios if u.documento == doc), None)

        if not usuario:
            print("  ✗ Usuario no encontrado.")
            return

        print(f"\n  Usuario actual:\n{usuario}")
        print("\n  Deja en blanco para conservar el valor actual.\n")

        # Nombre
        nuevo_nombre = input(f"  Nuevo nombre [{usuario.nombre}]: ").strip()
        if nuevo_nombre:
            usuario.nombre = nuevo_nombre

        # Correo
        nuevo_correo = input(f"  Nuevo correo [{usuario.correo}]: ").strip()
        if nuevo_correo:
            if not self._correo_valido(nuevo_correo):
                print("  ✗ Correo inválido. No se actualizó.")
            elif self._correo_existente(nuevo_correo, excluir_doc=doc):
                print("  ✗ Ese correo ya pertenece a otro usuario.")
            else:
                usuario.correo = nuevo_correo

        # Rol
        cambiar_rol = input("  ¿Cambiar rol? (s/n): ").strip().lower()
        if cambiar_rol == "s":
            print("  Nuevo rol:")
            usuario.rol = self._seleccionar_rol()

        # Estado
        cambiar_estado = input("  ¿Cambiar estado? (s/n): ").strip().lower()
        if cambiar_estado == "s":
            usuario.estado = "Inactivo" if usuario.estado == "Activo" else "Activo"
            print(f"  Estado cambiado a: {usuario.estado}")

        print("  ✓ Usuario actualizado.")

    # Eliminar usuario 
    def eliminar_usuario(self):
        print("\n── ELIMINAR USUARIO ──")
        doc = self._input_no_vacio("  Documento del usuario a eliminar: ")
        usuario = next((u for u in self.usuarios if u.documento == doc), None)

        if not usuario:
            print("  ✗ Usuario no encontrado.")
            return

        confirmacion = input(f"  ¿Eliminar a '{usuario.nombre}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            self.usuarios.remove(usuario)
            print("  ✓ Usuario eliminado.")
        else:
            print("  Operación cancelada.")

    # Mostrar usuarios activos  
    def mostrar_activos(self):
        print("\n── USUARIOS ACTIVOS ──")
        activos = [u for u in self.usuarios if u.estado == "Activo"]
        if not activos:
            print("  No hay usuarios activos.")
            return
        for i, u in enumerate(activos, 1):
            print(f"\n  [{i}]")
            print(u)

    # Contar usuarios por rol 
    def contar_roles(self):
        print("\n── USUARIOS POR ROL ──")
        if not self.usuarios:
            print("  No hay usuarios registrados.")
            return
        for rol in Usuario.ROLES_VALIDOS:
            cantidad = sum(1 for u in self.usuarios if u.rol == rol)
            print(f"  {rol}: {cantidad}")

    # Exportar a .txt 
    def guardar_archivo(self):
        nombre_archivo = "usuarios_exportados.txt"
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write("=" * 40 + "\n")
                f.write("     LISTADO DE USUARIOS\n")
                f.write("=" * 40 + "\n")
                if not self.usuarios:
                    f.write("No hay usuarios registrados.\n")
                else:
                    for i, u in enumerate(self.usuarios, 1):
                        f.write(f"\n[{i}]\n{u}\n")
                f.write("\n" + "=" * 40 + "\n")
                f.write(f"Total de usuarios: {len(self.usuarios)}\n")
            print(f"  ✓ Archivo guardado como '{nombre_archivo}'.")
        except Exception as e:
            print(f"  ✗ Error al guardar: {e}")



#  Menú principal

def menu():
    sistema = SistemaUsuarios()

    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE GESTIÓN DE USUARIOS")
        print("=" * 40)
        print("  1. Registrar usuario")
        print("  2. Mostrar todos los usuarios")
        print("  3. Buscar usuario")
        print("  4. Actualizar usuario")
        print("  5. Eliminar usuario")
        print("  6. Mostrar usuarios activos")
        print("  7. Contar usuarios por rol")
        print("  8. Exportar a archivo .txt")
        print("  0. Salir")
        print("=" * 40)

        op = input("  Selecciona una opción: ").strip()

        if op == "1":
            sistema.registrar_usuario()
        elif op == "2":
            sistema.mostrar_usuarios()
        elif op == "3":
            sistema.buscar_usuario()
        elif op == "4":
            sistema.actualizar_usuario()
        elif op == "5":
            sistema.eliminar_usuario()
        elif op == "6":
            sistema.mostrar_activos()
        elif op == "7":
            sistema.contar_roles()
        elif op == "8":
            sistema.guardar_archivo()
        elif op == "0":
            print("\n  Hasta luego.\n")
            break
        else:
            print("  ✗ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()