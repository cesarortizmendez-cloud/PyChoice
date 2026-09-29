# -*- coding: utf-8 -*-
"""
PyChoice - Modulo F: Visualizacion de datos (Lecciones 21 a 23).
Formato capitulo. En cada consola: np, pd, plt y los datos de ejemplo
`notas` (lista) y `datos` (DataFrame: mes, region, ventas, unidades).
Seaborn se carga bajo demanda al importarlo (loadPackagesFromImports).
"""

CHAPTERS_F = [

    # ============================================================ CAP 21
    {
        "num": 21,
        "slug": "matplotlib",
        "code": "leccion_21",
        "title": "Matplotlib a fondo",
        "subtitle": "Líneas, barras, histogramas y dispersión, con títulos y estilo",
        "apunte": "Lección 21 - Matplotlib",
        "concepts": [
            ("Figura y ejes", "La <b>figura</b> es el lienzo; los <b>ejes</b> (axes) son el área donde se dibuja."),
            ("plt.plot()", "Gráfico de <b>líneas</b>: ideal para mostrar evolución en el tiempo."),
            ("plt.bar()", "Gráfico de <b>barras</b>: comparar categorías."),
            ("plt.hist()", "<b>Histograma</b>: ver la distribución de una variable numérica."),
            ("plt.scatter()", "<b>Dispersión</b>: relación entre dos variables numéricas."),
            ("Títulos y etiquetas", "<code>title()</code>, <code>xlabel()</code>, <code>ylabel()</code> dan contexto al gráfico."),
            ("legend()", "Leyenda que identifica cada serie cuando hay varias."),
            ("subplots()", "Varios gráficos en una misma figura, en una rejilla."),
        ],
        "theory": """
<p><b>Matplotlib</b> es la librería base de visualización en Python: casi todo lo demás (incluido
seaborn) se construye sobre ella. Un gráfico bien hecho comunica en segundos lo que una tabla tardaría
párrafos en decir; por eso visualizar es una habilidad central del analista.</p>

<p><b>Figura y ejes.</b> Todo gráfico vive en una <b>figura</b> (el lienzo) que contiene uno o más
<b>ejes</b> (axes: el área con los datos, las marcas y las escalas). La interfaz más simple es
<code>pyplot</code> (alias <code>plt</code>), que gestiona la figura actual por ti: llamas a
<code>plt.plot(...)</code>, luego a <code>plt.title(...)</code>, y finalmente a <code>plt.show()</code>
para mostrarlo.</p>

<p><b>Elegir el gráfico correcto.</b> Cada tipo de gráfico sirve para algo: <b>líneas</b>
(<code>plot</code>) para evolución en el tiempo; <b>barras</b> (<code>bar</code>) para comparar
categorías; <b>histograma</b> (<code>hist</code>) para ver cómo se distribuye una variable numérica;
<b>dispersión</b> (<code>scatter</code>) para la relación entre dos variables. Usar el gráfico
equivocado confunde en lugar de aclarar.</p>

<p><b>Dar contexto.</b> Un gráfico sin títulos ni etiquetas es un acertijo. Siempre conviene añadir
<code>title()</code> (qué muestra), <code>xlabel()</code> e <code>ylabel()</code> (qué representa cada
eje) y, cuando hay varias series, una <code>legend()</code> que las identifique. Estos detalles son la
diferencia entre un gráfico útil y uno inútil.</p>

<p><b>Personalizar.</b> Casi todo se puede ajustar: el <b>color</b> (<code>color="..."</code>), el
grosor, el estilo de línea, el tamaño de la figura (<code>figsize</code>). La personalización no es
decoración: bien usada, dirige la atención al mensaje. Mal usada, distrae. Menos suele ser más.</p>

<p><b>Varios gráficos juntos.</b> Con <code>plt.subplots(filas, columnas)</code> creas una rejilla de
ejes para comparar gráficos lado a lado en una sola figura. Es útil para paneles y comparaciones. En
esta lección trabajarás la interfaz <code>pyplot</code>, la más directa para empezar; con la práctica
descubrirás la interfaz orientada a objetos (<code>fig, ax = plt.subplots()</code>), más flexible para
gráficos complejos.</p>
""",
        "examples": [
            {
                "title": "Gráfico de líneas con contexto",
                "explain": "Evolución en el tiempo, con título y etiquetas de ejes.",
                "code": 'import matplotlib.pyplot as plt\nmeses = ["ene", "feb", "mar", "abr", "may"]\nventas = [120, 95, 130, 110, 88]\nplt.plot(meses, ventas, marker="o", color="#00ff9c")\nplt.title("Ventas por mes")\nplt.xlabel("mes"); plt.ylabel("ventas")\nplt.show()',
            },
            {
                "title": "Gráfico de barras",
                "explain": "Comparar categorías: ventas por región.",
                "code": 'import matplotlib.pyplot as plt\nresumen = datos.groupby("region")["ventas"].sum()\nplt.bar(resumen.index, resumen.values, color="#22d3ee")\nplt.title("Ventas totales por región")\nplt.show()',
            },
            {
                "title": "Histograma",
                "explain": "La distribución de una variable numérica.",
                "code": 'import matplotlib.pyplot as plt\nimport numpy as np\nx = np.random.default_rng(0).normal(100, 15, 300)\nplt.hist(x, bins=20, color="#a87bff", edgecolor="#0b0f14")\nplt.title("Distribución simulada")\nplt.show()',
            },
            {
                "title": "Dispersión con color",
                "explain": "Relación entre dos variables numéricas.",
                "code": 'import matplotlib.pyplot as plt\nplt.scatter(datos["unidades"], datos["ventas"], s=80, color="#ff2e97")\nplt.xlabel("unidades"); plt.ylabel("ventas")\nplt.title("Ventas vs unidades")\nplt.show()',
            },
            {
                "title": "Varias series y leyenda",
                "explain": "Dos líneas en un gráfico, identificadas con leyenda.",
                "code": 'import matplotlib.pyplot as plt\nmeses = ["ene", "feb", "mar", "abr"]\nplt.plot(meses, [120, 95, 130, 110], marker="o", label="norte")\nplt.plot(meses, [80, 100, 90, 120], marker="s", label="sur")\nplt.title("Ventas por región")\nplt.legend()\nplt.show()',
            },
            {
                "title": "Subplots: dos gráficos juntos",
                "explain": "Una figura con dos ejes para comparar.",
                "code": 'import matplotlib.pyplot as plt\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))\nax1.bar(["a", "b", "c"], [3, 7, 5], color="#00ff9c")\nax1.set_title("Barras")\nax2.plot([1, 2, 3, 4], [1, 4, 9, 16], color="#22d3ee")\nax2.set_title("Línea")\nplt.tight_layout()\nplt.show()',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Grafica una línea con los valores de <code>notas</code> y ponle título.",
            "Haz un gráfico de barras de <code>ventas</code> por <code>region</code> (usa groupby).",
            "Grafica un histograma de <code>datos[\"ventas\"]</code>.",
            "Haz un scatter de <code>unidades</code> (x) vs <code>ventas</code> (y) con etiquetas de ejes.",
            "Dibuja dos líneas en un mismo gráfico y agrega una <code>legend()</code>.",
            "Cambia el color y el marcador de una línea.",
            "Crea una figura con <code>subplots(1, 2)</code> y dibuja un gráfico distinto en cada eje.",
            "Añade <code>xlabel</code>, <code>ylabel</code> y <code>title</code> a un gráfico de barras.",
            "Grafica una torta (<code>plt.pie</code>) de las ventas por región.",
        ],
    },

    # ============================================================ CAP 22
    {
        "num": 22,
        "slug": "seaborn",
        "code": "leccion_22",
        "title": "Seaborn: gráficos estadísticos",
        "subtitle": "Visualización estadística de alto nivel, directa desde el DataFrame",
        "apunte": "Lección 22 - Seaborn",
        "concepts": [
            ("Seaborn (sns)", "Librería de visualización construida sobre matplotlib, especializada en gráficos estadísticos."),
            ("Trabaja con DataFrames", "Le pasas el DataFrame y los nombres de columnas: <code>data=df, x=\"...\", y=\"...\"</code>."),
            ("hue", "Agrupa por color según una columna categórica, en un solo gráfico."),
            ("histplot / kdeplot", "Distribución de una variable (histograma / curva de densidad)."),
            ("boxplot / violinplot", "Distribución por categoría, con cuartiles y atípicos."),
            ("scatterplot", "Relación entre dos variables, con opción de color y tamaño por otra."),
            ("heatmap", "Mapa de calor: ideal para la matriz de correlación."),
            ("Estética por defecto", "Seaborn produce gráficos más pulidos con menos código que matplotlib."),
        ],
        "theory": """
<p><b>Seaborn</b> es una librería de visualización construida <b>sobre matplotlib</b> y especializada
en <b>gráficos estadísticos</b>. Su gran ventaja: produce gráficos más pulidos con mucho menos código,
y trabaja <b>directamente con DataFrames</b> de pandas. Para el análisis exploratorio, suele ser más
cómoda que matplotlib puro.</p>

<p><b>La idea clave: datos + nombres.</b> En seaborn no pasas listas de valores, sino el DataFrame y
los <b>nombres de las columnas</b>: <code>sns.scatterplot(data=df, x="unidades", y="ventas")</code>.
Seaborn se encarga de leer las columnas, poner las etiquetas y elegir una estética razonable. Piensa en
qué variable va en cada eje, y él hace el resto.</p>

<p><b>El superpoder: hue.</b> El parámetro <code>hue</code> agrupa por <b>color</b> según una columna
categórica, todo en un mismo gráfico: <code>sns.scatterplot(data=df, x="x", y="y", hue="region")</code>
pinta cada región de un color distinto. Añadir una dimensión con color, sin escribir bucles, es lo que
hace a seaborn tan potente para explorar relaciones.</p>

<p><b>Gráficos estadísticos listos.</b> Seaborn trae de fábrica los gráficos que más usa un analista:
<code>histplot</code> y <code>kdeplot</code> (distribución), <code>boxplot</code> y
<code>violinplot</code> (distribución por categoría), <code>barplot</code> (que además calcula
promedios e intervalos de confianza), <code>countplot</code> (frecuencias) y <code>heatmap</code>
(mapa de calor, perfecto para una matriz de correlación).</p>

<p><b>Convive con matplotlib.</b> Como seaborn dibuja sobre matplotlib, puedes combinar ambos: crear
el gráfico con seaborn y luego ajustar el título o los ejes con <code>plt</code>. No compiten: seaborn
te da un buen punto de partida y matplotlib te da el control fino.</p>

<p><b>En PyChoice.</b> Seaborn se carga <b>la primera vez que lo importas</b> (puede tardar unos
segundos esa primera vez, mientras se descarga; luego queda en caché). Empieza tus ejemplos con
<code>import seaborn as sns</code> y a continuación úsalo con el DataFrame <code>datos</code> o con el
tuyo. Verás lo poco que cuesta obtener un gráfico presentable.</p>
""",
        "examples": [
            {
                "title": "Barras desde el DataFrame",
                "explain": "seaborn calcula el promedio por categoría automáticamente.",
                "code": 'import seaborn as sns\nimport matplotlib.pyplot as plt\nsns.barplot(data=datos, x="region", y="ventas", estimator="mean")\nplt.title("Ventas promedio por región")\nplt.show()',
            },
            {
                "title": "Distribución con histplot",
                "explain": "La distribución de una variable, con una curva de densidad opcional.",
                "code": 'import seaborn as sns\nimport matplotlib.pyplot as plt\nsns.histplot(datos["ventas"], bins=6, kde=True, color="#00ff9c")\nplt.title("Distribución de ventas")\nplt.show()',
            },
            {
                "title": "Boxplot por categoría",
                "explain": "Compara la distribución de ventas entre regiones.",
                "code": 'import seaborn as sns\nimport matplotlib.pyplot as plt\nsns.boxplot(data=datos, x="region", y="ventas")\nplt.title("Ventas por región")\nplt.show()',
            },
            {
                "title": "Dispersión con hue",
                "explain": "El color añade una tercera dimensión: la región.",
                "code": 'import seaborn as sns\nimport matplotlib.pyplot as plt\nsns.scatterplot(data=datos, x="unidades", y="ventas", hue="region", s=100)\nplt.title("Ventas vs unidades por región")\nplt.show()',
            },
            {
                "title": "Mapa de calor de correlación",
                "explain": "Un heatmap muestra la matriz de correlación de un vistazo.",
                "code": 'import seaborn as sns\nimport matplotlib.pyplot as plt\ncorr = datos[["ventas", "unidades"]].corr()\nsns.heatmap(corr, annot=True, cmap="viridis")\nplt.title("Correlación")\nplt.show()',
            },
            {
                "title": "Conteo de categorías (countplot)",
                "explain": "Cuenta cuántas filas hay por categoría, sin agrupar a mano.",
                "code": 'import seaborn as sns\nimport matplotlib.pyplot as plt\nsns.countplot(data=datos, x="region")\nplt.title("Filas por región")\nplt.show()',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Con seaborn, haz un <code>barplot</code> de <code>ventas</code> por <code>region</code>.",
            "Grafica la distribución de <code>unidades</code> con <code>histplot</code> y <code>kde=True</code>.",
            "Haz un <code>boxplot</code> de <code>ventas</code> por <code>region</code>.",
            "Crea un <code>scatterplot</code> de <code>unidades</code> vs <code>ventas</code> con <code>hue=\"region\"</code>.",
            "Muestra un <code>heatmap</code> de la correlación de <code>datos[[\"ventas\", \"unidades\"]]</code>.",
            "Usa <code>countplot</code> para contar filas por <code>region</code>.",
            "Cambia la paleta de colores de un gráfico con el parámetro <code>palette</code>.",
            "Combina seaborn con matplotlib: crea un gráfico y cámbiale el título con <code>plt.title()</code>.",
            "Haz un <code>violinplot</code> de <code>ventas</code> por <code>region</code>.",
        ],
    },

    # ============================================================ CAP 23
    {
        "num": 23,
        "slug": "storytelling",
        "code": "leccion_23",
        "title": "Storytelling con datos",
        "subtitle": "Comunicar un mensaje claro, honesto y memorable con tus gráficos",
        "apunte": "Lección 23 - Storytelling con datos",
        "concepts": [
            ("Mensaje primero", "Antes de graficar, define qué idea quieres que el lector recuerde."),
            ("Gráfico correcto", "El tipo de gráfico debe servir al mensaje, no al revés."),
            ("Título que comunica", "Un buen título dice la conclusión, no solo el tema (\"Las ventas cayeron 20%\", no \"Ventas\")."),
            ("Menos es más", "Elimina lo que no aporta (chart junk): rejillas, bordes y adornos innecesarios."),
            ("Color con propósito", "Usa color para <b>destacar</b> lo importante, no para decorar."),
            ("Orden", "Ordenar las barras (por valor) facilita comparar y leer."),
            ("Anotaciones", "Una nota o etiqueta en el punto clave guía la mirada del lector."),
            ("Honestidad", "No distorsiones: barras desde cero, escalas justas. El gráfico no debe engañar."),
        ],
        "theory": """
<p>Un gráfico técnicamente correcto puede seguir siendo un mal gráfico si no <b>comunica</b>. El
<b>storytelling con datos</b> es el arte de convertir un análisis en un mensaje claro que el público
entienda y recuerde. No es maquillaje: es la diferencia entre que tu trabajo influya en una decisión o
se ignore.</p>

<p><b>El mensaje primero.</b> Antes de abrir matplotlib, pregúntate: <b>¿qué quiero que el lector se
lleve?</b> Un gráfico debería tener <b>una</b> idea principal. Si intentas mostrar todo, no muestras
nada. Definido el mensaje, eliges el gráfico que mejor lo sirva y descartas el resto.</p>

<p><b>El título hace el trabajo.</b> El error más común es titular con el <b>tema</b> ("Ventas por
mes") en lugar de la <b>conclusión</b> ("Las ventas cayeron 20% en marzo"). Un título que afirma el
mensaje hace que el lector lo capte aunque no analice el gráfico en detalle. Es el elemento más leído:
aprovéchalo.</p>

<p><b>Menos es más.</b> Todo elemento que no aporta al mensaje —rejillas densas, bordes, colores
llamativos, decoraciones— es <b>ruido</b> (lo que Edward Tufte llamó <i>chart junk</i>). Quitarlo hace
que el dato resalte. Un gráfico limpio no es aburrido: es <b>legible</b>. El <b>color</b> se reserva
para <b>destacar</b> lo importante: si todo es de colores, nada resalta; si una sola barra es de color
y el resto gris, la mirada va directo a ella.</p>

<p><b>Facilitar la lectura.</b> Detalles que ayudan: <b>ordenar</b> las barras por valor (comparar es
más fácil), <b>anotar</b> el punto clave con una etiqueta o flecha, y usar etiquetas directas en vez de
leyendas cuando se puede. La meta es que el lector entienda sin esfuerzo.</p>

<p><b>Honestidad ante todo.</b> Un gráfico puede mentir sin mentir en los números: un eje que no
empieza en cero exagera diferencias, una escala manipulada distorsiona una tendencia. La ética del
analista incluye <b>no engañar</b>, ni siquiera para reforzar tu punto. Un gráfico honesto y claro
genera confianza; uno tramposo, tarde o temprano, la destruye. Comunicar bien y con integridad es la
habilidad que corona todo lo que has aprendido en esta ruta.</p>
""",
        "examples": [
            {
                "title": "El título comunica el mensaje",
                "explain": "Compara un título genérico con uno que dice la conclusión.",
                "code": 'import matplotlib.pyplot as plt\nmeses = ["ene", "feb", "mar", "abr"]\nv = [120, 118, 95, 92]\nplt.plot(meses, v, marker="o", color="#ff2e97")\nplt.title("Las ventas cayeron 21% desde febrero")  # conclusión, no solo el tema\nplt.ylabel("ventas")\nplt.show()',
            },
            {
                "title": "Ordenar las barras",
                "explain": "Ordenadas por valor, comparar es inmediato.",
                "code": 'import matplotlib.pyplot as plt\nresumen = datos.groupby("region")["ventas"].sum().sort_values()\nplt.barh(resumen.index, resumen.values, color="#22d3ee")\nplt.title("Ventas por región (ordenadas)")\nplt.show()',
            },
            {
                "title": "Destacar con color",
                "explain": "Una barra de color y el resto en gris: la mirada va al dato clave.",
                "code": 'import matplotlib.pyplot as plt\ncats = ["A", "B", "C", "D"]\nvals = [30, 45, 80, 40]\ncolores = ["#3a4a5c"] * 4\ncolores[2] = "#00ff9c"   # destacamos la mayor\nplt.bar(cats, vals, color=colores)\nplt.title("El producto C lidera las ventas")\nplt.show()',
            },
            {
                "title": "Menos es más (quitar ruido)",
                "explain": "Eliminamos bordes superiores y derechos para limpiar el gráfico.",
                "code": 'import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nax.bar(["a", "b", "c"], [3, 7, 5], color="#00ff9c")\nax.spines["top"].set_visible(False)\nax.spines["right"].set_visible(False)\nax.set_title("Gráfico limpio")\nplt.show()',
            },
            {
                "title": "Anotar el punto clave",
                "explain": "Una etiqueta guía la mirada hacia lo importante.",
                "code": 'import matplotlib.pyplot as plt\nmeses = ["ene", "feb", "mar", "abr"]\nv = [120, 95, 130, 88]\nplt.plot(meses, v, marker="o", color="#22d3ee")\nplt.annotate("máximo", xy=("mar", 130), xytext=("feb", 140),\n             arrowprops=dict(arrowstyle="->", color="#ff2e97"))\nplt.title("Ventas por mes")\nplt.show()',
            },
            {
                "title": "Honestidad: el eje desde cero",
                "explain": "En barras, empezar el eje Y en 0 evita exagerar diferencias.",
                "code": 'import matplotlib.pyplot as plt\nplt.bar(["A", "B"], [102, 100], color="#a87bff")\nplt.ylim(0, 120)   # desde cero, la diferencia real (2%) se ve honesta\nplt.title("Diferencia real entre A y B")\nplt.show()',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Toma un gráfico de barras y cámbiale el título por uno que exprese la <b>conclusión</b>.",
            "Ordena de mayor a menor las barras de ventas por región antes de graficar.",
            "Destaca con color la barra más alta y deja el resto en gris.",
            "Quita los bordes superior y derecho de un gráfico con <code>spines</code>.",
            "Anota el valor máximo de una serie con <code>plt.annotate()</code>.",
            "Haz un gráfico de barras con el eje Y empezando en 0 (<code>ylim</code>).",
            "Reemplaza una leyenda por una etiqueta directa sobre la línea correspondiente.",
            "Elige un dataset y escribe, en un comentario, cuál es el mensaje principal antes de graficarlo.",
            "Compara el mismo dato con el eje desde 0 y con el eje recortado; observa cómo cambia la percepción.",
        ],
    },
]
