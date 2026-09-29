# -*- coding: utf-8 -*-
"""
PyChoice - Modulo E: Analisis exploratorio de datos (Lecciones 18 a 20).
Formato capitulo. En cada consola: np, pd, plt y los datos de ejemplo
`notas` (lista) y `datos` (DataFrame: mes, region, ventas, unidades).
"""

CHAPTERS_E = [

    # ============================================================ CAP 18
    {
        "num": 18,
        "slug": "eda",
        "code": "leccion_18",
        "title": "Análisis exploratorio: preguntar a los datos",
        "subtitle": "Mirar, resumir y detectar problemas antes de concluir",
        "apunte": "Lección 18 - EDA",
        "concepts": [
            ("EDA", "Análisis Exploratorio de Datos: la fase de <b>entender</b> los datos antes de modelar o concluir."),
            ("Primer vistazo", "<code>head()</code>, <code>tail()</code> y <code>sample()</code> muestran filas para hacerse una idea."),
            ("info()", "Resumen de columnas: nombres, tipos y cuántos valores no nulos tiene cada una."),
            ("describe()", "Resumen estadístico de las columnas numéricas (y, con <code>include=\"object\"</code>, de las de texto)."),
            ("shape / dtypes", "<code>shape</code> da (filas, columnas); <code>dtypes</code>, el tipo de cada columna."),
            ("value_counts()", "Frecuencia de cada categoría en una columna."),
            ("nunique()", "Cuántos valores <b>distintos</b> tiene una columna."),
            ("Hipótesis", "EDA es un diálogo: mirar los datos sugiere preguntas, y cada pregunta se responde con una consulta."),
        ],
        "theory": """
<p>Antes de modelar, graficar bonito o sacar conclusiones, un buen analista <b>explora</b>. El
<b>Análisis Exploratorio de Datos</b> (EDA, por sus siglas en inglés) es la fase de <b>entender</b> el
conjunto: qué contiene, qué forma tiene, qué problemas esconde y qué preguntas vale la pena hacerle.
Saltarse esta fase es la causa número uno de conclusiones erróneas.</p>

<p><b>El primer vistazo.</b> Al recibir una tabla nueva, lo primero es <b>mirarla</b>:
<code>head()</code> muestra las primeras filas, <code>tail()</code> las últimas y
<code>sample()</code> unas al azar (útil para no dejarse engañar por el orden). <code>shape</code> te
dice cuántas filas y columnas hay, y <code>columns</code> los nombres. En segundos te haces una idea
del tamaño y la estructura.</p>

<p><b>La radiografía: info().</b> <code>df.info()</code> es una de las órdenes más valiosas: lista
cada columna con su <b>tipo</b> y cuántos <b>valores no nulos</b> tiene. De un vistazo detectas
columnas con datos faltantes y tipos incorrectos (un número guardado como texto, por ejemplo). Es el
punto de partida de la limpieza.</p>

<p><b>El resumen: describe().</b> <code>df.describe()</code> entrega, para cada columna numérica, el
conteo, la media, la desviación, el mínimo, los cuartiles y el máximo. Aquí ya empiezan a saltar
señales: un mínimo negativo donde no debería, un máximo absurdo, una media muy lejos de la mediana.
Para columnas de texto, <code>describe(include="object")</code> muestra cuántas categorías hay y cuál
es la más frecuente.</p>

<p><b>Las categóricas.</b> Para las variables de texto (región, producto…), la herramienta clave es
<code>value_counts()</code>, que cuenta cuántas veces aparece cada categoría, y <code>nunique()</code>,
que dice cuántas categorías distintas hay. Así descubres, por ejemplo, que la columna "región" tiene
"Norte", "norte" y "NORTE" como si fueran distintas (una señal de que hay que limpiar).</p>

<p><b>EDA es un diálogo.</b> No es una lista fija de pasos, sino una <b>conversación</b> con los
datos: miras, algo te llama la atención, formulas una pregunta ("¿qué región vende más?"), la
respondes con una consulta, y esa respuesta abre nuevas preguntas. La curiosidad guiada por datos es
la mejor herramienta del analista. Y todo lo que aprendiste antes —filtrar, agrupar, resumir— es el
vocabulario de esa conversación.</p>
""",
        "examples": [
            {
                "title": "Primer vistazo",
                "explain": "Tamaño, columnas, tipos y una muestra de filas.",
                "code": 'print("forma:", datos.shape)\nprint("columnas:", list(datos.columns))\nprint("\\ntipos:\\n", datos.dtypes)\nprint("\\nprimeras filas:\\n", datos.head(3))',
            },
            {
                "title": "La radiografía: info()",
                "explain": "Tipos y valores no nulos por columna: detecta faltantes y tipos.",
                "code": 'datos.info()',
            },
            {
                "title": "Resumen con describe()",
                "explain": "Estadísticos de las columnas numéricas de un vistazo.",
                "code": 'print(datos.describe())',
            },
            {
                "title": "Explorar categóricas",
                "explain": "Cuántas categorías hay y cuántas veces aparece cada una.",
                "code": 'print("regiones distintas:", datos["region"].nunique())\nprint("\\nconteo por región:\\n", datos["region"].value_counts())',
            },
            {
                "title": "Preguntar: promedio por grupo",
                "explain": "Una pregunta típica de EDA respondida con groupby.",
                "code": 'print("¿qué región vende más en promedio?")\nprint(datos.groupby("region")["ventas"].mean().sort_values(ascending=False))',
            },
            {
                "title": "Detectar rarezas",
                "explain": "Mínimos y máximos ayudan a encontrar valores sospechosos.",
                "code": 'print("ventas -> min:", datos["ventas"].min(), "max:", datos["ventas"].max())\nprint("unidades -> min:", datos["unidades"].min(), "max:", datos["unidades"].max())',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Muestra la forma (<code>shape</code>) y los tipos (<code>dtypes</code>) de <code>datos</code>.",
            "Ejecuta <code>datos.info()</code> e identifica si hay columnas con faltantes.",
            "Muestra el <code>describe()</code> y observa la media y el máximo de <code>ventas</code>.",
            "Cuenta las categorías de <code>region</code> con <code>value_counts()</code>.",
            "Averigua cuántas regiones distintas hay con <code>nunique()</code>.",
            "Muestra 3 filas al azar con <code>sample(3)</code>.",
            "Responde con groupby: ¿qué región tiene más <code>unidades</code> en promedio?",
            "Encuentra el mínimo y el máximo de <code>unidades</code>.",
            "Con <code>describe(include=\"object\")</code>, resume las columnas de texto.",
        ],
    },

    # ============================================================ CAP 19
    {
        "num": 19,
        "slug": "estadistica-descriptiva",
        "code": "leccion_19",
        "title": "Estadística descriptiva aplicada",
        "subtitle": "Centro, dispersión, cuartiles y detección de atípicos",
        "apunte": "Lección 19 - Estadística descriptiva",
        "concepts": [
            ("Media / mediana / moda", "Tres medidas de centro: promedio, valor central y valor más frecuente."),
            ("Rango", "Diferencia entre el máximo y el mínimo. La medida de dispersión más simple."),
            ("Varianza y desviación", "Cuánto se alejan los datos de la media. <code>std()</code> es la desviación estándar."),
            ("Cuartiles", "Dividen los datos ordenados en cuatro partes: Q1 (25%), Q2 (mediana, 50%) y Q3 (75%)."),
            ("Percentiles / quantile()", "El valor bajo el cual queda cierto porcentaje de los datos."),
            ("IQR", "Rango intercuartílico: Q3 − Q1. Contiene el 50% central de los datos."),
            ("Atípico (outlier)", "Valor anómalo. Regla común: fuera de [Q1 − 1.5·IQR, Q3 + 1.5·IQR]."),
            ("Histograma / boxplot", "Gráficos para ver la forma de la distribución y los atípicos."),
        ],
        "theory": """
<p>La estadística descriptiva resume un conjunto de datos en pocos números que capturan su
<b>centro</b>, su <b>dispersión</b> y su <b>forma</b>. Interpretar bien estas medidas —no solo
calcularlas— es lo que distingue a un analista.</p>

<p><b>Medidas de centro.</b> La <b>media</b> es el promedio; la <b>mediana</b>, el valor que queda en
el medio al ordenar; la <b>moda</b>, el valor más frecuente. Comparar media y mediana es revelador: si
son muy distintas, hay <b>asimetría</b> o valores extremos tirando de la media. En sueldos, por
ejemplo, la mediana suele describir mejor "al típico" que la media.</p>

<p><b>Medidas de dispersión.</b> Dos grupos pueden tener la misma media y ser muy distintos: uno
homogéneo y otro disperso. El <b>rango</b> (máximo − mínimo) es la medida más simple. La
<b>desviación estándar</b> (<code>std</code>) mide la dispersión promedio respecto a la media: pequeña
= datos parecidos; grande = datos dispersos. La <b>varianza</b> es su cuadrado.</p>

<p><b>Cuartiles y percentiles.</b> Al ordenar los datos y partirlos en cuatro, los <b>cuartiles</b>
marcan los cortes: Q1 deja bajo sí el 25% de los datos, Q2 el 50% (la mediana) y Q3 el 75%. Los
<b>percentiles</b> generalizan la idea a cualquier porcentaje (el percentil 90 es el valor bajo el
cual está el 90% de los datos). Con <code>quantile()</code> los calculas.</p>

<p><b>Detección de atípicos.</b> Un <b>atípico</b> (outlier) es un valor que se aleja mucho del
resto. Una regla muy usada emplea el <b>rango intercuartílico</b> (IQR = Q3 − Q1): se consideran
atípicos los valores fuera del intervalo [Q1 − 1.5·IQR, Q3 + 1.5·IQR]. Detectarlos es importante
porque pueden ser errores de captura… o los casos más interesantes (un fraude, una venta récord). No
se eliminan a ciegas: se <b>investigan</b>.</p>

<p><b>Ver la distribución.</b> Los números se complementan con gráficos. El <b>histograma</b> muestra
cómo se reparten los datos (¿simétricos?, ¿concentrados?, ¿con dos picos?). El <b>diagrama de caja</b>
(<code>boxplot</code>) resume los cuartiles y marca los atípicos visualmente. Una imagen de la
distribución suele decir más que una tabla de medidas.</p>
""",
        "examples": [
            {
                "title": "Medidas de centro",
                "explain": "Media, mediana y moda de una columna.",
                "code": 'v = datos["ventas"]\nprint("media:", round(v.mean(), 2))\nprint("mediana:", v.median())\nprint("moda:", v.mode().tolist())',
            },
            {
                "title": "Medidas de dispersión",
                "explain": "Rango, varianza y desviación estándar.",
                "code": 'v = datos["ventas"]\nprint("rango:", v.max() - v.min())\nprint("varianza:", round(v.var(), 2))\nprint("desv. estándar:", round(v.std(), 2))',
            },
            {
                "title": "Cuartiles y percentiles",
                "explain": "<code>quantile()</code> calcula los cortes por porcentaje.",
                "code": 'v = datos["ventas"]\nprint("Q1 (25%):", v.quantile(0.25))\nprint("Q2 (50%):", v.quantile(0.50))\nprint("Q3 (75%):", v.quantile(0.75))\nprint("percentil 90:", v.quantile(0.90))',
            },
            {
                "title": "Detección de atípicos (IQR)",
                "explain": "Marcamos valores fuera de [Q1 − 1.5·IQR, Q3 + 1.5·IQR].",
                "code": 'import numpy as np\nx = np.array([50, 52, 49, 51, 200, 48, 5])\nq1, q3 = np.percentile(x, [25, 75])\niqr = q3 - q1\nlo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr\nprint("límites:", round(lo, 1), "a", round(hi, 1))\nprint("atípicos:", x[(x < lo) | (x > hi)])',
            },
            {
                "title": "Histograma",
                "explain": "Un histograma muestra la forma de la distribución.",
                "code": 'import matplotlib.pyplot as plt\nimport numpy as np\ndatos_sim = np.random.default_rng(1).normal(100, 15, 200)\nplt.hist(datos_sim, bins=15, color="#00ff9c", edgecolor="#0b0f14")\nplt.title("Distribución simulada")\nplt.show()',
            },
            {
                "title": "Diagrama de caja (boxplot)",
                "explain": "El boxplot resume cuartiles y marca atípicos.",
                "code": 'import matplotlib.pyplot as plt\nplt.boxplot(datos["ventas"], vert=False)\nplt.title("Ventas")\nplt.show()',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Calcula media, mediana y moda de <code>datos[\"unidades\"]</code>.",
            "Calcula el rango y la desviación estándar de <code>ventas</code>.",
            "Obtén Q1, Q2 y Q3 de <code>ventas</code> con <code>quantile()</code>.",
            "Calcula el percentil 90 de <code>unidades</code>.",
            "Aplica la regla del IQR a <code>[10, 12, 11, 13, 90, 9]</code> y encuentra el atípico.",
            "Grafica un histograma de la lista <code>notas</code>.",
            "Grafica un boxplot de <code>datos[\"unidades\"]</code>.",
            "Compara la media y la mediana de <code>ventas</code>: ¿hay asimetría?",
            "Calcula el IQR de <code>ventas</code> (Q3 − Q1).",
        ],
    },

    # ============================================================ CAP 20
    {
        "num": 20,
        "slug": "correlacion",
        "code": "leccion_20",
        "title": "Correlación y relaciones",
        "subtitle": "¿Cómo se relacionan dos variables? Correlación, dispersión y cruces",
        "apunte": "Lección 20 - Correlación y relaciones",
        "concepts": [
            ("Correlación", "Mide si dos variables numéricas se mueven juntas. Va de −1 a +1."),
            ("Coef. de Pearson", "El más común: +1 relación positiva perfecta, −1 negativa perfecta, 0 sin relación lineal."),
            ("corr()", "Calcula la correlación entre columnas; sobre un DataFrame da la <b>matriz de correlación</b>."),
            ("Gráfico de dispersión", "<code>scatter</code>: cada punto es una observación (x, y). Revela la forma de la relación."),
            ("Correlación ≠ causalidad", "Que dos cosas se muevan juntas no significa que una cause la otra."),
            ("crosstab()", "Tabla cruzada de frecuencias entre dos variables categóricas."),
            ("Relación por grupos", "Comparar una medida entre grupos también revela relaciones (groupby)."),
            ("Variable de confusión", "Un tercer factor que explica una correlación aparente entre otras dos."),
        ],
        "theory": """
<p>Gran parte del análisis consiste en buscar <b>relaciones</b>: ¿a mayor publicidad, más ventas?, ¿el
precio afecta la demanda?, ¿qué regiones se parecen? Detectar y medir cómo se relacionan las variables
es el corazón del análisis exploratorio avanzado.</p>

<p><b>Correlación.</b> Entre dos variables numéricas, la <b>correlación</b> mide si tienden a moverse
<b>juntas</b>. El <b>coeficiente de Pearson</b> va de <b>−1 a +1</b>: cerca de +1, cuando una sube la
otra sube (relación positiva fuerte); cerca de −1, cuando una sube la otra baja (negativa); cerca de
0, no hay relación lineal. Con <code>df.corr()</code> obtienes la <b>matriz de correlación</b> de todas
las columnas numéricas a la vez.</p>

<p><b>Verla: el gráfico de dispersión.</b> El número resume, pero el <b>scatter</b>
(<code>plt.scatter(x, y)</code>) muestra la relación real: cada punto es una observación. Una nube que
sube de izquierda a derecha indica correlación positiva; una que baja, negativa; una sin patrón, poca
relación. El gráfico también revela relaciones <b>no lineales</b> que la correlación de Pearson no
capta.</p>

<p><b>La advertencia más importante: correlación no es causalidad.</b> Que dos variables estén
correlacionadas <b>no</b> significa que una <b>cause</b> la otra. El ejemplo clásico: las ventas de
helados y los ahogamientos suben juntas… no porque el helado ahogue, sino por una <b>variable de
confusión</b>: el calor. Confundir correlación con causalidad es el error de interpretación más común
y más costoso. Ante una correlación, la pregunta correcta es "¿por qué?", no "¿cuál causa cuál?".</p>

<p><b>Relaciones entre categóricas.</b> Cuando las variables son categorías (región y tipo de
cliente, por ejemplo), la correlación numérica no aplica. Ahí se usa <b>crosstab</b>: una tabla que
cuenta cuántas observaciones caen en cada combinación. Y comparar una medida entre grupos
(<code>groupby</code>) es otra forma directa de ver si el grupo se relaciona con el resultado.</p>

<p><b>El criterio del analista.</b> Las herramientas dicen <i>qué</i> variables se relacionan; el
<b>criterio y el conocimiento del dominio</b> dicen <i>qué significa</i>. Medir es fácil; interpretar
con honestidad —sin exagerar ni inventar causas— es la verdadera habilidad. Con esto cierras el
análisis exploratorio y quedas listo para comunicar hallazgos y, más adelante, modelar.</p>
""",
        "examples": [
            {
                "title": "Correlación entre dos columnas",
                "explain": "Un valor cercano a +1 indica que suben juntas.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({\n    "publicidad": [10, 20, 30, 40, 50],\n    "ventas": [100, 140, 190, 230, 300],\n})\nprint("correlación:", round(df["publicidad"].corr(df["ventas"]), 3))',
            },
            {
                "title": "Matriz de correlación",
                "explain": "<code>corr()</code> sobre el DataFrame relaciona todas las columnas numéricas.",
                "code": 'print(datos[["ventas", "unidades"]].corr())',
            },
            {
                "title": "Gráfico de dispersión",
                "explain": "Cada punto es una observación; la nube muestra la relación.",
                "code": 'import matplotlib.pyplot as plt\nplt.scatter(datos["unidades"], datos["ventas"], color="#22d3ee")\nplt.xlabel("unidades"); plt.ylabel("ventas")\nplt.title("Ventas vs unidades")\nplt.show()',
            },
            {
                "title": "Correlación no es causalidad",
                "explain": "Dos series correlacionadas por una causa común (el calor), no entre sí.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({\n    "helados": [10, 30, 60, 90],\n    "ahogamientos": [1, 3, 6, 9],\n})\nprint("correlación:", round(df["helados"].corr(df["ahogamientos"]), 2))\nprint("¡Ojo! ambas suben por el calor, no una por la otra.")',
            },
            {
                "title": "Tabla cruzada (crosstab)",
                "explain": "Frecuencias entre dos variables categóricas.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({\n    "region": ["norte", "sur", "norte", "sur", "norte"],\n    "nivel": ["alto", "bajo", "alto", "alto", "bajo"],\n})\nprint(pd.crosstab(df["region"], df["nivel"]))',
            },
            {
                "title": "Relación por grupos",
                "explain": "Comparar una medida entre grupos también revela relaciones.",
                "code": 'print(datos.groupby("region")[["ventas", "unidades"]].mean())',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Calcula la correlación entre <code>ventas</code> y <code>unidades</code> con <code>corr()</code>.",
            "Muestra la matriz de correlación de <code>datos[[\"ventas\", \"unidades\"]]</code>.",
            "Grafica un scatter de <code>unidades</code> (x) vs <code>ventas</code> (y).",
            "Crea dos listas que suban juntas y calcula su correlación (debería acercarse a 1).",
            "Crea dos listas donde una suba y la otra baje, y calcula su correlación (cercana a −1).",
            "Explica con tus palabras, en un comentario, por qué correlación no implica causalidad.",
            "Con <code>crosstab</code>, cruza <code>region</code> con una columna categórica que inventes.",
            "Compara la media de <code>ventas</code> por <code>region</code> con <code>groupby</code>.",
            "Grafica un scatter y colorea los puntos; observa si hay tendencia.",
        ],
    },
]
