"""Gestión de Tareas
Aplicación de consola para agregar, listar y eliminar tareas."""

def mostrar_menu():
    """Muestra el menú de opciones en consola."""
    print("\n=== MENÚ ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista."""
    tarea = input("Ingrese la tarea: ").strip()
    if tarea == "":
        print("La tarea no puede estar vacía.")
        return
    
    fecha = input("Ingrese la fecha de entrega (ej: 25/10/2025): ").strip()
    if fecha == "":
        print("La fecha no puede estar vacía.")
        return

    tareas.append({"descripcion": tarea, "fecha": fecha})
    print("Tarea agregada con éxito.")

def ver_tareas(tareas):
    """Muestra todas las tareas almacenadas."""
    print("\n📋 Tareas:")
    if len(tareas) > 0:
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t['descripcion']} -  Fecha: {t['fecha']}")
    else:
        print("No hay tareas registradas.")

def eliminar_tarea(tareas):
    """Elimina una tarea según el número ingresado por el usuario."""
    if len(tareas) == 0:
        print("No hay tareas para eliminar.")
        return
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= indice <= len(tareas):
            eliminada = tareas.pop(indice - 1)
            print(f"Tarea '{eliminada['descripcion']}' eliminada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def main():
    """Función principal del programa."""
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

