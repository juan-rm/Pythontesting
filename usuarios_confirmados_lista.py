active = True
lista_usuarios =[]
while active :
    usuario = input ("Nombre del proximo asistente, sino desea introducir nuevo asistente indiquelo marcando quit\n")
    if usuario != "quit" :
        lista_usuarios.append(usuario)
    else :
        active = False    
print(lista_usuarios)
i=0
lista_asistentes = []
while lista_usuarios :
      print(lista_usuarios[i] , "\n")  
      asistencia = input("Confirma su asistencia? Si/No ")
      if asistencia == "Si":
          lista_asistentes.append(lista_usuarios[i])
      else :
          print(lista_usuarios[i] , "no asistira al evento")
      lista_usuarios.pop(0)
print(lista_asistentes)     


