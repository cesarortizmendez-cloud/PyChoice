# -*- coding: utf-8 -*-
"""
PyChoice - Ruta "Ingeniero de IA con Python".
Modulo J - Fundamentos de IA y pensamiento algoritmico (lecciones 39-41).

Todo el codigo corre en el navegador (numpy, matplotlib bajo demanda).
Se usan los generadores de problemas del motor: mochila(), ciudades(), distancias().
"""

CHAPTERS_J = [

    # ============================================================ CAP 39
    {
        "num": 39,
        "slug": "ia-panorama",
        "code": "leccion_39",
        "title": "Panorama de la IA con Python",
        "subtitle": "Qué es la inteligencia artificial y cómo se programa desde su base",
        "apunte": "Módulo J · Lección 1 - Panorama de la IA",
        "concepts": [
            ("Inteligencia Artificial (IA)", "Conjunto de técnicas que permiten a un programa <b>resolver problemas que asociamos a la inteligencia</b>: decidir, aprender, buscar, optimizar o razonar. No es una sola cosa: es una familia de enfoques."),
            ("Aprendizaje automático (ML)", "Rama de la IA donde el programa <b>aprende patrones a partir de datos</b> en vez de seguir reglas fijas. Es lo que viste en el módulo H (regresión, clasificación)."),
            ("Optimización", "Encontrar la <b>mejor solución</b> posible según un criterio (máximo beneficio, mínimo costo). Gran parte de la IA moderna es, por dentro, optimización."),
            ("Búsqueda", "Explorar un conjunto de soluciones posibles para hallar una buena. Muchos problemas de IA se plantean como <b>buscar</b> en un espacio enorme."),
            ("Agente", "Programa que <b>percibe</b> una situación y <b>actúa</b> para lograr un objetivo. Un robot, un jugador automático o un recomendador son agentes."),
            ("Función objetivo (fitness)", "La medida numérica de <b>qué tan buena es una solución</b>. Optimizar es hacerla lo más grande (o pequeña) posible. Es el corazón de casi todo algoritmo de IA."),
            ("Heurística", "Una regla práctica que da <b>buenas soluciones rápido</b>, sin garantía de que sean las mejores. Ejemplo: «elige siempre lo que más rinde ahora»."),
            ("Metaheurística", "Estrategia general de búsqueda que <b>guía</b> a las heurísticas para explorar bien el espacio de soluciones (genéticos, hormigas, recocido…). Son el eje de esta ruta."),
        ],
        "theory": """
<p><b>¿Qué es realmente la inteligencia artificial?</b> Más allá del marketing, la IA es un
<b>conjunto de técnicas</b> para que un programa resuelva problemas difíciles: decidir entre muchas
opciones, aprender de ejemplos, encontrar la mejor combinación posible o planificar una secuencia de
acciones. No existe «la» IA: existen <b>familias</b> de métodos, y un buen ingeniero sabe cuál usar
para cada problema.</p>

<p><b>Las grandes familias.</b> La <b>IA simbólica</b> resuelve con reglas y lógica explícita (si pasa
esto, haz aquello). El <b>aprendizaje automático (ML)</b> —que ya conociste— aprende patrones desde
datos. La <b>optimización y la búsqueda</b> exploran un espacio de soluciones para hallar la mejor. Y
los <b>agentes</b> perciben y actúan en un entorno para lograr metas (ahí entra el aprendizaje por
refuerzo). Esta ruta se concentra en <b>optimización, metaheurísticas y redes neuronales</b>, que son
la base sobre la que se construye casi todo lo demás.</p>

<p><b>La idea que une todo: la función objetivo.</b> Casi cualquier problema de IA se puede escribir
así: hay muchas <b>soluciones posibles</b> y una <b>función objetivo</b> (o <i>fitness</i>) que le
pone nota a cada una. El trabajo del algoritmo es <b>encontrar la solución con mejor nota</b>.
Entrenar una red neuronal es minimizar el error; planificar una ruta es minimizar la distancia; armar
una cartera es maximizar el retorno. Si aprendes a pensar en términos de «solución + función
objetivo», ya piensas como ingeniero de IA.</p>

<p><b>¿Por qué programar los algoritmos desde su base?</b> Hoy es fácil llamar a una librería y
obtener un resultado. Pero entender <b>cómo funciona por dentro</b> un algoritmo genético o el
descenso de gradiente es lo que te permite elegir bien, ajustar cuando falla y no tratar la IA como
una caja negra. Por eso en esta ruta los construiremos <b>a mano</b> con numpy antes (o además) de
usar librerías.</p>

<p><b>Heurísticas y metaheurísticas.</b> Muchos problemas tienen tantas soluciones posibles que
probarlas todas es imposible (lo veremos en la próxima lección). Ahí aparecen las <b>heurísticas</b>:
reglas prácticas que dan buenas respuestas rápido. Y las <b>metaheurísticas</b> —genéticos, colonia
de hormigas, recocido simulado, enjambre de partículas— son estrategias generales que guían la
búsqueda de forma inteligente, inspiradas muchas veces en la naturaleza. Son el corazón de los
módulos K y L.</p>

<p><b>Python e IA, y el caso de PyChoice.</b> Python es hoy el lenguaje dominante de la IA por su
legibilidad y su ecosistema: <b>numpy</b> (cálculo), <b>scikit-learn</b> (ML clásico), <b>scipy</b>
(optimización) y, fuera del navegador, PyTorch y TensorFlow para deep learning. En PyChoice todo corre
en tu navegador con numpy, scipy y scikit-learn; construiremos metaheurísticas y redes desde cero, que
es la mejor forma de <b>entenderlas de verdad</b>. El deep learning con frameworks lo veremos como
teoría y siguiente paso.</p>

<p><b>Un cambio de mentalidad.</b> Programar IA no es memorizar fórmulas: es <b>modelar</b> un
problema (¿qué es una solución?, ¿cómo la puntúo?) y luego <b>elegir una estrategia</b> para buscar la
mejor. Empecemos con esa forma de pensar.</p>
""",
        "examples": [
            {
                "title": "Una función objetivo mide qué tan buena es una solución",
                "explain": "En IA, casi todo parte de una <b>función objetivo</b>: recibe una solución y devuelve una nota. Aquí su máximo está en x = 3.",
                "code": 'def calidad(x):\n    return -(x - 3) ** 2 + 10   # nota maxima cuando x = 3\n\nfor x in [0, 1, 3, 5]:\n    print("x =", x, "-> calidad =", calidad(x))',
            },
            {
                "title": "Decidir = elegir la mejor opción",
                "explain": "Un agente que decide compara opciones y toma la de mayor puntaje. Esto ya es una forma simple de IA.",
                "code": 'opciones = ["A", "B", "C", "D"]\npuntajes = [7, 9, 4, 8]\n\nmejor = puntajes.index(max(puntajes))\nprint("Mejor opcion:", opciones[mejor], "con puntaje", puntajes[mejor])',
            },
            {
                "title": "Fuerza bruta: probar todas las opciones",
                "explain": "Si el espacio es pequeño, podemos evaluar <b>todas</b> las soluciones y quedarnos con la mejor. Garantiza el óptimo… si alcanzan las combinaciones.",
                "code": 'def calidad(x):\n    return -(x - 3) ** 2 + 10\n\nmejor_x, mejor_v = None, -1e9\nfor x in range(0, 11):          # probar TODOS los enteros de 0 a 10\n    v = calidad(x)\n    if v > mejor_v:\n        mejor_x, mejor_v = x, v\n\nprint("Mejor x:", mejor_x, "| calidad:", mejor_v)',
            },
            {
                "title": "Una heurística: elige lo que más rinde",
                "explain": "Una <b>heurística voraz</b> para la mochila: meter primero lo de mejor relación valor/peso. Rápida, aunque no siempre óptima.",
                "code": 'import numpy as np\n\nvalores = np.array([60, 100, 120])\npesos   = np.array([10, 20, 30])\ncapacidad = 50\n\norden = np.argsort(-(valores / pesos))   # mejor ratio primero\npeso, valor = 0, 0\nfor i in orden:\n    if peso + pesos[i] <= capacidad:\n        peso += pesos[i]; valor += valores[i]\n\nprint("Heuristica voraz -> valor:", valor, "| peso:", peso, "/", capacidad)',
            },
            {
                "title": "El azar como herramienta de búsqueda",
                "explain": "Cuando no podemos probar todo, generamos soluciones <b>al azar</b> y nos quedamos con la mejor. Es la base de las metaheurísticas.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\n\ndef calidad(x):\n    return -(x - 3) ** 2 + 10\n\nmejor = -1e9\nfor _ in range(20):\n    x = rng.uniform(0, 10)        # candidato al azar\n    mejor = max(mejor, calidad(x))\n\nprint("Mejor calidad hallada al azar:", round(mejor, 3))',
            },
            {
                "title": "Un problema real ya cargado: la mochila",
                "explain": "PyChoice trae generadores de problemas. <code>mochila(n)</code> crea objetos con peso y valor para practicar optimización.",
                "code": 'm = mochila(8)     # generador incluido en PyChoice\nprint(m)\nprint("peso total si llevo todo:", m["peso"].sum())\nprint("valor total si llevo todo:", m["valor"].sum())',
            },
        ],
        "dataset": "mochila(), ciudades()",
        "exercises": [
            "Escribe una función objetivo <code>calidad(x) = -(x-5)**2 + 20</code> y evalúala en x = 0, 3, 5 y 8. ¿Dónde da el máximo?",
            "Dada la lista <code>puntajes = [3, 8, 5, 9, 2]</code>, encuentra e imprime el índice y el valor del mejor.",
            "Con fuerza bruta, busca el entero entre 0 y 20 que maximiza <code>-(x-7)**2 + 50</code>.",
            "Genera <code>mochila(6)</code> y muestra la relación valor/peso de cada objeto.",
            "Aplica la heurística voraz (mejor ratio primero) a <code>mochila(6)</code> con capacidad = la mitad del peso total.",
            "Usa <code>rng = np.random.default_rng(1)</code> para generar 30 valores al azar en [0, 10] y quédate con el que maximiza <code>-(x-3)**2+10</code>.",
            "Explica en un comentario la diferencia entre una <b>heurística</b> y la <b>fuerza bruta</b>.",
            "Crea 4 «agentes» con puntajes distintos y decide cuál actúa (el de mayor puntaje) usando <code>max()</code>.",
            "Con <code>ciudades(5)</code>, muestra las coordenadas y calcula la distancia entre la ciudad 0 y la 1 (usa <code>np.hypot</code> o Pitágoras).",
            "Reflexiona en código: imprime cuántas combinaciones hay que revisar en una mochila de 20 objetos (<code>2**20</code>).",
        ],
    },

    # ============================================================ CAP 40
    {
        "num": 40,
        "slug": "ia-busqueda-optimizacion",
        "code": "leccion_40",
        "title": "Problemas de búsqueda y optimización",
        "subtitle": "Cómo modelar un problema: solución, objetivo, restricciones y vecindario",
        "apunte": "Módulo J · Lección 2 - Búsqueda y optimización",
        "concepts": [
            ("Representación de la solución", "Cómo se <b>codifica</b> una solución en datos: una lista de 0/1 (llevo/no llevo), una permutación (orden de ciudades), un vector de números. Elegir bien la representación es medio problema resuelto."),
            ("Espacio de soluciones", "El <b>conjunto de todas</b> las soluciones posibles. Suele ser gigantesco: por eso no se puede revisar entero."),
            ("Función de costo/objetivo", "La nota de cada solución. En un problema de <b>minimizar</b> se llama costo; en uno de <b>maximizar</b>, objetivo o fitness."),
            ("Restricciones", "Condiciones que una solución <b>debe cumplir</b> para ser válida (p. ej. no superar la capacidad de la mochila). Las que no cumplen son <b>infactibles</b>."),
            ("Vecindario", "El conjunto de soluciones «parecidas» a una dada, a las que se llega con un <b>pequeño cambio</b> (cambiar un bit, intercambiar dos ciudades). Clave para la búsqueda local."),
            ("Fuerza bruta", "Evaluar <b>todas</b> las soluciones. Garantiza el óptimo pero solo sirve en espacios pequeños."),
            ("Búsqueda voraz (greedy)", "Construir la solución tomando en cada paso <b>lo que parece mejor ahora</b>. Rápida, pero puede quedar lejos del óptimo."),
            ("Explosión combinatoria", "El espacio de soluciones crece <b>explosivamente</b> con el tamaño (2ⁿ, n!). Por eso la fuerza bruta se vuelve imposible enseguida."),
        ],
        "theory": """
<p><b>Modelar antes de programar.</b> Frente a un problema de IA, lo primero no es escribir código:
es <b>modelar</b>. Hay que responder tres preguntas. ¿Qué es una <b>solución</b> y cómo la
represento? ¿Cómo <b>puntúo</b> una solución (función objetivo o costo)? ¿Qué <b>restricciones</b>
debe cumplir para ser válida? Con esas tres respuestas, cualquier método de búsqueda se vuelve
aplicable.</p>

<p><b>La representación lo es casi todo.</b> Una misma realidad se puede codificar de varias formas, y
la elección cambia por completo la dificultad. En la <b>mochila</b>, una solución es una lista de
ceros y unos: <code>[1,0,1,...]</code> indica qué objetos llevo. En el <b>viajante (TSP)</b>, una
solución es una <b>permutación</b>: el orden en que visito las ciudades. Elegir una buena
representación —compacta y fácil de modificar— es medio problema resuelto.</p>

<p><b>El espacio de soluciones es enorme.</b> El conjunto de todas las soluciones posibles crece muy
rápido. Con n objetos en la mochila hay <b>2ⁿ</b> combinaciones; con n ciudades hay del orden de
<b>n!</b> rutas. Para 20 objetos son más de un millón; para 15 ciudades, billones de rutas. A esto se
le llama <b>explosión combinatoria</b>, y es la razón de ser de toda esta ruta: cuando no se puede
revisar todo, hay que <b>buscar con inteligencia</b>.</p>

<p><b>Fuerza bruta: correcta pero cara.</b> La fuerza bruta evalúa <b>todas</b> las soluciones y
garantiza encontrar la mejor. Es la referencia ideal… pero solo funciona en problemas pequeños. Nos
sirve para <b>comprobar</b> si un método más rápido encuentra el óptimo en casos chicos, antes de
soltarlo en problemas grandes.</p>

<p><b>Búsqueda voraz (greedy): rápida pero miope.</b> Una estrategia mucho más veloz es construir la
solución tomando en cada paso <b>lo que más conviene en ese momento</b> (en la mochila, el objeto de
mejor relación valor/peso). Suele dar resultados decentes al instante, pero es <b>miope</b>: una buena
decisión local puede cerrar el paso a una solución global mejor. Comparar greedy contra la fuerza
bruta en casos pequeños enseña mucho.</p>

<p><b>Restricciones y factibilidad.</b> Casi todo problema real tiene <b>restricciones</b>: la mochila
no puede superar su capacidad, una ruta debe visitar cada ciudad una sola vez. Una solución que las
viola es <b>infactible</b> y hay que descartarla o penalizarla. Manejar bien las restricciones es
parte esencial del oficio.</p>

<p><b>Vecindario: la puerta a la búsqueda local.</b> Si tengo una solución, sus <b>vecinas</b> son
las que obtengo con un <b>cambio pequeño</b>: cambiar un bit en la mochila, intercambiar dos ciudades
en una ruta. Moverse de una solución a una vecina mejor es la idea del <b>hill climbing</b> y de casi
todas las metaheurísticas que veremos. Definir bien el vecindario es definir cómo se explora.</p>
""",
        "examples": [
            {
                "title": "Representar una solución de la mochila",
                "explain": "Una lista de 0/1 dice qué objetos llevo. Con ella calculamos peso y valor totales.",
                "code": 'import numpy as np\nm = mochila(8)\npesos = m["peso"].to_numpy()\nvalores = m["valor"].to_numpy()\n\nsel = np.array([1, 0, 1, 0, 0, 1, 0, 1])   # solucion: 1 = lo llevo\nprint("peso total :", (sel * pesos).sum())\nprint("valor total:", (sel * valores).sum())',
            },
            {
                "title": "Fuerza bruta en la mochila (n pequeño)",
                "explain": "Con 10 objetos hay solo 1024 combinaciones: podemos probarlas todas y hallar el óptimo exacto.",
                "code": 'import numpy as np, itertools\nm = mochila(10)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5)\n\nmejor_v, mejor_sel = 0, None\nfor combo in itertools.product([0, 1], repeat=len(m)):\n    sel = np.array(combo)\n    if (sel * pesos).sum() <= cap:          # respeta la restriccion\n        v = (sel * valores).sum()\n        if v > mejor_v:\n            mejor_v, mejor_sel = v, sel\n\nprint("capacidad:", cap, "| valor optimo:", mejor_v)\nprint("seleccion optima:", mejor_sel)',
            },
            {
                "title": "Búsqueda voraz y comparación con el óptimo",
                "explain": "La heurística voraz es instantánea. Compárala con el óptimo del ejemplo anterior: a veces coincide, a veces no.",
                "code": 'import numpy as np\nm = mochila(10)\npesos = m["peso"].to_numpy(); valores = m["valor"].to_numpy()\ncap = int(pesos.sum() * 0.5)\n\norden = np.argsort(-(valores / pesos))    # mejor ratio primero\npeso, valor = 0, 0\nfor i in orden:\n    if peso + pesos[i] <= cap:\n        peso += pesos[i]; valor += valores[i]\n\nprint("Voraz -> valor:", valor, "| peso:", peso, "/", cap)',
            },
            {
                "title": "La explosión combinatoria",
                "explain": "Por esto la fuerza bruta se vuelve imposible: el número de soluciones crece sin control.",
                "code": 'import math\nprint("MOCHILA (2^n combinaciones):")\nfor n in [10, 20, 30, 50]:\n    print(f"  {n:>3} objetos -> {2**n:,} combinaciones")\n\nprint("\\nTSP (rutas distintas ~ (n-1)!/2):")\nfor n in [5, 8, 10, 12]:\n    print(f"  {n:>3} ciudades -> {math.factorial(n-1)//2:,} rutas")',
            },
            {
                "title": "El vecindario de una solución",
                "explain": "Las vecinas se obtienen con un cambio mínimo: aquí, invertir un bit. La búsqueda local se mueve entre vecinas.",
                "code": 'import numpy as np\nsol = np.array([0, 1, 0, 0, 1])\nprint("solucion:", sol)\nprint("vecinas (cambiando un bit cada vez):")\nfor i in range(len(sol)):\n    v = sol.copy(); v[i] = 1 - v[i]\n    print("  ", v)',
            },
        ],
        "dataset": "mochila(), ciudades()",
        "exercises": [
            "Genera <code>mochila(8)</code> y evalúa la solución <code>[1,1,0,0,1,0,1,0]</code>: peso y valor totales.",
            "Comprueba si esa solución es <b>factible</b> con capacidad = 60 (peso ≤ 60).",
            "Aplica fuerza bruta a <code>mochila(12)</code> con capacidad = mitad del peso total y reporta el valor óptimo (ojo: 2¹² = 4096, aún manejable).",
            "Aplica la heurística voraz al mismo problema y compara con el óptimo: ¿coinciden?",
            "Imprime, con un bucle, cuántas combinaciones tiene una mochila de 5, 10, 15 y 20 objetos.",
            "Genera todas las vecinas (cambiando un bit) de <code>[1,0,1,0]</code>.",
            "Para <code>ciudades(6)</code>, construye la matriz de distancias con <code>distancias(ciudades(6))</code> y muestra su forma.",
            "Calcula el largo de la ruta 0→1→2→3→4→5→0 sumando distancias consecutivas de esa matriz.",
            "Escribe una función <code>factible(sel, pesos, cap)</code> que devuelva True/False.",
            "Explica en un comentario por qué la búsqueda voraz puede fallar aunque sea rápida.",
        ],
    },

    # ============================================================ CAP 41
    {
        "num": 41,
        "slug": "ia-azar-evaluacion",
        "code": "leccion_41",
        "title": "Azar reproducible y evaluación de algoritmos",
        "subtitle": "Semillas, búsqueda aleatoria, curvas de convergencia y comparación justa",
        "apunte": "Módulo J · Lección 3 - Azar y evaluación",
        "concepts": [
            ("Semilla (seed)", "Número que <b>inicializa</b> el generador de azar. Con la misma semilla obtienes <b>los mismos resultados</b>: experimentos repetibles."),
            ("Generador rng", "<code>np.random.default_rng(seed)</code> crea un generador moderno de números aleatorios. Es la forma recomendada hoy (mejor que <code>np.random.seed</code>)."),
            ("Reproducibilidad", "Que otra persona (o tú mañana) pueda <b>repetir exactamente</b> tu experimento. Es un pilar del método científico y de la ingeniería seria."),
            ("Búsqueda aleatoria", "Generar soluciones al azar y quedarse con la mejor. Es la <b>línea base</b>: cualquier metaheurística debería superarla."),
            ("Métrica de desempeño", "El número con que juzgas un algoritmo: el <b>mejor valor</b> encontrado, el tiempo, o cuántas evaluaciones necesitó."),
            ("Presupuesto (budget)", "El número de <b>evaluaciones</b> que le damos a un algoritmo. Comparar es justo solo con el <b>mismo presupuesto</b> para todos."),
            ("Curva de convergencia", "Gráfico del <b>mejor valor hasta el momento</b> a medida que avanza la búsqueda. Muestra qué tan rápido mejora un algoritmo."),
            ("Comparación con varias semillas", "Como hay azar, un solo intento engaña. Se repite con <b>varias semillas</b> y se reporta el promedio y la variabilidad."),
        ],
        "theory": """
<p><b>El azar es una herramienta, no un descuido.</b> Las metaheurísticas usan azar para explorar el
espacio de soluciones. Pero azar <b>no</b> significa incontrolable: en ingeniería necesitamos que un
experimento se pueda <b>repetir</b>. La clave es la <b>semilla</b>.</p>

<p><b>Semillas y reproducibilidad.</b> Un generador de números aleatorios parte de una <b>semilla</b>.
Con la misma semilla produce exactamente la misma secuencia. Por eso, si fijas
<code>rng = np.random.default_rng(7)</code>, tu experimento dará el mismo resultado hoy, mañana y en
el computador de otra persona. Esto es <b>reproducibilidad</b>, y es lo que separa un experimento
serio de un «me salió una vez». Usa siempre un generador propio (<code>default_rng</code>) en vez de
las funciones globales de numpy.</p>

<p><b>La búsqueda aleatoria como línea base.</b> El algoritmo más simple que usa azar es la
<b>búsqueda aleatoria</b>: genera muchas soluciones al azar, evalúa cada una y guarda la mejor. Es
tosca, pero es una <b>referencia honesta</b>: si una metaheurística sofisticada no le gana a la
búsqueda aleatoria con el mismo esfuerzo, algo anda mal. Toda comparación empieza por una buena línea
base.</p>

<p><b>Medir bien: el presupuesto.</b> Para comparar algoritmos de forma justa hay que darles el
<b>mismo presupuesto</b>, normalmente el mismo número de <b>evaluaciones</b> de la función objetivo
(que suele ser lo caro). Comparar un método que evaluó 100 veces contra otro que evaluó 10.000 no dice
nada. Fijar el presupuesto es la regla de oro de la evaluación.</p>

<p><b>La curva de convergencia.</b> Una sola cifra final esconde información. La <b>curva de
convergencia</b> grafica el <b>mejor valor encontrado hasta el momento</b> en función del número de
evaluaciones. Nos dice si un algoritmo mejora rápido al principio, si se estanca, o si sigue ganando
al final. Es la radiografía del comportamiento de una búsqueda.</p>

<p><b>Varias semillas, no una.</b> Como hay azar, un único experimento puede tener suerte o mala
suerte. Lo correcto es <b>repetir con varias semillas</b> (por ejemplo 10) y reportar el
<b>promedio</b> y la <b>desviación</b> de los resultados. Así distinguimos una mejora real de una
casualidad. Esta disciplina —semilla, presupuesto, repeticiones, curva— la usaremos en cada
metaheurística de los módulos siguientes.</p>

<p><b>Funciones de prueba.</b> Para comparar algoritmos se usan <b>funciones de banco</b> con
dificultad conocida, como <b>Rastrigin</b> (llena de mínimos locales). Sirven para ver si un método
se queda atrapado o logra escapar hacia el óptimo global. Las veremos de nuevo en el módulo K.</p>
""",
        "examples": [
            {
                "title": "Misma semilla, mismos resultados",
                "explain": "La reproducibilidad se logra fijando la semilla: dos generadores con la misma semilla dan lo mismo.",
                "code": 'import numpy as np\na = np.random.default_rng(42).integers(0, 100, 5)\nb = np.random.default_rng(42).integers(0, 100, 5)\nprint("a =", a)\nprint("b =", b)\nprint("iguales:", bool((a == b).all()))',
            },
            {
                "title": "Búsqueda aleatoria (línea base)",
                "explain": "Generamos soluciones al azar dentro de un presupuesto y guardamos la mejor. Simple y honesta.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\n\ndef f(x):\n    return -(x - 3) ** 2 + 10        # maximo en x = 3\n\nmejor = -1e9\nfor _ in range(100):                 # presupuesto: 100 evaluaciones\n    x = rng.uniform(-5, 10)\n    mejor = max(mejor, f(x))\nprint("mejor tras 100 intentos:", round(mejor, 4))',
            },
            {
                "title": "Curva de convergencia",
                "explain": "Guardamos el mejor valor hasta el momento y lo graficamos: así se ve cómo mejora la búsqueda.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(7)\n\ndef f(x):\n    return -(x - 3) ** 2 + 10\n\nmejor = -1e9; curva = []\nfor _ in range(200):\n    x = rng.uniform(-5, 10)\n    mejor = max(mejor, f(x))\n    curva.append(mejor)\n\nplt.plot(curva)\nplt.xlabel("evaluaciones"); plt.ylabel("mejor valor")\nplt.title("Curva de convergencia (busqueda aleatoria)")\nplt.show()',
            },
            {
                "title": "Comparar con varias semillas",
                "explain": "Un solo intento engaña. Repetimos con 10 semillas y reportamos promedio y desviación.",
                "code": 'import numpy as np\n\ndef f(x):\n    return -(x - 3) ** 2 + 10\n\ndef random_search(seed, n=100):\n    rng = np.random.default_rng(seed)\n    mejor = -1e9\n    for _ in range(n):\n        mejor = max(mejor, f(rng.uniform(-5, 10)))\n    return mejor\n\nres = [random_search(s) for s in range(10)]\nprint("mejores por semilla:", [round(r, 2) for r in res])\nprint("promedio:", round(np.mean(res), 3), "| desviacion:", round(np.std(res), 3))',
            },
            {
                "title": "Una función de prueba: Rastrigin",
                "explain": "Rastrigin está llena de mínimos locales. Es un banco de pruebas clásico para metaheurísticas.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\n\ndef rastrigin(x):\n    return 10 + x**2 - 10 * np.cos(2 * np.pi * x)\n\nx = np.linspace(-5, 5, 400)\nplt.plot(x, rastrigin(x))\nplt.title("Rastrigin 1D: muchos minimos locales")\nplt.xlabel("x"); plt.ylabel("f(x)"); plt.show()',
            },
            {
                "title": "Más presupuesto suele dar mejor resultado",
                "explain": "Comparamos la búsqueda aleatoria con distintos presupuestos, con la misma semilla.",
                "code": 'import numpy as np\n\ndef f(x):\n    return -(x - 3) ** 2 + 10\n\nfor n in [10, 100, 1000, 10000]:\n    rng = np.random.default_rng(0)\n    mejor = -1e9\n    for _ in range(n):\n        mejor = max(mejor, f(rng.uniform(-5, 10)))\n    print(f"presupuesto {n:>6} -> mejor {round(mejor, 5)}")',
            },
        ],
        "dataset": "funciones de prueba",
        "exercises": [
            "Crea dos generadores con <code>default_rng(2024)</code> y verifica que producen los mismos 5 números.",
            "Programa una búsqueda aleatoria de 200 evaluaciones para maximizar <code>-(x-4)**2+15</code> en [0, 10].",
            "Grafica la curva de convergencia de esa búsqueda.",
            "Repite la búsqueda con 15 semillas (0 a 14) y reporta promedio y desviación del mejor valor.",
            "Compara presupuestos 50, 500 y 5000: ¿cuánto mejora el resultado?",
            "Grafica la función de Rastrigin 1D entre -3 y 3.",
            "Escribe una función <code>random_search(seed, n)</code> reutilizable y pruébala con dos semillas.",
            "Modifica la búsqueda para <b>minimizar</b> Rastrigin (guarda el menor valor) con 500 evaluaciones.",
            "Explica en un comentario por qué es injusto comparar dos algoritmos con distinto presupuesto.",
            "Guarda en una lista el mejor valor de cada semilla y muestra el mejor y el peor caso.",
        ],
    },
]
