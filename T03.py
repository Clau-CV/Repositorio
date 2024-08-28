diccionario = {
    "nombre": "Chris",
    "edad": 24,
    "ciudad": "Tokyo"
}

# pop()
edad = diccionario.pop("edad")
print(f"pop: {edad}")  # Imprime 24
print(f"Diccionario después de pop: {diccionario}")

# get()
ciudad = diccionario.get("ciudad")
print(f"get: {ciudad}")

# copy()
copia_diccionario = diccionario.copy()
print(f"copy: {copia_diccionario}")

# keys()
claves = diccionario.keys()
print(f"keys: {claves}")

# items()
items = diccionario.items()
print(f"items: {items}")  #

# clear()
diccionario.clear()
print(f"clear: {diccionario}")

# Reiniciar
diccionario = {"nombre": "Chris", "edad": 24, "ciudad": "Tokyo"}

# fromkeys()
nuevas_claves = ["a", "b", "c"]
nuevo_diccionario = dict.fromkeys(nuevas_claves, 0)
print(f"fromkeys: {nuevo_diccionario}")

# popitem()
ultima_clave, ultimo_valor = diccionario.popitem()
print(f"popitem: Clave - {ultima_clave}, Valor - {ultimo_valor}")
print(f"Diccionario después de popitem: {diccionario}")

# setdefault()
pais = diccionario.setdefault("pais", "Japón")
print(f"setdefault: {pais}")
print(f"Diccionario después de setdefault: {diccionario}")

# update()
diccionario.update({"edad": 22, "ciudad": "Kyoto"})
print(f"update: {diccionario}")

# values()
valores = diccionario.values()
print(f"values: {valores}")