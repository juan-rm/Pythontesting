users = {"sujeto1" : {"primer_nombre" : "Alberto" , "apellido" : "Gimenez"} , "sujeto2" : {"primer_nombre" : "Manolo" , "apellido" : "Ramirez"}}
print("Los nombres de los usuarios son:")
for usuario in users.keys() :
    diccionario_usuario = users[usuario]
    for nombre in diccionario_usuario.keys() :
       if nombre == "primer_nombre" :
        print(diccionario_usuario["primer_nombre"])