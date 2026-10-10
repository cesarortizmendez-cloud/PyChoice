# -*- coding: utf-8 -*-
"""
PyChoice - Ruta "Ingeniero de Investigacion de Operaciones".
Modulo P - Fundamentos de modelamiento y programacion lineal (lecciones 61-64).

Nivel pro, con modelamiento industrial. Todo corre en el navegador:
LP con HiGHS via scipy.optimize.linprog; simplex didactico en numpy.
"""

CHAPTERS_P = [

    # ============================================================ CAP 61
    {
        "num": 61,
        "slug": "io-del-enunciado-al-modelo",
        "code": "leccion_61",
        "title": "Investigación de operaciones: del enunciado al modelo",
        "subtitle": "Traducir un problema industrial a variables, objetivo y restricciones",
        "apunte": "Módulo P · Lección 1 - Del enunciado al modelo",
        "concepts": [
            ("Investigación de operaciones", "Disciplina que aplica <b>modelos matemáticos</b> para tomar las mejores decisiones en operaciones reales: producción, logística, inventarios, personal."),
            ("Variables de decisión", "Las <b>incógnitas que controlamos</b>: cuánto producir de cada producto, cuántas unidades enviar, cuántos turnos abrir. Es lo que el modelo debe determinar."),
            ("Función objetivo", "La cantidad a <b>maximizar</b> (ganancia, servicio) o <b>minimizar</b> (costo, tiempo), expresada como función lineal de las variables."),
            ("Restricciones", "Los <b>límites</b> del problema: capacidad de máquinas, mano de obra, demanda, presupuesto. Se escriben como desigualdades o igualdades lineales."),
            ("Parámetros", "Los <b>datos conocidos</b>: márgenes unitarios, consumos por unidad, disponibilidades. Son los coeficientes del modelo."),
            ("Región factible", "El conjunto de todas las soluciones que <b>cumplen las restricciones</b>. En LP es un poliedro (una figura de lados planos)."),
            ("Programación lineal (LP)", "Cuando objetivo y restricciones son <b>lineales</b> y las variables continuas. El caso más resoluble y más usado en la industria."),
            ("Teorema fundamental", "El óptimo de un LP (si existe) está siempre en un <b>vértice</b> de la región factible. Por eso basta revisar los vértices."),
        ],
        "theory": """
<p><b>Decidir con modelos.</b> La investigación de operaciones (IO) nació para tomar <b>mejores
decisiones</b> en operaciones complejas —producción, transporte, personal, inventarios— usando
matemáticas en vez de intuición. Un ingeniero de IO no adivina cuánto producir: lo <b>modela</b> y lo
<b>optimiza</b>. Esta ruta te enseña a hacerlo con Python.</p>

<p><b>El arte de modelar.</b> Antes del solver viene lo difícil: traducir un enunciado de negocio a un
modelo. Siempre se responden tres preguntas. <b>¿Qué decidimos?</b> → las <b>variables de decisión</b>
(p. ej. x₁ = toneladas de producto A, x₂ = de producto B). <b>¿Qué queremos?</b> → la <b>función
objetivo</b> (maximizar la ganancia total). <b>¿Qué nos limita?</b> → las <b>restricciones</b>
(horas-máquina, mano de obra, demanda máxima, mínimos de contrato). Modelar bien es la habilidad
central del oficio.</p>

<p><b>Un ejemplo industrial.</b> Una planta fabrica dos productos. Cada tonelada de A deja $40 de
margen y usa 1 h de mezclado y 3 h de secado; cada tonelada de B deja $30, usa 2 h de mezclado y 1 h de
secado. Hay 40 h de mezclado y 60 h de secado por turno. ¿Cuánto producir de cada uno para maximizar el
margen? Las variables son las toneladas; el objetivo, 40x₁ + 30x₂; las restricciones, el consumo de
cada recurso ≤ su disponibilidad, y x₁, x₂ ≥ 0.</p>

<p><b>Forma estándar y linealidad.</b> Un problema es de <b>programación lineal</b> cuando el objetivo y
todas las restricciones son <b>lineales</b> (sumas de variables por constantes, sin productos ni
potencias entre variables) y las variables pueden tomar valores continuos. La linealidad descansa en
tres supuestos: <b>proporcionalidad</b> (el doble de producción usa el doble de recursos),
<b>aditividad</b> (los efectos se suman) y <b>divisibilidad</b> (se pueden producir 3,5 toneladas). En
la industria estos supuestos se cumplen a menudo con muy buena aproximación.</p>

<p><b>La geometría: por qué los vértices.</b> Con dos variables, cada restricción es una recta y la
<b>región factible</b> es el polígono que cumple todas. La función objetivo es una familia de rectas
paralelas; empujarla en la dirección de mejora la detiene en un <b>vértice</b> del polígono. Este es el
<b>teorema fundamental</b> de la programación lineal: el óptimo siempre está en un vértice. Con más
variables el polígono es un poliedro, pero la idea no cambia.</p>

<p><b>De la geometría al cálculo.</b> Revisar vértices a mano solo sirve con dos o tres variables; un
problema industrial real tiene cientos. Por eso existen algoritmos como el <b>simplex</b> (lección 63) y
solvers como <b>HiGHS</b> (lección 62), que encuentran el vértice óptimo con eficiencia. En esta lección
modelamos y entendemos la geometría; en las siguientes, resolvemos a escala.</p>
""",
        "examples": [
            {
                "title": "Representar un modelo en Python",
                "explain": "Guardamos los datos del problema (márgenes, consumos, disponibilidades) como vectores y matrices.",
                "code": 'import numpy as np\n# Productos A y B: margen por tonelada\nmargen = np.array([40, 30])\n# Consumo por tonelada: filas = recursos (mezclado, secado), columnas = productos\nA = np.array([[1, 2],      # mezclado\n              [3, 1]])     # secado\ndisp = np.array([40, 60])  # horas disponibles por recurso\nprint("objetivo: maximizar", margen[0], "x1 +", margen[1], "x2")\nprint("sujeto a consumo <= disponibilidad:\\n", A, "<=", disp)',
            },
            {
                "title": "Evaluar un plan y verificar factibilidad",
                "explain": "Para un plan candidato calculamos el margen y comprobamos que no excede ningún recurso.",
                "code": 'import numpy as np\nmargen = np.array([40, 30]); A = np.array([[1,2],[3,1]]); disp = np.array([40,60])\n\nplan = np.array([15, 10])          # 15 t de A, 10 t de B\nuso = A @ plan\nfactible = np.all(uso <= disp)\nprint("uso de recursos:", uso, "| disponibles:", disp)\nprint("factible:", bool(factible), "| margen:", margen @ plan)',
            },
            {
                "title": "El óptimo está en un vértice",
                "explain": "Enumeramos los vértices de la región factible (2 variables) y evaluamos el objetivo en cada uno.",
                "code": 'import numpy as np\nfrom itertools import combinations\nmargen = np.array([40, 30])\n# restricciones como filas [a1, a2, b] de a1*x1 + a2*x2 <= b, incluyendo x>=0\nR = np.array([[1,2,40],[3,1,60],[-1,0,0],[0,-1,0]], float)\n\nverts = []\nfor (i, j) in combinations(range(len(R)), 2):\n    Amat = R[[i,j],:2]; bvec = R[[i,j],2]\n    if abs(np.linalg.det(Amat)) > 1e-9:\n        p = np.linalg.solve(Amat, bvec)\n        if np.all(R[:,:2] @ p <= R[:,2] + 1e-6):   # cumple todas\n            verts.append(p)\nfor p in verts:\n    print("vertice", np.round(p,1), "-> margen", round(margen @ p,1))',
            },
            {
                "title": "Graficar la región factible",
                "explain": "Visualizamos las rectas de restricción y la región factible del problema de producción.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nx = np.linspace(0, 40, 200)\nplt.plot(x, (40 - x) / 2, label="mezclado: x1+2x2<=40")\nplt.plot(x, 60 - 3*x, label="secado: 3x1+x2<=60")\ny_max = np.minimum((40 - x)/2, 60 - 3*x)\nplt.fill_between(x, 0, np.clip(y_max, 0, None), alpha=0.2, color="green")\nplt.xlim(0, 25); plt.ylim(0, 25); plt.xlabel("x1 (producto A)"); plt.ylabel("x2 (producto B)")\nplt.legend(); plt.title("Region factible"); plt.show()',
            },
            {
                "title": "Un modelo industrial más grande",
                "explain": "Tres productos y tres líneas: así escala la representación matricial de un problema real.",
                "code": 'import numpy as np\nproductos = ["estandar", "premium", "industrial"]\nmargen = np.array([25, 40, 32])\n# consumo (h por unidad): filas = corte, ensamble, empaque\nA = np.array([[2, 3, 2],\n              [1, 4, 2],\n              [1, 1, 2]])\ndisp = np.array([500, 600, 400])\nplan = np.array([80, 60, 50])\nprint("margen total del plan:", margen @ plan)\nprint("uso por linea:", A @ plan, "| disponible:", disp)\nprint("factible:", bool(np.all(A @ plan <= disp)))',
            },
        ],
        "dataset": "modelos en el código",
        "exercises": [
            "Modela en Python: una fábrica de sillas ($18) y mesas ($30); cada silla usa 2 h de carpintería y 1 de pintura; cada mesa 4 y 2. Hay 120 h de carpintería y 80 de pintura.",
            "Evalúa el margen y la factibilidad del plan (20 sillas, 15 mesas).",
            "Enumera los vértices de la región factible de ese problema.",
            "¿Qué vértice da el mayor margen?",
            "Grafica la región factible de las sillas y mesas.",
            "Agrega una restricción de demanda: no más de 25 mesas.",
            "Modela un problema de 3 productos con 2 recursos y evalúa un plan.",
            "Comprueba en código que duplicar un plan factible duplica el uso de recursos (proporcionalidad).",
            "Escribe en comentarios cuáles son las variables, el objetivo y las restricciones de tu modelo.",
            "Explica en un comentario por qué el óptimo de un LP está en un vértice.",
        ],
    },

    # ============================================================ CAP 62
    {
        "num": 62,
        "slug": "programacion-lineal-highs",
        "code": "leccion_62",
        "title": "Programación lineal con Python (HiGHS)",
        "subtitle": "Resolver modelos industriales reales con scipy.optimize.linprog",
        "apunte": "Módulo P · Lección 2 - LP con HiGHS",
        "concepts": [
            ("linprog", "La función de SciPy para resolver programación lineal. Usa el solver de código abierto <b>HiGHS</b>, de nivel profesional."),
            ("Forma estándar de SciPy", "linprog <b>minimiza</b> <code>c·x</code> sujeto a <code>A_ub·x ≤ b_ub</code>, <code>A_eq·x = b_eq</code> y <code>bounds</code>."),
            ("Maximizar", "Para maximizar, se minimiza <code>−c</code>. El óptimo es el mismo; la ganancia es <code>−fun</code>."),
            ("Restricciones ≤ y ≥", "Las ≤ van directo en <code>A_ub</code>. Una ≥ se convierte multiplicando la fila por <b>−1</b>."),
            ("Restricciones de igualdad", "Balances exactos (producir justo la demanda, conservar flujo) van en <code>A_eq</code>/<code>b_eq</code>."),
            ("Cotas (bounds)", "Límites por variable: no-negatividad, capacidad máxima, mínimos de contrato. Una por variable: <code>(low, high)</code>."),
            ("Solución óptima", "<code>res.x</code> son los valores óptimos de las variables; <code>res.fun</code>, el valor del objetivo (minimizado)."),
            ("Estado del solver", "<code>res.status</code>: 0 óptimo, 2 <b>infactible</b> (ninguna solución), 3 <b>no acotado</b>. Siempre hay que revisarlo."),
        ],
        "theory": """
<p><b>Del modelo a la solución, en una llamada.</b> Una vez modelado el problema, resolverlo es
directo: <b>HiGHS</b>, uno de los mejores solvers de código abierto, viene integrado en SciPy y corre
<b>en el navegador</b>. La puerta de entrada es <code>scipy.optimize.linprog</code>.</p>

<p><b>La forma estándar de SciPy.</b> linprog <b>siempre minimiza</b> <code>c·x</code> sujeto a
restricciones de <b>menor o igual</b> (<code>A_ub·x ≤ b_ub</code>), de <b>igualdad</b>
(<code>A_eq·x = b_eq</code>) y <b>cotas</b> por variable (<code>bounds</code>). Modelar para linprog es,
sobre todo, <b>llevar tu problema a esta forma</b>. Dos conversiones resuelven casi todo.</p>

<p><b>Maximizar = minimizar el negativo.</b> La mayoría de los problemas industriales <b>maximizan</b>
ganancia. linprog minimiza, así que se le pasa <code>c = −margen</code> y la ganancia óptima es
<code>−res.fun</code>. Es la misma conversión que vimos en optimización.</p>

<p><b>De ≥ a ≤.</b> Muchas restricciones son de <b>mínimo</b> (cumplir al menos cierta proteína, servir
al menos la demanda). Como linprog quiere ≤, se <b>multiplica la fila por −1</b>: <code>a·x ≥ b</code>
equivale a <code>−a·x ≤ −b</code>. Con esto y las igualdades para los <b>balances</b> (producir justo la
demanda, conservar el flujo en una red), se modela prácticamente cualquier LP.</p>

<p><b>Las cotas y el estado.</b> Las <b>cotas</b> expresan la no-negatividad (no se produce negativo) y
límites por variable (capacidad de una línea, mínimos de contrato). Y algo que un profesional nunca
omite: revisar <code>res.status</code>. Un modelo puede ser <b>infactible</b> (las restricciones se
contradicen) o <b>no acotado</b> (falta una restricción y la ganancia «se dispara»). Esos estados no son
errores de Python: son <b>información</b> de que el modelo está mal planteado.</p>

<p><b>Tres clásicos industriales.</b> En esta lección resolvemos los modelos más usados: la <b>mezcla de
producción</b> (qué y cuánto fabricar para maximizar margen), el <b>problema de mezcla/dieta</b>
(combinar insumos al mínimo costo cumpliendo requisitos de calidad) y el <b>transporte</b> (enviar desde
plantas a centros al mínimo costo respetando ofertas y demandas). Con estos tres patrones se modela una
enorme parte de los problemas reales.</p>
""",
        "examples": [
            {
                "title": "Mezcla de producción (maximizar margen)",
                "explain": "El problema de la planta de la lección 61, ahora resuelto con HiGHS. Maximizar = minimizar −margen.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\nmargen = [40, 30]\nA_ub = [[1, 2], [3, 1]]        # mezclado, secado\nb_ub = [40, 60]\n\nres = linprog(c=[-m for m in margen], A_ub=A_ub, b_ub=b_ub,\n              bounds=[(0, None), (0, None)])\nprint("estado:", res.status, "(0 = optimo)")\nprint("produccion optima:", np.round(res.x, 2), "toneladas")\nprint("margen maximo:", round(-res.fun, 2))',
            },
            {
                "title": "Mezcla de alimento (minimizar costo, ≥)",
                "explain": "Mezclar maíz y soya al mínimo costo cumpliendo mínimos de proteína y energía. Las ≥ se multiplican por −1.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\n# costo por kg\ncosto = [0.30, 0.45]              # maiz, soya\n# aportes por kg: proteina, energia\nprot = [0.09, 0.45]; energ = [3.4, 2.6]\n# requisitos minimos por kg de mezcla\nreq_prot, req_energ = 0.20, 3.0\n\n# a*x >= b  ->  -a*x <= -b\nA_ub = [[-prot[0], -prot[1]], [-energ[0], -energ[1]]]\nb_ub = [-req_prot, -req_energ]\nA_eq = [[1, 1]]; b_eq = [1]        # la mezcla suma 1 kg\nres = linprog(c=costo, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,\n              bounds=[(0, None), (0, None)])\nprint("mezcla optima (maiz, soya):", np.round(res.x, 3), "kg")\nprint("costo por kg:", round(res.fun, 4))',
            },
            {
                "title": "Planificación multi-producto",
                "explain": "Cuatro productos, tres recursos y una demanda máxima por producto: un modelo industrial realista.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\nmargen = [25, 40, 32, 18]\nA_ub = [[2, 3, 2, 1],     # corte\n        [1, 4, 2, 2],     # ensamble\n        [1, 1, 2, 1]]     # empaque\nb_ub = [500, 600, 400]\ncotas = [(0, 120), (0, 80), (0, 100), (0, 150)]   # demanda maxima por producto\n\nres = linprog(c=[-m for m in margen], A_ub=A_ub, b_ub=b_ub, bounds=cotas)\nprint("plan optimo:", np.round(res.x, 1))\nprint("margen maximo:", round(-res.fun, 1))',
            },
            {
                "title": "Restricción de igualdad (usar toda la capacidad)",
                "explain": "A veces un recurso debe usarse exactamente (un horno que no se puede apagar). Va en A_eq.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\nmargen = [40, 30]\nA_ub = [[1, 2]]; b_ub = [40]          # mezclado <= 40\nA_eq = [[3, 1]]; b_eq = [60]          # secado = 60 exacto\nres = linprog(c=[-m for m in margen], A_ub=A_ub, b_ub=b_ub,\n              A_eq=A_eq, b_eq=b_eq, bounds=[(0, None), (0, None)])\nprint("produccion:", np.round(res.x, 2), "| margen:", round(-res.fun, 2))',
            },
            {
                "title": "Problema de transporte",
                "explain": "Enviar desde 2 plantas a 3 centros al mínimo costo, respetando ofertas y demandas (balanceado).",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\n# costo[i][j]: planta i -> centro j\ncosto = np.array([[4, 6, 8], [5, 3, 7]], float)\noferta = [50, 40]; demanda = [30, 35, 25]      # suman 90 = 90\nm, n = costo.shape\nc = costo.ravel()\n# oferta: para cada planta, suma_j x_ij <= oferta_i\nA_ub = []; b_ub = []\nfor i in range(m):\n    fila = np.zeros((m, n)); fila[i, :] = 1; A_ub.append(fila.ravel()); b_ub.append(oferta[i])\n# demanda: para cada centro, suma_i x_ij = demanda_j\nA_eq = []; b_eq = []\nfor j in range(n):\n    fila = np.zeros((m, n)); fila[:, j] = 1; A_eq.append(fila.ravel()); b_eq.append(demanda[j])\nres = linprog(c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * (m * n))\nprint("plan de envio:\\n", np.round(res.x.reshape(m, n), 1))\nprint("costo total:", round(res.fun, 1))',
            },
        ],
        "dataset": "modelos en el código",
        "exercises": [
            "Resuelve con linprog el problema de sillas y mesas de la lección 61.",
            "Interpreta <code>res.x</code> y <code>res.fun</code> en términos del negocio.",
            "Mezcla de alimento: agrega un tercer insumo (afrecho) y vuelve a optimizar.",
            "Agrega al modelo multi-producto un mínimo de contrato (al menos 10 del producto 1).",
            "Convierte una restricción ≥ a la forma ≤ a mano y verifica con linprog.",
            "Haz infactible un modelo (requisitos imposibles) y observa <code>res.status</code>.",
            "Quita una restricción clave para volver un modelo no acotado y mira el estado.",
            "Resuelve un transporte de 3 plantas y 3 centros.",
            "Cambia un costo de transporte y observa cómo cambia el plan óptimo.",
            "Explica en un comentario por qué maximizar equivale a minimizar el negativo.",
        ],
    },

    # ============================================================ CAP 63
    {
        "num": 63,
        "slug": "metodo-simplex",
        "code": "leccion_63",
        "title": "El método simplex paso a paso",
        "subtitle": "Qué hace el solver por dentro: forma estándar, tablas y pivoteo",
        "apunte": "Módulo P · Lección 3 - Método simplex",
        "concepts": [
            ("Forma estándar", "El LP con <b>igualdades</b>: cada restricción ≤ se vuelve = agregando una <b>variable de holgura</b> ≥ 0."),
            ("Variable de holgura", "Mide el recurso <b>sin usar</b> de una restricción. Si vale 0, el recurso está al límite (activo)."),
            ("Tabla simplex", "La matriz que representa el sistema en cada paso: restricciones, holguras, lado derecho y fila objetivo."),
            ("Solución básica factible", "Un <b>vértice</b> de la región factible. El simplex salta de vértice en vértice mejorando."),
            ("Variable entrante", "La que <b>entra</b> a la base: la de coeficiente más negativo en la fila objetivo (la que más mejora)."),
            ("Variable saliente", "La que <b>sale</b> de la base, elegida por la <b>prueba del cociente mínimo</b> para no violar restricciones."),
            ("Pivoteo", "La operación de álgebra que actualiza la tabla al cambiar de vértice (eliminación de Gauss sobre el elemento pivote)."),
            ("Prueba de optimalidad", "Cuando <b>no quedan</b> coeficientes negativos en la fila objetivo, el vértice actual es <b>óptimo</b>."),
        ],
        "theory": """
<p><b>Abrir la caja negra.</b> HiGHS resuelve en un instante, pero un ingeniero de IO debe entender
<b>cómo</b>. El <b>método simplex</b> (Dantzig, 1947) es el algoritmo que hizo práctica la programación
lineal y sigue siendo el corazón de muchos solvers. Su idea es elegante: <b>recorrer los vértices</b> de
la región factible, saltando siempre a uno mejor, hasta que no haya mejora posible.</p>

<p><b>Forma estándar con holguras.</b> El simplex trabaja con <b>igualdades</b>. Una restricción como
<code>x₁ + 2x₂ ≤ 40</code> se convierte en <code>x₁ + 2x₂ + s₁ = 40</code> agregando una <b>variable de
holgura</b> <code>s₁ ≥ 0</code>, que representa el <b>recurso no usado</b>. Si al final una holgura vale
0, ese recurso quedó <b>al límite</b> (lo veremos clave en sensibilidad). Cada restricción aporta su
holgura.</p>

<p><b>La tabla simplex.</b> Todo el problema se escribe en una <b>tabla</b>: las filas son las
restricciones (con sus holguras y lado derecho) y una fila extra para el <b>objetivo</b>. La <b>solución
básica factible</b> que representa es un vértice: las variables «básicas» toman valor y las demás valen
cero. El simplex transforma esta tabla para moverse a vértices mejores.</p>

<p><b>Entrante, saliente, pivote.</b> Cada iteración tiene tres pasos. La <b>variable entrante</b> es la
de coeficiente más negativo en la fila objetivo: la que, al crecer, más mejora el resultado. La
<b>variable saliente</b> se elige con la <b>prueba del cociente mínimo</b> (lado derecho dividido por la
columna entrante, el menor positivo), que garantiza no salirse de la región factible. Y el <b>pivoteo</b>
—eliminación de Gauss sobre el elemento pivote— actualiza toda la tabla al nuevo vértice.</p>

<p><b>Cuándo parar.</b> El simplex se detiene cuando en la fila objetivo <b>ya no hay coeficientes
negativos</b>: no existe ninguna variable que, al entrar, mejore el resultado. Ese es el <b>test de
optimalidad</b>, y el vértice actual es la solución óptima. En problemas de maximización bien planteados,
el simplex llega al óptimo en pocas iteraciones.</p>

<p><b>Por qué programarlo.</b> Implementar el simplex con numpy —aunque en la práctica usemos HiGHS— es
lo que convierte la programación lineal de «magia» en algo que entiendes y puedes depurar. Aquí lo
construimos para un problema industrial pequeño y <b>comprobamos</b> que da exactamente lo mismo que el
solver profesional.</p>
""",
        "examples": [
            {
                "title": "Pasar a forma estándar (agregar holguras)",
                "explain": "Construimos la tabla inicial: restricciones con holguras, lado derecho y fila objetivo (−margen).",
                "code": 'import numpy as np\n# max 40x1 + 30x2 ; x1+2x2<=40 ; 3x1+x2<=60\nA = np.array([[1, 2], [3, 1]], float); b = np.array([40, 60], float); c = np.array([40, 30], float)\nm, n = A.shape\nT = np.zeros((m + 1, n + m + 1))\nT[:m, :n] = A\nT[:m, n:n+m] = np.eye(m)     # holguras\nT[:m, -1] = b\nT[-1, :n] = -c               # fila objetivo\nprint("tabla inicial [x1 x2 | s1 s2 | b]:\\n", T)',
            },
            {
                "title": "Una iteración de pivoteo",
                "explain": "Elegimos variable entrante (más negativa en la fila objetivo) y saliente (cociente mínimo), y pivoteamos.",
                "code": 'import numpy as np\nA = np.array([[1,2],[3,1]], float); b = np.array([40,60], float); c = np.array([40,30], float)\nm, n = A.shape\nT = np.zeros((m+1, n+m+1)); T[:m,:n]=A; T[:m,n:n+m]=np.eye(m); T[:m,-1]=b; T[-1,:n]=-c\n\nj = int(np.argmin(T[-1, :-1]))                     # entrante\ncol = T[:-1, j]\nraz = np.where(col > 1e-9, T[:-1, -1] / col, np.inf)\ni = int(np.argmin(raz))                            # saliente\nprint("entra columna", j, "| sale fila", i, "| pivote =", T[i, j])\nT[i, :] /= T[i, j]\nfor k in range(m + 1):\n    if k != i:\n        T[k, :] -= T[k, j] * T[i, :]\nprint("tabla tras una iteracion:\\n", np.round(T, 2))',
            },
            {
                "title": "Simplex completo en numpy",
                "explain": "Iteramos hasta que no queden negativos en la fila objetivo. Devuelve la solución óptima.",
                "code": 'import numpy as np\ndef simplex_max(c, A, b):\n    A = np.array(A, float); b = np.array(b, float); c = np.array(c, float)\n    m, n = A.shape\n    T = np.zeros((m+1, n+m+1)); T[:m,:n]=A; T[:m,n:n+m]=np.eye(m); T[:m,-1]=b; T[-1,:n]=-c\n    while np.min(T[-1, :-1]) < -1e-9:\n        j = int(np.argmin(T[-1, :-1])); col = T[:-1, j]\n        raz = np.where(col > 1e-9, T[:-1, -1] / col, np.inf)\n        i = int(np.argmin(raz))\n        T[i, :] /= T[i, j]\n        for k in range(m+1):\n            if k != i: T[k, :] -= T[k, j] * T[i, :]\n    x = np.zeros(n)\n    for j in range(n):\n        col = T[:-1, j]\n        if abs(col.sum() - 1) < 1e-6 and np.sum(np.abs(col) > 1e-6) == 1:\n            x[j] = T[np.argmax(col), -1]\n    return x, T[-1, -1]\n\nx, z = simplex_max([40, 30], [[1,2],[3,1]], [40, 60])\nprint("solucion:", np.round(x, 2), "| objetivo:", round(z, 2))',
            },
            {
                "title": "Comparar con HiGHS",
                "explain": "El simplex didáctico debe dar el mismo óptimo que el solver profesional.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\ndef simplex_max(c, A, b):\n    A=np.array(A,float); b=np.array(b,float); c=np.array(c,float); m,n=A.shape\n    T=np.zeros((m+1,n+m+1)); T[:m,:n]=A; T[:m,n:n+m]=np.eye(m); T[:m,-1]=b; T[-1,:n]=-c\n    while np.min(T[-1,:-1])<-1e-9:\n        j=int(np.argmin(T[-1,:-1])); col=T[:-1,j]\n        raz=np.where(col>1e-9, T[:-1,-1]/col, np.inf); i=int(np.argmin(raz))\n        T[i,:]/=T[i,j]\n        for k in range(m+1):\n            if k!=i: T[k,:]-=T[k,j]*T[i,:]\n    return T[-1,-1]\n\nz_simplex = simplex_max([40,30], [[1,2],[3,1]], [40,60])\nz_highs = -linprog([-40,-30], A_ub=[[1,2],[3,1]], b_ub=[40,60]).fun\nprint("simplex:", round(z_simplex, 2), "| HiGHS:", round(z_highs, 2))',
            },
            {
                "title": "Interpretar las holguras finales",
                "explain": "Resolvemos y miramos cuánto recurso sobra en cada restricción (holgura = recurso no usado).",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\nA = np.array([[1,2],[3,1]]); b = np.array([40,60])\nres = linprog([-40,-30], A_ub=A, b_ub=b, bounds=[(0,None)]*2)\nholgura = b - A @ res.x\nfor i, h in enumerate(holgura):\n    estado = "AL LIMITE (activo)" if abs(h) < 1e-6 else f"sobran {h:.1f}"\n    print(f"recurso {i+1}: {estado}")',
            },
        ],
        "dataset": "modelos en el código",
        "exercises": [
            "Pasa a forma estándar el problema de sillas y mesas (agrega holguras) y arma la tabla inicial.",
            "Haz una iteración de pivoteo a mano sobre esa tabla.",
            "Usa <code>simplex_max</code> para resolver el problema de sillas y mesas.",
            "Compara tu resultado con linprog: ¿coinciden?",
            "Resuelve con el simplex el problema de producción de la lección 61.",
            "Muestra las holguras finales e indica qué recursos quedan al límite.",
            "Cuenta cuántas iteraciones hace el simplex (agrega un contador).",
            "Prueba el simplex con un tercer producto (3 variables).",
            "Verifica que las variables no básicas valen 0 en la solución.",
            "Explica en un comentario qué representa una variable de holgura.",
        ],
    },

    # ============================================================ CAP 64
    {
        "num": 64,
        "slug": "sensibilidad-dualidad",
        "code": "leccion_64",
        "title": "Análisis de sensibilidad y dualidad",
        "subtitle": "Qué vale cada recurso y cómo decidir dónde invertir",
        "apunte": "Módulo P · Lección 4 - Sensibilidad y dualidad",
        "concepts": [
            ("Análisis de sensibilidad", "Estudiar cómo cambia la solución óptima si cambian los <b>datos</b> (disponibilidades, márgenes). Esencial para decidir en la práctica."),
            ("Precio sombra", "Cuánto <b>mejora el objetivo</b> por cada unidad adicional de un recurso. Es el <b>valor marginal</b> de ese recurso."),
            ("Restricción activa", "La que se cumple con <b>igualdad</b> (holgura 0): el recurso está <b>agotado</b> y limita la solución. Solo estas tienen precio sombra > 0."),
            ("Restricción inactiva", "La que tiene <b>holgura</b> (recurso sobrante). Su precio sombra es 0: tener más de ese recurso no mejora nada."),
            ("Costo reducido", "Para una variable que vale 0 en el óptimo, cuánto debería <b>mejorar su margen</b> para que valga la pena producirla."),
            ("Problema dual", "A todo LP (primal) le corresponde un <b>dual</b>: minimizar el valor de los recursos. Sus variables son los <b>precios sombra</b>."),
            ("Dualidad fuerte", "El óptimo del primal y el del dual <b>coinciden</b>. Una comprobación y una interpretación poderosas."),
            ("Rango de sensibilidad", "El intervalo en que un dato puede cambiar <b>sin que cambie</b> la base óptima (qué variables son básicas)."),
        ],
        "theory": """
<p><b>El óptimo no es el final.</b> Resolver un LP da la mejor decisión <b>para los datos actuales</b>.
Pero en la industria los datos cambian y, sobre todo, surge la pregunta clave: <b>¿dónde conviene
invertir?</b> El <b>análisis de sensibilidad</b> responde eso sin re-resolver mil veces, y es lo que
distingue a un ingeniero de IO de alguien que solo «corre el solver».</p>

<p><b>El precio sombra: el valor de un recurso.</b> El <b>precio sombra</b> de una restricción es cuánto
<b>mejoraría el objetivo</b> si tuviéramos <b>una unidad más</b> de ese recurso. Si una hora extra de la
máquina cuello de botella sube la ganancia en $20, su precio sombra es 20: eso es lo máximo que
convendría pagar por esa hora extra. HiGHS lo entrega en <code>res.ineqlin.marginals</code> (con signo
según la convención de minimización: para un problema de maximización, el precio sombra es
<code>−marginal</code>).</p>

<p><b>Escaso vs. abundante.</b> Aquí está la idea más útil. Una <b>restricción activa</b> (holgura 0)
corresponde a un recurso <b>agotado</b>: es un <b>cuello de botella</b> y tiene precio sombra positivo,
porque más de él permitiría ganar más. Una <b>restricción inactiva</b> (con holgura) corresponde a un
recurso que <b>sobra</b>: su precio sombra es <b>0</b>, porque tener aún más no cambia nada. Por eso
invertir en ampliar un recurso que ya sobra es tirar el dinero.</p>

<p><b>Costos reducidos.</b> ¿Y los productos que el óptimo decide <b>no fabricar</b> (valen 0)? Su
<b>costo reducido</b> dice cuánto tendría que <b>mejorar su margen</b> para que entre en el plan. Si un
producto no se fabrica y su costo reducido es −5, habría que subir su margen en más de 5 para que valga
la pena. Es información directa para precios y portafolio.</p>

<p><b>El problema dual.</b> Todo LP (el <b>primal</b>: maximizar ganancia usando recursos limitados)
tiene un <b>dual</b>: minimizar el <b>valor total de los recursos</b>, donde las variables duales son
justamente los <b>precios sombra</b>. No es una curiosidad matemática: el dual <b>valora los recursos</b>
de la empresa. Y la <b>dualidad fuerte</b> garantiza que el óptimo del primal y el del dual
<b>coinciden</b> —una comprobación elegante y una forma profunda de entender el problema desde dos
ángulos.</p>

<p><b>Rangos de sensibilidad.</b> Finalmente, los <b>rangos</b> dicen cuánto puede cambiar un dato (un
margen, una disponibilidad) <b>antes</b> de que la solución óptima cambie de estructura. Permiten saber
qué tan <b>robusta</b> es una decisión frente a la incertidumbre. Con todo esto, el LP deja de ser «un
número» y se vuelve una herramienta de <b>gestión</b>: qué vale cada recurso, dónde invertir, cuánto
cobrar, cuán seguros estamos.</p>
""",
        "examples": [
            {
                "title": "Precios sombra desde HiGHS",
                "explain": "El valor marginal de cada recurso. Para maximización, el precio sombra es −marginal.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\nA = [[1, 2], [3, 1]]; b = [40, 60]\nres = linprog([-40, -30], A_ub=A, b_ub=b, bounds=[(0, None)] * 2)\nprecio_sombra = -res.ineqlin.marginals\nprint("produccion optima:", np.round(res.x, 2), "| margen:", round(-res.fun, 2))\nfor i, ps in enumerate(precio_sombra):\n    print(f"recurso {i+1}: precio sombra = {ps:.2f} (valor de 1 hora extra)")',
            },
            {
                "title": "Escaso vs. abundante (holguras)",
                "explain": "Qué recursos están al límite (cuello de botella) y cuáles sobran. Solo los escasos tienen precio sombra.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\nA = np.array([[1, 2], [3, 1]]); b = np.array([40, 60])\nres = linprog([-40, -30], A_ub=A, b_ub=b, bounds=[(0, None)] * 2)\nholgura = b - A @ res.x; ps = -res.ineqlin.marginals\nfor i in range(len(b)):\n    tipo = "ESCASO (cuello de botella)" if holgura[i] < 1e-6 else f"abundante (sobran {holgura[i]:.1f})"\n    print(f"recurso {i+1}: {tipo} | precio sombra {ps[i]:.2f}")',
            },
            {
                "title": "Verificar el precio sombra",
                "explain": "Damos 1 unidad más del recurso escaso y comprobamos que el margen sube justo su precio sombra.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\ndef margen_opt(b):\n    return -linprog([-40, -30], A_ub=[[1,2],[3,1]], b_ub=b, bounds=[(0,None)]*2).fun\n\nbase = margen_opt([40, 60])\nmas = margen_opt([40, 61])        # 1 hora extra de secado\nprint("margen base:", round(base, 2))\nprint("con 1 h extra de secado:", round(mas, 2))\nprint("mejora (precio sombra):", round(mas - base, 2))',
            },
            {
                "title": "El problema dual",
                "explain": "El dual minimiza el valor de los recursos; sus variables son los precios sombra. Verificamos dualidad fuerte.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\n# Primal: max 40x1+30x2 ; x1+2x2<=40 ; 3x1+x2<=60\n# Dual:  min 40y1+60y2 ; y1+3y2>=40 ; 2y1+y2>=30 ; y>=0\ndual = linprog([40, 60], A_ub=[[-1, -3], [-2, -1]], b_ub=[-40, -30], bounds=[(0, None)] * 2)\nprimal = linprog([-40, -30], A_ub=[[1,2],[3,1]], b_ub=[40,60], bounds=[(0,None)]*2)\nprint("optimo primal:", round(-primal.fun, 2))\nprint("optimo dual  :", round(dual.fun, 2), "(deben coincidir: dualidad fuerte)")\nprint("variables duales (precios sombra):", np.round(dual.x, 2))',
            },
            {
                "title": "Decisión industrial: ¿dónde invertir?",
                "explain": "Comparamos los precios sombra para decidir qué recurso ampliar primero.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\nrecursos = ["mezclado", "secado"]\nA = [[1, 2], [3, 1]]; b = [40, 60]\nres = linprog([-40, -30], A_ub=A, b_ub=b, bounds=[(0, None)] * 2)\nps = -res.ineqlin.marginals\nmejor = int(np.argmax(ps))\nprint("precios sombra:", {recursos[i]: round(ps[i], 2) for i in range(len(ps))})\nprint(f"-> conviene ampliar primero: {recursos[mejor]} (mayor valor marginal)")',
            },
            {
                "title": "Costos reducidos (productos no fabricados)",
                "explain": "Para una variable en 0 en el óptimo, su costo reducido indica cuánto debería mejorar su margen.",
                "code": 'import numpy as np\nfrom scipy.optimize import linprog\n# 3 productos; supongamos que el optimo deja uno en 0\nmargen = [40, 30, 20]\nA = [[1, 2, 2], [3, 1, 2]]; b = [40, 60]\nres = linprog([-m for m in margen], A_ub=A, b_ub=b, bounds=[(0, None)] * 3)\ncr = res.lower.marginals        # costo reducido de cada variable (cota inferior)\nfor i in range(3):\n    print(f"producto {i+1}: x = {res.x[i]:.1f} | costo reducido = {cr[i]:.2f}")',
            },
        ],
        "dataset": "modelos en el código",
        "exercises": [
            "Calcula los precios sombra del problema de sillas y mesas.",
            "Indica qué recurso es el cuello de botella y cuál sobra.",
            "Verifica un precio sombra dando 1 unidad extra del recurso escaso.",
            "Plantea y resuelve el problema dual de tu modelo; comprueba la dualidad fuerte.",
            "Decide en qué recurso invertir primero según los precios sombra.",
            "Calcula el costo reducido de un producto que el óptimo deja en 0.",
            "Sube el margen de ese producto hasta que entre al plan y comprueba.",
            "Explora: ¿hasta cuánto puedes subir una disponibilidad antes de que el precio sombra cambie?",
            "Interpreta en una frase de negocio el precio sombra más alto de tu modelo.",
            "Explica en un comentario qué significa que una restricción esté «activa».",
        ],
    },
]
