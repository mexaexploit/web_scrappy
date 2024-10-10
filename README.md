Herramienta de Web Scraping
Este proyecto es una herramienta sencilla de web scraping que permite a los usuarios extraer contenido de páginas HTML, buscar patrones específicos usando expresiones regulares y extraer enlaces o imágenes de la página web.

Funcionalidades
Descargar contenido HTML: Descargar y guardar el contenido HTML de una URL proporcionada.
Extraer contenido entre etiquetas: Especificar etiquetas de inicio y fin para extraer el contenido entre ellas.
Buscar usando expresiones regulares: Buscar patrones dentro del HTML usando expresiones regulares personalizadas.
Extraer enlaces: Encontrar todos los enlaces (<a href="">) en la página web.
Extraer imágenes: Extraer todas las fuentes de imágenes (<img src="">) de la página web.
Requisitos
Este proyecto no requiere de bibliotecas externas, ya que solo utiliza bibliotecas estándar de Python:

urllib
re
Estas bibliotecas son parte de la biblioteca estándar de Python, por lo que no es necesario instalar nada adicional.

Uso
Clona el repositorio:

bash
Copy code
git clone https://github.com/mexaexploit/web_scrappy.git
Navega al directorio del proyecto:

bash
Copy code
python3 web_scrappy.py
El script te pedirá la URL de la página objetivo y te permitirá:

Extraer contenido entre etiquetas
Buscar texto usando expresiones regulares
Extraer todos los enlaces de la página
Extraer todas las imágenes de la página
