alien = {"color" : "verde" , "posicion_x" : 0 , "posicion_y" : 25, "speed" : "medium"}
if alien["speed"] == "slow" :
    x_increment = 1
elif alien["speed"] == "medium" :
    x_increment = 2
else :
    x_increment = 3
alien["posicion_x"]= alien["posicion_x"]  + x_increment
print("la nueva posicion del alien es" , alien["posicion_x"])

