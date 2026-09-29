# -*- coding: utf-8 -*-
"""
PyChoice - Modulo D: Manipulacion de datos (Lecciones 13 a 17).
Formato capitulo. Teoria extendida + 8 conceptos + ejemplos ejecutables +
ejercicios. En cada consola: np, pd, plt y los datos de ejemplo `notas`
(lista) y `datos` (DataFrame: mes, region, ventas, unidades).
"""

CHAPTERS_D = [

    # ============================================================ CAP 13
    {
        "num": 13,
        "slug": "numpy",
        "code": "leccion_13",
        "title": "NumPy a fondo",
        "subtitle": "Arrays, operaciones vectorizadas y cálculo numérico rápido",
        "apunte": "Lección 13 - NumPy",
        "concepts": [
            ("array (ndarray)", "La estructura central de NumPy: una rejilla de valores <b>del mismo tipo</b>, mucho más rápida que una lista para cálculos."),
            ("dtype", "El tipo de dato del array (int64, float64…). Todos los elementos comparten el mismo tipo."),
            ("shape", "La forma del array: cuántas filas y columnas. <code>reshape()</code> la reorganiza."),
            ("Vectorización", "Operar sobre todo el array de una vez (<code>a * 2</code>), sin bucles y a gran velocidad."),
            ("Indexado y slicing", "Acceso por posición, igual que en listas, pero también en 2D: <code>a[fila, columna]</code>."),
            ("Máscara booleana", "Filtrar con una condición: <code>a[a &gt; 5]</code> deja solo los que la cumplen."),
            ("axis", "El eje sobre el que se calcula: <code>axis=0</code> por columnas, <code>axis=1</code> por filas."),
            ("Broadcasting", "NumPy ajusta automáticamente formas distintas para operar (un array con un escalar, por ejemplo)."),
        ],
        "theory": """
<p><b>NumPy</b> (Numerical Python) es la librería sobre la que se construye casi todo el ecosistema de
datos de Python, incluido pandas. Su aporte es el <b>array</b> (o <code>ndarray</code>): una
colección de números <b>del mismo tipo</b>, organizada en una o varias dimensiones, diseñada para el
cálculo numérico masivo y veloz.</p>

<p><b>Array vs lista.</b> Una lista de Python puede mezclar tipos y es flexible, pero lenta para
cálculos. Un array de NumPy es <b>homogéneo</b> (un solo <code>dtype</code>) y guarda los datos de
forma compacta, lo que permite operar sobre millones de números en un instante. Es la diferencia entre
sumar a mano y usar una calculadora industrial.</p>

<p><b>Vectorización: el superpoder.</b> Con NumPy no necesitas bucles para operar sobre muchos
valores: <code>ventas * 1.19</code> aplica el IVA a <b>todo</b> el array a la vez. Esto se llama
<b>vectorización</b>, y además de ser más corto de escribir, es órdenes de magnitud más rápido que un
<code>for</code>. Las funciones estadísticas (<code>mean</code>, <code>std</code>, <code>sum</code>,
<code>min</code>, <code>max</code>) vienen incorporadas.</p>

<p><b>Forma e indexado.</b> Cada array tiene una <b>forma</b> (<code>shape</code>): un array 1D es una
fila; uno 2D es una tabla de filas y columnas. <code>reshape()</code> reorganiza esa forma. El acceso
por posición funciona como en listas, y en 2D se indica <code>array[fila, columna]</code>; los cortes
(<code>slicing</code>) también aplican.</p>

<p><b>Máscaras booleanas.</b> Igual que en pandas, puedes filtrar con una condición:
<code>a[a &gt; 50]</code> devuelve solo los elementos que cumplen. Por dentro, la condición crea un
array de <code>True</code>/<code>False</code> que selecciona los valores. Es la base del filtrado de
datos.</p>

<p><b>axis y broadcasting.</b> En arrays 2D, muchas operaciones aceptan un <b>eje</b>:
<code>a.sum(axis=0)</code> suma por columnas y <code>axis=1</code> por filas. Y el
<b>broadcasting</b> permite operar arrays de formas distintas (por ejemplo, restar a cada fila un
vector) sin escribir bucles: NumPy "estira" automáticamente las dimensiones compatibles. Estas ideas
reaparecen constantemente en pandas, porque una columna de un DataFrame es, en el fondo, un array de
NumPy.</p>
""",
        "examples": [
            {
                "title": "Crear arrays y sus atributos",
                "explain": "Un array se crea desde una lista. <code>shape</code> y <code>dtype</code> lo describen.",
                "code": 'import numpy as np\na = np.array([120, 95, 130, 110, 88])\nprint("array:", a)\nprint("shape:", a.shape, "| dtype:", a.dtype)\nprint("desde rango:", np.arange(0, 10, 2))\nprint("ceros:", np.zeros(3))',
            },
            {
                "title": "Operaciones vectorizadas",
                "explain": "Operas sobre todo el array a la vez, sin bucles, y con funciones incorporadas.",
                "code": 'import numpy as np\nventas = np.array([120, 95, 130, 110, 88])\nprint("con IVA:", ventas * 1.19)\nprint("media:", ventas.mean())\nprint("desv:", round(ventas.std(), 2))\nprint("total:", ventas.sum())',
            },
            {
                "title": "Indexado y slicing",
                "explain": "Acceso por posición en 1D y en 2D (<code>[fila, columna]</code>).",
                "code": 'import numpy as np\nm = np.array([[1, 2, 3],\n              [4, 5, 6]])\nprint("elemento [0,2]:", m[0, 2])\nprint("primera fila:", m[0])\nprint("segunda columna:", m[:, 1])',
            },
            {
                "title": "Máscara booleana",
                "explain": "Filtra los elementos que cumplen una condición.",
                "code": 'import numpy as np\na = np.array([120, 95, 130, 110, 88])\nprint("mayores a 100:", a[a > 100])\nprint("¿cuáles?:", a > 100)',
            },
            {
                "title": "reshape y axis",
                "explain": "Reorganiza la forma y calcula por columnas (axis=0) o filas (axis=1).",
                "code": 'import numpy as np\na = np.arange(1, 7).reshape(2, 3)\nprint(a)\nprint("suma por columna:", a.sum(axis=0))\nprint("suma por fila:", a.sum(axis=1))',
            },
            {
                "title": "Broadcasting",
                "explain": "NumPy ajusta formas distintas para operar sin bucles.",
                "code": 'import numpy as np\nprecios = np.array([100, 200, 300])\nprint("+ 10%:", precios * 1.1)\nmatriz = np.array([[1, 2, 3], [4, 5, 6]])\nprint("resta vector:\\n", matriz - np.array([1, 1, 1]))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Crea un array con <code>np.arange(1, 11)</code> y muestra su media y su suma.",
            "Crea un array de 5 números y multiplícalo por 3 (vectorización).",
            "De <code>[10, 25, 3, 40, 8]</code>, usa una máscara para quedarte con los mayores a 10.",
            "Crea una matriz 3×3 con <code>np.arange(1,10).reshape(3,3)</code> y muéstrala.",
            "Suma esa matriz por columnas (<code>axis=0</code>) y por filas (<code>axis=1</code>).",
            "Calcula la desviación estándar de un array de tu elección con <code>.std()</code>.",
            "Con broadcasting, resta 5 a cada elemento de un array.",
            "Crea un array de ceros de tamaño 4 con <code>np.zeros(4)</code>.",
            "Averigua el <code>shape</code> y el <code>dtype</code> de <code>np.array([1.5, 2.5, 3.5])</code>.",
        ],
    },

    # ============================================================ CAP 14
    {
        "num": 14,
        "slug": "seleccion-pandas",
        "code": "leccion_14",
        "title": "Selección en pandas: loc e iloc",
        "subtitle": "Elegir filas y columnas con precisión, por etiqueta o por posición",
        "apunte": "Lección 14 - Selección avanzada",
        "concepts": [
            ("Índice (index)", "La etiqueta de cada fila. Por defecto es 0, 1, 2…, pero puede ser un texto o una fecha."),
            (".loc", "Selección por <b>etiqueta</b>: <code>df.loc[fila, columna]</code>. Incluye ambos extremos en los rangos."),
            (".iloc", "Selección por <b>posición</b> (número): <code>df.iloc[0, 2]</code>. Excluye el extremo final, como el slicing."),
            ("Seleccionar columnas", "Una con <code>df['col']</code>; varias con una lista <code>df[['a','b']]</code>."),
            ("Filtro booleano", "Filas que cumplen una condición: <code>df[df['x'] &gt; 5]</code>."),
            ("Condiciones múltiples", "Se combinan con <code>&amp;</code> (y) y <code>|</code> (o), cada una entre paréntesis."),
            ("set_index()", "Convierte una columna en el índice de la tabla, para acceder por esa etiqueta."),
            (".at / .iat", "Acceso rápido a <b>un</b> valor por etiqueta (<code>.at</code>) o posición (<code>.iat</code>)."),
        ],
        "theory": """
<p>Seleccionar exactamente las filas y columnas que necesitas es la habilidad más usada al trabajar
con pandas. Hay dos formas principales, y entender su diferencia evita muchos errores:
<code>.loc</code> y <code>.iloc</code>.</p>

<p><b>El índice.</b> Cada fila de un DataFrame tiene una <b>etiqueta</b> en su <b>índice</b>. Por
defecto es un número (0, 1, 2…), pero puede ser un nombre, un código o una fecha. Entender que hay una
"etiqueta de fila" es la clave para dominar la selección.</p>

<p><b>.iloc — por posición.</b> Usa <b>números de posición</b>, como en las listas:
<code>df.iloc[0]</code> es la primera fila, <code>df.iloc[0, 2]</code> el valor de la primera fila y
tercera columna, y <code>df.iloc[0:3]</code> las tres primeras filas (excluye el índice final, igual
que el slicing normal).</p>

<p><b>.loc — por etiqueta.</b> Usa las <b>etiquetas</b> del índice y los <b>nombres</b> de las
columnas: <code>df.loc[0, "ventas"]</code>. Con <code>.loc</code>, los rangos <b>incluyen</b> ambos
extremos (<code>df.loc[0:3]</code> trae 4 filas). Es la forma más legible cuando trabajas con nombres
de columna.</p>

<p><b>Filtrar filas.</b> El filtrado booleano que ya conoces (<code>df[df["ventas"] &gt; 100]</code>)
también se combina con <code>.loc</code> para elegir a la vez filas y columnas:
<code>df.loc[df["ventas"] &gt; 100, ["mes", "ventas"]]</code>. Y varias condiciones se unen con
<code>&amp;</code> (y) y <code>|</code> (o), <b>cada una entre paréntesis</b>: es un error muy común
olvidarlos.</p>

<p><b>Cambiar el índice.</b> Con <code>set_index("columna")</code> conviertes una columna en el índice
de la tabla, lo que permite acceder a las filas por esa etiqueta (por ejemplo, por mes o por código de
producto) con <code>.loc</code>. Es útil cuando cada fila tiene un identificador natural.</p>

<p><b>Un valor puntual.</b> Cuando solo quieres <b>un</b> dato, <code>.at</code> (por etiqueta) e
<code>.iat</code> (por posición) son la forma más rápida. En resumen: <code>iloc</code> para pensar en
<b>posiciones</b>, <code>loc</code> para pensar en <b>nombres</b>. Con esos dos cubres casi toda la
selección.</p>
""",
        "examples": [
            {
                "title": "iloc: por posición",
                "explain": "Números de fila y columna, como en una lista.",
                "code": 'print("primera fila:\\n", datos.iloc[0])\nprint("\\nvalor [0,2]:", datos.iloc[0, 2])\nprint("\\nprimeras 3 filas:\\n", datos.iloc[0:3])',
            },
            {
                "title": "loc: por etiqueta",
                "explain": "Nombres de columna; con el índice por defecto, la etiqueta de fila es el número.",
                "code": 'print(datos.loc[0, "ventas"])\nprint(datos.loc[0:2, ["mes", "ventas"]])',
            },
            {
                "title": "Filtro booleano",
                "explain": "Filas que cumplen una condición sobre una columna.",
                "code": 'altas = datos[datos["ventas"] > 100]\nprint(altas)',
            },
            {
                "title": "Condiciones múltiples",
                "explain": "Se combinan con & (y) / | (o); cada condición entre paréntesis.",
                "code": 'sel = datos[(datos["ventas"] > 100) & (datos["region"] == "norte")]\nprint(sel)',
            },
            {
                "title": "loc con filtro y columnas",
                "explain": "Elegir filas por condición y quedarte con ciertas columnas.",
                "code": 'print(datos.loc[datos["ventas"] > 100, ["mes", "region", "ventas"]])',
            },
            {
                "title": "set_index: acceder por etiqueta",
                "explain": "Convertimos 'mes' en índice para acceder por el nombre del mes.",
                "code": 'porMes = datos.set_index("mes")\nprint(porMes.loc["mar"])',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Muestra la segunda fila de <code>datos</code> con <code>iloc</code>.",
            "Con <code>iloc</code>, muestra el valor de la fila 0 y la columna 2.",
            "Con <code>loc</code>, muestra las columnas <code>mes</code> y <code>region</code> de las 3 primeras filas.",
            "Filtra las filas con <code>unidades &gt;= 10</code>.",
            "Filtra las filas con <code>ventas &gt; 100</code> <b>y</b> <code>region == \"sur\"</code>.",
            "Filtra las filas de región <code>\"norte\"</code> <b>o</b> <code>\"centro\"</code> con <code>|</code>.",
            "Convierte <code>mes</code> en índice con <code>set_index()</code> y accede a la fila <code>\"ene\"</code>.",
            "Con <code>loc</code> y un filtro, muestra solo <code>mes</code> y <code>ventas</code> de las ventas sobre 100.",
            "Muestra las últimas 2 filas de <code>datos</code> con <code>iloc[-2:]</code>.",
        ],
    },

    # ============================================================ CAP 15
    {
        "num": 15,
        "slug": "limpieza",
        "code": "leccion_15",
        "title": "Limpieza de datos",
        "subtitle": "Faltantes, duplicados, tipos y texto: preparar datos reales",
        "apunte": "Lección 15 - Limpieza de datos",
        "concepts": [
            ("Valor faltante (NaN)", "Una celda vacía. pandas la representa como <code>NaN</code> (Not a Number)."),
            ("isna() / notna()", "Detectan faltantes: devuelven True/False por celda. <code>df.isna().sum()</code> cuenta por columna."),
            ("dropna()", "Elimina filas (o columnas) con faltantes."),
            ("fillna()", "Rellena los faltantes con un valor (0, la media, un texto…)."),
            ("duplicated() / drop_duplicates()", "Detectan y eliminan filas repetidas."),
            ("astype()", "Convierte el tipo de una columna: <code>df['x'].astype(int)</code>."),
            (".str", "Accesor para limpiar texto en una columna: <code>df['c'].str.strip().str.lower()</code>."),
            ("rename() / replace()", "Renombrar columnas y sustituir valores concretos."),
        ],
        "theory": """
<p>Hay una frase famosa en el oficio: el <b>80% del trabajo de un analista es limpiar datos</b>. Los
datos reales llegan sucios: celdas vacías, filas repetidas, números guardados como texto, mayúsculas
inconsistentes, espacios sobrantes. Antes de analizar, hay que <b>preparar</b>. pandas ofrece
herramientas para cada caso.</p>

<p><b>Valores faltantes.</b> Una celda vacía se representa como <code>NaN</code>. Lo primero es
<b>detectarlos</b>: <code>df.isna()</code> devuelve True/False por celda, y <code>df.isna().sum()</code>
cuenta cuántos hay por columna. Luego decides qué hacer: <code>dropna()</code> <b>elimina</b> las
filas con faltantes (útil si son pocas), o <code>fillna(valor)</code> los <b>rellena</b> (con un 0, la
media de la columna, o un texto como "desconocido"). No hay una receta única: depende del contexto.</p>

<p><b>Duplicados.</b> A veces la misma fila aparece varias veces (por errores de carga o de captura).
<code>df.duplicated()</code> las marca y <code>df.drop_duplicates()</code> las elimina, dejando una
sola copia. Siempre conviene revisar si hay duplicados antes de contar o sumar, para no inflar los
resultados.</p>

<p><b>Tipos incorrectos.</b> Es muy común que una columna numérica llegue como <b>texto</b> (por
ejemplo, "1.990" con separadores). Mientras siga siendo texto no puedes calcular con ella. Con
<code>astype()</code> conviertes el tipo: <code>df["precio"].astype(int)</code>. A veces hay que
limpiar el texto primero (quitar símbolos) y luego convertir.</p>

<p><b>Limpiar texto.</b> Las columnas de texto se limpian con el accesor <code>.str</code>, que aplica
métodos de texto a toda la columna: <code>df["ciudad"].str.strip().str.lower()</code> quita espacios y
pasa a minúsculas de una vez. Es la forma de estandarizar categorías (que "Norte", "norte" y
" NORTE " cuenten como lo mismo).</p>

<p><b>Renombrar y reemplazar.</b> <code>rename()</code> cambia nombres de columnas para que sean
claros y consistentes, y <code>replace()</code> sustituye valores concretos (por ejemplo, unificar
"S" y "Sí" en uno solo). Una tabla bien nombrada y consistente es la base de un análisis confiable.</p>

<p><b>La regla de oro.</b> Nunca analices datos sucios. Dedica tiempo a explorarlos, detectar
problemas y corregirlos; un análisis impecable sobre datos malos entrega conclusiones malas. La
limpieza no es un paso menor: es <b>parte esencial</b> del análisis.</p>
""",
        "examples": [
            {
                "title": "Detectar faltantes",
                "explain": "Creamos una tabla con huecos (NaN) y contamos los faltantes por columna.",
                "code": 'import pandas as pd\nimport numpy as np\ndf = pd.DataFrame({\n    "ciudad": ["Santiago", None, "Valpo", "Concepción"],\n    "ventas": [120, 95, np.nan, 88],\n})\nprint(df)\nprint("\\nfaltantes por columna:\\n", df.isna().sum())',
            },
            {
                "title": "Eliminar o rellenar faltantes",
                "explain": "<code>dropna()</code> quita filas con NaN; <code>fillna()</code> los rellena.",
                "code": 'import pandas as pd, numpy as np\ndf = pd.DataFrame({"ventas": [120, np.nan, 130, np.nan, 88]})\nprint("sin nulos:\\n", df.dropna())\nprint("\\nrellenado con la media:\\n", df.fillna(df["ventas"].mean()))',
            },
            {
                "title": "Duplicados",
                "explain": "Detectar y eliminar filas repetidas.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({"region": ["norte", "sur", "norte", "norte"]})\nprint("¿duplicada?:\\n", df.duplicated())\nprint("\\nsin duplicados:\\n", df.drop_duplicates())',
            },
            {
                "title": "Convertir tipos",
                "explain": "Una columna de texto numérico se convierte para poder calcular.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({"precio": ["1000", "2500", "990"]})\nprint("tipos antes:", df["precio"].dtype)\ndf["precio"] = df["precio"].astype(int)\nprint("suma:", df["precio"].sum(), "| tipo:", df["precio"].dtype)',
            },
            {
                "title": "Limpiar texto con .str",
                "explain": "Estandarizamos una columna de texto: sin espacios y en minúsculas.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({"region": [" Norte ", "SUR", "norte "]})\ndf["region"] = df["region"].str.strip().str.lower()\nprint(df)\nprint("\\nconteo:\\n", df["region"].value_counts())',
            },
            {
                "title": "Renombrar y reemplazar",
                "explain": "Nombres claros y valores unificados.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({"reg": ["N", "S", "N"], "vta": [120, 95, 130]})\ndf = df.rename(columns={"reg": "region", "vta": "ventas"})\ndf["region"] = df["region"].replace({"N": "norte", "S": "sur"})\nprint(df)',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Crea un DataFrame con algunos <code>None</code> y cuenta los faltantes por columna con <code>isna().sum()</code>.",
            "Elimina las filas con faltantes de ese DataFrame con <code>dropna()</code>.",
            "Rellena los faltantes de una columna numérica con su media usando <code>fillna()</code>.",
            "Crea un DataFrame con filas repetidas y quítalas con <code>drop_duplicates()</code>.",
            "Convierte la columna de texto <code>[\"10\", \"20\", \"30\"]</code> a entero con <code>astype()</code> y súmala.",
            "Estandariza una columna de texto con <code>.str.strip().str.lower()</code>.",
            "Renombra dos columnas de un DataFrame con <code>rename()</code>.",
            "Con <code>replace()</code>, cambia los valores <code>\"S\"</code> y <code>\"N\"</code> por <code>\"sí\"</code> y <code>\"no\"</code>.",
            "Cuenta cuántas filas quedan antes y después de limpiar duplicados y nulos.",
        ],
    },

    # ============================================================ CAP 16
    {
        "num": 16,
        "slug": "combinar-reformar",
        "code": "leccion_16",
        "title": "Combinar y reformar tablas",
        "subtitle": "Unir fuentes, agrupar y reorganizar con concat, merge y pivot",
        "apunte": "Lección 16 - Combinar y reformar",
        "concepts": [
            ("concat()", "Apila tablas: una sobre otra (más filas) o lado a lado (más columnas)."),
            ("merge()", "Une dos tablas por una <b>columna en común</b> (clave). Es el JOIN de las bases de datos / el BUSCARV de Excel."),
            ("Tipo de unión", "<code>inner</code> (solo coincidencias), <code>left</code> (conserva todas las de la izquierda), etc."),
            ("Clave (key)", "La columna por la que se emparejan las filas al hacer merge (<code>on=\"id\"</code>)."),
            ("groupby() + agg()", "Agrupar por una columna y resumir cada grupo con una o varias medidas."),
            ("pivot_table()", "Resumen cruzado: filas × columnas con un valor agregado en cada celda."),
            ("sort_values()", "Ordena la tabla por una o varias columnas."),
            ("melt()", "Transforma de formato ancho a largo (lo inverso de pivotar)."),
        ],
        "theory": """
<p>Rara vez los datos vienen en una sola tabla lista para usar. Un analista <b>combina</b> fuentes,
<b>agrupa</b> para resumir y <b>reorganiza</b> la forma de los datos según la pregunta que quiere
responder. pandas ofrece herramientas potentes para las tres cosas.</p>

<p><b>Apilar: concat.</b> <code>pd.concat()</code> junta tablas. Apiladas verticalmente (una sobre
otra) suman <b>filas</b> —útil cuando tienes los mismos datos en varios archivos, por ejemplo un mes
por archivo—; apiladas horizontalmente suman <b>columnas</b>. Es la operación de "juntar lo mismo".</p>

<p><b>Unir por clave: merge.</b> La operación estrella. <code>pd.merge()</code> combina dos tablas
<b>emparejando filas por una columna en común</b> (la <b>clave</b>). Es el equivalente al
<code>JOIN</code> de las bases de datos o al <code>BUSCARV</code>/<code>VLOOKUP</code> de Excel: por
ejemplo, unir una tabla de ventas con una tabla de productos usando el código de producto. El
<b>tipo de unión</b> decide qué filas se conservan: <code>inner</code> deja solo las que coinciden en
ambas, <code>left</code> conserva todas las de la primera tabla (aunque no tengan pareja), y así.
Elegir bien el tipo evita perder datos sin darte cuenta.</p>

<p><b>Agrupar: groupby.</b> Ya lo viste: <code>df.groupby("region")["ventas"].mean()</code> separa por
grupo y resume. Con <code>agg()</code> pides varias medidas a la vez. Es el patrón
<i>dividir-aplicar-combinar</i>, y es central en el análisis.</p>

<p><b>Reorganizar: pivot_table.</b> A veces necesitas un <b>resumen cruzado</b>: por ejemplo, ventas
por región (filas) y por mes (columnas). <code>pivot_table()</code> hace exactamente eso: eliges qué
va en las filas, qué en las columnas y qué valor agregar (suma, media…) en cada celda. Es como una
tabla dinámica de Excel. Su operación inversa, <code>melt()</code>, pasa de formato "ancho" (muchas
columnas) a "largo" (pocas columnas y más filas), que suele ser mejor para graficar.</p>

<p><b>Ordenar.</b> <code>sort_values("columna")</code> ordena la tabla; con <code>ascending=False</code>
de mayor a menor. Ordenar es clave para presentar rankings y encontrar los valores más altos o más
bajos.</p>

<p><b>La idea de fondo.</b> Estas operaciones son las que convierten datos crudos y dispersos en una
tabla-respuesta. Dominarlas es, en gran medida, saber "hablar con los datos": preguntar y obtener
exactamente el resumen que necesitas.</p>
""",
        "examples": [
            {
                "title": "concat: apilar tablas",
                "explain": "Juntamos dos tablas con las mismas columnas (más filas).",
                "code": 'import pandas as pd\nene = pd.DataFrame({"region": ["norte", "sur"], "ventas": [120, 95]})\nfeb = pd.DataFrame({"region": ["norte", "sur"], "ventas": [130, 110]})\ntodo = pd.concat([ene, feb], ignore_index=True)\nprint(todo)',
            },
            {
                "title": "merge: unir por clave",
                "explain": "Unimos ventas con los precios de cada producto por la columna 'producto'.",
                "code": 'import pandas as pd\nventas = pd.DataFrame({"producto": ["pan", "leche", "pan"], "cantidad": [3, 2, 5]})\nprecios = pd.DataFrame({"producto": ["pan", "leche"], "precio": [990, 1200]})\nunido = pd.merge(ventas, precios, on="producto")\nunido["total"] = unido["cantidad"] * unido["precio"]\nprint(unido)',
            },
            {
                "title": "Tipo de unión: left",
                "explain": "Con <code>how=\"left\"</code> conservamos todas las filas de la izquierda.",
                "code": 'import pandas as pd\na = pd.DataFrame({"id": [1, 2, 3], "nombre": ["Ana", "Luis", "Eva"]})\nb = pd.DataFrame({"id": [1, 3], "puntos": [10, 8]})\nprint(pd.merge(a, b, on="id", how="left"))',
            },
            {
                "title": "groupby + agg",
                "explain": "Resumen por grupo con varias medidas.",
                "code": 'print(datos.groupby("region")["ventas"].agg(["sum", "mean", "count"]))',
            },
            {
                "title": "pivot_table: resumen cruzado",
                "explain": "Ventas por región (filas) — como una tabla dinámica.",
                "code": 'print(pd.pivot_table(datos, index="region", values="ventas", aggfunc="sum"))',
            },
            {
                "title": "Ordenar",
                "explain": "Ordenamos la tabla por ventas, de mayor a menor.",
                "code": 'print(datos.sort_values("ventas", ascending=False))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Crea dos DataFrames con las mismas columnas y apílalos con <code>pd.concat()</code>.",
            "Crea una tabla de productos con precio y otra de ventas con cantidad, y únelas con <code>merge()</code>.",
            "En el merge anterior, calcula una columna <code>total = cantidad * precio</code>.",
            "Haz un <code>merge</code> con <code>how=\"left\"</code> y observa qué filas se conservan.",
            "Agrupa <code>datos</code> por <code>region</code> y obtén suma y media de <code>ventas</code> con <code>agg()</code>.",
            "Crea una <code>pivot_table</code> de ventas por región.",
            "Ordena <code>datos</code> por <code>unidades</code> de mayor a menor.",
            "Ordena <code>datos</code> por dos columnas: primero <code>region</code>, luego <code>ventas</code>.",
            "Concatena <code>datos</code> consigo mismo y verifica que se duplicó el número de filas.",
        ],
    },

    # ============================================================ CAP 17
    {
        "num": 17,
        "slug": "fechas",
        "code": "leccion_17",
        "title": "Fechas y series de tiempo",
        "subtitle": "Trabajar con fechas: componentes, rangos y agrupación por período",
        "apunte": "Lección 17 - Fechas y tiempo",
        "concepts": [
            ("datetime", "El tipo de dato para fechas y horas. pandas lo maneja de forma nativa."),
            ("pd.to_datetime()", "Convierte texto (o números) a fechas reales para poder operar con ellas."),
            (".dt", "Accesor que extrae componentes de una columna de fechas: <code>.dt.year</code>, <code>.dt.month</code>, <code>.dt.day</code>."),
            ("date_range()", "Genera una secuencia de fechas: <code>pd.date_range(\"2026-01-01\", periods=5)</code>."),
            ("Timedelta", "La diferencia entre dos fechas (días, horas)."),
            ("Índice de fechas", "Usar las fechas como índice permite filtrar y agrupar por tiempo con facilidad."),
            ("resample()", "Agrupa una serie temporal por período (día, mes, año) para resumir."),
            ("Filtro por rango", "Seleccionar filas entre dos fechas."),
        ],
        "theory": """
<p>El tiempo es una dimensión omnipresente en los datos: ventas por día, temperaturas por hora,
usuarios por mes. Trabajar bien con <b>fechas</b> abre un tipo de análisis muy valioso: las
<b>series de tiempo</b>. pandas tiene soporte nativo y potente para ello.</p>

<p><b>Fechas de verdad, no texto.</b> Una fecha guardada como texto ("2026-03-15") no sirve para
calcular: no puedes restar dos textos ni ordenarlos como fechas de forma fiable. El primer paso es
<b>convertir</b> con <code>pd.to_datetime()</code>, que transforma el texto en un objeto
<code>datetime</code> real. A partir de ahí, pandas entiende que es una fecha.</p>

<p><b>Extraer componentes.</b> Con el accesor <code>.dt</code> obtienes las partes de una fecha sobre
toda una columna: <code>fecha.dt.year</code>, <code>.dt.month</code>, <code>.dt.day</code>,
<code>.dt.day_name()</code>. Esto permite, por ejemplo, agrupar ventas por mes o por día de la semana
a partir de una columna de fechas.</p>

<p><b>Generar y medir.</b> <code>pd.date_range()</code> crea secuencias de fechas (útil para armar
calendarios o ejes de tiempo). Y restar dos fechas da un <b>Timedelta</b>: la <b>diferencia</b> en
días u horas, que puedes usar para calcular antigüedades, duraciones o plazos.</p>

<p><b>El tiempo como índice.</b> Cuando las fechas son el <b>índice</b> del DataFrame, pandas ofrece
superpoderes: puedes filtrar por rango (<code>df.loc["2026-01":"2026-03"]</code>) y, sobre todo,
<b>reagrupar por período</b> con <code>resample()</code>: convertir datos diarios en mensuales
sumando o promediando, por ejemplo. Es la base del análisis de tendencias.</p>

<p><b>Por qué importa.</b> Casi todo negocio piensa en el tiempo: ¿vendemos más los fines de semana?,
¿crece mes a mes?, ¿hay estacionalidad? Saber convertir, extraer, agrupar y filtrar por fecha te
permite responder estas preguntas. Es una habilidad que distingue a un analista de datos competente,
y la puerta de entrada a temas más avanzados de pronóstico.</p>
""",
        "examples": [
            {
                "title": "Convertir y generar fechas",
                "explain": "<code>to_datetime</code> convierte texto a fecha; <code>date_range</code> genera secuencias.",
                "code": 'import pandas as pd\nf = pd.to_datetime("2026-03-15")\nprint("fecha:", f, "| tipo:", type(f).__name__)\nrango = pd.date_range("2026-01-01", periods=5, freq="D")\nprint(rango)',
            },
            {
                "title": "Extraer componentes con .dt",
                "explain": "De una columna de fechas obtenemos año, mes y día de la semana.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({"fecha": pd.to_datetime(["2026-01-05", "2026-02-20", "2026-03-10"])})\ndf["mes"] = df["fecha"].dt.month\ndf["dia_semana"] = df["fecha"].dt.day_name()\nprint(df)',
            },
            {
                "title": "Diferencia entre fechas",
                "explain": "Restar dos fechas da un Timedelta: los días entre ellas.",
                "code": 'import pandas as pd\ninicio = pd.to_datetime("2026-01-01")\nfin = pd.to_datetime("2026-03-15")\nprint("diferencia:", (fin - inicio).days, "días")',
            },
            {
                "title": "Serie con índice de fechas",
                "explain": "Con las fechas como índice, filtrar por tiempo es directo.",
                "code": 'import pandas as pd\nfechas = pd.date_range("2026-01-01", periods=6, freq="D")\ns = pd.DataFrame({"ventas": [10, 12, 9, 15, 20, 8]}, index=fechas)\nprint(s.loc["2026-01-03":"2026-01-05"])',
            },
            {
                "title": "Agrupar por mes",
                "explain": "Extraemos el período mensual con <code>.dt.to_period(\"M\")</code> y sumamos por mes.",
                "code": 'import pandas as pd, numpy as np\nfechas = pd.date_range("2026-01-01", periods=60, freq="D")\ns = pd.DataFrame({"fecha": fechas, "ventas": np.arange(60)})\ns["mes"] = s["fecha"].dt.to_period("M")\nprint(s.groupby("mes")["ventas"].sum())',
            },
            {
                "title": "Filtrar por rango de fechas",
                "explain": "Seleccionar las filas entre dos fechas.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({\n    "fecha": pd.to_datetime(["2026-01-10", "2026-02-15", "2026-03-20"]),\n    "ventas": [100, 150, 120],\n})\nmask = (df["fecha"] >= "2026-02-01") & (df["fecha"] <= "2026-03-31")\nprint(df[mask])',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Convierte el texto <code>\"2026-07-20\"</code> a fecha con <code>pd.to_datetime()</code>.",
            "Genera 7 fechas diarias desde <code>\"2026-05-01\"</code> con <code>date_range()</code>.",
            "De una columna de fechas, extrae el año y el mes con <code>.dt</code>.",
            "Calcula cuántos días hay entre <code>\"2026-01-01\"</code> y <code>\"2026-12-31\"</code>.",
            "Crea una tabla con índice de fechas y filtra un rango con <code>.loc</code>.",
            "Agrega el día de la semana a una columna de fechas con <code>.dt.day_name()</code>.",
            "Con <code>resample</code>, agrupa por mes una serie diaria y suma las ventas.",
            "Filtra las filas de una tabla cuya fecha esté en febrero de 2026.",
            "Ordena una tabla por su columna de fechas de la más antigua a la más reciente.",
        ],
    },
]
