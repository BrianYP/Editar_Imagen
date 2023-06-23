import os
import zipfile

ruta = "C:\\Users\\Brahyan\\Documents\\tareaMaryem"


Zip  = zipfile.ZipFile("trabajitos.zip", "w")

tipo_archivos = ["Mogotes.jpg","himno.txt", "himnoAntioquia.txt", "himnoSantander.txt"]


for archivos in os.listdir(ruta):
    for tipos in tipo_archivos:
        if archivos.endswith(tipos):

            Zip.write(archivos,compress_type=zipfile.ZIP_DEFLATED)
            informacion = Zip.getinfo(archivos)
            print("el tipo de archivo es" ,tipos, archivos)
            print(informacion.compress_size, "Archivo comprimido")
            print(informacion.file_size, "Archivo sin comprimir")
            valores = ((informacion.file_size - informacion.compress_size)*100)/informacion.file_size
            print("El archivo comprimido corresponde al ", valores, "%")



Zip.close()