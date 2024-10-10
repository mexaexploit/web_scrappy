import urllib.request
import re

def main():
    url = input("Introduce la url objetivo : ")
    try:
            consulta = urllib.request.urlopen(url)
            
            contenido = consulta.read().decode('utf-8')
        
            with open('web.html','w+') as file_web:
                file_web.write(contenido)
            
            print(f"Contenido de {url} guardado en web.html")
            
    except Exception as e:
        print(f"Error al acceder a la pagina : {e}")
        

def parsear_contenido():
    try:
        with open('web.html','r') as web:
            contenido = web.read()

        inicio = input("Introduzca una etiqueta o valor de inicio a buscar : ")
        final = input("Introduzca una etiqueta o valor a final a buscar : ")
        
        resultado = re.search(f'{inicio}(.*?){final}',contenido,re.DOTALL)
        if resultado:
            print(f"Resultado encontrado entre {inicio} y {final} : \n{resultado.group(1)}")
        else:
            print("No se encontro resultado entre las etiquetas especificadas")
    except FileNotFoundError:
        print("El archivo 'web.html' no se encuentra")
            
def search():
    buscar = input("Introduce con expresiones regulares palabra a buscar : ")
    try: 
        with open('web.html','r') as web: 
            contenido = web.read()
            resultado = re.findall(buscar,contenido,re.DOTALL)
            if resultado:
                print(f"Resultado encontrado para '{buscar}'")
                for i, res in enumerate (resultado,1):
                    print(f"{i}.{res}")
            else:
                print("Resultado no encontrado")
    except FileNotFoundError:
        print("No se encontro el archivo 'web.html'")
        
def extraer_enlaces():
    try:
        with open('web.html','r') as web:
            contenido = web.read()
        
        enlaces = re.findall(r'href="(.*?)"',contenido)
        if enlaces:
            print("Enlaces encontrados en la pagina : ")
            for enlace in enlaces:
                print(enlace)
        else:
            print("No se encontraron enlaces")
    except FileNotFoundError:
            print("No se encontro el archivo web.html")
            
def extraer_imagenes():
    try:
        with open('web.html','r') as web:
            contenido = web.read()
            
            imagenes = re.findall(r'<img[^>]*src="(.*?)"', contenido)
            if imagenes:
                for img in imagenes:
                    print("Imagenes encontradas en la pagina : ")
                    print(img)
            else:
                print("No se encontraron imagenes")
    except FileNotFoundError:
        print("No se encontro el archivo 'web.html'")
        
                        
            
if __name__ == '__main__':
    main()
    
    while True:
        print("\n Opciones:")
        
        print("1. Para extraer contenido entre etiquetas")
        print("2. Para buscar contenido con expresiones regulares")
        print("3. Para extraer enlaces de la pagina")
        print("4. Para extraer imagenes de la pagina")
        print("5. salir...")
        
        opcion = input("Seleccione una opcion : ")
        
        if opcion == '1':
            parsear_contenido()
        elif opcion == '2':
            search()
        elif opcion == '3':
            extraer_enlaces()
        elif opcion == '4':
            extraer_imagenes()
        elif opcion == '5':
            break
        else:
            print("Opcion no valida, intentelo de nuevo")    