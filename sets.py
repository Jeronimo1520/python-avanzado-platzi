#Operaciones con conjuntos con videojuegos.

aventura = {"Uncharted","The legend of Zelda","Assassin's Creed",}
sigilo = {"Assassin's Creed","Hitman","Metal Gear"}
accion = {"Assassin's Creed","Hitman","BioShock","GTA","Batman:Arkham","Spiderman"}
superheroes = {"Spiderman,","Batman:Arkham"}

union_aventura_sigilo = aventura | sigilo
print(union_aventura_sigilo)

inter_sigilo_accion = sigilo & accion
print(inter_sigilo_accion)

difer_accion_super = accion - superheroes
print(difer_accion_super)

difersime_aventura_accion = aventura ^ accion
print(difersime_aventura_accion)