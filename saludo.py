def saludar(nombre_completo):
    if not nombre_completo or not nombre_completo.strip():
        return "Error: el nombre no puede estar vacio"
    return f"Hola {nombre_completo}"

print(saludar("GitHub"))
