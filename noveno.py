alejandro={"nombre": "alejandro","edad": 45 , "ciudad": "catacho","aficiones": ["lectura","video juegos","descamsar"]}
print(alejandro)
luci={"nombre": "lucia","edad": 30 , "ciudad": "medallo","aficiones": ["escrbir","cantar","viajar"]}
print(luci)
trabajadores={0: alejandro, 1:luci}
print(trabajadores)
print(f"la longitud del diccionario de alejandro es de: {len(alejandro)}")
print(f"la longitud del diccionario de alejandro es de: {len(trabajadores)}")

# añadir un nuevo elemento 
alejandro["cargos"]= "CEO"
print(alejandro)
alejandro.update({"sueldo": 90000, "vaciones" : "muchas"})
print(alejandro)

# 
valor=alejandro.pop("cargo")
print(alejandro)
print(f"el valor eliminado es: {valor}")

print("acceder a un elemento de un diccionario")
edad= alejandro["edad"]
print(f" la edad de alejandro es {edad}")
