ingredientes_disponibles = ["peperoni" , "panceta" , "queso" , "pimientos" , "tomate" , "aguacate" , "jamon" , "piña"]
ingredientes_deseados = ["tomate" , "jamon", "piña", "alcaparras"]
for ingrediente_disponible in ingredientes_disponibles:
   if ingrediente_disponible in ingredientes_deseados:
       print("añadimos" , ingrediente_disponible ," a la pizza") 
   else:
       print("no disponemos de " , ingrediente_disponible)    