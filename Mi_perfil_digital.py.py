# uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Ronald Santiago Arias Quintero"
edad = 14
estatura = 1.78
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("@ronald.arias297")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Fanatico", "artista": "Blessd", "duracion": "3:56"},
{"titulo": "Balconcito", "artista": "Blessd", "duracion": "5:01"},
{"titulo": "SUPERSTAR", "artista": "Blessd", "duracion": "3:15"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")