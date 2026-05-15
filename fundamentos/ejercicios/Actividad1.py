class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, categoria):
        self.codigo    = codigo
        self.nombre    = nombre
        self.precio    = precio
        self.cantidad  = cantidad
        self.categoria = categoria

    def estado(self):
        if self.cantidad == 0:
            return "Agotado"
        elif self.cantidad <= 5:
            return "Stock bajo"
        else:
            return "Disponible"

    def mostrar_info(self):
        return (f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
                f"Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | "
                f"Categoria: {self.categoria} | Estado: {self.estado()}")


class SistemaInventario:
    def __init__(self):
        self.productos = []


    def _pedir_float_positivo(self, mensaje):
        """Solicita un número decimal >= 0, repite hasta obtener uno válido."""
        while True:
            try:
                valor = float(input(mensaje))
                if valor < 0:
                    print("  ✗ El valor no puede ser negativo.")
                else:
                    return valor
            except ValueError:
                print("  ✗ Ingresa un número válido (ej: 1500 o 3.99).")

    def _pedir_int_positivo(self, mensaje):
        """Solicita un entero >= 0, repite hasta obtener uno válido."""
        while True:
            try:
                valor = int(input(mensaje))
                if valor < 0:
                    print("  ✗ El valor no puede ser negativo.")
                else:
                    return valor
            except ValueError:
                print("  ✗ Ingresa un número entero válido (ej: 10).")

    def _pedir_texto(self, mensaje):
        """Solicita texto no vacío, repite hasta obtener uno válido."""
        while True:
            valor = input(mensaje).strip()
            if valor == "":
                print("  ✗ Este campo no puede estar vacío.")
            else:
                return valor

    def _buscar_por_codigo(self, codigo):
        """Retorna el objeto Producto si existe, o None."""
        for prod in self.productos:
            if prod.codigo == codigo:
                return prod
        return None


    def registrar_producto(self):
        print("\n  -- Registrar producto --")

        # Código único
        while True:
            codigo = self._pedir_texto("  Codigo: ")
            if self._buscar_por_codigo(codigo):
                print("  ✗ Ese codigo ya existe, usa uno diferente.")
            else:
                break

        nombre    = self._pedir_texto("  Nombre: ")
        precio    = self._pedir_float_positivo("  Precio: $")
        cantidad  = self._pedir_int_positivo("  Cantidad disponible: ")
        categoria = self._pedir_texto("  Categoria: ")

        nuevo = Producto(codigo, nombre, precio, cantidad, categoria)
        self.productos.append(nuevo)
        print("  ✓ Producto registrado exitosamente.")

    def mostrar_productos(self):
        print("\n  -- Lista de productos --")
        if len(self.productos) == 0:
            print("  No hay productos registrados.")
            return
        for prod in self.productos:
            print(" ", prod.mostrar_info())

    def buscar_producto(self):
        print("\n  -- Buscar producto --")
        print("  1. Por codigo")
        print("  2. Por nombre")
        criterio = input("  Seleccione: ").strip()

        if criterio == "1":
            codigo = self._pedir_texto("  Codigo a buscar: ")
            prod = self._buscar_por_codigo(codigo)
            if prod:
                print("  Producto encontrado:")
                print(" ", prod.mostrar_info())
            else:
                print("  ✗ Producto no encontrado.")

        elif criterio == "2":
            nombre_buscar = self._pedir_texto("  Nombre a buscar: ").lower()
            encontrados = [p for p in self.productos if nombre_buscar in p.nombre.lower()]
            if encontrados:
                print(f"  {len(encontrados)} resultado(s):")
                for prod in encontrados:
                    print(" ", prod.mostrar_info())
            else:
                print("  ✗ No se encontraron productos con ese nombre.")
        else:
            print("  ✗ Opción inválida.")

    def actualizar_producto(self):
        print("\n  -- Actualizar producto --")
        codigo = self._pedir_texto("  Codigo del producto a actualizar: ")
        prod = self._buscar_por_codigo(codigo)

        if prod is None:
            print("  ✗ Producto no encontrado.")
            return

        print(f"  Producto actual: {prod.mostrar_info()}")
        print("  ¿Qué desea actualizar?")
        print("  1. Precio")
        print("  2. Cantidad")
        print("  3. Categoria")

        opcion = input("  Seleccione: ").strip()

        if opcion == "1":
            prod.precio = self._pedir_float_positivo("  Nuevo precio: $")
            print("  ✓ Precio actualizado.")
        elif opcion == "2":
            prod.cantidad = self._pedir_int_positivo("  Nueva cantidad: ")
            print("  ✓ Cantidad actualizada.")
        elif opcion == "3":
            prod.categoria = self._pedir_texto("  Nueva categoria: ")
            print("  ✓ Categoria actualizada.")
        else:
            print("  ✗ Opción inválida.")

    def eliminar_producto(self):
        print("\n  -- Eliminar producto --")
        codigo = self._pedir_texto("  Codigo del producto a eliminar: ")
        prod = self._buscar_por_codigo(codigo)

        if prod is None:
            print("  ✗ Producto no encontrado.")
            return

        confirmacion = input(f"  ¿Seguro que deseas eliminar '{prod.nombre}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            self.productos.remove(prod)
            print("  ✓ Producto eliminado exitosamente.")
        else:
            print("  Eliminación cancelada.")


    def calcular_total_inventario(self):
        print("\n  -- Valor total del inventario --")
        if len(self.productos) == 0:
            print("  No hay productos registrados.")
            return

        total = 0
        for prod in self.productos:
            subtotal = prod.precio * prod.cantidad
            print(f"  {prod.nombre}: ${prod.precio:.2f} x {prod.cantidad} = ${subtotal:.2f}")
            total += subtotal

        print(f"  {'─'*40}")
        print(f"  TOTAL INVENTARIO: ${total:.2f}")

    def mostrar_agotados(self):
        print("\n  -- Productos agotados (cantidad = 0) --")
        agotados = [p for p in self.productos if p.cantidad == 0]

        if len(agotados) == 0:
            print("  No hay productos agotados.")
        else:
            print(f"  {len(agotados)} producto(s) agotado(s):")
            for prod in agotados:
                print(" ", prod.mostrar_info())

    def guardar_archivo(self):
        print("\n  -- Guardar en archivo --")
        if len(self.productos) == 0:
            print("  No hay productos para guardar.")
            return

        with open("inventario.txt", "w", encoding="utf-8") as archivo:
            archivo.write("===== INVENTARIO =====\n\n")
            for prod in self.productos:
                archivo.write(prod.mostrar_info() + "\n")
            archivo.write(f"\nTotal de productos: {len(self.productos)}\n")

            total = sum(p.precio * p.cantidad for p in self.productos)
            archivo.write(f"Valor total del inventario: ${total:.2f}\n")

        print("  ✓ Inventario guardado en 'inventario.txt'.")

    # ─── MENÚ ─────────────────────────────────────────────────────────────────

    def menu(self):
        while True:
            print("""
  ===== SISTEMA DE INVENTARIO =====
  1. Registrar producto
  2. Mostrar todos los productos
  3. Buscar producto
  4. Actualizar producto
  5. Eliminar producto
  6. Calcular valor total del inventario
  7. Mostrar productos agotados
  8. Guardar en archivo .txt
  9. Salir
  ==================================
            """)

            opcion = input("  Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.mostrar_productos()
            elif opcion == "3":
                self.buscar_producto()
            elif opcion == "4":
                self.actualizar_producto()
            elif opcion == "5":
                self.eliminar_producto()
            elif opcion == "6":
                self.calcular_total_inventario()
            elif opcion == "7":
                self.mostrar_agotados()
            elif opcion == "8":
                self.guardar_archivo()
            elif opcion == "9":
                print("  Saliendo del sistema...")
                break
            else:
                print("  ✗ Opción inválida, intente nuevamente.")


sistema = SistemaInventario()
sistema.menu()  