# -*- coding: utf-8 -*-
"""
PyChoice - Modulo G: Estadistica y probabilidad (Lecciones 24 a 26).
Formato capitulo. En cada consola: np, pd, plt y los datos de ejemplo
`notas` (lista) y `datos` (DataFrame). scipy se carga bajo demanda al
importarlo (loadPackagesFromImports en pyengine.js).
"""

CHAPTERS_G = [

    # ============================================================ CAP 24
    {
        "num": 24,
        "slug": "probabilidad",
        "code": "leccion_24",
        "title": "Probabilidad básica",
        "subtitle": "Medir la incertidumbre y simularla con Python",
        "apunte": "Lección 24 - Probabilidad",
        "concepts": [
            ("Probabilidad", "Una medida entre 0 y 1 de qué tan posible es un evento. 0 = imposible, 1 = seguro."),
            ("Espacio muestral", "Todos los resultados posibles de un experimento (para un dado: 1,2,3,4,5,6)."),
            ("Evento", "Un subconjunto de resultados que nos interesa (por ejemplo, \"sacar par\")."),
            ("Frecuencia relativa", "La proporción de veces que ocurre un evento al repetir el experimento."),
            ("Ley de los grandes números", "Al aumentar las repeticiones, la frecuencia relativa se acerca a la probabilidad teórica."),
            ("Independencia", "Dos eventos son independientes si uno no afecta la probabilidad del otro."),
            ("Probabilidad condicional", "La probabilidad de un evento <b>dado</b> que otro ya ocurrió: P(A | B)."),
            ("Simulación", "Estimar probabilidades repitiendo el experimento con números aleatorios (Monte Carlo)."),
        ],
        "theory": """
<p>La <b>probabilidad</b> es el lenguaje de la incertidumbre. Casi ninguna decisión con datos es
totalmente segura: hablamos de qué tan <b>probable</b> es un resultado. Formalmente, la probabilidad
de un evento es un número entre <b>0</b> (imposible) y <b>1</b> (seguro); un 0.5 significa "la mitad de
las veces".</p>

<p><b>Los ingredientes.</b> Un <b>experimento</b> tiene un <b>espacio muestral</b> (todos los
resultados posibles) y nos interesan ciertos <b>eventos</b> (subconjuntos de resultados). Para un dado
justo, el espacio es {1,2,3,4,5,6} y el evento "sacar par" es {2,4,6}, con probabilidad 3/6 = 0.5. Esta
es la probabilidad <b>teórica</b>: la calculamos por conteo.</p>

<p><b>Frecuencia relativa.</b> En la práctica, muchas veces no conocemos la probabilidad teórica y la
<b>estimamos</b> repitiendo el experimento y midiendo la <b>frecuencia relativa</b>: la proporción de
veces que ocurre el evento. Si lanzas una moneda 1000 veces y sale cara 503, estimas P(cara) ≈ 0.503.</p>

<p><b>La ley de los grandes números.</b> ¿Por qué funciona estimar así? Por la <b>ley de los grandes
números</b>: cuantas más repeticiones haces, más se acerca la frecuencia relativa a la probabilidad
verdadera. Con 10 lanzamientos puedes obtener 0.7 de caras por azar; con 100.000, estarás muy cerca de
0.5. Es el fundamento de la estadística.</p>

<p><b>Combinar eventos.</b> Dos eventos son <b>independientes</b> si uno no afecta al otro (dos monedas
distintas). Para eventos independientes, la probabilidad de que ocurran <b>ambos</b> es el producto:
P(A y B) = P(A)·P(B). La <b>probabilidad condicional</b> P(A | B) es la probabilidad de A <b>dado</b>
que B ocurrió, y es la base de razonamientos más avanzados (como el teorema de Bayes).</p>

<p><b>Simular con Python.</b> Una de las cosas más poderosas que permite la programación es
<b>simular</b>: en lugar de calcular a mano, repetimos el experimento miles de veces con números
aleatorios (<code>numpy.random</code>) y medimos la frecuencia. Es el método de <b>Monte Carlo</b>, y
resuelve problemas de probabilidad que serían difíciles con fórmulas. En esta lección lo usarás para
"ver" la probabilidad en acción.</p>
""",
        "examples": [
            {
                "title": "Simular lanzar una moneda",
                "explain": "Generamos 0/1 al azar y medimos la proporción de caras (frecuencia relativa).",
                "code": 'import numpy as np\nrng = np.random.default_rng(0)\nlanzamientos = rng.integers(0, 2, size=1000)  # 0 = sello, 1 = cara\nprint("caras en 1000 lanzamientos:", lanzamientos.sum())\nprint("proporción de caras:", lanzamientos.mean())',
            },
            {
                "title": "Ley de los grandes números",
                "explain": "Con más lanzamientos, la proporción se acerca a 0.5.",
                "code": 'import numpy as np\nrng = np.random.default_rng(1)\nfor n in [10, 100, 1000, 100000]:\n    prop = rng.integers(0, 2, n).mean()\n    print(f"{n:>6} lanzamientos -> {prop:.3f}")',
            },
            {
                "title": "Probabilidad de un evento (dado)",
                "explain": "Estimamos P(sacar 5 o 6) simulando un dado muchas veces.",
                "code": 'import numpy as np\nrng = np.random.default_rng(2)\ndado = rng.integers(1, 7, size=10000)\nprint("P(5 o 6) estimada:", (dado >= 5).mean())\nprint("teórica:", round(2/6, 3))',
            },
            {
                "title": "Eventos independientes (P de ambos)",
                "explain": "Dos monedas: P(ambas caras) ≈ 0.5 × 0.5 = 0.25.",
                "code": 'import numpy as np\nrng = np.random.default_rng(3)\na = rng.integers(0, 2, 10000)\nb = rng.integers(0, 2, 10000)\nprint("P(ambas caras):", ((a == 1) & (b == 1)).mean())',
            },
            {
                "title": "Distribución de la suma de dos dados",
                "explain": "Simulamos y vemos qué sumas son más probables (el 7 lidera).",
                "code": 'import numpy as np, pandas as pd\nrng = np.random.default_rng(4)\nsuma = rng.integers(1, 7, 10000) + rng.integers(1, 7, 10000)\nprint(pd.Series(suma).value_counts(normalize=True).sort_index().round(3))',
            },
            {
                "title": "Probabilidad condicional",
                "explain": "P(suma ≥ 8 dado que el primer dado fue 6), estimada por simulación.",
                "code": 'import numpy as np\nrng = np.random.default_rng(5)\nd1 = rng.integers(1, 7, 100000)\nd2 = rng.integers(1, 7, 100000)\nsuma = d1 + d2\ncond = d1 == 6\nprint("P(suma>=8 | d1=6):", round((suma[cond] >= 8).mean(), 3))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Simula 2000 lanzamientos de una moneda y calcula la proporción de sellos.",
            "Muestra cómo la proporción de caras se acerca a 0.5 al aumentar los lanzamientos.",
            "Simula un dado y estima la probabilidad de sacar un número par.",
            "Estima P(sacar un 6) con un dado simulado 10.000 veces y compárala con 1/6.",
            "Con dos monedas independientes, estima P(al menos una cara).",
            "Simula la suma de dos dados y encuentra cuál suma es la más frecuente.",
            "Estima P(suma = 7) al lanzar dos dados.",
            "Estima P(el segundo dado sea par | el primero fue 1).",
            "Simula extraer una carta y estima la probabilidad de que sea de corazones (13 de 52).",
        ],
    },

    # ============================================================ CAP 25
    {
        "num": 25,
        "slug": "distribuciones",
        "code": "leccion_25",
        "title": "Distribuciones de probabilidad",
        "subtitle": "Normal, binomial, uniforme y Poisson: modelar el azar",
        "apunte": "Lección 25 - Distribuciones",
        "concepts": [
            ("Variable aleatoria", "Una cantidad cuyo valor depende del azar (el resultado de un dado, una altura)."),
            ("Distribución", "Describe qué valores toma una variable aleatoria y con qué probabilidad."),
            ("Distribución normal", "La \"campana de Gauss\": simétrica, definida por su media (μ) y desviación (σ). Muy común en la naturaleza."),
            ("Regla 68-95-99.7", "En una normal, ~68% de los datos caen a ±1σ, ~95% a ±2σ y ~99.7% a ±3σ."),
            ("Binomial", "Cuenta éxitos en n intentos con probabilidad p (caras en 10 lanzamientos)."),
            ("Uniforme", "Todos los valores de un rango son igualmente probables."),
            ("Poisson", "Cuenta eventos raros en un intervalo (llamadas por hora, con tasa λ)."),
            ("scipy.stats", "El módulo con todas las distribuciones: <code>pdf</code>/<code>pmf</code>, <code>cdf</code>, <code>ppf</code>."),
        ],
        "theory": """
<p>Una <b>variable aleatoria</b> es una cantidad cuyo valor depende del azar. Su comportamiento se
describe con una <b>distribución de probabilidad</b>: qué valores puede tomar y con qué probabilidad
cada uno. Reconocer la distribución de tus datos te permite modelarlos, hacer predicciones y aplicar la
herramienta estadística correcta.</p>

<p><b>La distribución normal.</b> Es la más importante: la famosa <b>campana de Gauss</b>, simétrica en
torno a su <b>media</b> (μ) y con una anchura dada por su <b>desviación estándar</b> (σ). Aparece por
todas partes —alturas, errores de medición, promedios— gracias a un resultado profundo (el teorema
central del límite). Una guía práctica es la <b>regla 68-95-99.7</b>: alrededor del 68% de los datos
caen dentro de ±1σ de la media, el 95% dentro de ±2σ y el 99.7% dentro de ±3σ. Con eso ya intuyes qué
es "normal" y qué es "raro" en tus datos.</p>

<p><b>La binomial.</b> Modela el número de <b>éxitos</b> en <code>n</code> intentos independientes,
cada uno con probabilidad <code>p</code> de éxito: cuántas caras en 10 lanzamientos, cuántos clientes
compran de 100 visitas. Es discreta (cuenta enteros) y se resume con dos parámetros: n y p.</p>

<p><b>La uniforme y la de Poisson.</b> En la <b>uniforme</b>, todos los valores de un rango son
igualmente probables (como elegir un número al azar entre 0 y 1). La <b>de Poisson</b> cuenta cuántos
<b>eventos raros</b> ocurren en un intervalo fijo (llamadas a un call center por hora, defectos por
lote), gobernada por una tasa media <code>λ</code>. Cada distribución encaja con un tipo de fenómeno.</p>

<p><b>PDF/PMF, CDF y cuantiles.</b> Toda distribución se manipula con tres funciones. La <b>PDF</b>
(densidad, para continuas) o <b>PMF</b> (masa, para discretas) da la probabilidad de un valor. La
<b>CDF</b> (acumulada) da la probabilidad de estar <b>por debajo</b> de un valor. Y la función
<b>cuantil</b> (<code>ppf</code>) hace lo inverso: qué valor deja bajo sí cierto porcentaje. Con estas
tres respondes casi cualquier pregunta.</p>

<p><b>scipy.stats.</b> En Python, la librería <b>scipy</b> trae todas las distribuciones listas en el
módulo <code>scipy.stats</code>: <code>norm</code>, <code>binom</code>, <code>uniform</code>,
<code>poisson</code> y muchas más, cada una con <code>pdf</code>/<code>pmf</code>, <code>cdf</code> y
<code>ppf</code>. En PyChoice, scipy se descarga la primera vez que lo importas. Combinado con
<code>numpy</code> para simular y <code>matplotlib</code> para graficar, tienes un laboratorio de
probabilidad completo.</p>
""",
        "examples": [
            {
                "title": "La distribución normal",
                "explain": "Generamos datos normales y los graficamos: la campana de Gauss.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nx = np.random.default_rng(0).normal(100, 15, 1000)\nplt.hist(x, bins=25, color="#00ff9c", edgecolor="#0b0f14")\nplt.title("Normal: media=100, desv=15")\nplt.show()',
            },
            {
                "title": "Regla 68-95-99.7",
                "explain": "Contamos qué proporción cae dentro de 1, 2 y 3 desviaciones.",
                "code": 'import numpy as np\nz = np.random.default_rng(1).normal(0, 1, 100000)\nfor k in [1, 2, 3]:\n    dentro = ((z > -k) & (z < k)).mean() * 100\n    print(f"dentro de +/-{k} sigma: {dentro:.1f}%")',
            },
            {
                "title": "Distribución binomial",
                "explain": "Probabilidad de obtener exactamente k caras en n lanzamientos.",
                "code": 'from scipy.stats import binom\nprint("P(3 caras en 10, p=0.5):", round(binom.pmf(3, 10, 0.5), 4))\nprint("P(<=3 caras):", round(binom.cdf(3, 10, 0.5), 4))\nprint("media esperada:", binom.mean(10, 0.5))',
            },
            {
                "title": "Distribución uniforme",
                "explain": "Todos los valores del rango son igualmente probables.",
                "code": 'import numpy as np\nu = np.random.default_rng(2).uniform(0, 10, size=8)\nprint(u.round(2))\nprint("media (esperada ~5):", round(u.mean(), 2))',
            },
            {
                "title": "Normal con scipy: cdf y ppf",
                "explain": "cdf da probabilidad acumulada; ppf da el cuantil (valor z).",
                "code": 'from scipy.stats import norm\nprint("cdf(1.96):", round(norm.cdf(1.96), 4))   # ~0.975\nprint("ppf(0.975):", round(norm.ppf(0.975), 4)) # ~1.96\nprint("P entre -1 y 1:", round(norm.cdf(1) - norm.cdf(-1), 4))',
            },
            {
                "title": "Distribución de Poisson",
                "explain": "Eventos raros con tasa media λ (por ejemplo, 3 llamadas por hora).",
                "code": 'from scipy.stats import poisson\nlam = 3\nprint("P(exactamente 2):", round(poisson.pmf(2, lam), 4))\nprint("P(0 eventos):", round(poisson.pmf(0, lam), 4))\nprint("P(<=1 evento):", round(poisson.cdf(1, lam), 4))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Genera 500 datos normales con media 50 y desviación 10, y grafica su histograma.",
            "Verifica la regla 68-95-99.7 con datos normales estándar.",
            "Con <code>binom</code>, calcula la probabilidad de 5 caras en 8 lanzamientos.",
            "Calcula la probabilidad binomial acumulada de obtener 2 o menos éxitos en 10 con p=0.3.",
            "Genera 10 números uniformes entre 0 y 1 y muestra su media.",
            "Con <code>norm</code>, calcula la probabilidad de que un valor esté entre −2 y 2.",
            "Usa <code>norm.ppf(0.95)</code> para hallar el cuantil 95.",
            "Con <code>poisson</code>, calcula P(exactamente 4 eventos) con λ=2.",
            "Grafica un histograma de datos binomiales simulados con <code>rng.binomial(10, 0.5, 1000)</code>.",
        ],
    },

    # ============================================================ CAP 26
    {
        "num": 26,
        "slug": "inferencia",
        "code": "leccion_26",
        "title": "Inferencia: intervalos y pruebas de hipótesis",
        "subtitle": "De la muestra a la población: estimar y decidir con evidencia",
        "apunte": "Lección 26 - Inferencia estadística",
        "concepts": [
            ("Población vs muestra", "La <b>población</b> es todo; la <b>muestra</b> es la parte que observamos y con la que estimamos."),
            ("Estimación", "Usar la muestra para aproximar un parámetro de la población (por ejemplo, su media)."),
            ("Error estándar", "Cuánto varía la media muestral de una muestra a otra. Baja al crecer la muestra."),
            ("Intervalo de confianza", "Un rango que, con cierta confianza (95%), contiene el valor real del parámetro."),
            ("Hipótesis nula (H0)", "La afirmación por defecto (\"no hay efecto / no hay diferencia\") que se pone a prueba."),
            ("Valor p", "La probabilidad de ver un resultado así de extremo si H0 fuera verdadera. Pequeño = evidencia contra H0."),
            ("Nivel de significancia", "El umbral (típicamente 0.05) bajo el cual rechazamos H0."),
            ("Prueba t", "Compara medias: de una muestra contra un valor, o entre dos muestras."),
        ],
        "theory": """
<p>Casi nunca podemos medir a <b>toda</b> la población: encuestamos a 1000 personas, no a un país
entero. La <b>inferencia estadística</b> es el arte de sacar conclusiones sobre la <b>población</b> a
partir de una <b>muestra</b>, cuantificando la incertidumbre. Es la culminación de todo lo estadístico
que has visto.</p>

<p><b>Estimar y su incertidumbre.</b> Con la muestra <b>estimamos</b> parámetros de la población (su
media, por ejemplo). Pero cada muestra da un valor algo distinto: esa variabilidad se mide con el
<b>error estándar</b>, que disminuye al aumentar el tamaño de la muestra (más datos, estimación más
estable). Nunca damos un número solo: lo acompañamos de su margen de error.</p>

<p><b>Intervalo de confianza.</b> En lugar de decir "la media es 850", decimos "estoy 95% seguro de
que está entre 820 y 880". Ese es un <b>intervalo de confianza al 95%</b>: un rango que, con esa
confianza, contiene el valor real. Cuanto más grande la muestra, más estrecho (y útil) el intervalo. Es
la forma honesta de reportar una estimación.</p>

<p><b>Pruebas de hipótesis.</b> Muchas preguntas son de <b>sí o no</b>: ¿este cambio mejoró las ventas?
¿los dos grupos difieren de verdad o es azar? El método parte de una <b>hipótesis nula</b> (H0), la
posición escéptica: "no hay efecto". Luego se calcula qué tan probable sería obtener los datos
observados <b>si H0 fuera cierta</b>: ese es el <b>valor p</b>. Un valor p pequeño significa que los
datos serían muy raros bajo H0, así que la <b>rechazamos</b>.</p>

<p><b>El umbral 0.05.</b> Por convención, si el valor p es menor que el <b>nivel de significancia</b>
(típicamente <b>0.05</b>), se considera el resultado <b>estadísticamente significativo</b> y se rechaza
H0. La <b>prueba t</b> es la herramienta clásica para comparar medias: de una muestra contra un valor
esperado (<code>ttest_1samp</code>) o entre dos grupos (<code>ttest_ind</code>).</p>

<p><b>Cautela e interpretación.</b> El valor p es de los conceptos más malinterpretados de la
estadística. <b>No</b> es la probabilidad de que H0 sea cierta, ni mide el tamaño del efecto: solo dice
qué tan compatibles son los datos con H0. "Significativo" no es lo mismo que "importante". Un buen
analista reporta el intervalo de confianza y el tamaño del efecto, no solo si p &lt; 0.05. La estadística
da herramientas; el criterio y la honestidad las convierten en conclusiones confiables.</p>
""",
        "examples": [
            {
                "title": "Población vs muestra",
                "explain": "La media de una muestra aproxima la de la población.",
                "code": 'import numpy as np\nrng = np.random.default_rng(2)\npoblacion = rng.normal(850, 120, 100000)\nprint("media población (parámetro):", round(poblacion.mean(), 1))\nmuestra = rng.choice(poblacion, 50)\nprint("media muestral (estimación):", round(muestra.mean(), 1))',
            },
            {
                "title": "Error estándar de la media",
                "explain": "Mide la variabilidad de la media muestral. Baja con más datos.",
                "code": 'import numpy as np, scipy.stats as stats\ndata = np.array([98, 102, 95, 100, 105, 97, 101, 99])\nprint("media:", data.mean())\nprint("error estándar:", round(stats.sem(data), 3))',
            },
            {
                "title": "Intervalo de confianza (95%)",
                "explain": "Un rango que, con 95% de confianza, contiene la media real.",
                "code": 'import numpy as np, scipy.stats as stats\ndata = np.array([98, 102, 95, 100, 105, 97, 101, 99])\nn = len(data)\nic = stats.t.interval(0.95, df=n-1, loc=data.mean(), scale=stats.sem(data))\nprint("media:", data.mean())\nprint("IC 95%:", tuple(round(v, 2) for v in ic))',
            },
            {
                "title": "Prueba t de una muestra",
                "explain": "¿La media difiere de 100? H0: media = 100.",
                "code": 'import numpy as np, scipy.stats as stats\ndata = np.array([102, 99, 101, 98, 103, 100, 97, 104])\nt, p = stats.ttest_1samp(data, 100)\nprint("t:", round(t, 3), "| p:", round(p, 4))\nprint("¿significativo?", "sí" if p < 0.05 else "no")',
            },
            {
                "title": "Prueba t de dos muestras",
                "explain": "¿Difieren las medias de dos grupos?",
                "code": 'import scipy.stats as stats\ngrupo_a = [80, 82, 85, 79, 88, 81]\ngrupo_b = [90, 92, 87, 95, 91, 89]\nt, p = stats.ttest_ind(grupo_a, grupo_b)\nprint("t:", round(t, 3), "| p:", round(p, 5))\nprint("¿diferencia significativa?", "sí" if p < 0.05 else "no")',
            },
            {
                "title": "Interpretar el valor p",
                "explain": "La regla de decisión con el umbral 0.05.",
                "code": 'for p in [0.001, 0.03, 0.08, 0.5]:\n    veredicto = "rechazo H0" if p < 0.05 else "no rechazo H0"\n    print(f"p = {p:>5}  ->  {veredicto}")',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Crea una población normal y extrae una muestra de 40; compara sus medias.",
            "Calcula el error estándar de la media de <code>datos[\"ventas\"]</code>.",
            "Calcula un intervalo de confianza al 95% para la media de una lista de números.",
            "Haz una prueba t de una muestra: ¿la media de <code>notas</code> difiere de 5?",
            "Compara dos grupos con <code>ttest_ind</code> e interpreta el valor p.",
            "Con un valor p de 0.02, decide si rechazas H0 al nivel 0.05.",
            "Explica en un comentario por qué un p pequeño es evidencia contra H0.",
            "Calcula un intervalo de confianza al 90% (cambia la confianza a 0.90).",
            "Muestra cómo el error estándar baja al aumentar el tamaño de la muestra.",
        ],
    },
]
