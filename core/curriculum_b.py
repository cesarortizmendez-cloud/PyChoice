# -*- coding: utf-8 -*-
"""
PyChoice - Lecciones 5 a 8 (formato capitulo, estilo EstadisticaR).
Teoria extendida (software educativo) + conceptos clave enriquecidos.
Cada consola trae np, pd, plt y los datos de ejemplo `notas` (lista) y
`datos` (DataFrame: mes, region, ventas, unidades).
"""

CHAPTERS_B = [

    # ============================================================ CAP 05
    {
        "num": 5,
        "slug": "cargar-excel",
        "code": "leccion_05",
        "title": "Cargar Excel y trabajar con sus columnas",
        "subtitle": "Leer una planilla como DataFrame y usar sus columnas como variables",
        "apunte": "Lección 5 - Datos desde Excel",
        "concepts": [
            ("pd.read_excel()", "Lee un archivo <code>.xlsx</code> y lo convierte en DataFrame. Necesita la librería <code>openpyxl</code>. Con <code>sheet_name=</code> eliges la hoja."),
            ("pd.read_csv()", "Lee un archivo <code>.csv</code> (texto separado por comas). Muy usado por ser universal y liviano."),
            ("DataFrame", "La tabla completa: filas identificadas por un <b>índice</b> y columnas con nombre y tipo (<code>dtype</code>)."),
            ("Columna (Series)", "Una columna, se accede con <code>datos['ventas']</code>. Es una <code>Series</code>: una secuencia etiquetada de valores."),
            ("head() / info() / shape", "<code>head()</code> muestra las primeras filas, <code>info()</code> el resumen de columnas y tipos, y <code>shape</code> el tamaño (filas, columnas)."),
            ("Filtro booleano", "Seleccionar filas que cumplen una condición: <code>datos[datos['ventas'] &gt; 100]</code>."),
            ("Seleccionar columnas", "Una columna con <code>datos['col']</code>; varias con una lista: <code>datos[['mes','ventas']]</code>."),
            ("to_excel() / to_csv()", "Guardan un DataFrame a archivo. En PyChoice, el botón <b>exportar excel</b> descarga el resultado."),
        ],
        "theory": """
<p>El insumo diario de un analista es una <b>planilla</b>: ventas, encuestas, registros, sensores.
El primer paso de casi cualquier análisis es <b>cargar</b> esos datos a Python. Con pandas eso es una
sola línea, y a partir de ahí trabajas la planilla con la potencia de un lenguaje de programación.</p>

<p><b>Leer un archivo.</b> Para Excel: <code>datos = pd.read_excel("archivo.xlsx")</code> (requiere la
librería <code>openpyxl</code>, que pandas usa por debajo; con <code>sheet_name=</code> eliges qué
hoja leer). Para CSV: <code>datos = pd.read_csv("archivo.csv")</code>. El CSV es un formato de texto
plano, universal y liviano, muy común al exportar datos. El resultado, en ambos casos, es un
<b>DataFrame</b>.</p>

<p><b>Anatomía de un DataFrame.</b> Un DataFrame es una tabla con tres partes: un <b>índice</b> (la
etiqueta de cada fila, por defecto 0, 1, 2…), las <b>columnas</b> (cada una con su nombre) y los
<b>tipos</b> de dato de cada columna (<code>dtype</code>: número, texto, fecha…). Antes de calcular
nada conviene <b>explorar</b>: <code>datos.head()</code> muestra las primeras filas,
<code>datos.shape</code> el tamaño, <code>datos.columns</code> los nombres y <code>datos.info()</code>
un resumen de tipos y valores faltantes.</p>

<p><b>Las columnas son tus variables.</b> Cada columna se obtiene con <code>datos["nombre"]</code> y
es una <b>Series</b>: una secuencia de valores con la que puedes operar directamente
(<code>datos["ventas"].mean()</code>, <code>datos["ventas"].max()</code>). Seleccionar <b>varias</b>
columnas se hace pasando una lista: <code>datos[["mes", "ventas"]]</code>. Piensa en una columna como
una variable llena de muchos datos a la vez.</p>

<p><b>Filtrar filas.</b> La operación más frecuente es quedarse con las filas que cumplen una
condición. Se escribe poniendo la condición entre corchetes: <code>datos[datos["ventas"] &gt; 100]</code>
devuelve solo las filas con ventas mayores a 100. Esto se llama <b>filtro booleano</b> porque, por
dentro, la condición genera una columna de <code>True</code>/<code>False</code> y pandas conserva las
filas marcadas como <code>True</code>. Es la traducción a código de "muéstrame solo los casos que
me interesan".</p>

<p><b>Guardar resultados.</b> Cuando llegas a una tabla resumen, la exportas con
<code>to_excel("salida.xlsx")</code> o <code>to_csv("salida.csv")</code>. En PyChoice tienes el botón
<b>cargar excel</b> (tu archivo queda disponible como <code>datos</code>) y <b>exportar excel</b>
(descarga cualquier DataFrame). Para practicar sin cargar nada, ya viene un DataFrame
<code>datos</code> de ejemplo con columnas <code>mes</code>, <code>region</code>, <code>ventas</code> y
<code>unidades</code>.</p>

<p><b>Detalles a cuidar al leer archivos reales:</b> la <b>ruta</b> del archivo (dónde está), el
<b>separador</b> en un CSV (a veces es <code>;</code> en vez de <code>,</code>), la <b>codificación</b>
(acentos) y los <b>valores faltantes</b>. pandas ofrece parámetros para todo eso; con la práctica los
irás conociendo.</p>
""",
        "examples": [
            {
                "title": "Ver la tabla",
                "explain": "Primero se explora: <code>head()</code> muestra las primeras filas, <code>shape</code> el tamaño y <code>columns</code> los nombres.",
                "code": 'print(datos.head())\nprint("filas x columnas:", datos.shape)\nprint("columnas:", list(datos.columns))',
            },
            {
                "title": "Una columna como variable",
                "explain": "Con <code>datos[\"columna\"]</code> obtienes una columna (Series) para trabajarla aparte.",
                "code": 'ventas = datos["ventas"]\nprint(ventas)\nprint("tipo:", type(ventas))',
            },
            {
                "title": "Estadísticos de una columna",
                "explain": "Las columnas numéricas traen métodos de resumen listos.",
                "code": 'print("media:", datos["ventas"].mean())\nprint("suma:", datos["ventas"].sum())\nprint("máximo:", datos["ventas"].max())',
            },
            {
                "title": "Filtrar filas por condición",
                "explain": "Una condición entre corchetes deja solo las filas que la cumplen.",
                "code": 'altas = datos[datos["ventas"] > 100]\nprint(altas)',
            },
            {
                "title": "Seleccionar columnas y filtrar",
                "explain": "Puedes combinar: filtrar filas y quedarte con algunas columnas.",
                "code": 'norte = datos[datos["region"] == "norte"]\nprint(norte[["mes", "ventas"]])',
            },
            {
                "title": "Resumen y tu propio Excel",
                "explain": "<code>describe()</code> resume toda la tabla. Prueba <b>cargar excel</b> con tu archivo y vuelve a ejecutar.",
                "code": 'print(datos.describe())',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Muestra las primeras 3 filas de <code>datos</code> con <code>head(3)</code>.",
            "Calcula la media y el máximo de la columna <code>unidades</code>.",
            "Filtra las filas donde <code>region</code> sea <code>\"sur\"</code>.",
            "Carga un Excel propio con el botón y muestra su <code>describe()</code>.",
            "Muestra solo las columnas <code>mes</code> y <code>ventas</code> de toda la tabla.",
            "Cuenta cuántas filas cumplen <code>ventas &gt; 100</code> (usa <code>len()</code> sobre el filtro).",
            "Filtra las filas de región <code>\"norte\"</code> con <code>ventas &gt; 100</code> (dos condiciones con <code>&amp;</code>).",
            "Ordena la tabla por <code>ventas</code> de mayor a menor con <code>sort_values()</code>.",
            "Calcula el total de <code>ventas</code> de todo el DataFrame con <code>.sum()</code>.",
        ],
    },

    # ============================================================ CAP 06
    {
        "num": 6,
        "slug": "bucles",
        "code": "leccion_06",
        "title": "Funciones FOR y WHILE",
        "subtitle": "Repetir tareas: recorrer datos y acumular resultados",
        "apunte": "Lección 6 - Bucles",
        "concepts": [
            ("Bucle", "Estructura que repite un bloque de código muchas veces sin reescribirlo."),
            ("for", "Repite un bloque <b>para cada</b> elemento de una secuencia (lista, rango, columna, texto)."),
            ("Iterable", "Cualquier cosa que se puede recorrer elemento a elemento: listas, cadenas, rangos, Series."),
            ("range()", "Genera una secuencia de números: <code>range(5)</code> → 0,1,2,3,4; <code>range(1,6)</code> → 1..5."),
            ("while", "Repite <b>mientras</b> una condición sea verdadera. Requiere que algo cambie para poder terminar."),
            ("Acumulador", "Variable que empieza en 0 (o vacía) y va sumando o contando dentro del bucle."),
            ("break / continue", "<code>break</code> corta el bucle de inmediato; <code>continue</code> salta a la siguiente vuelta."),
            ("Vectorización", "En pandas/NumPy conviene evitar bucles cuando hay una operación de columna equivalente (más rápida y clara)."),
        ],
        "theory": """
<p>Programar es, en buena parte, <b>automatizar tareas repetitivas</b>. Un <b>bucle</b> permite
repetir instrucciones muchas veces sin escribirlas una y otra vez. Es lo que convierte "calcula el
promedio de estas 8 notas" en "calcula el promedio de estas 8.000 notas" con el mismo código.</p>

<p><b>El bucle for.</b> Recorre los elementos de una secuencia (un <b>iterable</b>) uno por uno:
una lista, un rango de números, los caracteres de un texto o los valores de una columna. Su forma es
<code>for elemento in secuencia:</code> seguido de un bloque sangrado que se ejecuta una vez por cada
elemento. En cada vuelta, la variable (<code>elemento</code>) toma el valor siguiente.</p>

<p><b>range(): repetir N veces.</b> Cuando quieres repetir un número fijo de veces o generar una
serie de números, usas <code>range()</code>. <code>range(5)</code> produce 0,1,2,3,4;
<code>range(1, 6)</code> produce 1,2,3,4,5; y <code>range(0, 10, 2)</code> va de 2 en 2. Es la forma
habitual de numerar pasos o iteraciones.</p>

<p><b>El bucle while.</b> Repite <b>mientras</b> una condición se mantenga verdadera. Se usa cuando
no sabes de antemano cuántas vueltas harás, sino que dependes de una condición (por ejemplo, "sigue
restando del saldo hasta que llegue a cero"). <b>Atención:</b> dentro del <code>while</code> algo
debe cambiar para que la condición deje de cumplirse; si no, se produce un <b>bucle infinito</b> y el
programa se cuelga.</p>

<p><b>El patrón acumulador.</b> Muchísimos cálculos siguen la misma receta: se crea una variable en
0 (o una lista vacía) <b>antes</b> del bucle, y dentro se va <b>sumando</b> o <b>contando</b>. Así se
calculan a mano totales, promedios o conteos. Combinado con un <code>if</code> dentro del bucle,
puedes acumular <b>solo</b> lo que cumple una condición: contar aprobados, sumar ventas de una región,
etc. Este patrón <b>for + if</b> es la base del análisis de datos "a mano".</p>

<p><b>Control fino: break y continue.</b> A veces quieres detener el bucle antes de tiempo
(<code>break</code>, por ejemplo al encontrar lo que buscabas) o saltarte una vuelta concreta
(<code>continue</code>, por ejemplo para ignorar un dato inválido).</p>

<p><b>Un adelanto importante.</b> Con pandas y NumPy muchas veces <b>no</b> necesitarás un bucle: una
operación de columna (como <code>datos["ventas"].sum()</code>) hace en una línea, y más rápido, lo
que un bucle haría en varias. Eso se llama <b>vectorización</b>. Aprender los bucles es esencial para
entender la lógica; pero, cuando exista la versión de columna, esa suele ser la mejor opción.</p>
""",
        "examples": [
            {
                "title": "for sobre una lista",
                "explain": "Recorre cada elemento de <code>notas</code> y lo muestra.",
                "code": 'for n in notas:\n    print("nota:", n)',
            },
            {
                "title": "range(): repetir N veces",
                "explain": "<code>range()</code> genera números. Útil para repetir o numerar.",
                "code": 'for i in range(1, 6):\n    print(f"vuelta {i}")',
            },
            {
                "title": "Acumulador: sumar con un bucle",
                "explain": "Empieza en 0 y suma en cada vuelta. Así se calcula un total a mano.",
                "code": 'total = 0\nfor n in notas:\n    total = total + n\nprint("total:", round(total, 2))\nprint("promedio:", round(total / len(notas), 2))',
            },
            {
                "title": "while: repetir con condición",
                "explain": "Repite mientras la condición sea verdadera. Cuidado de que en algún momento deje de cumplirse.",
                "code": 'saldo = 1000\nmeses = 0\nwhile saldo > 0:\n    saldo = saldo - 300\n    meses = meses + 1\nprint("meses hasta agotar:", meses)',
            },
            {
                "title": "for + if: contar condicional",
                "explain": "Recorremos y contamos solo lo que cumple la condición.",
                "code": 'aprobadas = 0\nfor n in notas:\n    if n >= 5:\n        aprobadas += 1\nprint("notas >= 5:", aprobadas)',
            },
            {
                "title": "Recorrer una columna del DataFrame",
                "explain": "Puedes iterar los valores de una columna igual que una lista.",
                "code": 'suma = 0\nfor v in datos["ventas"]:\n    suma += v\nprint("suma de ventas:", suma)',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Recorre <code>range(1, 11)</code> e imprime la tabla del 3 (3, 6, 9, ...).",
            "Con un acumulador y un <code>for</code>, suma los valores de <code>datos['unidades']</code>.",
            "Con <code>for + if</code>, cuenta cuántas ventas superan 100.",
            "Con un <code>while</code>, parte de 100 y ve restando 15 hasta llegar a 0 o menos; cuenta los pasos.",
            "Recorre <code>notas</code> e imprime <code>\"alta\"</code> si la nota es &gt;= 5, o <code>\"baja\"</code> si no.",
            "Con <code>for</code> y <code>range</code>, imprime todos los números pares del 0 al 20.",
            "Con <code>for + if</code>, suma solo los valores impares de <code>[3, 8, 5, 2, 9, 4]</code>.",
            "Con un <code>while</code>, encuentra el primer número natural cuyo cuadrado supere 100.",
            "Recorre <code>datos['ventas']</code> y encuentra (con un bucle) el valor máximo sin usar <code>max()</code>.",
        ],
    },

    # ============================================================ CAP 07
    {
        "num": 7,
        "slug": "pandas-estadistica-1",
        "code": "leccion_07",
        "title": "Estadística con Pandas I",
        "subtitle": "Resumir datos: medidas, conteos y agrupaciones",
        "apunte": "Lección 7 - Estadística descriptiva con Pandas",
        "concepts": [
            ("Estadística descriptiva", "Resume un conjunto de datos en pocos números y gráficos, para entenderlo sin mirar fila por fila."),
            ("Media / mediana", "La <b>media</b> es el promedio; la <b>mediana</b> es el valor central. La mediana resiste mejor los valores extremos (atípicos)."),
            ("Desviación estándar", "<code>std()</code>: mide cuánto se dispersan los datos respecto a la media. Poca desviación = datos parecidos."),
            ("describe()", "Entrega de golpe conteo, media, desviación, mínimo, cuartiles y máximo de las columnas numéricas."),
            ("value_counts()", "Cuenta cuántas veces aparece cada categoría en una columna de texto (frecuencias)."),
            ("groupby()", "Agrupa las filas por una columna y calcula una medida por grupo. Patrón <i>dividir-aplicar-combinar</i>."),
            ("agg()", "Aplica varias medidas a la vez a cada grupo: <code>agg(['mean','max','count'])</code>."),
            ("NaN", "Valor faltante (Not a Number). Muchas funciones lo ignoran automáticamente, pero conviene saber que existe."),
        ],
        "theory": """
<p>La <b>estadística descriptiva</b> es el arte de resumir. Un conjunto de miles de filas es
imposible de entender mirándolo directamente; lo que hacemos es <b>condensarlo</b> en unas pocas
medidas que capturan su forma: dónde está el centro, cuánto varían los datos y cómo se reparten.
pandas trae todas estas medidas listas para usar sobre columnas.</p>

<p><b>Medidas de centro.</b> La <b>media</b> (<code>mean()</code>) es el promedio: la suma dividida
por la cantidad. La <b>mediana</b> (<code>median()</code>) es el valor que queda justo en el medio al
ordenar los datos. ¿Por qué dos? Porque la media puede engañar cuando hay <b>valores extremos</b>:
si en un grupo de sueldos hay uno altísimo, la media sube y deja de representar al grupo, mientras que
la mediana se mantiene estable. Comparar ambas ya dice mucho sobre los datos.</p>

<p><b>Medidas de dispersión.</b> La <b>desviación estándar</b> (<code>std()</code>) mide cuánto se
alejan los datos de la media, en promedio. Una desviación pequeña indica datos homogéneos (parecidos
entre sí); una grande, datos muy dispersos. Junto con el <b>mínimo</b>, el <b>máximo</b> y el
<b>rango</b> (máximo − mínimo), dan una idea de la variabilidad.</p>

<p><b>describe(): la foto rápida.</b> El método <code>datos.describe()</code> entrega en una sola
tabla el conteo, la media, la desviación estándar, el mínimo, los <b>cuartiles</b> (los valores que
dividen los datos en cuatro partes: 25%, 50% y 75%) y el máximo de cada columna numérica. Es casi
siempre lo primero que se ejecuta al recibir una tabla nueva.</p>

<p><b>Variables categóricas.</b> No todo es numérico: la región, el género o el producto son
<b>categorías</b>. Para ellas, la medida clave es la <b>frecuencia</b>: cuántas veces aparece cada
categoría. Eso lo entrega <code>value_counts()</code>, que es el equivalente a una tabla de conteo.</p>

<p><b>La operación estrella: groupby.</b> El verdadero poder del análisis aparece al <b>agrupar</b>.
<code>datos.groupby("region")["ventas"].mean()</code> separa los datos por región y calcula el
promedio de ventas <b>de cada grupo</b>. Esto responde preguntas como "¿qué región vende más?". El
patrón se llama <b>dividir-aplicar-combinar</b>: se parte la tabla en grupos, se aplica una medida a
cada uno y se combinan los resultados. Con <code>agg()</code> puedes pedir varias medidas a la vez
(media, máximo, conteo) por grupo.</p>

<p><b>Un detalle práctico: los faltantes (NaN).</b> Los datos reales suelen tener celdas vacías,
que pandas representa como <code>NaN</code>. La mayoría de las funciones estadísticas los ignoran
automáticamente al calcular, pero es importante saber que están ahí, porque pueden afectar conteos y
promedios. Detectarlos y tratarlos es parte de la limpieza de datos.</p>
""",
        "examples": [
            {
                "title": "Resumen completo con describe()",
                "explain": "Una foto de las columnas numéricas: conteo, media, desviación, mínimo, cuartiles y máximo.",
                "code": 'print(datos.describe())',
            },
            {
                "title": "Medidas de una columna",
                "explain": "Media, mediana y desviación estándar de las ventas.",
                "code": 'v = datos["ventas"]\nprint("media:", round(v.mean(), 2))\nprint("mediana:", v.median())\nprint("desv. est:", round(v.std(), 2))',
            },
            {
                "title": "Mínimo, máximo, conteo, suma",
                "explain": "Las medidas básicas de posición y totales.",
                "code": 'v = datos["ventas"]\nprint("min:", v.min(), " max:", v.max())\nprint("cantidad:", v.count())\nprint("suma:", v.sum())',
            },
            {
                "title": "Conteo por categoría",
                "explain": "<code>value_counts()</code> cuenta cuántas filas hay por cada región.",
                "code": 'print(datos["region"].value_counts())',
            },
            {
                "title": "Agrupar y resumir (groupby)",
                "explain": "Promedio de ventas por región: separa por grupo y calcula la media de cada uno.",
                "code": 'print(datos.groupby("region")["ventas"].mean())',
            },
            {
                "title": "Varias medidas por grupo (agg)",
                "explain": "Con <code>agg()</code> pides varias medidas a la vez para cada grupo.",
                "code": 'resumen = datos.groupby("region")["ventas"].agg(["mean", "max", "count"])\nprint(resumen)',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Muestra la media y la desviación estándar de la columna <code>unidades</code>.",
            "Cuenta cuántas filas hay por cada <code>region</code> con <code>value_counts()</code>.",
            "Agrupa por <code>region</code> y calcula la suma de <code>ventas</code>.",
            "Con <code>agg()</code>, obtén media y máximo de <code>unidades</code> por región.",
            "Muestra el <code>describe()</code> completo e identifica el valor máximo de <code>ventas</code>.",
            "Calcula la mediana de <code>ventas</code> y compárala con la media: ¿cuál es mayor?",
            "Agrupa por <code>region</code> y obtén la media de <code>ventas</code> y de <code>unidades</code> a la vez.",
            "Ordena de mayor a menor el resultado de agrupar <code>ventas</code> por región (<code>sort_values()</code>).",
            "Calcula el porcentaje que representa cada región sobre el total de ventas.",
        ],
    },

    # ============================================================ CAP 08
    {
        "num": 8,
        "slug": "pandas-estadistica-2",
        "code": "leccion_08",
        "title": "Estadística con Pandas II (con IF, FOR y WHILE)",
        "subtitle": "Combinar pandas con condiciones y bucles para analizar y decidir",
        "apunte": "Lección 8 - Pandas aplicado",
        "concepts": [
            ("Filtro booleano", "Seleccionar filas con una condición: <code>datos[datos['ventas'] &gt; 100]</code>. Es la forma <i>vectorizada</i> de filtrar."),
            ("Columna derivada", "Crear una columna nueva a partir de otras: <code>datos['total'] = datos['ventas'] * precio</code>."),
            ("apply()", "Aplica una función (o una regla) a cada valor de una columna. Útil para clasificar o transformar."),
            ("lambda", "Función anónima de una línea: <code>lambda x: 'alta' if x &gt; 100 else 'baja'</code>."),
            ("iterrows()", "Recorre las filas del DataFrame una a una con un <code>for</code>. Claro para aprender, pero lento en tablas grandes."),
            ("Condición + grupo", "Combinar filtro y <code>groupby</code> para responder preguntas precisas."),
            ("Vectorización vs bucle", "Cuando exista la operación de columna, prefiérela al bucle: es más rápida y legible."),
            ("Decidir con datos", "El objetivo final: convertir la tabla en una conclusión o una acción. Es el propósito de PyChoice."),
        ],
        "theory": """
<p>Hasta aquí aprendiste las piezas por separado: pandas para las tablas, <code>if</code> para
decidir, <code>for</code> y <code>while</code> para repetir. El salto de calidad de un analista está
en <b>combinarlas</b> para responder preguntas reales sobre los datos y, al final, <b>tomar
decisiones</b>: el corazón de PyChoice.</p>

<p><b>Filtrar con condiciones (la forma vectorizada).</b> Ya viste el filtro booleano:
<code>datos[datos["ventas"] &gt; media]</code> deja solo las filas que cumplen la regla. Esta es la
manera <b>preferida</b> de filtrar en pandas porque opera sobre toda la columna a la vez, sin
escribir un bucle. Puedes combinar condiciones con <code>&amp;</code> (y) y <code>|</code> (o),
poniendo cada condición entre paréntesis: <code>datos[(datos["ventas"] &gt; 100) &amp; (datos["region"] == "norte")]</code>.</p>

<p><b>Crear información nueva: columnas derivadas.</b> A partir de las columnas existentes puedes
calcular otras: un ingreso, un margen, un ticket promedio, una razón. Se asigna simplemente:
<code>datos["ticket"] = datos["ventas"] / datos["unidades"]</code>. Así enriqueces la tabla con las
métricas que tu análisis necesita.</p>

<p><b>Clasificar con apply y lambda.</b> Cuando quieres aplicar una <b>regla</b> a cada valor de una
columna (por ejemplo, etiquetar cada venta como "alta" o "baja"), usas <code>apply()</code> junto con
una <b>función lambda</b> (una función corta y anónima):
<code>datos["nivel"] = datos["ventas"].apply(lambda x: "alta" if x &gt; 100 else "baja")</code>. Es
una forma compacta y potente de transformar o categorizar una columna entera.</p>

<p><b>Recorrer fila por fila: iterrows.</b> A veces la lógica es tan específica que conviene recorrer
la tabla fila a fila con <code>for i, fila in datos.iterrows():</code> y decidir dentro con
<code>if</code>. Es muy claro para aprender y para casos puntuales. <b>Pero</b> ten presente que en
tablas grandes es <b>lento</b>: siempre que exista una operación de columna equivalente (un filtro,
un <code>apply</code>, un <code>groupby</code>), esa será más rápida. Aprende <code>iterrows</code>
para entender la lógica, y reserva la vectorización para producir.</p>

<p><b>Resumir con reglas.</b> Combinando filtros con <code>groupby</code> y <code>agg</code>
respondes preguntas cada vez más finas: "promedio de ventas por región, solo en los meses sobre la
meta", por ejemplo. Y con un <b>acumulador</b> dentro de un bucle puedes contar o sumar exactamente
lo que definas.</p>

<p><b>Del dato a la decisión.</b> Todo este recorrido tiene un fin: <b>decidir con datos</b>. Un
análisis no termina en un número, sino en una conclusión accionable: qué región reforzar, qué
producto impulsar, si se cumplió la meta. Esa es, precisamente, la promesa de PyChoice: aprender
Python para <b>tomar mejores decisiones basadas en datos</b>. Con lo aprendido en estas ocho
lecciones ya tienes la base para hacerlo.</p>
""",
        "examples": [
            {
                "title": "Filtrar con una condición",
                "explain": "Nos quedamos solo con las filas cuyas ventas superan la media.",
                "code": 'media = datos["ventas"].mean()\naltas = datos[datos["ventas"] > media]\nprint("media:", round(media, 1))\nprint(altas[["mes", "region", "ventas"]])',
            },
            {
                "title": "Crear una columna derivada",
                "explain": "Nueva columna: ventas por unidad (ticket promedio).",
                "code": 'datos["ticket"] = (datos["ventas"] / datos["unidades"]).round(1)\nprint(datos[["mes", "ventas", "unidades", "ticket"]])',
            },
            {
                "title": "Recorrer filas con for + if",
                "explain": "<code>iterrows()</code> entrega cada fila; con <code>if</code> la clasificamos.",
                "code": 'for i, fila in datos.iterrows():\n    estado = "alta" if fila["ventas"] > 100 else "baja"\n    print(fila["mes"], fila["ventas"], "->", estado)',
            },
            {
                "title": "Acumular con un bucle y una condición",
                "explain": "Contamos y sumamos solo las ventas de la región norte.",
                "code": 'suma = 0\ncuenta = 0\nfor i, fila in datos.iterrows():\n    if fila["region"] == "norte":\n        suma += fila["ventas"]\n        cuenta += 1\nprint("ventas norte:", suma, "en", cuenta, "meses")',
            },
            {
                "title": "Clasificar una columna con apply",
                "explain": "<code>apply()</code> aplica una regla a cada valor y crea una categoría.",
                "code": 'datos["nivel"] = datos["ventas"].apply(lambda x: "alta" if x > 100 else "baja")\nprint(datos[["mes", "ventas", "nivel"]])\nprint(datos["nivel"].value_counts())',
            },
            {
                "title": "Reporte final: filtrar, agrupar y exportar",
                "explain": "Combinamos todo y dejamos un resumen. Prueba <b>exportar excel</b> con el objeto <code>resumen</code>.",
                "code": 'resumen = datos.groupby("region")["ventas"].agg(["mean", "sum", "count"]).round(1)\nprint(resumen)',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Filtra las filas donde <code>unidades</code> sea mayor o igual a 10.",
            "Crea una columna <code>ingreso = ventas * 1000</code> y muéstrala.",
            "Con <code>iterrows()</code> y un <code>if</code>, cuenta cuántos meses fueron de región \"sur\".",
            "Agrupa por <code>region</code>, calcula la media de ventas y expórtala a Excel.",
            "Crea una columna <code>nivel</code> con <code>apply()</code>: <code>\"alta\"</code> si <code>ventas &gt; 100</code>, si no <code>\"baja\"</code>.",
            "Filtra las filas con <code>ventas &gt; 100</code> <b>y</b> <code>region == \"norte\"</code> (condición combinada con <code>&amp;</code>).",
            "Con un acumulador y un <code>for</code>, suma las <code>unidades</code> solo de los meses con <code>ventas &gt; 100</code>.",
            "Reporte final: agrupa por <code>region</code>, calcula media y suma de <code>ventas</code>, ordénalo y muéstralo.",
            "Crea una columna <code>cumple_meta</code> que sea <code>True</code> si <code>ventas &gt;= 100</code> y cuenta cuántos <code>True</code> hay.",
        ],
    },
]
