# -*- coding: utf-8 -*-
"""
PyChoice - Ruta "Ingeniero de IA con Python".
Modulo K - Optimizacion y metaheuristicas I: busqueda local (lecciones 42-45).

Todo corre en el navegador. scipy y matplotlib se autocargan al usarse.
Generadores del motor: mochila(), ciudades(), distancias().
Tamanos pequenos y pocas iteraciones para que corra rapido en Pyodide.
"""

CHAPTERS_K = [

    # ============================================================ CAP 42
    {
        "num": 42,
        "slug": "optimizacion-scipy",
        "code": "leccion_42",
        "title": "Optimización con SciPy",
        "subtitle": "Minimizar funciones, mínimos locales vs. globales y funciones de prueba",
        "apunte": "Módulo K · Lección 1 - Optimización con SciPy",
        "concepts": [
            ("Optimización continua", "Buscar el valor de una o más <b>variables reales</b> que hace mínima (o máxima) una función. La base del entrenamiento de modelos y de mucha ingeniería."),
            ("Minimizar / maximizar", "Por convención se <b>minimiza</b>. Para maximizar <code>f</code>, se minimiza <code>-f</code>: el punto óptimo es el mismo."),
            ("scipy.optimize.minimize", "La función estrella de SciPy para optimizar. Recibe una función, un punto inicial y un método, y devuelve el mínimo encontrado."),
            ("Punto inicial (x0)", "Desde dónde empieza a buscar el optimizador. En funciones difíciles, <b>cambiar x0 cambia el resultado</b>."),
            ("Mínimo local", "Un punto mejor que sus vecinos, pero <b>no necesariamente el mejor de todos</b>. Los métodos de gradiente suelen quedar atrapados aquí."),
            ("Mínimo global", "El <b>mejor punto de toda la función</b>. Encontrarlo con garantía es difícil en funciones con muchos valles."),
            ("Método", "El algoritmo interno: <code>Nelder-Mead</code> (sin derivadas), <code>BFGS</code> (usa gradiente), <code>Powell</code>… Cada uno con sus fortalezas."),
            ("Función multimodal", "Función con <b>muchos mínimos locales</b> (Rastrigin, Himmelblau). Sirven de banco de pruebas para ver qué algoritmo escapa de las trampas."),
        ],
        "theory": """
<p><b>Optimizar es el motor de la IA.</b> Entrenar una red, ajustar una regresión o minimizar un
costo son, en el fondo, el mismo problema: encontrar los <b>valores</b> que hacen mínima una función.
SciPy trae herramientas listas para esto en variables continuas, y entenderlas prepara el terreno para
las metaheurísticas.</p>

<p><b>La convención de minimizar.</b> En optimización casi todo se plantea como <b>minimizar</b>. Si
lo tuyo es maximizar una ganancia <code>f</code>, basta con minimizar <code>-f</code>: el punto óptimo
es idéntico. Tenerlo claro evita confusiones al leer librerías.</p>

<p><b>minimize, en una línea.</b> <code>scipy.optimize.minimize(f, x0, method=...)</code> recibe la
función a minimizar, un <b>punto inicial</b> <code>x0</code> y un <b>método</b>. Devuelve un objeto con
<code>.x</code> (el punto óptimo hallado) y <code>.fun</code> (el valor allí). SciPy se autocarga la
primera vez que lo importas en PyChoice.</p>

<p><b>El punto inicial importa (y mucho).</b> Los métodos clásicos son <b>locales</b>: se dejan
«resbalar cuesta abajo» desde <code>x0</code> hasta el valle más cercano. En una función con un solo
valle eso basta. Pero en una función <b>multimodal</b>, con muchos valles, terminan en el mínimo
<b>local</b> más próximo al punto de partida: si cambias <code>x0</code>, cambias la respuesta.</p>

<p><b>Local vs global.</b> Un <b>mínimo local</b> es mejor que sus vecinos inmediatos; el <b>mínimo
global</b> es el mejor de toda la función. Los métodos de gradiente son rápidos pero <b>se atascan</b>
en mínimos locales. Superar esa limitación es exactamente lo que buscan las metaheurísticas (recocido,
genéticos, hormigas) de las próximas lecciones.</p>

<p><b>Métodos.</b> <code>Nelder-Mead</code> no necesita derivadas y es robusto para empezar;
<code>BFGS</code> usa el gradiente y converge rápido en funciones suaves; <code>Powell</code> es otra
opción sin derivadas. No hay un método «mejor» para todo: depende de la función.</p>

<p><b>Funciones de prueba.</b> Para comparar optimizadores se usan funciones con dificultad conocida,
como <b>Rastrigin</b> (un valle central rodeado de muchísimos mínimos locales) o <b>Himmelblau</b>
(cuatro mínimos globales). Nos acompañarán en todo el módulo para ver quién escapa de las trampas.</p>
""",
        "examples": [
            {
                "title": "Minimizar una parábola",
                "explain": "En una función con un solo valle, <code>minimize</code> encuentra el mínimo sin problema. Su mínimo está en x = 3.",
                "code": 'from scipy.optimize import minimize\n\ndef f(x):\n    return (x - 3) ** 2 + 2\n\nres = minimize(f, x0=[0.0], method="Nelder-Mead")\nprint("x optimo:", round(res.x[0], 4))\nprint("valor minimo:", round(res.fun, 4))',
            },
            {
                "title": "Maximizar = minimizar el negativo",
                "explain": "Para maximizar, minimizamos <code>-f</code>. El máximo de esta función está en x = 5.",
                "code": 'from scipy.optimize import minimize\n\ndef ganancia(x):\n    return -(x - 5) ** 2 + 20     # queremos su MAXIMO\n\nres = minimize(lambda x: -ganancia(x), x0=[0.0], method="Nelder-Mead")\nprint("x que maximiza:", round(res.x[0], 4))\nprint("ganancia maxima:", round(ganancia(res.x[0]), 4))',
            },
            {
                "title": "El punto inicial cambia el resultado",
                "explain": "En Rastrigin (multimodal), partir de distintos <code>x0</code> lleva a distintos mínimos locales.",
                "code": 'import numpy as np\nfrom scipy.optimize import minimize\n\ndef rastrigin(x):\n    x = np.asarray(x)\n    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))\n\nfor x0 in [-4.0, -1.5, 0.3, 2.7]:\n    r = minimize(rastrigin, x0=[x0], method="Nelder-Mead")\n    print(f"x0={x0:>5} -> x*={r.x[0]:.3f}  f={r.fun:.3f}")',
            },
            {
                "title": "Optimización en 2 variables",
                "explain": "<code>minimize</code> también trabaja con vectores. Aquí, la función esfera con mínimo en (0, 0).",
                "code": 'import numpy as np\nfrom scipy.optimize import minimize\n\ndef esfera(v):\n    return v[0]**2 + v[1]**2\n\nres = minimize(esfera, x0=[3.0, -2.0], method="BFGS")\nprint("punto optimo:", np.round(res.x, 4))\nprint("valor:", round(res.fun, 6))',
            },
            {
                "title": "Ver la función y el mínimo hallado",
                "explain": "Graficamos Rastrigin 1D y marcamos el punto al que llegó el optimizador desde x0 = 2.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nfrom scipy.optimize import minimize\n\ndef rastrigin(x):\n    x = np.asarray(x)\n    return 10 + x**2 - 10 * np.cos(2 * np.pi * x)\n\nr = minimize(lambda x: rastrigin(x)[0] if np.ndim(x) else rastrigin(x), x0=[2.0], method="Nelder-Mead")\nxs = np.linspace(-5, 5, 400)\nplt.plot(xs, rastrigin(xs))\nplt.scatter([r.x[0]], [r.fun], color="red", zorder=5, label="minimo hallado")\nplt.title("Rastrigin y el punto al que llega SciPy")\nplt.legend(); plt.show()',
            },
            {
                "title": "Comparar métodos",
                "explain": "Distintos métodos pueden dar resultados algo distintos según la función y el punto inicial.",
                "code": 'import numpy as np\nfrom scipy.optimize import minimize\n\ndef f(v):\n    return (v[0] - 1)**2 + (v[1] + 2)**2 + 1\n\nfor m in ["Nelder-Mead", "Powell", "BFGS"]:\n    r = minimize(f, x0=[0.0, 0.0], method=m)\n    print(f"{m:>12}: x*={np.round(r.x, 3)}  f={r.fun:.4f}")',
            },
        ],
        "dataset": "funciones de prueba",
        "exercises": [
            "Minimiza <code>f(x) = (x-7)**2 + 5</code> con <code>minimize</code> y punto inicial 0.",
            "Maximiza <code>-(x-2)**2 + 9</code> minimizando su negativo.",
            "Minimiza la función esfera en 3 variables desde <code>x0 = [5, 5, 5]</code>.",
            "En Rastrigin 1D, prueba 5 puntos iniciales distintos y observa a qué mínimo llega cada uno.",
            "Compara los métodos <code>Nelder-Mead</code> y <code>Powell</code> en la función esfera 2D.",
            "Grafica la función <code>(x-1)**2</code> entre -3 y 5 y marca su mínimo.",
            "Define Himmelblau <code>(x²+y-11)² + (x+y²-7)²</code> y minimízala desde (0,0).",
            "Explica en un comentario por qué <code>minimize</code> puede no hallar el mínimo global.",
            "Repite la minimización de Rastrigin desde 10 puntos iniciales al azar y quédate con el mejor resultado.",
            "Investiga: imprime el objeto que devuelve <code>minimize</code> y comenta qué contienen <code>.x</code> y <code>.fun</code>.",
        ],
    },

    # ============================================================ CAP 43
    {
        "num": 43,
        "slug": "hill-climbing",
        "code": "leccion_43",
        "title": "Hill climbing (ascenso de colina)",
        "subtitle": "Búsqueda local: moverse a un vecino mejor hasta quedar atascado",
        "apunte": "Módulo K · Lección 2 - Hill climbing",
        "concepts": [
            ("Búsqueda local", "Estrategia que parte de una solución y se <b>mueve a soluciones vecinas mejores</b>, paso a paso, sin mirar todo el espacio."),
            ("Solución actual", "El punto donde está la búsqueda ahora. En cada paso se intenta mejorarlo."),
            ("Vecino", "Una solución que se obtiene con un <b>cambio pequeño</b> de la actual (perturbar un número, cambiar un bit)."),
            ("Movimiento de mejora", "Aceptar el vecino <b>solo si es mejor</b> que la solución actual. Es la regla básica del hill climbing."),
            ("Óptimo local", "Un punto del que <b>ningún vecino es mejor</b>. El hill climbing se detiene ahí, aunque no sea el óptimo global."),
            ("Reinicio aleatorio", "Volver a empezar desde otro punto al azar. Repetido varias veces, aumenta la chance de hallar el óptimo global (<i>random restart</i>)."),
            ("Paso (step)", "El tamaño de la perturbación al generar un vecino. Muy grande explora sin afinar; muy chico afina pero avanza lento."),
            ("Convergencia prematura", "Quedar atrapado pronto en un óptimo local mediocre. Es la debilidad central de la búsqueda local pura."),
        ],
        "theory": """
<p><b>La idea más simple que funciona.</b> El <b>hill climbing</b> («ascenso de colina») es la
metaheurística más básica: parte de una solución cualquiera y, en cada paso, mira una solución
<b>vecina</b>; si es mejor, se muda a ella; si no, la descarta. Repite hasta que ningún vecino mejora.
Es como subir un cerro con niebla dando siempre el paso que sube.</p>

<p><b>Vecinos y pasos.</b> Todo depende de cómo definas el <b>vecindario</b>. En una variable continua,
un vecino es <code>x</code> más un pequeño ruido; el <b>paso</b> (tamaño del ruido) marca el equilibrio
entre explorar y afinar. En problemas discretos como la mochila, un vecino es la solución con <b>un
bit cambiado</b>. Elegir el vecindario es diseñar cómo se mueve la búsqueda.</p>

<p><b>La trampa: el óptimo local.</b> El hill climbing sube hasta que no hay vecino mejor y ahí se
<b>detiene</b>. El problema es que ese punto puede ser un <b>óptimo local</b>: la cima de una colina
pequeña, no la montaña más alta. Como nunca acepta empeorar, no puede «bajar» para cruzar a una colina
mejor. En funciones multimodales (Rastrigin) esto ocurre casi siempre.</p>

<p><b>El remedio simple: reinicios aleatorios.</b> Una forma barata de mejorar es repetir el hill
climbing desde <b>varios puntos iniciales al azar</b> y quedarse con el mejor resultado. Cada reinicio
explora una zona distinta, así que crece la probabilidad de caer cerca del óptimo global. Es sencillo y
sorprendentemente efectivo.</p>

<p><b>Determinista salvo por el inicio.</b> Con el mismo punto de partida y el mismo vecindario, el
hill climbing hace siempre lo mismo. Por eso fijamos la <b>semilla</b>: para que el experimento sea
reproducible y comparable, como vimos en la lección 41.</p>

<p><b>Por qué importa.</b> Casi todas las metaheurísticas de este módulo y del siguiente son, en el
fondo, <b>hill climbing mejorado</b>: el recocido simulado le agrega la capacidad de aceptar peores
soluciones para escapar de las trampas; la búsqueda tabú le agrega memoria. Entender bien esta base
hace fácil lo que viene.</p>
""",
        "examples": [
            {
                "title": "Hill climbing en una función continua",
                "explain": "Partimos de un x al azar y nos movemos a un vecino solo si mejora. Máximo en x = 3.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\n\ndef f(x):\n    return -(x - 3) ** 2 + 10        # maximizar\n\nx = rng.uniform(-5, 10)\nfor _ in range(200):\n    vecino = x + rng.normal(0, 0.5)   # paso pequeno\n    if f(vecino) > f(x):\n        x = vecino\nprint("x final:", round(x, 4), "| f:", round(f(x), 4))',
            },
            {
                "title": "Se atasca en un óptimo local",
                "explain": "En Rastrigin (multimodal), el hill climbing suele quedar atrapado en el valle más cercano al inicio.",
                "code": 'import numpy as np\nrng = np.random.default_rng(3)\n\ndef rastrigin(x):\n    return 10 + x**2 - 10 * np.cos(2 * np.pi * x)   # minimizar (optimo en x=0)\n\nx = rng.uniform(-5, 5)\nfor _ in range(300):\n    vecino = x + rng.normal(0, 0.3)\n    if rastrigin(vecino) < rastrigin(x):\n        x = vecino\nprint("x final:", round(x, 3), "| f:", round(rastrigin(x), 3), "(optimo global: 0)")',
            },
            {
                "title": "Reinicios aleatorios al rescate",
                "explain": "Repetimos desde varios puntos al azar y guardamos el mejor: mucho más cerca del óptimo global.",
                "code": 'import numpy as np\nrng = np.random.default_rng(3)\n\ndef rastrigin(x):\n    return 10 + x**2 - 10 * np.cos(2 * np.pi * x)\n\ndef escalar(x0):\n    x = x0\n    for _ in range(300):\n        v = x + rng.normal(0, 0.3)\n        if rastrigin(v) < rastrigin(x):\n            x = v\n    return x\n\nmejor = None\nfor _ in range(20):                 # 20 reinicios\n    x = escalar(rng.uniform(-5, 5))\n    if mejor is None or rastrigin(x) < rastrigin(mejor):\n        mejor = x\nprint("mejor x:", round(mejor, 3), "| f:", round(rastrigin(mejor), 4))',
            },
            {
                "title": "Hill climbing en la mochila (vecino = cambiar un bit)",
                "explain": "En problemas discretos, el vecino invierte un bit. Aceptamos si mejora el valor sin pasarnos de capacidad.",
                "code": 'import numpy as np\nrng = np.random.default_rng(5)\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5)\n\ndef valor(sel):\n    return (sel * valores).sum() if (sel * pesos).sum() <= cap else -1\n\nsel = np.zeros(len(m), dtype=int)\nfor _ in range(500):\n    i = rng.integers(len(m))\n    vecino = sel.copy(); vecino[i] = 1 - vecino[i]\n    if valor(vecino) > valor(sel):\n        sel = vecino\nprint("valor:", valor(sel), "| peso:", (sel*pesos).sum(), "/", cap)',
            },
            {
                "title": "Curva de mejora",
                "explain": "Guardamos el mejor valor en cada paso para ver cómo sube y luego se estanca.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(7)\n\ndef f(x):\n    return -(x - 3) ** 2 + 10\n\nx = rng.uniform(-5, 10); curva = []\nfor _ in range(150):\n    v = x + rng.normal(0, 0.5)\n    if f(v) > f(x):\n        x = v\n    curva.append(f(x))\nplt.plot(curva); plt.xlabel("pasos"); plt.ylabel("f actual")\nplt.title("Hill climbing: mejora y estancamiento"); plt.show()',
            },
        ],
        "dataset": "mochila(), funciones de prueba",
        "exercises": [
            "Programa un hill climbing para maximizar <code>-(x-6)**2 + 12</code> partiendo de x = 0.",
            "Prueba dos tamaños de paso (0.1 y 1.0) y compara a qué valor llega cada uno.",
            "Aplica hill climbing a Rastrigin y muestra que queda atrapado en un óptimo local.",
            "Agrega reinicios aleatorios (15) y compara el mejor resultado con el caso de un solo intento.",
            "Aplica hill climbing a <code>mochila(12)</code> (vecino = cambiar un bit) y reporta el valor final.",
            "Grafica la curva de mejora de tu hill climbing en la mochila.",
            "Modifica el criterio para <b>minimizar</b> en vez de maximizar una función.",
            "Cuenta cuántos pasos de mejora efectivos hubo (cuántas veces se aceptó un vecino).",
            "Compara hill climbing con 1 inicio vs. 30 reinicios en Rastrigin: promedio de 5 semillas.",
            "Explica en un comentario por qué el hill climbing no puede escapar de un óptimo local.",
        ],
    },

    # ============================================================ CAP 44
    {
        "num": 44,
        "slug": "recocido-simulado",
        "code": "leccion_44",
        "title": "Recocido simulado (Simulated Annealing)",
        "subtitle": "Aceptar peores soluciones para escapar de los óptimos locales",
        "apunte": "Módulo K · Lección 3 - Recocido simulado",
        "concepts": [
            ("Recocido simulado", "Metaheurística inspirada en el <b>enfriamiento lento de un metal</b>: acepta a veces soluciones peores para no quedar atrapada, y se vuelve exigente al enfriarse."),
            ("Temperatura (T)", "Parámetro que controla cuán dispuesta está la búsqueda a <b>aceptar peores soluciones</b>. Alta = explora; baja = afina."),
            ("Enfriamiento (cooling)", "Reducir T poco a poco (p. ej. <code>T = T * 0.99</code>). Al principio explora; al final se comporta como hill climbing."),
            ("Criterio de Metropolis", "Aceptar un vecino peor con probabilidad <code>exp(-Δ/T)</code>, donde Δ es cuánto empeora. A mayor T o menor Δ, más chance de aceptar."),
            ("Aceptar peores soluciones", "La clave del método: permitir empeorar temporalmente para poder <b>bajar de una colina y subir a otra mejor</b>."),
            ("Escapar de óptimos locales", "Gracias a aceptar peores, el recocido puede salir de trampas donde el hill climbing se quedaría."),
            ("Esquema de enfriamiento", "La regla con que baja T (geométrico, lineal…) y la T inicial. Afecta mucho la calidad del resultado."),
            ("Exploración vs. explotación", "El equilibrio entre <b>buscar ampliamente</b> (T alta) y <b>refinar</b> lo hallado (T baja). El recocido lo maneja con el tiempo."),
        ],
        "theory": """
<p><b>Una idea tomada de la metalurgia.</b> Cuando se forja un metal, se calienta y luego se
<b>enfría lentamente</b> para que sus átomos se ordenen en una estructura de mínima energía. El
<b>recocido simulado</b> imita ese proceso: al principio, «caliente», acepta casi cualquier cambio
(explora); al enfriarse, se vuelve cada vez más exigente (afina). Es hill climbing con una idea
brillante añadida.</p>

<p><b>El truco: aceptar peores soluciones.</b> El hill climbing fracasa porque nunca empeora, así que
no puede bajar de una colina para cruzar a otra más alta. El recocido simulado <b>sí acepta a veces un
vecino peor</b>, con una probabilidad que depende de dos cosas: cuánto empeora (Δ) y la temperatura
actual (T). La fórmula es el <b>criterio de Metropolis</b>: <code>P = exp(-Δ / T)</code>. Si el vecino
mejora, se acepta siempre; si empeora, se acepta con esa probabilidad.</p>

<p><b>El papel de la temperatura.</b> Con T <b>alta</b>, <code>exp(-Δ/T)</code> es cercano a 1: se
aceptan muchos empeoramientos y la búsqueda <b>explora</b> con libertad. Con T <b>baja</b>, la
probabilidad se acerca a 0: casi solo se aceptan mejoras y la búsqueda <b>explota</b> (afina) la mejor
zona encontrada. El recocido pasa suavemente de una fase a otra.</p>

<p><b>El enfriamiento.</b> T no es fija: baja poco a poco según un <b>esquema de enfriamiento</b>. El
más común es geométrico: <code>T = T * α</code> con α cercano a 1 (0.99, 0.995). Una T inicial
suficientemente alta y un enfriamiento no demasiado brusco son la receta para buenos resultados. Al
final, con T casi cero, el recocido se comporta como hill climbing y pule la solución.</p>

<p><b>Dónde brilla: problemas combinatorios.</b> El recocido es excelente para problemas como el
<b>viajante (TSP)</b>. Ahí una solución es un orden de ciudades y un vecino se obtiene
<b>intercambiando dos</b>. Empezando por una ruta al azar y enfriando, el recocido suele encontrar
rutas muy buenas sin revisar ni una fracción de las posibles.</p>

<p><b>Reproducibilidad y comparación.</b> Como usa azar, fijamos la semilla y comparamos con la misma
disciplina de la lección 41: misma cantidad de iteraciones, curva de convergencia y varias semillas.
Verás que el recocido supera claramente al hill climbing en funciones con trampas.</p>
""",
        "examples": [
            {
                "title": "La probabilidad de aceptar un empeoramiento",
                "explain": "El criterio de Metropolis: con T alta se acepta casi todo; con T baja, casi nada. Δ es cuánto empeora.",
                "code": 'import numpy as np\ndelta = 2.0     # el vecino empeora en 2\nfor T in [10.0, 2.0, 0.5, 0.1]:\n    p = np.exp(-delta / T)\n    print(f"T={T:>5} -> probabilidad de aceptar = {p:.3f}")',
            },
            {
                "title": "Recocido en una función multimodal",
                "explain": "Minimiza Rastrigin aceptando a veces peores soluciones. Compara el resultado con el hill climbing atascado.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\n\ndef rastrigin(x):\n    return 10 + x**2 - 10 * np.cos(2 * np.pi * x)\n\nx = rng.uniform(-5, 5); actual = rastrigin(x)\nmejor_x, mejor = x, actual\nT = 5.0\nfor _ in range(3000):\n    v = x + rng.normal(0, 0.4)\n    d = rastrigin(v) - actual\n    if d < 0 or rng.random() < np.exp(-d / T):\n        x, actual = v, rastrigin(v)\n        if actual < mejor:\n            mejor_x, mejor = x, actual\n    T *= 0.998\nprint("mejor x:", round(mejor_x, 3), "| f:", round(mejor, 4), "(optimo: 0)")',
            },
            {
                "title": "Recocido para el viajante (TSP)",
                "explain": "Una solución es un orden de ciudades; el vecino intercambia dos. Reportamos el largo antes y después.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\ncoords = ciudades(10)\nD = distancias(coords)\nn = len(coords)\n\ndef largo(ruta):\n    return sum(D[ruta[i], ruta[(i + 1) % n]] for i in range(n))\n\nruta = np.arange(n); rng.shuffle(ruta)\ninicial = largo(ruta)\nactual = inicial; mejor_ruta = ruta.copy(); mejor = actual\nT = 100.0\nfor _ in range(4000):\n    i, j = rng.integers(0, n, 2)\n    nueva = ruta.copy(); nueva[i], nueva[j] = nueva[j], nueva[i]\n    d = largo(nueva) - actual\n    if d < 0 or rng.random() < np.exp(-d / T):\n        ruta, actual = nueva, actual + d\n        if actual < mejor:\n            mejor, mejor_ruta = actual, nueva.copy()\n    T *= 0.999\nprint("largo inicial:", round(inicial, 1))\nprint("largo final  :", round(mejor, 1))',
            },
            {
                "title": "El enfriamiento importa",
                "explain": "Comparamos distintos factores de enfriamiento α en Rastrigin. Enfriar demasiado rápido empeora el resultado.",
                "code": 'import numpy as np\n\ndef rastrigin(x):\n    return 10 + x**2 - 10 * np.cos(2 * np.pi * x)\n\ndef recocido(alpha, seed=1):\n    rng = np.random.default_rng(seed)\n    x = rng.uniform(-5, 5); actual = rastrigin(x); mejor = actual; T = 5.0\n    for _ in range(3000):\n        v = x + rng.normal(0, 0.4); d = rastrigin(v) - actual\n        if d < 0 or rng.random() < np.exp(-d / T):\n            x, actual = v, rastrigin(v); mejor = min(mejor, actual)\n        T *= alpha\n    return mejor\n\nfor a in [0.90, 0.99, 0.999]:\n    print(f"alpha={a} -> mejor f = {recocido(a):.4f}")',
            },
            {
                "title": "Recocido vs. hill climbing (curvas)",
                "explain": "Graficamos el mejor valor de ambos: el recocido escapa de la trampa donde el hill climbing se estanca.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\n\ndef rastrigin(x):\n    return 10 + x**2 - 10 * np.cos(2 * np.pi * x)\n\ndef corre(sim, seed=2):\n    rng = np.random.default_rng(seed)\n    x = rng.uniform(-5, 5); actual = rastrigin(x); mejor = actual; T = 5.0; curva = []\n    for _ in range(1500):\n        v = x + rng.normal(0, 0.4); d = rastrigin(v) - actual\n        acepta = d < 0 or (sim and rng.random() < np.exp(-d / max(T, 1e-9)))\n        if acepta:\n            x, actual = v, rastrigin(v); mejor = min(mejor, actual)\n        T *= 0.998\n        curva.append(mejor)\n    return curva\n\nplt.plot(corre(True), label="recocido")\nplt.plot(corre(False), label="hill climbing")\nplt.xlabel("iteraciones"); plt.ylabel("mejor f"); plt.legend()\nplt.title("Recocido escapa; hill climbing se estanca"); plt.show()',
            },
        ],
        "dataset": "ciudades(), funciones de prueba",
        "exercises": [
            "Calcula <code>exp(-delta/T)</code> para delta = 1 y T = 5, 1 y 0.2. Interpreta.",
            "Programa un recocido para minimizar Rastrigin y compáralo con un hill climbing simple.",
            "Aplica recocido al TSP con <code>ciudades(12)</code> y reporta el largo inicial y final.",
            "Prueba tres temperaturas iniciales (1, 10, 100) y compara el resultado en el TSP.",
            "Prueba tres factores de enfriamiento (0.9, 0.99, 0.999) y compara.",
            "Grafica la curva de convergencia de tu recocido.",
            "Repite el recocido del TSP con 5 semillas y reporta el promedio del largo final.",
            "Modifica el vecino del TSP: en vez de intercambiar dos ciudades, invierte un tramo (2-opt) y compara.",
            "Cuenta cuántas veces se aceptó una solución peor durante la búsqueda.",
            "Explica en un comentario por qué bajar T convierte al recocido en un hill climbing.",
        ],
    },

    # ============================================================ CAP 45
    {
        "num": 45,
        "slug": "busqueda-tabu",
        "code": "leccion_45",
        "title": "Búsqueda tabú (Tabu Search)",
        "subtitle": "Usar memoria para no repetir movimientos y escapar de los ciclos",
        "apunte": "Módulo K · Lección 4 - Búsqueda tabú",
        "concepts": [
            ("Búsqueda tabú", "Búsqueda local con <b>memoria</b>: siempre se mueve al mejor vecino, pero <b>prohíbe deshacer</b> movimientos recientes para no dar vueltas en círculo."),
            ("Lista tabú", "Memoria de corto plazo con los <b>movimientos prohibidos</b> por unas cuantas iteraciones (su <i>tenencia</i> o <i>tabu tenure</i>)."),
            ("Mejor vecino", "A diferencia del hill climbing, se elige el <b>mejor de todos los vecinos</b> permitidos, aunque sea peor que la solución actual."),
            ("Movimiento", "El cambio que lleva de una solución a un vecino (cambiar el bit <i>i</i>, intercambiar las ciudades <i>i, j</i>). Es lo que se marca como tabú."),
            ("Criterio de aspiración", "Regla que <b>levanta el tabú</b> si un movimiento prohibido llevaría a la <b>mejor solución vista hasta ahora</b>."),
            ("Mejor global", "La mejor solución encontrada en toda la búsqueda; se guarda aparte, porque la actual puede empeorar a propósito."),
            ("Intensificación", "Concentrar la búsqueda en zonas prometedoras ya halladas."),
            ("Diversificación", "Empujar la búsqueda hacia zonas nuevas para no quedarse en lo mismo. La lista tabú ayuda a diversificar."),
        ],
        "theory": """
<p><b>Memoria para no repetir errores.</b> El hill climbing se atasca y el recocido escapa con azar.
La <b>búsqueda tabú</b> propone otra idea: <b>recordar</b> por dónde acaba de pasar para no volver. En
cada paso examina los vecinos, se mueve al <b>mejor permitido</b> (aunque sea peor que el actual) y
apunta el movimiento en una <b>lista tabú</b> que lo prohíbe por unas cuantas iteraciones. Así evita
caer en ciclos y puede cruzar mesetas y valles.</p>

<p><b>Siempre al mejor vecino.</b> A diferencia del hill climbing, que solo acepta mejoras, la búsqueda
tabú <b>siempre avanza</b> al mejor vecino disponible. Si todos los vecinos son peores, igual se mueve
al «menos malo». Eso le permite <b>bajar</b> de una colina para buscar otra —como el recocido, pero
guiado por memoria en vez de azar.</p>

<p><b>La lista tabú.</b> Cada <b>movimiento</b> (por ejemplo «cambié el bit 4» o «intercambié las
ciudades 2 y 7») queda <b>prohibido</b> durante un número fijo de iteraciones, llamado <i>tenencia</i>.
Mientras esté en la lista, no se puede deshacer. Esto impide que la búsqueda oscile entre dos
soluciones para siempre y la obliga a <b>explorar territorio nuevo</b> (diversificación).</p>

<p><b>El criterio de aspiración.</b> Prohibir a ciegas puede hacernos perder un gran movimiento. Por
eso existe el <b>criterio de aspiración</b>: si un movimiento tabú llevaría a la <b>mejor solución
vista hasta ahora</b>, se le <b>perdona</b> el tabú y se acepta. Es una válvula de sentido común.</p>

<p><b>Guardar el mejor aparte.</b> Como la solución actual puede empeorar a propósito, siempre
mantenemos por separado el <b>mejor global</b> encontrado. Al terminar, esa es la respuesta. Es el
mismo cuidado que tuvimos en el recocido.</p>

<p><b>Intensificar y diversificar.</b> Toda buena búsqueda equilibra dos fuerzas: <b>intensificar</b>
(exprimir una zona prometedora) y <b>diversificar</b> (irse a explorar otra). La lista tabú es, sobre
todo, un mecanismo de diversificación de corto plazo. Versiones más avanzadas agregan memoria de largo
plazo, pero con esta base ya resuelves muy bien mochila y TSP pequeños.</p>
""",
        "examples": [
            {
                "title": "Búsqueda tabú en la mochila",
                "explain": "En cada paso probamos todos los vecinos (cambiar un bit), evitamos los movimientos tabú y vamos al mejor.",
                "code": 'import numpy as np\nrng = np.random.default_rng(5)\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5)\n\ndef valor(sel):\n    return (sel * valores).sum() if (sel * pesos).sum() <= cap else -1\n\nn = len(m)\nsel = np.zeros(n, dtype=int)\nmejor_sel, mejor = sel.copy(), valor(sel)\ntabu = {}                       # bit -> iteracion hasta la que esta prohibido\nfor it in range(120):\n    mejor_v, mejor_i = -1e9, None\n    for i in range(n):\n        if tabu.get(i, 0) > it:\n            continue            # movimiento tabu\n        cand = sel.copy(); cand[i] = 1 - cand[i]\n        if valor(cand) > mejor_v:\n            mejor_v, mejor_i = valor(cand), i\n    sel = sel.copy(); sel[mejor_i] = 1 - sel[mejor_i]\n    tabu[mejor_i] = it + 5      # prohibido 5 iteraciones\n    if valor(sel) > mejor:\n        mejor, mejor_sel = valor(sel), sel.copy()\nprint("valor tabu:", mejor, "| peso:", (mejor_sel*pesos).sum(), "/", cap)',
            },
            {
                "title": "Cómo funciona la lista tabú",
                "explain": "La lista guarda hasta qué iteración está prohibido cada movimiento. Aquí la mostramos evolucionar.",
                "code": 'tabu = {}\nfor it, movimiento in enumerate([2, 5, 2, 1, 5]):\n    activos = {k: v for k, v in tabu.items() if v > it}\n    prohibido = tabu.get(movimiento, 0) > it\n    print(f"it {it}: mover {movimiento} -> {\'TABU\' if prohibido else \'ok\'} | activos: {activos}")\n    tabu[movimiento] = it + 3',
            },
            {
                "title": "Tabú vs. hill climbing en la mochila",
                "explain": "Comparamos el valor final de ambos en el mismo problema: la memoria suele ayudar a mejorar.",
                "code": 'import numpy as np\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef valor(sel):\n    return (sel * valores).sum() if (sel * pesos).sum() <= cap else -1\n\ndef hill(seed):\n    rng = np.random.default_rng(seed); sel = np.zeros(n, dtype=int)\n    for _ in range(500):\n        i = rng.integers(n); c = sel.copy(); c[i] = 1 - c[i]\n        if valor(c) > valor(sel): sel = c\n    return valor(sel)\n\ndef tabu_search():\n    sel = np.zeros(n, dtype=int); mejor = valor(sel); tabu = {}\n    for it in range(120):\n        mv, mi = -1e9, None\n        for i in range(n):\n            if tabu.get(i, 0) > it: continue\n            c = sel.copy(); c[i] = 1 - c[i]\n            if valor(c) > mv: mv, mi = valor(c), i\n        sel = sel.copy(); sel[mi] = 1 - sel[mi]; tabu[mi] = it + 5\n        mejor = max(mejor, valor(sel))\n    return mejor\n\nprint("hill climbing:", hill(1))\nprint("busqueda tabu:", tabu_search())',
            },
            {
                "title": "Criterio de aspiración",
                "explain": "Si un movimiento tabú lograra la mejor solución vista, se le perdona el tabú. Aquí se marca cuándo ocurre.",
                "code": 'import numpy as np\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef valor(sel):\n    return (sel * valores).sum() if (sel * pesos).sum() <= cap else -1\n\nsel = np.zeros(n, dtype=int); mejor = valor(sel); tabu = {}; aspiraciones = 0\nfor it in range(120):\n    mv, mi = -1e9, None\n    for i in range(n):\n        c = sel.copy(); c[i] = 1 - c[i]; v = valor(c)\n        es_tabu = tabu.get(i, 0) > it\n        if es_tabu and not v > mejor:      # tabu, salvo que supere al mejor global\n            continue\n        if es_tabu and v > mejor:\n            aspiraciones += 1              # aspiracion: se perdona el tabu\n        if v > mv: mv, mi = v, i\n    sel = sel.copy(); sel[mi] = 1 - sel[mi]; tabu[mi] = it + 5\n    mejor = max(mejor, valor(sel))\nprint("valor:", mejor, "| veces que aplico aspiracion:", aspiraciones)',
            },
            {
                "title": "Curva de la búsqueda tabú",
                "explain": "Graficamos el mejor valor por iteración: sube y se estabiliza cerca del óptimo.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef valor(sel):\n    return (sel * valores).sum() if (sel * pesos).sum() <= cap else -1\n\nsel = np.zeros(n, dtype=int); mejor = valor(sel); tabu = {}; curva = []\nfor it in range(120):\n    mv, mi = -1e9, None\n    for i in range(n):\n        if tabu.get(i, 0) > it: continue\n        c = sel.copy(); c[i] = 1 - c[i]\n        if valor(c) > mv: mv, mi = valor(c), i\n    sel = sel.copy(); sel[mi] = 1 - sel[mi]; tabu[mi] = it + 5\n    mejor = max(mejor, valor(sel)); curva.append(mejor)\nplt.plot(curva); plt.xlabel("iteraciones"); plt.ylabel("mejor valor")\nplt.title("Busqueda tabu en la mochila"); plt.show()',
            },
        ],
        "dataset": "mochila(), ciudades()",
        "exercises": [
            "Aplica búsqueda tabú a <code>mochila(12)</code> y reporta el mejor valor.",
            "Cambia la tenencia tabú (3, 5, 10) y compara los resultados.",
            "Compara búsqueda tabú con hill climbing en el mismo problema.",
            "Simula a mano una lista tabú con la secuencia de movimientos [1, 3, 1, 2, 3] y tenencia 2.",
            "Agrega el criterio de aspiración y cuenta cuántas veces se activa.",
            "Grafica la curva del mejor valor de tu búsqueda tabú.",
            "Compara con el óptimo por fuerza bruta en <code>mochila(12)</code>: ¿lo alcanza?",
            "Adapta la búsqueda tabú al TSP con <code>ciudades(8)</code> (movimiento = intercambiar dos ciudades).",
            "Repite con 5 semillas de problema distintas y reporta el promedio.",
            "Explica en un comentario la diferencia entre intensificar y diversificar.",
        ],
    },
]
