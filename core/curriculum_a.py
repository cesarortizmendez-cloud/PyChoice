# -*- coding: utf-8 -*-
"""
PyChoice - Lecciones 1 a 4 (formato capitulo, estilo EstadisticaR).
Teoria extendida (software educativo) + conceptos clave enriquecidos.
Cada consola trae np, pd, plt y los datos de ejemplo `notas` (lista) y
`datos` (DataFrame: mes, region, ventas, unidades).
"""

CHAPTERS_A = [

    # ============================================================ CAP 01
    {
        "num": 1,
        "slug": "instalacion",
        "code": "leccion_01",
        "title": "Instalación y entorno de Python",
        "subtitle": "Qué es Python, cómo instalarlo y dónde escribir tu código",
        "apunte": "Lección 1 - Instalación y entorno",
        "concepts": [
            ("Python", "Lenguaje de programación de propósito general, gratuito y de código abierto. Es <b>interpretado</b> (se ejecuta línea a línea) y de sintaxis muy legible, lo que lo hace ideal para empezar y para el análisis de datos."),
            ("Intérprete", "El programa que lee tu código y lo ejecuta. Cuando escribes <code>python archivo.py</code>, el intérprete traduce y corre cada instrucción."),
            ("Código fuente (.py)", "Un archivo de texto con instrucciones Python. Se edita en cualquier editor y se ejecuta con el intérprete."),
            ("pip", "El gestor de paquetes de Python. Instala librerías desde internet: <code>pip install pandas</code>."),
            ("Entorno virtual", "Una carpeta aislada con su propia versión de Python y librerías, para que cada proyecto no interfiera con otro. Se crea con <code>python -m venv venv</code>."),
            ("IDE / editor", "El lugar donde escribes código. Los favoritos de analistas: <b>VS Code</b>, <b>Jupyter Notebook</b> y <b>Google Colab</b> (en la nube)."),
            ("REPL", "Consola interactiva (Read-Eval-Print-Loop): escribes una orden y ves el resultado al instante. Perfecta para probar ideas."),
            ("Pyodide", "Python compilado a WebAssembly para correr <b>dentro del navegador</b>. Es el motor que usa PyChoice: no necesitas instalar nada para aprender."),
        ],
        "theory": """
<p><b>¿Qué es Python?</b> Python es un lenguaje de programación creado por Guido van Rossum a
comienzos de los años 90. Es <b>gratuito</b>, de <b>código abierto</b> y hoy es el lenguaje más
utilizado del mundo para el <b>análisis de datos</b>, la inteligencia artificial, la automatización
y el desarrollo web. Su gran ventaja es que fue diseñado para ser <b>legible</b>: el código se
parece bastante al lenguaje natural, con pocas reglas de puntuación, lo que reduce la barrera de
entrada para quien recién empieza.</p>

<p><b>Interpretado, no compilado.</b> A diferencia de lenguajes como C o Java, Python es
<b>interpretado</b>: no hay que "traducir" todo el programa antes de ejecutarlo. El
<b>intérprete</b> lee y ejecuta las instrucciones una por una. Esto hace que probar y corregir sea
muy rápido: escribes una línea, la ejecutas y ves de inmediato el resultado.</p>

<p><b>Cómo se instala en tu computador.</b> Se descarga la última versión (siempre <b>Python 3</b>;
la versión 2 quedó obsoleta) desde <a href="https://www.python.org" target="_blank" rel="noopener">python.org</a>.
En Windows es importante marcar la casilla <i>"Add Python to PATH"</i> durante la instalación, para
poder ejecutarlo desde cualquier terminal. Luego, para comprobar que quedó bien instalado, se abre
la terminal (o CMD) y se escribe <code>python --version</code>: debería responder con el número de
versión.</p>

<p><b>pip y las librerías.</b> Junto con Python se instala <b>pip</b>, la herramienta que descarga e
instala <b>librerías</b> (paquetes de código ya hecho). Por ejemplo, <code>pip install pandas numpy
matplotlib</code> instala las tres librerías que más usa un analista. Para mantener ordenado cada
proyecto, se suele crear un <b>entorno virtual</b> (<code>python -m venv venv</code>), una especie de
"caja" aislada con sus propias librerías.</p>

<p><b>¿Dónde se escribe el código?</b> Hay dos formas de trabajar. La <b>consola interactiva</b> o
<b>REPL</b> sirve para probar cosas rápidas: escribes y ves el resultado al instante. Y los
<b>scripts</b> o <b>notebooks</b>, que son archivos donde guardas un programa completo. Los entornos
más populares entre analistas son <b>VS Code</b> (editor potente y gratuito), <b>Jupyter
Notebook</b> (ideal para análisis paso a paso, mezclando código, texto y gráficos) y <b>Google
Colab</b> (Jupyter en la nube, sin instalar nada).</p>

<p><b>Y aquí, en PyChoice.</b> Para <b>aprender</b> no necesitas instalar nada: esta plataforma
ejecuta <b>Python real</b> directamente en tu navegador gracias a <b>Pyodide</b> (Python compilado a
WebAssembly). Escribe en el editor de cada ejemplo, pulsa <b>ejecutar</b> (o <b>Ctrl + Enter</b>) y
verás el resultado al lado. Cuando domines lo básico aquí, instalar Python en tu equipo te resultará
natural.</p>

<p><b>Un consejo para empezar:</b> no tengas miedo a equivocarte. Programar es, en gran parte,
probar, leer el mensaje de error y corregir. Cada error es información, no un fracaso.</p>
""",
        "examples": [
            {
                "title": "Tu primera orden",
                "explain": "El intérprete ejecuta lo que escribes. <code>print()</code> muestra un valor en la salida.",
                "code": 'print("Hola, Python")',
            },
            {
                "title": "Ver la versión de Python",
                "explain": "El módulo <code>sys</code> trae información del intérprete. Así confirmas qué versión estás usando.",
                "code": 'import sys\nprint(sys.version)',
            },
            {
                "title": "Comentarios",
                "explain": "Todo lo que va después de <code>#</code> no se ejecuta. Sirve para explicar tu código a ti y a otros.",
                "code": '# Esto es un comentario y Python lo ignora\nprint("Se ejecuta esta línea")  # comentario al final también',
            },
            {
                "title": "La consola como calculadora",
                "explain": "Puedes operar directamente. Prueba a cambiar los números y volver a ejecutar.",
                "code": 'print(2 + 2)\nprint(10 * 5)\nprint(2 ** 8)   # potencia',
            },
            {
                "title": "Explorar un objeto",
                "explain": "<code>type()</code> dice el tipo de un valor; con <code>dir()</code> ves qué puedes hacer con él. Explorar es parte de programar.",
                "code": 'texto = "datos"\nprint(type(texto))\nprint(len(texto))\nprint(texto.upper())',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Muestra un saludo con tu nombre usando <code>print()</code>.",
            "Averigua e imprime la versión de Python con el módulo <code>sys</code>.",
            "Escribe tres operaciones (suma, multiplicación y potencia), cada una con un comentario que la explique.",
            "Crea una variable con el nombre de tu ciudad y muestra cuántas letras tiene con <code>len()</code>.",
            "Muestra el tipo (<code>type()</code>) de un entero, un decimal y un texto.",
            "Convierte la palabra <code>\"python\"</code> a mayúsculas con <code>.upper()</code> y muéstrala.",
            "Calcula y muestra cuántos segundos tiene un día (24 × 60 × 60).",
            "En una sola línea, muestra tu nombre y tu edad separados por una coma dentro de <code>print()</code>.",
            "Investiga: usa <code>round(3.14159, 2)</code> para redondear y muestra el resultado.",
        ],
    },

    # ============================================================ CAP 02
    {
        "num": 2,
        "slug": "funciones-basicas",
        "code": "leccion_02",
        "title": "Funciones básicas de Python",
        "subtitle": "print, variables, comentarios, texto y concatenación",
        "apunte": "Lección 2 - Fundamentos del lenguaje",
        "concepts": [
            ("print()", "Función que muestra información en la salida. Acepta varios valores separados por coma y opciones como <code>sep</code> y <code>end</code>."),
            ("Variable", "Un nombre que guarda un valor con <code>=</code>. En Python no se declara el tipo: se asigna y listo (<i>tipado dinámico</i>). Por convención se nombran en <code>snake_case</code>."),
            ("Comentario (#)", "Texto que Python ignora. Documenta el <i>por qué</i> del código, no lo obvio. Un buen comentario ahorra horas después."),
            ("str (texto)", "Cadena de caracteres, siempre entre comillas (dobles o simples)."),
            ("int / float", "Números enteros (<code>10</code>) y decimales (<code>9.99</code>). Los decimales usan punto, no coma."),
            ("Concatenar", "Unir textos con <code>+</code>. Solo texto con texto: un número se convierte antes con <code>str()</code>."),
            ("Métodos de texto", "Funciones propias del texto: <code>.upper()</code>, <code>.lower()</code>, <code>.strip()</code> (quita espacios), <code>.replace()</code>. Esenciales para limpiar datos."),
            ("f-string", "Texto que interpola variables entre llaves: <code>f\"Hola {nombre}\"</code>. Admite cálculos y formato dentro de las llaves."),
        ],
        "theory": """
<p>Todo programa, por complejo que sea, se apoya en tres acciones básicas: <b>mostrar</b>
información, <b>guardar</b> datos y <b>operar</b> con ellos. Dominar estas tres es tener la mitad del
camino recorrido.</p>

<p><b>Mostrar: print().</b> La función <code>print()</code> escribe en la salida lo que le pongas
entre paréntesis. Puede recibir <b>varios valores separados por comas</b> (los une con un espacio) y
tiene opciones como <code>sep</code> (qué poner entre valores) y <code>end</code> (con qué terminar
la línea). Es tu ventana constante para ver qué está haciendo el programa.</p>

<p><b>Guardar: variables.</b> Una <b>variable</b> es un nombre que apunta a un valor. Se crea con el
signo <code>=</code> (<code>edad = 27</code>). Una particularidad de Python es el <b>tipado
dinámico</b>: no declaras si algo es número o texto, simplemente lo asignas y Python lo deduce. Los
nombres deben ser descriptivos y por convención se escriben en <code>snake_case</code> (minúsculas y
guion bajo): <code>precio_final</code>, <code>total_ventas</code>.</p>

<p><b>Los tipos básicos.</b> Los datos tienen <b>tipo</b>: <code>int</code> (enteros),
<code>float</code> (decimales, con punto), <code>str</code> (texto, entre comillas) y
<code>bool</code> (<code>True</code>/<code>False</code>). El tipo determina qué operaciones son
válidas: puedes restar dos números, pero no restar dos textos.</p>

<p><b>Trabajar con texto.</b> El texto se puede <b>concatenar</b> (unir) con <code>+</code>, pero
solo texto con texto: si quieres pegar un número, primero lo conviertes con <code>str()</code>. Esta
es una de las primeras trampas típicas: <code>"Edad: " + 30</code> da error, pero
<code>"Edad: " + str(30)</code> funciona. El texto además trae <b>métodos</b> muy útiles al limpiar
datos reales (que suelen venir con espacios, mayúsculas inconsistentes, etc.): <code>.strip()</code>
quita espacios, <code>.upper()</code>/<code>.lower()</code> cambian mayúsculas y
<code>.replace()</code> sustituye texto.</p>

<p><b>La forma moderna: f-strings.</b> Concatenar con <code>+</code> se vuelve engorroso. Los
<b>f-strings</b> (poner una <code>f</code> antes de las comillas) permiten insertar variables entre
llaves de forma legible: <code>f"{nombre} tiene {edad} años"</code>. Y dentro de las llaves puedes
<b>calcular</b> y dar <b>formato</b> (por ejemplo <code>{precio:.2f}</code> para dos decimales, o
<code>{valor:,}</code> para separador de miles). Es la manera recomendada de armar mensajes.</p>

<p><b>Números y operadores.</b> Python opera con <code>+ - * /</code>, además de <code>**</code>
(potencia) y <code>%</code> (resto de la división). Ojo: la división <code>/</code> siempre da un
decimal (<code>float</code>). Para redondear se usa <code>round(valor, decimales)</code>.</p>
""",
        "examples": [
            {
                "title": "print y comentarios",
                "explain": "Muestra texto entre comillas; usa <code>#</code> para comentar.",
                "code": '# mi primer programa\nprint("Aprendiendo Python")\nprint(\'También con comillas simples\')',
            },
            {
                "title": "Variables y tipos",
                "explain": "Guarda valores en variables. El texto lleva comillas; los números no.",
                "code": 'nombre = "Camila"\nedad = 27\naltura = 1.68\nprint(nombre, edad, altura)',
            },
            {
                "title": "Concatenar texto",
                "explain": "Une textos con <code>+</code>. Para unir un número, conviértelo con <code>str()</code>.",
                "code": 'nombre = "Ana"\nedad = 30\nprint("Hola " + nombre)\nprint(nombre + " tiene " + str(edad) + " años")',
            },
            {
                "title": "f-strings: la forma moderna",
                "explain": "Pon una <code>f</code> antes de las comillas y las variables entre llaves. Dentro puedes calcular y dar formato.",
                "code": 'producto = "café"\nprecio = 2990\nprint(f"{producto} cuesta ${precio}")\nprint(f"Con IVA: ${precio * 1.19:.0f}")',
            },
            {
                "title": "Trabajar con texto",
                "explain": "El texto trae métodos para transformarlo, esenciales al limpiar datos.",
                "code": 'ciudad = "  Santiago  "\nprint(ciudad.strip().upper())\nprint("data science".replace("data", "ciencia de"))\nprint(len("análisis"))',
            },
            {
                "title": "Números y operaciones",
                "explain": "Operadores: <code>+ - * /</code>, <code>**</code> (potencia), <code>%</code> (resto). <code>round()</code> redondea.",
                "code": 'print("suma:", 12 + 8)\nprint("división:", 100 / 7)\nprint("redondeada:", round(100 / 7, 2))\nprint("resto:", 17 % 5)',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Crea variables <code>nombre</code> y <code>apellido</code> y muestra el nombre completo concatenando con <code>+</code>.",
            "Con un <code>f-string</code>, muestra un mensaje que incluya un número y un cálculo.",
            "Toma el texto <code>\" Python \"</code>, quítale los espacios y pásalo a mayúsculas.",
            "Calcula el precio final de un producto de $15.000 con 19% de IVA y muéstralo redondeado.",
            "Crea <code>edad</code> (entero), <code>altura</code> (decimal) y <code>nombre</code> (texto) y muestra el tipo de cada una con <code>type()</code>.",
            "Concatena el texto <code>\"Total: \"</code> con el número <code>4500</code> (recuerda usar <code>str()</code>).",
            "Con <code>.replace()</code>, cambia <code>\"gato\"</code> por <code>\"perro\"</code> en la frase <code>\"mi gato es negro\"</code>.",
            "Muestra el resto de <code>100 % 7</code> y la potencia <code>3 ** 4</code> con etiquetas claras.",
            "Con un <code>f-string</code>, muestra el número <code>1234567</code> con separador de miles (<code>{n:,}</code>).",
            "Cuenta las letras de una frase con <code>len()</code> y muéstrala también en minúsculas con <code>.lower()</code>.",
        ],
    },

    # ============================================================ CAP 03
    {
        "num": 3,
        "slug": "librerias",
        "code": "leccion_03",
        "title": "Librerías: Pandas, NumPy y Matplotlib",
        "subtitle": "Qué son las librerías, cómo instalarlas e importarlas",
        "apunte": "Lección 3 - Librerías para datos",
        "concepts": [
            ("Librería / módulo", "Conjunto de funciones ya escritas que amplían Python. Un <i>módulo</i> es un archivo; una <i>librería</i> o paquete agrupa varios."),
            ("Biblioteca estándar", "Módulos que vienen con Python sin instalar nada: <code>math</code>, <code>statistics</code>, <code>random</code>, <code>datetime</code>…"),
            ("PyPI", "El repositorio oficial (Python Package Index) desde donde <code>pip</code> descarga las librerías de terceros."),
            ("pip install", "Instala una librería: <code>pip install pandas numpy matplotlib</code>. Se hace una sola vez por entorno."),
            ("import ... as", "Carga una librería y le da un alias corto: <code>import pandas as pd</code>. También existe <code>from math import sqrt</code>."),
            ("NumPy (np)", "Cálculo numérico con <b>arrays</b>: operaciones sobre muchos números a la vez (vectorizadas), muy rápidas."),
            ("pandas (pd)", "Tablas de datos: <code>Series</code> (una columna) y <code>DataFrame</code> (tabla completa). El corazón del análisis."),
            ("Matplotlib (plt)", "Creación de gráficos: barras, líneas, histogramas, dispersión. El módulo habitual es <code>matplotlib.pyplot</code>."),
        ],
        "theory": """
<p>Python base ya es útil, pero su verdadera potencia para el análisis de datos viene de las
<b>librerías</b>: paquetes de funciones ya escritas y probadas por la comunidad. En lugar de
programar todo desde cero, te "paras sobre hombros de gigantes" y reutilizas trabajo de miles de
personas.</p>

<p><b>Dos tipos de librerías.</b> Están las de la <b>biblioteca estándar</b>, que vienen incluidas
con Python (por ejemplo <code>math</code>, <code>statistics</code>, <code>random</code>,
<code>datetime</code>), y las de <b>terceros</b>, que se descargan desde <b>PyPI</b> (el repositorio
oficial) con <code>pip</code>. Para un analista, las tres imprescindibles son <b>NumPy</b>,
<b>pandas</b> y <b>Matplotlib</b>.</p>

<p><b>Cómo se instalan.</b> En tu computador se instalan una sola vez, desde la terminal:</p>
<p><code>pip install pandas numpy matplotlib</code></p>
<p>Esto las descarga de PyPI y las deja disponibles para tus programas. En PyChoice ya vienen
instaladas y cargadas, así que puedes usarlas de inmediato.</p>

<p><b>Cómo se usan: import.</b> Antes de usar una librería hay que <b>importarla</b>, normalmente al
inicio del programa. La convención es darle un <b>alias</b> corto: <code>import numpy as np</code>,
<code>import pandas as pd</code>, <code>import matplotlib.pyplot as plt</code>. Estos alias
(<code>np</code>, <code>pd</code>, <code>plt</code>) son un estándar universal: los verás en
cualquier tutorial o proyecto del mundo. También puedes importar solo una función:
<code>from math import sqrt</code>.</p>

<p><b>NumPy: cálculo veloz.</b> Su estructura central es el <b>array</b>, parecido a una lista pero
capaz de operar sobre todos sus valores <b>a la vez</b> (lo que se llama <i>vectorización</i>), sin
escribir bucles y con enorme rapidez. <code>ventas * 1.19</code> aplica el IVA a todos los valores
de una sola vez.</p>

<p><b>pandas: la tabla.</b> Aporta dos estructuras: la <b>Series</b> (una columna con etiquetas) y
el <b>DataFrame</b> (una tabla completa, como una hoja de Excel). Casi todo el análisis de datos
consiste en leer datos en un DataFrame, limpiarlos, resumirlos y graficarlos. pandas se apoya en
NumPy por debajo.</p>

<p><b>Matplotlib: los gráficos.</b> Es la librería base para visualizar. Con
<code>matplotlib.pyplot</code> (alias <code>plt</code>) creas barras, líneas, histogramas y nubes de
puntos. Sobre ella se construyen otras más modernas como <b>seaborn</b>. Más adelante también
aparece <b>scikit-learn</b> para modelos de machine learning: todo este conjunto forma el
<i>ecosistema de datos</i> de Python.</p>
""",
        "examples": [
            {
                "title": "Importar con alias",
                "explain": "Se importan una vez al inicio. El alias (<code>np</code>, <code>pd</code>, <code>plt</code>) ahorra escritura.",
                "code": 'import numpy as np\nimport pandas as pd\nprint("numpy:", np.__version__)\nprint("pandas:", pd.__version__)',
            },
            {
                "title": "NumPy: cálculo con arreglos",
                "explain": "Un <code>array</code> de NumPy opera sobre todos sus valores a la vez (vectorizado), sin bucles.",
                "code": 'import numpy as np\nventas = np.array([120, 95, 130, 110, 88])\nprint("media:", ventas.mean())\nprint("desv:", round(ventas.std(), 2))\nprint("con IVA:", ventas * 1.19)',
            },
            {
                "title": "pandas: crear una tabla",
                "explain": "Un <code>DataFrame</code> es una tabla: columnas con nombre y filas. Es la estructura clave del analista.",
                "code": 'import pandas as pd\ntabla = pd.DataFrame({\n    "producto": ["pan", "leche", "café"],\n    "precio": [990, 1200, 2990],\n})\nprint(tabla)',
            },
            {
                "title": "Matplotlib: un gráfico",
                "explain": "Con <code>plt</code> creas gráficos. Aquí, un gráfico de barras. Pulsa ejecutar y míralo abajo.",
                "code": 'import matplotlib.pyplot as plt\nproductos = ["pan", "leche", "café"]\nprecios = [990, 1200, 2990]\nplt.bar(productos, precios, color="#00ff9c")\nplt.title("Precios")\nplt.show()',
            },
            {
                "title": "Datos de ejemplo listos",
                "explain": "En PyChoice ya tienes el DataFrame <code>datos</code> cargado para practicar. Prueba también <b>cargar excel</b>.",
                "code": 'print(datos)\nprint("\\nColumnas:", list(datos.columns))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Importa NumPy y crea un array con 5 números; muestra su media y su máximo.",
            "Crea un <code>DataFrame</code> con dos columnas (nombre y edad) de 3 personas.",
            "Grafica con barras los precios de tres productos que inventes.",
            "Muestra las columnas y el número de filas del DataFrame <code>datos</code>.",
            "Con NumPy, multiplica un array de 5 números por 2 y muéstralo (vectorización, sin bucles).",
            "Importa el módulo <code>math</code> y calcula la raíz cuadrada de 144 con <code>math.sqrt()</code>.",
            "Crea un <code>DataFrame</code> de 3 productos con columnas <code>precio</code> y <code>stock</code>, y muéstralo.",
            "Grafica un histograma de la lista <code>notas</code> con <code>plt.hist()</code>.",
            "Con NumPy, obtén la desviación estándar (<code>.std()</code>) de un array de tu elección.",
        ],
    },

    # ============================================================ CAP 04
    {
        "num": 4,
        "slug": "condicionales",
        "code": "leccion_04",
        "title": "Funciones condicionales (if, elif, else)",
        "subtitle": "Comparar, decidir y ejecutar según se cumpla una condición",
        "apunte": "Lección 4 - Condicionales",
        "concepts": [
            ("bool", "Tipo lógico con dos valores: <code>True</code> y <code>False</code>. Es lo que devuelve toda comparación."),
            ("Comparadores", "<code>==</code> (igual), <code>!=</code> (distinto), <code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, <code>&lt;=</code>. Ojo: <code>==</code> compara, <code>=</code> asigna."),
            ("if", "Ejecuta un bloque de código solo si la condición es verdadera."),
            ("elif", "\"else if\": añade condiciones intermedias. Se evalúan en orden y gana la primera que se cumple."),
            ("else", "El caso restante: se ejecuta cuando ninguna condición anterior se cumplió."),
            ("and / or / not", "Combinan condiciones: <code>and</code> exige ambas, <code>or</code> al menos una, <code>not</code> invierte."),
            ("Sangría (indentación)", "Los 4 espacios al inicio de línea indican qué código está <i>dentro</i> del if. En Python la sangría define la estructura; no es opcional."),
            ("Dos puntos (:)", "Toda estructura (if, for, while, def) termina su línea de encabezado con <code>:</code> y sigue con un bloque sangrado."),
        ],
        "theory": """
<p>Analizar datos casi siempre desemboca en <b>decidir</b>: ¿aprueba o reprueba?, ¿es cliente
frecuente o no?, ¿supera la meta? Las estructuras <b>condicionales</b> permiten que el programa tome
caminos distintos según los datos.</p>

<p><b>Todo parte de un booleano.</b> Una <b>comparación</b> entre dos valores devuelve un
<code>bool</code>: <code>True</code> o <code>False</code>. Por ejemplo <code>10 &gt; 5</code> es
<code>True</code> y <code>3 == 4</code> es <code>False</code>. Los comparadores son <code>==</code>
(igual a), <code>!=</code> (distinto de), <code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code> y
<code>&lt;=</code>. <b>Cuidado con una confusión clásica:</b> <code>=</code> <i>asigna</i> un valor a
una variable, mientras que <code>==</code> <i>compara</i>. Usar uno por otro es de los errores más
comunes al empezar.</p>

<p><b>La estructura if.</b> El <code>if</code> ejecuta un bloque <b>solo si</b> la condición es
verdadera. Su forma es: la palabra <code>if</code>, la condición, dos puntos <code>:</code>, y en la
línea siguiente el bloque <b>sangrado</b> (con 4 espacios). Ese sangrado no es decoración: en Python
la <b>indentación</b> es la que define qué instrucciones están dentro del <code>if</code> y cuáles
fuera. Un error de sangría cambia el significado del programa o produce un error.</p>

<p><b>else y elif.</b> Con <code>else</code> defines el caso contrario (lo que se hace cuando la
condición <i>no</i> se cumple). Con <code>elif</code> (contracción de "else if") añades casos
intermedios: Python los evalúa de arriba hacia abajo y ejecuta el <b>primero</b> que resulte
verdadero, ignorando el resto. Es la manera de clasificar en varias categorías (por ejemplo: frío /
templado / calor).</p>

<p><b>Combinar condiciones.</b> A menudo una decisión depende de varias cosas a la vez. Los
operadores lógicos las combinan: <code>and</code> exige que <b>ambas</b> se cumplan, <code>or</code>
que se cumpla <b>al menos una</b>, y <code>not</code> <b>invierte</b> el resultado. Por ejemplo,
"tiene acceso si es mayor de edad <b>y</b> es socio": <code>edad &gt;= 18 and socio</code>.</p>

<p><b>Por qué importa en datos.</b> Las condiciones son la base del <b>filtrado</b> (quedarse con
las filas que cumplen una regla), de la <b>clasificación</b> (etiquetar cada dato) y de la toma de
decisiones automática. En las próximas lecciones combinarás <code>if</code> con bucles y con pandas
para analizar tablas completas. Aquí sientas esa base.</p>

<p><b>Errores típicos a vigilar:</b> olvidar los dos puntos <code>:</code>, mezclar
<code>=</code> con <code>==</code>, y una indentación inconsistente (mezclar espacios y tabulaciones).
Lee siempre el mensaje de error: suele indicar la línea exacta del problema.</p>
""",
        "examples": [
            {
                "title": "Comparaciones producen booleanos",
                "explain": "Antes de decidir, conviene ver qué devuelve una comparación.",
                "code": 'print(10 > 5)\nprint(3 == 4)\nprint("a" != "b")',
            },
            {
                "title": "if / else",
                "explain": "Si la condición es verdadera, corre el primer bloque; si no, el <code>else</code>.",
                "code": 'nota = 5.2\nif nota >= 4:\n    print("Aprobado")\nelse:\n    print("Reprobado")',
            },
            {
                "title": "if / elif / else",
                "explain": "Encadena varios casos. Python evalúa de arriba hacia abajo y ejecuta el primero que se cumpla.",
                "code": 'temp = 14\nif temp >= 30:\n    print("Calor")\nelif temp >= 15:\n    print("Templado")\nelse:\n    print("Frío")',
            },
            {
                "title": "Combinar condiciones",
                "explain": "<code>and</code> exige ambas; <code>or</code>, al menos una; <code>not</code> invierte.",
                "code": 'edad = 20\nsocio = True\nif edad >= 18 and socio:\n    print("Acceso permitido")\nelse:\n    print("Acceso denegado")',
            },
            {
                "title": "Decidir con datos",
                "explain": "Calculamos el promedio de <code>notas</code> y decidimos según una meta.",
                "code": 'promedio = sum(notas) / len(notas)\nprint("promedio:", round(promedio, 2))\nif promedio >= 5:\n    print("Buen rendimiento")\nelse:\n    print("A reforzar")',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Define una variable <code>edad</code> e imprime si la persona es mayor o menor de edad.",
            "Clasifica un número en positivo, negativo o cero con <code>if/elif/else</code>.",
            "Con <code>and</code>, decide si un alumno pasa: nota &gt;= 4 y asistencia &gt;= 0.75.",
            "Calcula el promedio de <code>datos['ventas']</code> y decide si supera 100.",
            "Clasifica una nota en <code>reprobado</code> (&lt; 4), <code>suficiente</code> (4 a 5.5) o <code>bueno</code> (&gt;= 5.5) con <code>if/elif/else</code>.",
            "Dado un número, imprime <code>\"par\"</code> o <code>\"impar\"</code> usando el resto <code>%</code>.",
            "Con <code>or</code>, decide si un día es fin de semana (<code>dia == \"sábado\" or dia == \"domingo\"</code>).",
            "Compara dos precios y muestra cuál es más caro, o si son iguales.",
            "Pide un semáforo: según el valor <code>\"rojo\"</code>, <code>\"amarillo\"</code> o <code>\"verde\"</code>, imprime la acción correspondiente.",
        ],
    },
]
