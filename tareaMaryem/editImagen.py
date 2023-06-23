import PIL
from PIL import Image,ImageFilter,ImageDraw,ImageFont


img = Image.open("peñol1.jpg")



def imagenOriginal():
    img = Image.open("peñol1.jpg")
    img.show()

def EscalaGrises():

    grises = img.convert("L")
    grises.show()



def Contorno():
    contornos = img.filter(ImageFilter.CONTOUR)
    contornos.show()

def FiltroRaro():
    raro = img.filter(ImageFilter.FIND_EDGES)
    raro.show()

def rotar():
    rotada = img.rotate(180)
    rotada.show()

def escribirASCII():
    copia2 = img.copy()
    Ascii = ImageDraw.Draw(copia2)
    font = ImageFont.truetype("arial.ttf", 80)
    Ascii.text((50,50),"ALT + 77",fill="black", font=font)
    copia2.show()


def escribirUNICODE():
    copia = img.copy()
    Uni = ImageDraw.Draw(copia)
    font = ImageFont.truetype("arial.ttf", 80)
    Uni.text((150,150),"U + 004D",fill="black", font=font)
    copia.show()


def menu():
    print("""1.Imagen Original \n2.Escala de grises \n3.Contorno \n4.Limite de colores \n5.Rotar la imagen 180°\n6.Escribir en ASCII\n7.Escribir en UNICODE""")
    opcion = int(input("Digite el numero de la opcion que desea ejecutar en la imagen "))

    while opcion != 0:
        if opcion == 1:
            imagenOriginal()

        elif opcion == 2:
            EscalaGrises()
        elif opcion == 3:
            Contorno()
        elif opcion == 4:
            FiltroRaro()
        elif opcion == 5:
            rotar()
        elif opcion == 6:
            escribirASCII()
        elif opcion == 7:
            escribirUNICODE()

        print("""1.Imagen Original \n2.Escala de grises \n3.Contorno \n4.Limite de colores \n5.Rotar la imagen 180°\n6.Escribir en ASCII\n7.Escribir en UNICODE""")
        opcion = int(input("Digite el numero de la opcion que desea ejecutar en la imagen "))


menu()