# -*- coding: utf-8 -*-
"""
PyChoice - Modulo C: Python intermedio (Lecciones 9 a 12).
Formato capitulo (estilo EstadisticaR). Teoria extendida + 8 conceptos +
ejemplos ejecutables + ejercicios. En cada consola: np, pd, plt y los datos
de ejemplo `notas` (lista) y `datos` (DataFrame).
"""

CHAPTERS_C = [

    # ============================================================ CAP 09
    {
        "num": 9,
        "slug": "estructuras",
        "code": "leccion_09",
        "title": "Estructuras de datos",
        "subtitle": "Listas, tuplas, diccionarios y conjuntos: organizar la información",
        "apunte": "Lección 9 - Estructuras de datos",
        "concepts": [
            ("Lista <code>[ ]</code>", "Colección <b>ordenada y mutable</b>: puedes agregar, quitar y cambiar elementos. La estructura más versátil."),
            ("Tupla <code>( )</code>", "Colección <b>ordenada e inmutable</b>: no cambia una vez creada. Ideal para datos fijos (una coordenada, una fila)."),
            ("Diccionario <code>{clave: valor}</code>", "Pares <b>clave → valor</b>. Se accede por la clave, no por posición. Es la forma natural de representar un registro."),
            ("Conjunto <code>set</code>", "Colección <b>sin duplicados y sin orden</b>. Útil para valores únicos y operaciones de conjuntos."),
            ("Mutabilidad", "Si una estructura se puede modificar tras crearla (listas, dicts, sets) o no (tuplas, textos)."),
            ("Índice vs clave", "Las listas/tuplas se acceden por <b>posición</b> (empieza en 0); los diccionarios por <b>clave</b>."),
            ("Métodos de lista", "<code>.append()</code>, <code>.insert()</code>, <code>.remove()</code>, <code>.sort()</code>, <code>.pop()</code>."),
            ("Pertenencia (<code>in</code>)", "Comprueba si un valor está en una colección: <code>\"a\" in lista</code>."),
        ],
        "theory": """
<p>Los datos rara vez vienen sueltos: vienen en <b>colecciones</b>. Python ofrece cuatro estructuras
fundamentales para organizarlos, y elegir la correcta hace el código más claro y eficiente. Son las
piezas con las que, más adelante, se construyen las tablas de pandas.</p>

<p><b>La lista</b> es la más usada: una secuencia <b>ordenada y mutable</b> entre corchetes
<code>[ ]</code>. Puedes acceder por posición (<code>lista[0]</code>), cortar tramos
(<code>lista[1:3]</code>) y modificarla con métodos como <code>.append()</code> (agregar),
<code>.remove()</code> (quitar) o <code>.sort()</code> (ordenar). Piensa en ella como una columna de
datos.</p>

<p><b>La tupla</b> es como una lista pero <b>inmutable</b>: se escribe con paréntesis <code>( )</code>
y no se puede cambiar una vez creada. Se usa para agrupar datos que no deben modificarse (una
coordenada <code>(x, y)</code>, una fila de resultados) y permite el <b>desempaquetado</b>:
<code>lat, lon = punto</code>.</p>

<p><b>El diccionario</b> es, para un analista, la estructura más importante después de la lista.
Guarda pares <b>clave → valor</b> entre llaves <code>{ }</code> y se accede por la <b>clave</b>, no
por posición: <code>persona["edad"]</code>. Es la forma natural de representar un <b>registro</b> (una
fila con campos nombrados). De hecho, una <b>lista de diccionarios</b> es prácticamente una tabla, y
pandas la convierte en un DataFrame directamente.</p>

<p><b>El conjunto</b> (<code>set</code>) guarda elementos <b>únicos y sin orden</b>. Sirve para
eliminar duplicados de golpe (<code>set(lista)</code>) y para operaciones de conjuntos: unión
(<code>|</code>), intersección (<code>&amp;</code>) y diferencia (<code>-</code>). Responde bien a la
pregunta "¿qué valores distintos hay?".</p>

<p><b>Mutabilidad: un concepto clave.</b> Listas, diccionarios y conjuntos son <b>mutables</b> (se
pueden modificar); tuplas y textos son <b>inmutables</b>. Entenderlo evita sorpresas, sobre todo al
pasar estructuras a funciones. Y el operador <code>in</code> permite preguntar si un valor pertenece
a cualquiera de estas colecciones.</p>

<p><b>Estructuras anidadas.</b> Estas piezas se combinan: listas de listas, listas de diccionarios,
diccionarios cuyos valores son listas… Así se representa información compleja del mundo real. Dominar
estas cuatro estructuras es el puente entre "programar" y "analizar datos".</p>
""",
        "examples": [
            {
                "title": "Listas a fondo",
                "explain": "Crear, indexar, cortar y modificar. Los métodos cambian la lista en el sitio.",
                "code": 'ventas = [120, 95, 130, 110]\nprint("primero:", ventas[0], "| ultimo:", ventas[-1])\nventas.append(88)          # agrega al final\nventas.sort()              # ordena\nprint("ordenada:", ventas)\nprint("cuántas:", len(ventas))',
            },
            {
                "title": "Tuplas: inmutables y desempaquetado",
                "explain": "No se pueden modificar. Muy útiles para agrupar y repartir valores.",
                "code": 'punto = (10, 20)\nx, y = punto            # desempaquetado\nprint("x =", x, "| y =", y)\nprint("tipo:", type(punto))',
            },
            {
                "title": "Diccionarios: clave → valor",
                "explain": "Un registro con campos nombrados. Se accede por la clave y se recorre con items().",
                "code": 'persona = {"nombre": "Ana", "edad": 30, "ciudad": "Santiago"}\nprint(persona["nombre"])\npersona["edad"] = 31       # actualizar\npersona["email"] = "ana@mail.cl"  # agregar\nfor clave, valor in persona.items():\n    print(clave, "->", valor)',
            },
            {
                "title": "Conjuntos: valores únicos",
                "explain": "Elimina duplicados y permite operaciones de conjuntos.",
                "code": 'regiones = ["norte", "sur", "norte", "centro", "sur"]\nunicas = set(regiones)\nprint("únicas:", unicas)\nprint("¿hay sur?:", "sur" in unicas)\nprint("cuántas distintas:", len(unicas))',
            },
            {
                "title": "Estructuras anidadas: una mini-tabla",
                "explain": "Una lista de diccionarios es, en esencia, una tabla: cada dict es una fila.",
                "code": 'tabla = [\n    {"producto": "pan", "precio": 990},\n    {"producto": "leche", "precio": 1200},\n    {"producto": "café", "precio": 2990},\n]\nfor fila in tabla:\n    print(fila["producto"], "->", fila["precio"])',
            },
            {
                "title": "De estructuras a pandas",
                "explain": "pandas convierte una lista de diccionarios en un DataFrame directamente.",
                "code": 'import pandas as pd\ntabla = [\n    {"producto": "pan", "precio": 990},\n    {"producto": "leche", "precio": 1200},\n]\ndf = pd.DataFrame(tabla)\nprint(df)',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Crea una lista con 5 ciudades, agrega una sexta con <code>.append()</code> y ordénala.",
            "Crea una tupla con tu año y mes de nacimiento y desempácala en dos variables.",
            "Crea un diccionario de un producto con <code>nombre</code>, <code>precio</code> y <code>stock</code>, y muéstralo.",
            "Recorre el diccionario anterior con <code>.items()</code> e imprime cada campo.",
            "A partir de <code>[1, 2, 2, 3, 3, 3]</code>, obtén los valores únicos con <code>set()</code>.",
            "Comprueba con <code>in</code> si <code>\"café\"</code> está en una lista de productos.",
            "Crea una lista de 3 diccionarios (persona con nombre y edad) y recórrela mostrando cada nombre.",
            "Convierte esa lista de diccionarios en un <code>DataFrame</code> con pandas.",
            "Dada la lista <code>[5, 3, 8, 1]</code>, usa <code>.sort()</code> y luego <code>.pop()</code> para quitar el último y muéstralo.",
        ],
    },

    # ============================================================ CAP 10
    {
        "num": 10,
        "slug": "funciones",
        "code": "leccion_10",
        "title": "Funciones",
        "subtitle": "Empaquetar código reutilizable con def, parámetros y return",
        "apunte": "Lección 10 - Funciones",
        "concepts": [
            ("Función", "Un bloque de código con nombre que realiza una tarea y se puede reutilizar cuantas veces quieras."),
            ("def", "Palabra clave para definir una función: <code>def nombre(parametros):</code>."),
            ("Parámetro / argumento", "El <b>parámetro</b> es la variable en la definición; el <b>argumento</b> es el valor que le pasas al llamarla."),
            ("return", "Devuelve un resultado al que la llamó. Distinto de <code>print</code>, que solo muestra."),
            ("Valor por defecto", "Un parámetro puede tener un valor por omisión: <code>def f(x, iva=0.19):</code>."),
            ("Argumento con nombre", "Al llamar puedes nombrar el argumento: <code>f(precio=100, iva=0.19)</code>."),
            ("Alcance (scope)", "Las variables creadas dentro de una función son <b>locales</b>: no existen fuera de ella."),
            ("lambda", "Función anónima de una línea: <code>lambda x: x * 2</code>. Muy usada con <code>apply</code>."),
        ],
        "theory": """
<p>A medida que un programa crece, repetir el mismo código en varios lugares se vuelve un problema:
es difícil de mantener y propenso a errores. Las <b>funciones</b> resuelven esto: empaquetan una
tarea con un nombre para <b>reutilizarla</b>. Es el principio <b>DRY</b> (<i>Don't Repeat
Yourself</i>): escribe la lógica una vez, úsala muchas.</p>

<p><b>Definir y llamar.</b> Una función se define con <code>def</code>, un nombre, unos
<b>parámetros</b> entre paréntesis y dos puntos; el cuerpo va sangrado. Luego se <b>llama</b> por su
nombre pasándole <b>argumentos</b>. Por ejemplo, <code>def saludar(nombre):</code> define, y
<code>saludar("Ana")</code> ejecuta.</p>

<p><b>return: devolver un resultado.</b> La mayoría de las funciones <b>calculan</b> algo y lo
<b>devuelven</b> con <code>return</code>, para poder usar ese valor después
(<code>total = sumar(3, 5)</code>). Es importante no confundir <code>return</code> con
<code>print</code>: <code>print</code> solo <b>muestra</b> en pantalla, mientras que
<code>return</code> <b>entrega</b> el valor al resto del programa. Una función puede incluso devolver
varios valores a la vez (como una tupla).</p>

<p><b>Parámetros flexibles.</b> Los parámetros pueden tener <b>valores por defecto</b>
(<code>def precio_final(neto, iva=0.19):</code>), de modo que si no los pasas, se usa el valor por
omisión. Y al llamar puedes usar <b>argumentos con nombre</b> para mayor claridad:
<code>precio_final(neto=1000, iva=0.19)</code>. Esto hace las funciones cómodas y legibles.</p>

<p><b>Alcance (scope).</b> Las variables que creas <b>dentro</b> de una función son <b>locales</b>:
viven solo mientras la función se ejecuta y no interfieren con el resto del programa. Esto es una
ventaja: cada función es una "caja" independiente. Los valores entran por los parámetros y salen por
el <code>return</code>.</p>

<p><b>Funciones lambda.</b> Para operaciones muy cortas existe la <b>función anónima</b> o
<code>lambda</code>: una función de una sola línea sin nombre, como <code>lambda x: x * 2</code>. Se
usan muchísimo en análisis de datos junto con <code>apply()</code> de pandas para transformar o
clasificar una columna entera con una regla breve.</p>

<p><b>Buenas prácticas.</b> Da a tus funciones nombres <b>descriptivos</b> (un verbo:
<code>calcular_promedio</code>), haz que cada una haga <b>una sola cosa</b>, y documenta qué hace con
un breve comentario o <i>docstring</i>. Funciones pequeñas y claras son la base de un código
mantenible.</p>
""",
        "examples": [
            {
                "title": "Definir y llamar",
                "explain": "Se define una vez con <code>def</code> y se usa cuantas veces quieras.",
                "code": 'def saludar(nombre):\n    print(f"Hola, {nombre}!")\n\nsaludar("Ana")\nsaludar("Luis")',
            },
            {
                "title": "Parámetros y return",
                "explain": "La función calcula y <b>devuelve</b> un valor para usarlo después.",
                "code": 'def sumar(a, b):\n    return a + b\n\ntotal = sumar(8, 5)\nprint("total:", total)\nprint("otra:", sumar(100, 200))',
            },
            {
                "title": "Valores por defecto y nombres",
                "explain": "Un parámetro puede tener valor por omisión; al llamar puedes nombrar los argumentos.",
                "code": 'def precio_final(neto, iva=0.19):\n    return round(neto * (1 + iva))\n\nprint(precio_final(1000))            # usa iva por defecto\nprint(precio_final(1000, iva=0.10))  # iva con nombre',
            },
            {
                "title": "Devolver varios valores",
                "explain": "Una función puede devolver una tupla, que se desempaqueta al recibirla.",
                "code": 'def resumen(numeros):\n    return min(numeros), max(numeros), sum(numeros) / len(numeros)\n\nmn, mx, prom = resumen([12, 7, 9, 15])\nprint("min:", mn, "| max:", mx, "| promedio:", prom)',
            },
            {
                "title": "Una función aplicada a datos",
                "explain": "Encapsula un cálculo estadístico y reutilízalo con distintas listas.",
                "code": 'def promedio(lista):\n    return sum(lista) / len(lista)\n\nprint("notas:", round(promedio(notas), 2))\nprint("otra :", promedio([10, 20, 30]))',
            },
            {
                "title": "lambda con apply",
                "explain": "Una regla breve aplicada a toda una columna con <code>apply()</code>.",
                "code": 'datos["nivel"] = datos["ventas"].apply(lambda x: "alta" if x > 100 else "baja")\nprint(datos[["mes", "ventas", "nivel"]])',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Define una función <code>saludar(nombre)</code> que imprima un saludo y llámala con dos nombres.",
            "Crea una función <code>doble(n)</code> que <b>devuelva</b> el doble de un número y muestra el resultado.",
            "Escribe <code>area_rectangulo(base, alto)</code> que devuelva el área.",
            "Haz <code>precio_final(neto, iva=0.19)</code> y pruébala con y sin el segundo argumento.",
            "Crea <code>maximo_minimo(lista)</code> que devuelva el máximo y el mínimo (dos valores).",
            "Define <code>promedio(lista)</code> y úsala sobre la lista <code>notas</code>.",
            "Con una <code>lambda</code>, crea una columna en <code>datos</code> que marque <code>\"ok\"</code> si <code>unidades &gt;= 10</code>, si no <code>\"bajo\"</code>.",
            "Escribe una función que reciba un texto y devuelva cuántas vocales tiene.",
            "Crea <code>clasifica_nota(n)</code> que devuelva <code>\"aprobado\"</code> o <code>\"reprobado\"</code> según <code>n &gt;= 4</code>.",
        ],
    },

    # ============================================================ CAP 11
    {
        "num": 11,
        "slug": "comprensiones",
        "code": "leccion_11",
        "title": "Comprensiones de listas y diccionarios",
        "subtitle": "Construir colecciones en una línea, de forma clara y potente",
        "apunte": "Lección 11 - Comprensiones",
        "concepts": [
            ("Comprensión de lista", "Construye una lista en una línea: <code>[expr for x in iterable]</code>."),
            ("Expresión", "Lo que se calcula para cada elemento (la parte izquierda de la comprensión)."),
            ("Condición (filtro)", "Se puede filtrar: <code>[x for x in it if condición]</code>."),
            ("Transformación", "Aplicar una operación a cada elemento: <code>[x*2 for x in nums]</code>."),
            ("Comprensión de diccionario", "Construye un dict: <code>{k: v for ...}</code>."),
            ("map()", "Aplica una función a cada elemento de un iterable."),
            ("filter()", "Conserva solo los elementos que cumplen una condición."),
            ("Legibilidad", "Las comprensiones son elegantes, pero si se vuelven ilegibles, un bucle normal es mejor."),
        ],
        "theory": """
<p>Un patrón aparece constantemente al programar con datos: recorrer una colección para
<b>construir otra</b> (transformar cada valor, o quedarse con algunos). Escribirlo con un bucle
funciona, pero Python ofrece una forma más compacta y legible: las <b>comprensiones</b>.</p>

<p><b>Comprensión de lista.</b> Su forma básica es <code>[expresión for elemento in iterable]</code>.
Por ejemplo, <code>[n*2 for n in numeros]</code> crea una nueva lista con el doble de cada número, en
una sola línea. Equivale a crear una lista vacía y hacer <code>append</code> dentro de un
<code>for</code>, pero más corto y claro.</p>

<p><b>Con condición (filtro).</b> Puedes añadir un <code>if</code> al final para quedarte solo con
ciertos elementos: <code>[n for n in numeros if n &gt; 0]</code> deja únicamente los positivos.
Combinando expresión y condición transformas y filtras a la vez:
<code>[n*2 for n in numeros if n % 2 == 0]</code> duplica solo los pares.</p>

<p><b>Comprensión de diccionario.</b> El mismo patrón sirve para construir diccionarios:
<code>{palabra: len(palabra) for palabra in lista}</code> crea un dict de palabra → largo. Es muy útil
para armar mapeos y tablas de referencia rápidamente.</p>

<p><b>map y filter.</b> Antes de las comprensiones, Python ya tenía <code>map()</code> (aplica una
función a cada elemento) y <code>filter()</code> (conserva los que cumplen una condición). Siguen
siendo válidas y las verás en código ajeno: <code>list(map(str.upper, palabras))</code> equivale a
<code>[p.upper() for p in palabras]</code>. En general, las comprensiones se leen mejor.</p>

<p><b>Cuándo usarlas.</b> Las comprensiones brillan para transformaciones simples y directas: hacen
el código más corto y expresivo. Pero si la lógica es compleja (varias condiciones, cálculos largos),
un bucle <code>for</code> tradicional será más legible. La regla de oro: <b>si no se entiende de un
vistazo, usa un bucle</b>. La claridad siempre gana.</p>

<p><b>Conexión con datos.</b> Estas ideas son el antecedente directo de las operaciones vectorizadas
de pandas: cuando escribes <code>datos["ventas"] * 1.19</code>, en el fondo estás transformando toda
una columna a la vez, la misma idea que una comprensión pero aún más eficiente.</p>
""",
        "examples": [
            {
                "title": "Comprensión de lista básica",
                "explain": "Construye una lista nueva aplicando una operación a cada elemento.",
                "code": 'numeros = [1, 2, 3, 4, 5]\ncuadrados = [n ** 2 for n in numeros]\nprint(cuadrados)',
            },
            {
                "title": "Con condición (filtro)",
                "explain": "El <code>if</code> al final deja solo los elementos que cumplen la condición.",
                "code": 'numeros = [4, 7, 10, 3, 8, 1]\npares = [n for n in numeros if n % 2 == 0]\nprint("pares:", pares)',
            },
            {
                "title": "Transformar texto",
                "explain": "Aplica un método a cada elemento de una lista de textos.",
                "code": 'palabras = ["datos", "python", "análisis"]\nmayus = [p.upper() for p in palabras]\nlargos = [len(p) for p in palabras]\nprint(mayus)\nprint(largos)',
            },
            {
                "title": "Comprensión de diccionario",
                "explain": "Construye un diccionario clave → valor en una línea.",
                "code": 'palabras = ["pan", "leche", "café"]\nlargos = {p: len(p) for p in palabras}\nprint(largos)',
            },
            {
                "title": "map y filter",
                "explain": "Formas clásicas equivalentes a una comprensión.",
                "code": 'numeros = [1, 2, 3, 4, 5, 6]\ndobles = list(map(lambda x: x * 2, numeros))\nmayores = list(filter(lambda x: x > 3, numeros))\nprint("dobles:", dobles)\nprint("mayores a 3:", mayores)',
            },
            {
                "title": "Comprensión aplicada a datos",
                "explain": "Genera una nueva lista a partir de una columna, filtrando y transformando.",
                "code": 'altas = [v for v in datos["ventas"] if v > 100]\nprint("ventas > 100:", altas)\nprint("con IVA:", [round(v * 1.19) for v in altas])',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Con una comprensión, crea la lista de los cubos (<code>n**3</code>) de <code>range(1, 6)</code>.",
            "Filtra con una comprensión los números mayores a 5 de <code>[2, 8, 4, 10, 1, 7]</code>.",
            "Crea una lista con la longitud de cada palabra en <code>[\"casa\", \"sol\", \"mar\"]</code>.",
            "Con una comprensión, duplica solo los números impares de <code>[1, 2, 3, 4, 5]</code>.",
            "Crea un diccionario que asocie cada número del 1 al 5 con su cuadrado.",
            "Usa <code>filter()</code> para quedarte con las notas de <code>notas</code> que sean &gt;= 5.",
            "A partir de <code>datos[\"ventas\"]</code>, crea una lista con <code>\"alta\"</code>/<code>\"baja\"</code> según superen 100.",
            "Con una comprensión, pasa a mayúsculas la lista <code>[\"norte\", \"sur\", \"centro\"]</code>.",
            "Crea una lista con los números de <code>range(1, 21)</code> que sean divisibles por 3.",
        ],
    },

    # ============================================================ CAP 12
    {
        "num": 12,
        "slug": "errores-archivos",
        "code": "leccion_12",
        "title": "Errores y archivos",
        "subtitle": "Manejar errores con try/except y leer/escribir archivos",
        "apunte": "Lección 12 - Errores y archivos",
        "concepts": [
            ("Excepción", "Un error que ocurre durante la ejecución y detiene el programa si no se maneja."),
            ("Traceback", "El mensaje de error: indica el tipo, la descripción y la línea donde ocurrió. Se lee de abajo hacia arriba."),
            ("try / except", "<code>try</code> intenta ejecutar; <code>except</code> captura el error y evita que el programa se caiga."),
            ("Tipos de error", "<code>ValueError</code>, <code>KeyError</code>, <code>ZeroDivisionError</code>, <code>FileNotFoundError</code>…"),
            ("finally", "Bloque que se ejecuta siempre, haya o no error (por ejemplo, para cerrar recursos)."),
            ("open()", "Abre un archivo para leer (<code>\"r\"</code>) o escribir (<code>\"w\"</code>)."),
            ("with", "<b>Context manager</b>: abre el archivo y lo cierra solo al terminar. La forma recomendada."),
            (".get() en dict", "Acceso seguro a un diccionario: devuelve <code>None</code> (o un valor) si la clave no existe, sin error."),
        ],
        "theory": """
<p>Los <b>errores</b> son parte normal de programar, y más aún al trabajar con datos reales, que
suelen venir incompletos o mal formados. Un buen programa no evita todos los errores: los
<b>anticipa</b> y los <b>maneja</b> con elegancia en lugar de caerse.</p>

<p><b>Leer un error (traceback).</b> Cuando algo falla, Python muestra un <b>traceback</b>: un
mensaje que indica el <b>tipo</b> de error, una <b>descripción</b> y la <b>línea</b> donde ocurrió. Se
lee de <b>abajo hacia arriba</b>: la última línea es la más importante. Aprender a leerlo es la
habilidad de depuración más valiosa. Por ejemplo, <code>ValueError: invalid literal for int()</code>
te dice que intentaste convertir a número algo que no lo era.</p>

<p><b>try / except.</b> Para que un error no detenga el programa, se envuelve el código riesgoso en
un bloque <code>try</code>, y se captura el fallo en un <code>except</code>. Así puedes mostrar un
mensaje amable o usar un valor por defecto en lugar de estrellarte. Conviene capturar el <b>tipo
específico</b> de error (<code>except ValueError:</code>) para no ocultar problemas inesperados.</p>

<p><b>else y finally.</b> Un <code>try</code> puede llevar un <code>else</code> (código que corre solo
si <b>no</b> hubo error) y un <code>finally</code> (código que corre <b>siempre</b>, haya error o no).
<code>finally</code> es útil para liberar recursos, como cerrar un archivo.</p>

<p><b>Archivos: abrir, leer y escribir.</b> La función <code>open()</code> abre un archivo indicando
el <b>modo</b>: <code>"r"</code> para leer, <code>"w"</code> para escribir (crea o reemplaza),
<code>"a"</code> para agregar. La forma recomendada es con <code>with</code>, un <b>context
manager</b> que <b>cierra el archivo automáticamente</b> al terminar, incluso si hay un error:
<code>with open("datos.txt", "w") as f: ...</code>. Dentro escribes con <code>f.write()</code> o lees
con <code>f.read()</code> / recorriendo línea a línea.</p>

<p><b>El puente hacia pandas.</b> En la práctica, para datos tabulares casi nunca abrirás archivos a
mano: usarás <code>pd.read_csv()</code> o <code>pd.read_excel()</code>, que ya viste. Pero entender
<code>open</code> y <code>with</code> es importante para archivos de texto, logs, configuraciones y
para comprender qué hace pandas por debajo.</p>

<p><b>Acceso seguro a diccionarios.</b> Un error muy común es <code>KeyError</code>: pedir una clave
que no existe. El método <code>.get()</code> lo evita: <code>persona.get("email", "sin correo")</code>
devuelve un valor por defecto en vez de fallar. Programar a la defensiva ahorra muchos dolores de
cabeza con datos incompletos.</p>
""",
        "examples": [
            {
                "title": "try / except básico",
                "explain": "Intentamos convertir un texto a número; si falla, avisamos en lugar de caernos.",
                "code": 'texto = "abc"\ntry:\n    numero = int(texto)\n    print("convertido:", numero)\nexcept ValueError:\n    print("No se pudo convertir", repr(texto), "a número")',
            },
            {
                "title": "Capturar el error correcto",
                "explain": "Cada tipo de error se captura por su nombre. Aquí, una división por cero.",
                "code": 'def dividir(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return "no se puede dividir por cero"\n\nprint(dividir(10, 2))\nprint(dividir(10, 0))',
            },
            {
                "title": "else y finally",
                "explain": "<code>else</code> corre si no hubo error; <code>finally</code> corre siempre.",
                "code": 'try:\n    valor = int("42")\nexcept ValueError:\n    print("error")\nelse:\n    print("todo bien, valor =", valor)\nfinally:\n    print("proceso terminado")',
            },
            {
                "title": "Escribir y leer un archivo",
                "explain": "Con <code>with</code> el archivo se cierra solo. Escribimos y luego leemos.",
                "code": 'with open("/tmp/notas.txt", "w") as f:\n    f.write("Ana,6.5\\n")\n    f.write("Luis,5.0\\n")\n\nwith open("/tmp/notas.txt", "r") as f:\n    contenido = f.read()\nprint(contenido)',
            },
            {
                "title": "Leer línea por línea",
                "explain": "Recorrer un archivo es como recorrer una lista de líneas.",
                "code": 'with open("/tmp/notas.txt", "w") as f:\n    f.write("norte\\nsur\\ncentro\\n")\n\nwith open("/tmp/notas.txt", "r") as f:\n    for linea in f:\n        print("región:", linea.strip())',
            },
            {
                "title": "Acceso seguro a un diccionario",
                "explain": "<code>.get()</code> evita el <code>KeyError</code> cuando la clave puede faltar.",
                "code": 'persona = {"nombre": "Ana", "edad": 30}\nprint(persona.get("email", "sin correo"))\nprint(persona.get("nombre", "desconocido"))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Con <code>try/except</code>, intenta convertir <code>\"12x\"</code> a entero y muestra un mensaje si falla.",
            "Escribe una función que divida dos números y capture la división por cero.",
            "Provoca un <code>KeyError</code> pidiendo una clave inexistente y luego resuélvelo con <code>.get()</code>.",
            "Usa <code>try/except/else/finally</code> con la conversión de <code>\"100\"</code> a entero.",
            "Escribe tres líneas en un archivo <code>/tmp/prueba.txt</code> y luego léelo completo.",
            "Recorre ese archivo línea por línea e imprime cada una sin el salto de línea (<code>.strip()</code>).",
            "Crea un diccionario de un producto y usa <code>.get()</code> para pedir un campo que no existe.",
            "Captura un <code>ValueError</code> al hacer <code>int(input_texto)</code> con un texto no numérico definido por ti.",
            "Escribe una función que reciba una lista y devuelva su promedio, capturando el caso de lista vacía (división por cero).",
        ],
    },
]
