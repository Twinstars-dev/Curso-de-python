import re

# La sintaxis \B coincide con cualquier cosa que no sea un límite de palabra:
patron=re.compile(r'\Bcat\B')
match1=patron.findall("My certificate is great")
match2=patron.findall("Your room is a catastrophe")
# print(match1)
# Es útil para encontrar coincidencias en medio de una palabra.

# El signo de interrogación coincide con cero o una instancia del calificador precedente.
# El * coincide con cero o más instancias del calificador precedente.
# El signo + coincide con una o más instancias del calificador precedente.
# El {n} coincide exactamente con n instancias del calificador precedente.
# El {n,} coincide con n o más instancias del calificador precedente.
# El {,m} coincide con 0 a m instancias del calificador precedente.
# El {n,m} coincide con al menos n y como máximo m instancias del calificador precedente.
# {n,m}? o *? o +? realiza una coincidencia no codiciosa del calificador precedente.
# ^spam significa que la cadena debe comenzar con spam .
# spam$ significa que la cadena debe terminar con spam .
# El punto coincide con cualquier carácter, excepto los caracteres de salto de línea.
# Los caracteres \d , \w y \s corresponden a un dígito, una palabra o un espacio, respectivamente.
# Los caracteres \D , \W y \S coinciden con cualquier cosa excepto un dígito, una palabra o un espacio, respectivamente. [abc] coincide con cualquier carácter entre corchetes (como a , b o c ).
# [^abc] coincide con cualquier carácter que no esté entre corchetes.
# (Hello) agrupa 'Hello' como un único calificador.

Sin_distincion_entre_mayusculas_y_minusculas=""
# Para que tu expresión regular no distinga entre mayúsculas y minúsculas,
# puedes pasar ` re.IGNORECASE` o `re.I` como segundo argumento a `
# re.compile()` 
patronRobocop=re.compile(r'robocop',re.I)
ejemplo1=patronRobocop.search("RoboCop es un policia que estuvo aquí ")
# print(ejemplo1.group())
ejemplo2=patronRobocop.search("RoboCOP es un policia que estuvo aquí ")
# print(ejemplo2.group())
ejemplo3=patronRobocop.search("ROBOCOp es un policia que estuvo aquí ")
# print(ejemplo3.group())
# La expresión regular ahora coincide con cadenas de texto 
# con cualquier combinación de mayúsculas y minúsculas.

Sustitucion_de_cadenas=""
# Las expresiones regulares no solo encuentran patrones de texto, 
# sino que también pueden sustituirlos por texto nuevo.
# El método `sub() ` de los objetos `Pattern` acepta dos argumentos. 
# El primero es una cadena que reemplazará a las coincidencias. 
# El segundo es la cadena de la expresión regular. 
# El método `sub()` devuelve una cadena con las sustituciones aplicadas

patron_agente=re.compile(r'Agente \w+')
agente1=patron_agente.sub("CENSURADO","Agente Ander contactó al Agente Bill.")
#print(agente1) #cambia el patron por otro en todas las coincidencias

# supongamos que desea censurar los nombres de los agentes secretos
# mostrando solo las primeras letras de sus nombres. 
# Para ello, podría usar la expresión regular Agent (\w)\w* y 
# pasar r'\1****' como primer argumento a sub()

Referencia_inversa=""
# A veces, puede que necesites usar el texto coincidente como 
# parte de la sustitución. En el primer argumento de sub() , 
# puedes incluir \1 , \2 , \3 , etc., para indicar 
# "Introduce el texto del grupo 1 , 2 , 3 , etc., en la sustitución".
agente_patron2=re.compile(r'Agente (\w)\w*')
agente2=agente_patron2.sub(r'\1****','Agente Alice contactó al Agente Bob')
print(agente2)
# El \1 en la cadena de la expresión regular se reemplaza por cualquier
# texto que haya coincidido con el grupo 1 , es decir, 
# el grupo (\w) de la expresión regular.

Gestión_de_expresiones_regulares_complejas_con_modo_detallado=""
# Las expresiones regulares son útiles si el patrón de texto 
# que necesitas comparar es simple. Sin embargo, comparar patrones 
# de texto complejos puede requerir expresiones regulares largas y 
# enrevesadas. Puedes mitigar esta complejidad indicándole a la función
# re.compile() que ignore los espacios en blanco y los comentarios
# dentro de la cadena de la expresión regular. Habilita este 
# "modo detallado" pasando la variable re.VERBOSE como segundo 
# argumento a re.compile() 

#Dificil: pattern = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-
#|\.)\d{4}(\s*(ext|x|ext\.)\s*\d{2,5})?)')

#Mas digerible:
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separador
    \d{3}  # Primeros 3 digitos
    (\s|-|\.)  # Separador
    \d{4}  # Ultimos 4 digitos
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)

#Recomendable usar el modulo Humre 

Combinando_ignorecase_dotall_verbose=""
algun_regex=re.compile("sal",re.I|re.DOTALL|re.DOTALL)
# Esta sintaxis es algo anticuada y proviene de versiones antiguas
# de Python. Los detalles de los operadores bit a bit quedan 
# fuera del alcance de este libro.

ejemplo=""
import pyperclip
paso1=""
telefono_regex=re.compile(r'''(
    (\d{3}|\(\d{3}\))? #Codigo de area opcional
    (\s|-|\.)? #separador
    (\d{3}) #primeros 3 digitos
    (\s|-|\.) #separador
    (\d{4}) #ultimos 4 digitos
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? #extension   
    )''',re.VERBOSE) #La última parte es unextensión opcional compuesta por cualquier número de espacios seguidos de ext , x o ext. , seguidos de dos a cinco dígitos.

paso2=""
email_regex=re.compile(r'''(
    [a-zA-Z0-0._%+-]+ # Nombre de usuario
    @   # arroba simbolo
    [a-zA-Z0-9.-]+  # nombre del dominio
    (\.[a-zA-Z]{2,4}) #con algo 
    )''',re.VERBOSE) #email completo

paso3=""
texto=str(pyperclip.paste())
coincidencias=[]
for groups in telefono_regex.findall(texto):
    telefono='-'.join([groups[1],groups[3],groups[5]])
    if [groups[6]!= '']:
        telefono+= 'x' + groups[6]
    coincidencias.append(telefono)

for groups in email_regex.findall(texto):
    coincidencias.append(groups[0])

paso4=""
if len(coincidencias)>0:
    pyperclip.copy('\n'.join(coincidencias))
    print("copiado al portapapeles")
    print('\n'.join(coincidencias))
else:
    print("Telefono o Email no encontrados")

HUMRE=""
#no tan usado

RESUMEN= " "
# Si bien una computadora puede buscar texto rápidamente,
# es necesario indicarle con precisión qué buscar. 
# Las expresiones regulares permiten especificar el patrón de 
# caracteres que se busca, en lugar del texto exacto. De hecho,
# algunas aplicaciones de procesamiento de texto y hojas de 
# cálculo ofrecen funciones de búsqueda y reemplazo que permiten 
# buscar mediante expresiones regulares. La sintaxis de las expresiones
# regulares, rica en signos de puntuación, se compone de calificadores
# que detallan qué caracteres deben coincidir y cuantificadores que 
# detallan cuántos deben coincidir.

# El módulo `re` que viene con Python te permite compilar una cadena 
# de expresiones regulares en un objeto `Pattern` . Estos objetos 
# tienen varios métodos: `search()` , para encontraruna sola 
# coincidencia; findall() , para encontrar todas las instancias 
# coincidentes; y sub() , para realizar una sustitución de texto
# mediante búsqueda y reemplazo.


