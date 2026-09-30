# -*- coding: utf-8 -*-
"""
PyChoice - Ruta "Ingeniero de IA con Python".
Modulo L - Metaheuristicas bioinspiradas / poblacionales (lecciones 46-49):
algoritmos geneticos, PSO y colonia de hormigas (ACO).

Todo corre en el navegador (numpy). Poblaciones e iteraciones pequenas a
proposito para que corra rapido en Pyodide.
Generadores del motor: mochila(), ciudades(), distancias().
"""

CHAPTERS_L = [

    # ============================================================ CAP 46
    {
        "num": 46,
        "slug": "algoritmos-geneticos-1",
        "code": "leccion_46",
        "title": "Algoritmos genéticos I",
        "subtitle": "Evolucionar una población de soluciones: selección, cruce y mutación",
        "apunte": "Módulo L · Lección 1 - Algoritmos genéticos I",
        "concepts": [
            ("Algoritmo genético (GA)", "Metaheurística inspirada en la <b>evolución biológica</b>: una población de soluciones mejora generación tras generación por selección, cruce y mutación."),
            ("Población", "El <b>conjunto de soluciones</b> candidatas que evoluciona a la vez. Trabajar con muchas a la vez permite explorar el espacio en paralelo."),
            ("Cromosoma / individuo", "Una <b>solución codificada</b>. En la mochila es una lista de 0/1 (los <i>genes</i>): llevar o no cada objeto."),
            ("Fitness", "La <b>calidad</b> de un individuo (su función objetivo). Los mejores tienen más chance de reproducirse."),
            ("Selección", "Elegir <b>padres</b> según su fitness. Por <b>torneo</b> (gana el mejor de un grupo al azar) o por <b>ruleta</b> (probabilidad proporcional al fitness)."),
            ("Cruce (crossover)", "Combinar dos padres para crear <b>hijos</b> que mezclan sus genes. Es la fuente principal de nuevas soluciones."),
            ("Mutación", "Cambiar al azar algún gen de un hijo (con baja probabilidad). Mantiene <b>diversidad</b> y evita el estancamiento."),
            ("Elitismo", "Conservar al <b>mejor individuo</b> (o unos pocos) intacto en la siguiente generación, para no perder la mejor solución hallada."),
        ],
        "theory": """
<p><b>La evolución como algoritmo.</b> Un <b>algoritmo genético</b> copia la lógica de la selección
natural: parte de una <b>población</b> de soluciones al azar y, generación tras generación, deja que
las mejores «se reproduzcan» y las peores desaparezcan. Con el tiempo, la población entera mejora. En
vez de una sola solución que sube una colina (hill climbing), aquí <b>muchas</b> soluciones exploran el
espacio a la vez.</p>

<p><b>El ciclo de una generación.</b> Cada generación repite cuatro pasos. Primero se calcula el
<b>fitness</b> de cada individuo. Luego la <b>selección</b> elige padres favoreciendo a los mejores. El
<b>cruce</b> combina pares de padres para crear hijos que mezclan sus genes. Y la <b>mutación</b>
cambia algún gen al azar con baja probabilidad. La nueva población reemplaza a la anterior y el ciclo
vuelve a empezar.</p>

<p><b>La representación: el cromosoma.</b> Como en la lección 40, todo empieza por cómo codificar una
solución. Para la <b>mochila</b>, un individuo es una lista de <b>0 y 1</b> (los genes): un 1 en la
posición <i>i</i> significa «llevo el objeto <i>i</i>». Esta codificación binaria es la más clásica y
la que usaremos aquí.</p>

<p><b>Selección: favorecer sin eliminar la diversidad.</b> La <b>selección por torneo</b> es simple y
efectiva: se toman al azar unos pocos individuos y gana el de mejor fitness. Al repetirla, los buenos
se eligen más seguido, pero los demás aún tienen chance —lo que mantiene <b>diversidad</b>. La
<b>ruleta</b> asigna probabilidad proporcional al fitness. Sin diversidad, la población se vuelve
uniforme demasiado pronto y deja de explorar.</p>

<p><b>Cruce y mutación: explorar y no estancarse.</b> El <b>cruce</b> es el corazón creativo: mezcla
dos buenas soluciones con la esperanza de que el hijo herede lo mejor de cada una. El más simple es el
<b>cruce de un punto</b>: se corta a ambos padres en el mismo lugar y se intercambian las mitades. La
<b>mutación</b> introduce cambios pequeños al azar; sin ella, la población pierde variedad y el GA se
estanca en soluciones parecidas entre sí.</p>

<p><b>Elitismo: no perder lo bueno.</b> El azar del cruce y la mutación podría <b>destruir</b> la mejor
solución encontrada. El <b>elitismo</b> lo evita: copia intacto al mejor individuo (o a unos pocos) a
la siguiente generación. Es una salvaguarda barata que casi siempre mejora los resultados.</p>

<p><b>Cuándo brillan los genéticos.</b> Son muy versátiles: sirven para problemas discretos (mochila),
de orden (TSP, próxima lección) y continuos. No garantizan el óptimo, pero encuentran soluciones muy
buenas en espacios enormes donde la fuerza bruta es imposible. En PyChoice usamos poblaciones y
generaciones pequeñas para que corran rápido; en los retos podrás subirlas.</p>
""",
        "examples": [
            {
                "title": "Población y fitness (mochila)",
                "explain": "Creamos una población binaria al azar y evaluamos su fitness (valor total, o 0 si excede la capacidad).",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef fitness(ind):\n    return (ind * valores).sum() if (ind * pesos).sum() <= cap else 0\n\npob = rng.integers(0, 2, size=(6, n))     # 6 individuos\nfor ind in pob:\n    print(ind, "-> fitness", fitness(ind))',
            },
            {
                "title": "Selección por torneo",
                "explain": "Tomamos k individuos al azar y devolvemos el de mejor fitness. Los buenos se eligen más seguido.",
                "code": 'import numpy as np\nrng = np.random.default_rng(1)\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef fitness(ind):\n    return (ind * valores).sum() if (ind * pesos).sum() <= cap else 0\n\ndef torneo(pob, k=3):\n    idx = rng.integers(0, len(pob), k)\n    return pob[max(idx, key=lambda i: fitness(pob[i]))]\n\npob = rng.integers(0, 2, size=(10, n))\nganador = torneo(pob)\nprint("ganador del torneo -> fitness", fitness(ganador))',
            },
            {
                "title": "Cruce de un punto y mutación",
                "explain": "El cruce intercambia mitades de dos padres; la mutación invierte algún gen con baja probabilidad.",
                "code": 'import numpy as np\nrng = np.random.default_rng(2)\nn = 10\np1 = rng.integers(0, 2, n); p2 = rng.integers(0, 2, n)\n\ndef cruce(a, b):\n    p = rng.integers(1, len(a))\n    return np.concatenate([a[:p], b[p:]])\n\ndef mutar(ind, prob=0.1):\n    ind = ind.copy()\n    for i in range(len(ind)):\n        if rng.random() < prob:\n            ind[i] = 1 - ind[i]\n    return ind\n\nprint("padre 1:", p1)\nprint("padre 2:", p2)\nhijo = mutar(cruce(p1, p2))\nprint("hijo   :", hijo)',
            },
            {
                "title": "Un algoritmo genético completo (mochila)",
                "explain": "Juntamos todo: selección por torneo, cruce, mutación y elitismo, durante varias generaciones.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef fitness(ind):\n    return (ind * valores).sum() if (ind * pesos).sum() <= cap else 0\ndef torneo(pob):\n    idx = rng.integers(0, len(pob), 3)\n    return pob[max(idx, key=lambda i: fitness(pob[i]))]\ndef cruce(a, b):\n    p = rng.integers(1, n); return np.concatenate([a[:p], b[p:]])\ndef mutar(ind, prob=0.05):\n    for i in range(n):\n        if rng.random() < prob: ind[i] = 1 - ind[i]\n    return ind\n\npob = rng.integers(0, 2, size=(40, n))\nfor gen in range(60):\n    pob = sorted(pob, key=fitness, reverse=True)\n    nueva = [pob[0].copy()]                 # elitismo\n    while len(nueva) < 40:\n        nueva.append(mutar(cruce(torneo(pob), torneo(pob))))\n    pob = np.array(nueva)\n\nmejor = max(pob, key=fitness)\nprint("mejor valor:", fitness(mejor), "| peso:", (mejor*pesos).sum(), "/", cap)',
            },
            {
                "title": "Curva de convergencia del GA",
                "explain": "Guardamos el mejor fitness de cada generación para ver cómo evoluciona la población.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(7)\nm = mochila(15)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef fitness(ind):\n    return (ind * valores).sum() if (ind * pesos).sum() <= cap else 0\ndef torneo(pob):\n    idx = rng.integers(0, len(pob), 3)\n    return pob[max(idx, key=lambda i: fitness(pob[i]))]\ndef cruce(a, b):\n    p = rng.integers(1, n); return np.concatenate([a[:p], b[p:]])\ndef mutar(ind, prob=0.05):\n    for i in range(n):\n        if rng.random() < prob: ind[i] = 1 - ind[i]\n    return ind\n\npob = rng.integers(0, 2, size=(40, n)); curva = []\nfor gen in range(60):\n    pob = sorted(pob, key=fitness, reverse=True)\n    curva.append(fitness(pob[0]))\n    nueva = [pob[0].copy()]\n    while len(nueva) < 40:\n        nueva.append(mutar(cruce(torneo(pob), torneo(pob))))\n    pob = np.array(nueva)\nplt.plot(curva); plt.xlabel("generacion"); plt.ylabel("mejor fitness")\nplt.title("Convergencia del algoritmo genetico"); plt.show()',
            },
            {
                "title": "¿Encuentra el óptimo? (comparar con fuerza bruta)",
                "explain": "En un problema pequeño, comparamos el resultado del GA con el óptimo exacto por fuerza bruta.",
                "code": 'import numpy as np, itertools\nrng = np.random.default_rng(0)\nm = mochila(12)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5); n = len(m)\n\ndef fitness(ind):\n    return (ind * valores).sum() if (ind * pesos).sum() <= cap else 0\n\n# optimo exacto\nopt = 0\nfor combo in itertools.product([0, 1], repeat=n):\n    opt = max(opt, fitness(np.array(combo)))\n\n# GA rapido\ndef torneo(pob):\n    idx = rng.integers(0, len(pob), 3)\n    return pob[max(idx, key=lambda i: fitness(pob[i]))]\npob = rng.integers(0, 2, size=(40, n))\nfor _ in range(50):\n    pob = sorted(pob, key=fitness, reverse=True)\n    nueva = [pob[0].copy()]\n    while len(nueva) < 40:\n        a, b = torneo(pob), torneo(pob)\n        p = rng.integers(1, n); h = np.concatenate([a[:p], b[p:]])\n        i = rng.integers(n); h[i] = 1 - h[i]\n        nueva.append(h)\n    pob = np.array(nueva)\nprint("optimo (fuerza bruta):", opt)\nprint("mejor del GA         :", max(fitness(x) for x in pob))',
            },
        ],
        "dataset": "mochila()",
        "exercises": [
            "Crea una población de 8 individuos para <code>mochila(10)</code> y muestra el fitness de cada uno.",
            "Programa la selección por torneo con k = 2 y con k = 5; ¿cuál favorece más a los mejores?",
            "Implementa el cruce de un punto y verifica que el hijo mezcla genes de ambos padres.",
            "Prueba la mutación con probabilidad 0.01 y 0.2; observa cuántos genes cambian.",
            "Corre el GA completo en <code>mochila(15)</code> y reporta el mejor valor.",
            "Agrega elitismo de 2 individuos (conserva los 2 mejores) y compara.",
            "Grafica la curva de convergencia del GA.",
            "Compara el GA contra el óptimo por fuerza bruta en <code>mochila(12)</code>.",
            "Prueba dos tamaños de población (20 y 80) y compara resultado y velocidad.",
            "Explica en un comentario el papel de la mutación en mantener la diversidad.",
        ],
    },

    # ============================================================ CAP 47
    {
        "num": 47,
        "slug": "algoritmos-geneticos-2",
        "code": "leccion_47",
        "title": "Algoritmos genéticos II: el viajante (TSP)",
        "subtitle": "Cuando la solución es un orden: permutaciones, cruce OX y mutación",
        "apunte": "Módulo L · Lección 2 - GA para el TSP",
        "concepts": [
            ("Representación por permutación", "Cuando la solución es un <b>orden</b> (la secuencia de ciudades), el cromosoma es una <b>permutación</b>: cada ciudad aparece exactamente una vez."),
            ("Función de costo", "En el TSP se <b>minimiza</b> el <b>largo total</b> de la ruta cerrada. El fitness es menor cuanto más corta la ruta."),
            ("Problema del cruce clásico", "El cruce de un punto <b>rompe</b> una permutación: puede repetir o perder ciudades. Hace falta un cruce especial."),
            ("Cruce de orden (OX)", "<i>Order Crossover</i>: copia un tramo de un padre y completa con el orden del otro, <b>respetando</b> que no se repitan ciudades."),
            ("Mutación por intercambio", "Intercambiar dos ciudades de la ruta. Cambio pequeño que mantiene la permutación válida."),
            ("Mutación por inversión", "Invertir un tramo de la ruta (movimiento <b>2-opt</b>). Muy eficaz para desenredar cruces en el TSP."),
            ("Elitismo", "Conservar la mejor ruta de cada generación para no perderla por azar."),
            ("Diversidad", "Variedad de rutas en la población. Si se pierde, el GA converge antes de tiempo a una ruta mediocre."),
        ],
        "theory": """
<p><b>Otro tipo de solución: el orden.</b> En la mochila una solución era «qué llevo» (0/1). En el
<b>viajante (TSP)</b> la solución es «en qué <b>orden</b> visito las ciudades»: una <b>permutación</b>
en la que cada ciudad aparece una sola vez. Cambiar la representación cambia todo el maquinaje del GA,
y es una lección clave de ingeniería: <b>el operador debe respetar la estructura del problema</b>.</p>

<p><b>El costo a minimizar.</b> Para una ruta que empieza y termina en la misma ciudad, el costo es el
<b>largo total</b>: la suma de las distancias entre ciudades consecutivas, más el regreso al inicio.
Usaremos la matriz de <code>distancias(ciudades(...))</code> del motor. Como el GA suele pensarse para
<b>maximizar</b>, minimizar el largo equivale a maximizar su negativo.</p>

<p><b>Por qué el cruce clásico no sirve.</b> Si aplicamos el cruce de un punto a dos permutaciones,
el hijo puede quedar con <b>ciudades repetidas</b> y otras <b>faltantes</b>: deja de ser una ruta
válida. Necesitamos un cruce que combine el orden de los padres <b>sin romper la permutación</b>.</p>

<p><b>El cruce de orden (OX).</b> El <i>Order Crossover</i> resuelve esto con elegancia: copia un
<b>tramo</b> del primer padre al hijo, y luego rellena las posiciones restantes recorriendo al segundo
padre <b>en su orden</b>, saltando las ciudades ya presentes. Así el hijo hereda un bloque de un padre
y la secuencia relativa del otro, y siempre es una permutación válida.</p>

<p><b>Mutaciones que respetan la permutación.</b> Dos operadores clásicos: la <b>mutación por
intercambio</b> cambia de lugar dos ciudades; la <b>mutación por inversión</b> da vuelta un tramo
completo (el movimiento <b>2-opt</b>), que es especialmente bueno para <b>deshacer cruces</b> de la
ruta. Ambas mantienen la validez de la solución.</p>

<p><b>Elitismo y diversidad.</b> Igual que antes, conservamos la mejor ruta de cada generación
(elitismo) para no perderla. Y vigilamos la <b>diversidad</b>: si toda la población se vuelve casi la
misma ruta, el GA deja de mejorar. Poblaciones suficientes, algo de mutación y el OX ayudan a
mantenerla.</p>

<p><b>Resultado.</b> Con ciudades pocas (10–12) y una población modesta, el GA encuentra rutas muy
cercanas a la óptima en pocas generaciones, sin revisar ni una ínfima parte de las
<b>(n-1)!/2</b> rutas posibles. Es la demostración palpable del poder de las metaheurísticas.</p>
""",
        "examples": [
            {
                "title": "Una ruta es una permutación",
                "explain": "El cromosoma del TSP es un orden de ciudades. Calculamos el largo de la ruta cerrada.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\ncoords = ciudades(10)\nD = distancias(coords)\nn = len(coords)\n\ndef largo(ruta):\n    return sum(D[ruta[i], ruta[(i + 1) % n]] for i in range(n))\n\nruta = np.arange(n); rng.shuffle(ruta)\nprint("ruta:", ruta)\nprint("largo:", round(largo(ruta), 1))',
            },
            {
                "title": "Mutaciones por intercambio e inversión",
                "explain": "Dos formas de mutar una permutación sin romperla: cambiar dos ciudades o invertir un tramo (2-opt).",
                "code": 'import numpy as np\nrng = np.random.default_rng(1)\nruta = np.arange(8)\nprint("original     :", ruta)\n\ni, j = rng.integers(0, 8, 2)\nswap = ruta.copy(); swap[i], swap[j] = swap[j], swap[i]\nprint("intercambio  :", swap)\n\na, b = sorted(rng.integers(0, 8, 2))\ninv = ruta.copy(); inv[a:b+1] = inv[a:b+1][::-1]\nprint("inversion    :", inv)',
            },
            {
                "title": "Cruce de orden (OX)",
                "explain": "Copia un tramo del padre 1 y completa con el orden del padre 2 sin repetir ciudades.",
                "code": 'import numpy as np\nrng = np.random.default_rng(2)\n\ndef ox(p1, p2):\n    n = len(p1)\n    a, b = sorted(rng.integers(0, n, 2))\n    hijo = [-1] * n\n    hijo[a:b] = list(p1[a:b])            # tramo del padre 1\n    resto = [c for c in p2 if c not in hijo]\n    k = 0\n    for i in range(n):\n        if hijo[i] == -1:\n            hijo[i] = resto[k]; k += 1\n    return np.array(hijo)\n\np1 = np.array([0,1,2,3,4,5,6,7])\np2 = np.array([7,6,5,4,3,2,1,0])\nhijo = ox(p1, p2)\nprint("hijo:", hijo, "| valido:", sorted(hijo) == list(range(8)))',
            },
            {
                "title": "GA completo para el TSP",
                "explain": "Población de rutas, selección por torneo, cruce OX, mutación por inversión y elitismo.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\ncoords = ciudades(10); D = distancias(coords); n = len(coords)\n\ndef largo(r):\n    return sum(D[r[i], r[(i+1) % n]] for i in range(n))\ndef torneo(pob):\n    idx = rng.integers(0, len(pob), 3)\n    return pob[min(idx, key=lambda i: largo(pob[i]))]\ndef ox(p1, p2):\n    a, b = sorted(rng.integers(0, n, 2)); hijo = [-1]*n; hijo[a:b] = list(p1[a:b])\n    resto = [c for c in p2 if c not in hijo]; k = 0\n    for i in range(n):\n        if hijo[i] == -1: hijo[i] = resto[k]; k += 1\n    return np.array(hijo)\ndef mutar(r):\n    a, b = sorted(rng.integers(0, n, 2)); r = r.copy(); r[a:b+1] = r[a:b+1][::-1]; return r\n\npob = [rng.permutation(n) for _ in range(60)]\ninicial = min(largo(r) for r in pob)\nfor _ in range(120):\n    pob = sorted(pob, key=largo)\n    nueva = [pob[0].copy()]                 # elitismo\n    while len(nueva) < 60:\n        h = ox(torneo(pob), torneo(pob))\n        if rng.random() < 0.3: h = mutar(h)\n        nueva.append(h)\n    pob = nueva\nmejor = min(pob, key=largo)\nprint("largo inicial:", round(inicial, 1))\nprint("largo final  :", round(largo(mejor), 1))',
            },
            {
                "title": "Convergencia: GA vs. rutas al azar",
                "explain": "El GA baja el largo generación a generación, muy por debajo de lo que da probar rutas al azar.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(7)\ncoords = ciudades(10); D = distancias(coords); n = len(coords)\n\ndef largo(r):\n    return sum(D[r[i], r[(i+1) % n]] for i in range(n))\ndef torneo(pob):\n    idx = rng.integers(0, len(pob), 3)\n    return pob[min(idx, key=lambda i: largo(pob[i]))]\ndef ox(p1, p2):\n    a, b = sorted(rng.integers(0, n, 2)); hijo = [-1]*n; hijo[a:b] = list(p1[a:b])\n    resto = [c for c in p2 if c not in hijo]; k = 0\n    for i in range(n):\n        if hijo[i] == -1: hijo[i] = resto[k]; k += 1\n    return np.array(hijo)\ndef mutar(r):\n    a, b = sorted(rng.integers(0, n, 2)); r = r.copy(); r[a:b+1] = r[a:b+1][::-1]; return r\n\npob = [rng.permutation(n) for _ in range(60)]; curva = []\nazar = min(largo(rng.permutation(n)) for _ in range(120))\nfor _ in range(120):\n    pob = sorted(pob, key=largo); curva.append(largo(pob[0]))\n    nueva = [pob[0].copy()]\n    while len(nueva) < 60:\n        h = ox(torneo(pob), torneo(pob))\n        if rng.random() < 0.3: h = mutar(h)\n        nueva.append(h)\n    pob = nueva\nplt.plot(curva, label="GA")\nplt.axhline(azar, color="gray", ls="--", label="mejor de 120 al azar")\nplt.xlabel("generacion"); plt.ylabel("largo de la mejor ruta"); plt.legend()\nplt.title("GA para el TSP"); plt.show()',
            },
        ],
        "dataset": "ciudades(), distancias()",
        "exercises": [
            "Genera una ruta al azar para <code>ciudades(8)</code> y calcula su largo.",
            "Implementa la mutación por intercambio y verifica que sigue siendo una permutación válida.",
            "Implementa la mutación por inversión (2-opt) y compárala con el intercambio.",
            "Programa el cruce OX y comprueba que el hijo contiene todas las ciudades una vez.",
            "Corre el GA del TSP en <code>ciudades(10)</code> y reporta largo inicial y final.",
            "Compara el resultado del GA con el mejor de 200 rutas al azar.",
            "Grafica la curva de convergencia del largo.",
            "Prueba con y sin elitismo: ¿cambia el resultado?",
            "Sube a <code>ciudades(15)</code> y ajusta población/generaciones para que corra en pocos segundos.",
            "Explica en un comentario por qué el cruce de un punto no sirve para permutaciones.",
        ],
    },

    # ============================================================ CAP 48
    {
        "num": 48,
        "slug": "pso-enjambre",
        "code": "leccion_48",
        "title": "Optimización por enjambre de partículas (PSO)",
        "subtitle": "Un enjambre que se guía por su memoria y por el mejor del grupo",
        "apunte": "Módulo L · Lección 3 - PSO",
        "concepts": [
            ("Enjambre", "Conjunto de <b>partículas</b> que exploran juntas el espacio de soluciones, compartiendo información sobre lo mejor encontrado."),
            ("Partícula", "Una <b>solución candidata</b> con una posición (dónde está) y una velocidad (hacia dónde se mueve). Pensada para problemas <b>continuos</b>."),
            ("Posición y velocidad", "La <b>posición</b> es la solución actual; la <b>velocidad</b> es el vector de cambio que se le suma en cada paso."),
            ("Mejor personal (pbest)", "La mejor posición que <b>esa</b> partícula ha visitado. Su memoria individual."),
            ("Mejor global (gbest)", "La mejor posición encontrada por <b>todo</b> el enjambre. Guía al grupo entero."),
            ("Inercia (w)", "Cuánto conserva la partícula su velocidad previa. Alta = explora; baja = se asienta."),
            ("Coeficientes cognitivo/social", "<code>c1</code> tira hacia el <b>pbest</b> (experiencia propia) y <code>c2</code> hacia el <b>gbest</b> (experiencia del grupo)."),
            ("Convergencia", "Con el tiempo las partículas se agrupan cerca del mejor punto hallado. Balancear w, c1 y c2 evita converger demasiado pronto."),
        ],
        "theory": """
<p><b>Inteligencia de enjambre.</b> El <b>PSO</b> (<i>Particle Swarm Optimization</i>) se inspira en
cómo se mueven las bandadas de aves o los bancos de peces: individuos simples que, <b>compartiendo
información</b>, logran un comportamiento colectivo inteligente. Es una de las metaheurísticas más
usadas para <b>optimización continua</b> (variables reales), donde los genéticos binarios no encajan
tan natural.</p>

<p><b>Partículas con posición y velocidad.</b> Cada <b>partícula</b> es una solución candidata con dos
vectores: su <b>posición</b> (la solución actual) y su <b>velocidad</b> (cómo va a cambiar). En cada
paso, la partícula actualiza su velocidad y luego se mueve: <code>posición += velocidad</code>. Todo el
enjambre hace esto a la vez.</p>

<p><b>Dos memorias guían el vuelo.</b> La velocidad de cada partícula se ajusta mirando dos
referencias: su <b>mejor personal</b> (<i>pbest</i>, el mejor lugar que ella misma visitó) y el
<b>mejor global</b> (<i>gbest</i>, el mejor lugar hallado por todo el enjambre). Así cada partícula
combina su <b>experiencia propia</b> con la <b>sabiduría del grupo</b>.</p>

<p><b>La fórmula de actualización.</b> La nueva velocidad es
<code>v = w·v + c1·r1·(pbest − x) + c2·r2·(gbest − x)</code>. El primer término (<b>inercia</b>, w)
mantiene el rumbo; el segundo (<b>cognitivo</b>, c1) atrae hacia el mejor propio; el tercero
(<b>social</b>, c2) atrae hacia el mejor del grupo. Los <code>r1, r2</code> son aleatorios y dan
variedad. Valores típicos: w≈0.7, c1≈c2≈1.5.</p>

<p><b>El equilibrio explorar/explotar, otra vez.</b> Igual que en el recocido, PSO balancea explorar y
afinar, pero con parámetros: una <b>inercia</b> alta y coeficientes moderados exploran; bajarlos hace
que el enjambre <b>se asiente</b> en la mejor zona. Si converge demasiado rápido, todas las partículas
se juntan antes de haber explorado bien.</p>

<p><b>Sencillo y potente.</b> PSO es fácil de programar (unas pocas líneas de numpy), no necesita
derivadas y funciona muy bien en funciones multimodales como Rastrigin. Por eso es popular para
ajustar parámetros continuos, incluidos —lo veremos en el módulo N— algunos de modelos de machine
learning.</p>

<p><b>Vectorización.</b> Como todo el enjambre se actualiza con las mismas operaciones, PSO se
<b>vectoriza</b> muy bien con numpy: posiciones y velocidades son matrices y las fórmulas se aplican de
una vez. Eso lo hace rápido incluso en el navegador.</p>
""",
        "examples": [
            {
                "title": "Inicializar el enjambre",
                "explain": "Cada partícula tiene una posición y una velocidad. Aquí, 5 partículas en 2 dimensiones.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\nX = rng.uniform(-5, 5, size=(5, 2))    # posiciones\nV = rng.uniform(-1, 1, size=(5, 2))    # velocidades\nprint("posiciones:\\n", np.round(X, 2))\nprint("velocidades:\\n", np.round(V, 2))',
            },
            {
                "title": "Un paso de actualización de velocidad",
                "explain": "La velocidad combina inercia, atracción al mejor personal (pbest) y al mejor global (gbest).",
                "code": 'import numpy as np\nrng = np.random.default_rng(1)\nw, c1, c2 = 0.7, 1.5, 1.5\nx = np.array([2.0, -3.0]); v = np.array([0.5, 0.5])\npbest = np.array([1.0, -2.0]); gbest = np.array([0.0, 0.0])\n\nr1, r2 = rng.random(2), rng.random(2)\nv = w * v + c1 * r1 * (pbest - x) + c2 * r2 * (gbest - x)\nx = x + v\nprint("nueva velocidad:", np.round(v, 3))\nprint("nueva posicion :", np.round(x, 3))',
            },
            {
                "title": "PSO completo en la función esfera (2D)",
                "explain": "El enjambre minimiza x²+y² (óptimo en el origen). En pocas iteraciones converge.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\n\ndef f(P):\n    return (P ** 2).sum(axis=1)     # esfera, minimo en (0,0)\n\nN, dim = 30, 2\nX = rng.uniform(-5, 5, (N, dim)); V = rng.uniform(-1, 1, (N, dim))\npbest = X.copy(); pbest_val = f(X)\ng = pbest[pbest_val.argmin()].copy()\nw, c1, c2 = 0.7, 1.5, 1.5\nfor _ in range(50):\n    r1, r2 = rng.random((N, dim)), rng.random((N, dim))\n    V = w * V + c1 * r1 * (pbest - X) + c2 * r2 * (g - X)\n    X = X + V\n    val = f(X)\n    mejora = val < pbest_val\n    pbest[mejora] = X[mejora]; pbest_val[mejora] = val[mejora]\n    g = pbest[pbest_val.argmin()].copy()\nprint("mejor posicion:", np.round(g, 4), "| f:", round(f(g[None])[0], 6))',
            },
            {
                "title": "PSO en Rastrigin (multimodal)",
                "explain": "En una función llena de mínimos locales, el enjambre suele hallar el óptimo global cerca de (0,0).",
                "code": 'import numpy as np\nrng = np.random.default_rng(3)\n\ndef rastrigin(P):\n    return 20 + (P**2 - 10 * np.cos(2 * np.pi * P)).sum(axis=1)\n\nN, dim = 40, 2\nX = rng.uniform(-5, 5, (N, dim)); V = rng.uniform(-1, 1, (N, dim))\npbest = X.copy(); pbest_val = rastrigin(X)\ng = pbest[pbest_val.argmin()].copy()\nw, c1, c2 = 0.7, 1.5, 1.5\nfor _ in range(80):\n    r1, r2 = rng.random((N, dim)), rng.random((N, dim))\n    V = w * V + c1 * r1 * (pbest - X) + c2 * r2 * (g - X)\n    X = np.clip(X + V, -5, 5)\n    val = rastrigin(X); mejora = val < pbest_val\n    pbest[mejora] = X[mejora]; pbest_val[mejora] = val[mejora]\n    g = pbest[pbest_val.argmin()].copy()\nprint("mejor:", np.round(g, 3), "| f:", round(rastrigin(g[None])[0], 4), "(optimo: 0)")',
            },
            {
                "title": "Curva de convergencia del enjambre",
                "explain": "Graficamos el mejor valor global por iteración: baja rápido y se estabiliza.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(7)\n\ndef f(P):\n    return (P ** 2).sum(axis=1)\n\nN, dim = 30, 2\nX = rng.uniform(-5, 5, (N, dim)); V = rng.uniform(-1, 1, (N, dim))\npbest = X.copy(); pbest_val = f(X); g = pbest[pbest_val.argmin()].copy()\nw, c1, c2 = 0.7, 1.5, 1.5; curva = []\nfor _ in range(50):\n    r1, r2 = rng.random((N, dim)), rng.random((N, dim))\n    V = w * V + c1 * r1 * (pbest - X) + c2 * r2 * (g - X)\n    X = X + V; val = f(X); mejora = val < pbest_val\n    pbest[mejora] = X[mejora]; pbest_val[mejora] = val[mejora]\n    g = pbest[pbest_val.argmin()].copy(); curva.append(f(g[None])[0])\nplt.plot(curva); plt.xlabel("iteracion"); plt.ylabel("mejor f global")\nplt.title("Convergencia de PSO (esfera)"); plt.show()',
            },
        ],
        "dataset": "funciones de prueba",
        "exercises": [
            "Inicializa un enjambre de 10 partículas en 2D y muestra posiciones y velocidades.",
            "Aplica un paso de actualización de velocidad a una partícula y comenta cada término.",
            "Corre PSO en la función esfera 2D y reporta el mejor punto.",
            "Corre PSO en Rastrigin 2D y compáralo con el óptimo global (0,0).",
            "Prueba tres valores de inercia (0.4, 0.7, 0.9) y compara la convergencia.",
            "Grafica la curva de convergencia del mejor valor global.",
            "Aumenta el enjambre a 100 partículas: ¿mejora el resultado? ¿y la velocidad?",
            "Extiende PSO a 3 dimensiones en la función esfera.",
            "Limita las posiciones al rango [-5, 5] con <code>np.clip</code> y observa el efecto.",
            "Explica en un comentario la diferencia entre pbest y gbest.",
        ],
    },

    # ============================================================ CAP 49
    {
        "num": 49,
        "slug": "colonia-hormigas",
        "code": "leccion_49",
        "title": "Colonia de hormigas (ACO)",
        "subtitle": "Rastros de feromona que construyen, entre muchas, una buena ruta",
        "apunte": "Módulo L · Lección 4 - Colonia de hormigas",
        "concepts": [
            ("Colonia de hormigas (ACO)", "Metaheurística inspirada en cómo las hormigas hallan caminos cortos dejando <b>feromona</b>: los buenos caminos se refuerzan y atraen a más hormigas."),
            ("Feromona (τ)", "Rastro químico simulado en cada arista (ciudad→ciudad). Cuanta más feromona, más probable que una hormiga tome ese paso."),
            ("Visibilidad / heurística (η)", "Información local: normalmente <b>1/distancia</b>. Favorece los pasos cortos, aunque no haya feromona todavía."),
            ("Regla de transición", "La probabilidad de ir a una ciudad combina feromona y visibilidad: <code>τ^α · η^β</code>, normalizado entre las ciudades no visitadas."),
            ("α y β", "Pesos: <b>α</b> da importancia a la feromona (experiencia colectiva) y <b>β</b> a la visibilidad (distancia). Su balance define el comportamiento."),
            ("Evaporación (ρ)", "En cada ciclo la feromona <b>se reduce</b> un factor ρ. Evita que rastros viejos dominen para siempre y ayuda a explorar."),
            ("Depósito de feromona", "Tras cada ciclo, las hormigas <b>refuerzan</b> las aristas de sus rutas, más cuanto más corta sea la ruta (p. ej. 1/largo)."),
            ("Convergencia", "Con los ciclos, la feromona se concentra en las mejores aristas y la colonia converge hacia una ruta corta."),
        ],
        "theory": """
<p><b>Sabiduría de la colonia.</b> Las hormigas reales encuentran el camino más corto entre el hormiguero
y la comida sin ver el mapa: al caminar dejan <b>feromona</b>, y como los caminos cortos se recorren
más rápido, acumulan más feromona y atraen a más hormigas. El <b>ACO</b> (<i>Ant Colony
Optimization</i>) lleva esa idea al computador para resolver problemas de rutas como el <b>TSP</b>.</p>

<p><b>Dos señales guían a cada hormiga.</b> Cuando una hormiga está en una ciudad y decide a cuál ir,
combina dos informaciones. La <b>feromona</b> (τ) en cada arista: la <b>experiencia colectiva</b> de
las hormigas anteriores. Y la <b>visibilidad</b> (η), normalmente <b>1/distancia</b>: una preferencia
local por los pasos cortos. Al principio no hay feromona, así que manda la visibilidad; con los ciclos,
la feromona empieza a pesar.</p>

<p><b>La regla de transición.</b> La probabilidad de que una hormiga vaya de la ciudad <i>i</i> a la
<i>j</i> es proporcional a <code>τ(i,j)^α · η(i,j)^β</code>, normalizada entre las ciudades <b>aún no
visitadas</b>. El exponente <b>α</b> pondera la feromona y <b>β</b> la visibilidad. Con α alto la
colonia sigue a la mayoría; con β alto, prioriza lo cercano. Es una decisión <b>probabilística</b>:
por eso distintas hormigas construyen rutas distintas.</p>

<p><b>Evaporación: olvidar para explorar.</b> Si la feromona solo se acumulara, los primeros caminos
dominarían para siempre. Por eso en cada ciclo <b>se evapora</b> una fracción ρ:
<code>τ = (1−ρ)·τ</code>. La evaporación borra poco a poco los rastros viejos y mantiene viva la
exploración, un equilibrio parecido al de las otras metaheurísticas.</p>

<p><b>Depósito: reforzar lo bueno.</b> Después de que todas las hormigas construyen su ruta, cada una
<b>deposita</b> feromona en las aristas que usó, y <b>más cuanto más corta</b> sea su ruta (por ejemplo
<code>1/largo</code>). Así las buenas rutas se refuerzan y, ciclo a ciclo, la feromona se concentra en
las aristas que forman recorridos cortos.</p>

<p><b>El ciclo completo.</b> Un ciclo de ACO es: cada hormiga construye una ruta con la regla de
transición; se evapora la feromona; se deposita según la calidad de cada ruta; se guarda la mejor ruta
vista. Repetir varios ciclos hace que la colonia <b>converja</b> hacia una solución corta, sin que
ninguna hormiga haya visto el problema completo.</p>

<p><b>Un final del módulo con broche.</b> ACO cierra las metaheurísticas bioinspiradas: como el genético
y el enjambre, es una <b>población</b> que coopera; como el recocido, equilibra explorar y explotar. Con
tamaños pequeños (10 ciudades, 20 hormigas, 50 ciclos) corre bien en el navegador y muestra el óptimo
del TSP emergiendo de reglas locales simples.</p>
""",
        "examples": [
            {
                "title": "Visibilidad: preferir lo cercano",
                "explain": "La visibilidad η es 1/distancia. Se calcula una vez desde la matriz de distancias (la diagonal se anula).",
                "code": 'import numpy as np\ncoords = ciudades(6); D = distancias(coords)\nwith np.errstate(divide="ignore"):\n    eta = 1.0 / D\neta[np.isinf(eta)] = 0.0        # sin auto-viajes\nprint(np.round(eta, 3))',
            },
            {
                "title": "Una hormiga construye una ruta",
                "explain": "Desde una ciudad, elige la siguiente con probabilidad proporcional a τ^α · η^β entre las no visitadas.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\ncoords = ciudades(8); D = distancias(coords); n = len(coords)\nwith np.errstate(divide="ignore"):\n    eta = 1.0 / D\neta[np.isinf(eta)] = 0.0\ntau = np.ones((n, n))          # feromona inicial uniforme\nalpha, beta = 1.0, 3.0\n\nactual = 0; ruta = [0]; visit = {0}\nfor _ in range(n - 1):\n    cand = [j for j in range(n) if j not in visit]\n    pesos = np.array([tau[actual, j]**alpha * eta[actual, j]**beta for j in cand])\n    pesos = pesos / pesos.sum()\n    sig = rng.choice(cand, p=pesos)\n    ruta.append(int(sig)); visit.add(int(sig)); actual = int(sig)\nprint("ruta construida:", ruta)',
            },
            {
                "title": "Evaporación y depósito de feromona",
                "explain": "Tras un ciclo: la feromona se evapora y cada hormiga refuerza sus aristas según 1/largo de su ruta.",
                "code": 'import numpy as np\ncoords = ciudades(6); D = distancias(coords); n = len(coords)\ntau = np.ones((n, n)); rho = 0.3\n\ndef largo(r):\n    return sum(D[r[i], r[(i+1) % n]] for i in range(n))\n\nrutas = [[0,1,2,3,4,5], [0,2,4,1,3,5]]\ntau *= (1 - rho)                         # evaporacion\nfor r in rutas:\n    aporte = 1.0 / largo(r)\n    for i in range(n):\n        a, b = r[i], r[(i+1) % n]\n        tau[a, b] += aporte; tau[b, a] += aporte\nprint("feromona tras un ciclo (redondeada):\\n", np.round(tau, 2))',
            },
            {
                "title": "ACO completo para el TSP",
                "explain": "Varias hormigas por ciclo, evaporación y depósito. La colonia converge a una ruta corta.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\ncoords = ciudades(10); D = distancias(coords); n = len(coords)\nwith np.errstate(divide="ignore"):\n    eta = 1.0 / D\neta[np.isinf(eta)] = 0.0\ntau = np.ones((n, n))\nalpha, beta, rho, hormigas = 1.0, 3.0, 0.3, 20\n\ndef largo(r):\n    return sum(D[r[i], r[(i+1) % n]] for i in range(n))\n\ndef construir():\n    actual = rng.integers(n); ruta = [actual]; visit = {actual}\n    for _ in range(n - 1):\n        cand = [j for j in range(n) if j not in visit]\n        p = np.array([tau[actual, j]**alpha * eta[actual, j]**beta for j in cand])\n        p = p / p.sum(); sig = int(rng.choice(cand, p=p))\n        ruta.append(sig); visit.add(sig); actual = sig\n    return ruta\n\nmejor, mejor_l = None, 1e9\nfor ciclo in range(50):\n    rutas = [construir() for _ in range(hormigas)]\n    tau *= (1 - rho)\n    for r in rutas:\n        L = largo(r)\n        if L < mejor_l: mejor, mejor_l = r, L\n        for i in range(n):\n            a, b = r[i], r[(i+1) % n]\n            tau[a, b] += 1.0 / L; tau[b, a] += 1.0 / L\nprint("mejor largo hallado:", round(mejor_l, 1))',
            },
            {
                "title": "Curva de convergencia de la colonia",
                "explain": "Guardamos el mejor largo por ciclo: la colonia mejora hasta estabilizarse.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(7)\ncoords = ciudades(10); D = distancias(coords); n = len(coords)\nwith np.errstate(divide="ignore"):\n    eta = 1.0 / D\neta[np.isinf(eta)] = 0.0\ntau = np.ones((n, n)); alpha, beta, rho = 1.0, 3.0, 0.3\n\ndef largo(r):\n    return sum(D[r[i], r[(i+1) % n]] for i in range(n))\ndef construir():\n    actual = rng.integers(n); ruta = [actual]; visit = {actual}\n    for _ in range(n - 1):\n        cand = [j for j in range(n) if j not in visit]\n        p = np.array([tau[actual, j]**alpha * eta[actual, j]**beta for j in cand])\n        p = p / p.sum(); sig = int(rng.choice(cand, p=p))\n        ruta.append(sig); visit.add(sig); actual = sig\n    return ruta\n\nmejor_l = 1e9; curva = []\nfor ciclo in range(50):\n    rutas = [construir() for _ in range(20)]\n    tau *= (1 - rho)\n    for r in rutas:\n        L = largo(r); mejor_l = min(mejor_l, L)\n        for i in range(n):\n            a, b = r[i], r[(i+1) % n]\n            tau[a, b] += 1.0 / L; tau[b, a] += 1.0 / L\n    curva.append(mejor_l)\nplt.plot(curva); plt.xlabel("ciclo"); plt.ylabel("mejor largo")\nplt.title("Colonia de hormigas (ACO) en el TSP"); plt.show()',
            },
        ],
        "dataset": "ciudades(), distancias()",
        "exercises": [
            "Calcula la matriz de visibilidad η = 1/distancia para <code>ciudades(6)</code>.",
            "Haz que una hormiga construya una ruta con feromona uniforme y muéstrala.",
            "Aplica evaporación (ρ = 0.5) a una matriz de feromona y observa el efecto.",
            "Deposita feromona de dos rutas y verifica que la más corta aporta más.",
            "Corre el ACO completo en <code>ciudades(10)</code> y reporta el mejor largo.",
            "Compara el ACO con el recocido simulado (lección 44) en el mismo problema.",
            "Prueba distintos β (1, 3, 5): ¿cómo cambia el resultado?",
            "Prueba distintos ρ (0.1, 0.3, 0.6): ¿cómo afecta la exploración?",
            "Grafica la curva de convergencia del mejor largo por ciclo.",
            "Explica en un comentario el papel de la evaporación de feromona.",
        ],
    },
]
