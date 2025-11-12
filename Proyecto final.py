"""Gestión de Tareas
Aplicación de consola para agregar, listar, editar y eliminar tareas."""

def mostrar_menu():
    """Muestra el menú de opciones en consola."""
    print("\n=== MENÚ ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

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
    
    """prioridad"""
    print("Elija la prioridad de la tarea:")
    print("1. Intensa")
    print("2. Moderada")
    print("3. Ligera")
    
    while True:
        opcion_prioridad = input("Seleccione una opción (1-3): ").strip()
        if opcion_prioridad == "1":
            prioridad = "Intensa"
            break
        elif opcion_prioridad == "2":
            prioridad = "Moderada"
            break
        elif opcion_prioridad == "3":
            prioridad = "Ligera"
            break
        else:
            print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
    
    tareas.append({"descripcion": tarea, "fecha": fecha, "prioridad": prioridad})
    print(f"Tarea agregada con éxito (Prioridad: {prioridad}).")

def ver_tareas(tareas):
    """Muestra todas las tareas almacenadas."""
    print("\n Tareas:")
    if len(tareas) > 0:
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t['descripcion']} - Fecha: {t['fecha']} - Prioridad: {t['prioridad']}")
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

def editar_tarea(tareas):
    """Edita una tarea existente."""
    if len(tareas) == 0:
        print("No hay ninguna tarea para editar.")
        return
    
    ver_tareas(tareas)
    
    try:
        indice = int(input("\nIngrese el número de la tarea a editar: "))
        if 1 <= indice <= len(tareas):
            tarea_actual = tareas[indice - 1]
            print(f"\nEditando: {tarea_actual['descripcion']}")
            print("\n¿Qué desea editar?")
            print("1. Descripción")
            print("2. Fecha")
            print("3. Prioridad")
            print("4. Todo")
            
            opcion_editar = input("Seleccione una opción: ").strip()
            
            if opcion_editar == "1":
                nueva_descripcion = input("Ingrese la nueva descripción: ").strip()
                if nueva_descripcion != "":
                    tarea_actual['descripcion'] = nueva_descripcion
                    print("Descripción actualizada.")
                else:
                    print("La descripción no puede estar vacía.")
                    
            elif opcion_editar == "2":
                nueva_fecha = input("Ingrese la nueva fecha (ej: 25/10/2025): ").strip()
                if nueva_fecha != "":
                    tarea_actual['fecha'] = nueva_fecha
                    print("Fecha actualizada.")
                else:
                    print("La fecha no puede estar vacía.")
                    
            elif opcion_editar == "3":
                print("\nElija la nueva prioridad:")
                print("1. Intensa")
                print("2. Moderada")
                print("3. Ligera")
                
                while True:
                    opcion_prioridad = input("Seleccione una opción (1-3): ").strip()
                    if opcion_prioridad == "1":
                        tarea_actual['prioridad'] = "Intensa"
                        print("Prioridad actualizada.")
                        break
                    elif opcion_prioridad == "2":
                        tarea_actual['prioridad'] = "Moderada"
                        print("Prioridad actualizada.")
                        break
                    elif opcion_prioridad == "3":
                        tarea_actual['prioridad'] = "Ligera"
                        print("Prioridad actualizada.")
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
                        
            elif opcion_editar == "4":
                nueva_descripcion = input("Ingrese la nueva descripción: ").strip()
                if nueva_descripcion == "":
                    print("La descripción no puede estar vacía.")
                    return
                
                nueva_fecha = input("Ingrese la nueva fecha (ej: 25/10/2025): ").strip()
                if nueva_fecha == "":
                    print("La fecha no puede estar vacía.")
                    return
                
                print("\nElija la nueva prioridad:")
                print("1. Intensa")
                print("2. Moderada")
                print("3. Ligera")
                
                while True:
                    opcion_prioridad = input("Seleccione una opción (1-3): ").strip()
                    if opcion_prioridad == "1":
                        nueva_prioridad = "Intensa"
                        break
                    elif opcion_prioridad == "2":
                        nueva_prioridad = "Moderada"
                        break
                    elif opcion_prioridad == "3":
                        nueva_prioridad = "Ligera"
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
                
                tarea_actual['descripcion'] = nueva_descripcion
                tarea_actual['fecha'] = nueva_fecha
                tarea_actual['prioridad'] = nueva_prioridad
                print("Tarea actualizada completamente.")
            else:
                print("Opción inválida.")
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
            editar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
