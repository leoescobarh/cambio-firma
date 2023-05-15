import glob

def cambiar_relacion_archivos(archivos, relacion_actual, relacion_nueva):
    for archivo in archivos:
        # Leer el contenido del archivo
        with open(archivo, 'r') as f:
            contenido = f.read()

        # Verificar si la relación actual está presente en el contenido del archivo
        if relacion_actual in contenido:
            # Reemplazar la relación actual por la nueva relación
            nuevo_contenido = contenido.replace(relacion_actual, relacion_nueva)

            # Escribir el contenido modificado de vuelta al archivo
            with open(archivo, 'w') as f:
                f.write(nuevo_contenido)

            print(f"Relación cambiada exitosamente en el archivo: {archivo}")
        else:
            print(f"La relación especificada no se encontró en el archivo: {archivo}")

# Obtener la lista de archivos en el directorio actual con extensión .sql o .txt
archivos = glob.glob("*.sql") + glob.glob("*.txt")

relacion_actual = "AND TRA.COD_ESTADO_FIRMA = 1"
relacion_nueva = "AND TRA.COD_ESTADO_FIRMA IN (1,2)"

# Eliminar espacios entre el "=" y el valor "1" en la relación actual
relacion_actual = relacion_actual.replace("= ", "=")

cambiar_relacion_archivos(archivos, relacion_actual, relacion_nueva)

# Imprimir la cantidad de archivos y sus rutas
print(f"Se subieron {len(archivos)} archivos:")
for archivo in archivos:
    print(archivo)
