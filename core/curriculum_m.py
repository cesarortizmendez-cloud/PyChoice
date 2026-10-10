# -*- coding: utf-8 -*-
"""
PyChoice - Ruta "Ingeniero de IA con Python".
Modulo M - Redes neuronales desde la base (lecciones 50-54).

De la neurona al backpropagation con numpy, y redes con scikit-learn (MLP).
Todo corre en el navegador (numpy; sklearn se autocarga al usarse).
Datasets del motor: clientes, viviendas, estudiantes.
"""

CHAPTERS_M = [

    # ============================================================ CAP 50
    {
        "num": 50,
        "slug": "neurona-perceptron",
        "code": "leccion_50",
        "title": "La neurona y el perceptrón",
        "subtitle": "La unidad básica de una red: suma ponderada, sesgo y activación",
        "apunte": "Módulo M · Lección 1 - La neurona y el perceptrón",
        "concepts": [
            ("Neurona artificial", "Unidad de cálculo que recibe varias entradas, las <b>combina</b> con pesos y produce una salida. Inspirada, muy libremente, en la neurona biológica."),
            ("Pesos (w)", "Un número por cada entrada que indica <b>cuánto importa</b>. Son lo que la red <b>aprende</b>."),
            ("Sesgo (bias, b)", "Un término extra que se suma siempre; permite <b>desplazar</b> el umbral de activación. Es como el intercepto de una recta."),
            ("Suma ponderada", "El corazón de la neurona: <code>z = w·x + b</code> (producto punto de pesos y entradas, más el sesgo)."),
            ("Función de activación", "Transforma la suma <code>z</code> en la salida. En el perceptrón es un <b>escalón</b> (0/1); luego usaremos funciones suaves."),
            ("Perceptrón", "La neurona más simple: suma ponderada + escalón. Clasifica en dos clases trazando una <b>recta</b> (o hiperplano)."),
            ("Regla de aprendizaje", "Cómo ajusta sus pesos: <code>w += lr·(y − ŷ)·x</code>. Si se equivoca, corrige en la dirección del error."),
            ("Separabilidad lineal", "Un perceptrón solo puede separar clases que se dividan con una <b>recta</b>. AND y OR sí; XOR no (lo veremos)."),
        ],
        "theory": """
<p><b>La pieza fundamental.</b> Toda red neuronal, por grande que sea, está hecha de una unidad
simple: la <b>neurona artificial</b>. Entender bien una neurona es entender el 80% de una red. Una
neurona recibe varias <b>entradas</b> (números), las combina y produce <b>una salida</b>.</p>

<p><b>Suma ponderada + activación.</b> La neurona hace dos cosas. Primero, una <b>suma ponderada</b>:
multiplica cada entrada por su <b>peso</b> y suma todo, más un <b>sesgo</b>:
<code>z = w₁x₁ + w₂x₂ + … + b</code>. Con numpy es un producto punto: <code>z = w·x + b</code>. Luego
aplica una <b>función de activación</b> a <code>z</code> para producir la salida. En el perceptrón, la
activación es un <b>escalón</b>: si <code>z ≥ 0</code> devuelve 1, si no, 0.</p>

<p><b>Los pesos son lo que se aprende.</b> Los pesos y el sesgo son los <b>parámetros</b> de la
neurona. Cambiarlos cambia qué calcula. <b>Entrenar</b> una red es, esencialmente, <b>encontrar los
pesos</b> que hacen que la salida sea la correcta —otra vez un problema de optimización, como toda la
ruta.</p>

<p><b>El perceptrón y su regla.</b> El <b>perceptrón</b> (Rosenblatt, 1958) fue la primera neurona que
<b>aprendía sola</b>. Su regla es intuitiva: para cada ejemplo, compara su predicción <code>ŷ</code>
con la respuesta real <code>y</code>; si acierta, no cambia nada; si se equivoca, ajusta los pesos en
la dirección que reduce el error: <code>w += lr·(y − ŷ)·x</code>, donde <code>lr</code> es la
<b>tasa de aprendizaje</b>. Repitiendo sobre los datos, los pesos convergen.</p>

<p><b>Qué puede y qué no.</b> Un perceptrón traza una <b>recta</b> (o un hiperplano) para separar dos
clases. Si los datos son <b>linealmente separables</b> —como las funciones lógicas AND y OR—, la
encuentra. Pero hay problemas que <b>ninguna recta</b> separa: el caso famoso es <b>XOR</b>. Esa
limitación, descubierta en 1969, casi mata el campo… hasta que llegaron las <b>capas ocultas</b>
(próxima lección), que la superan.</p>

<p><b>Por qué construirla a mano.</b> En la lección 53 usaremos redes de scikit-learn con una línea de
código. Pero programar la neurona con numpy —la suma ponderada, el escalón, la regla de aprendizaje—
es lo que hace que una red <b>deje de ser magia</b>. Todo lo demás son muchas de estas unidades
conectadas.</p>
""",
        "examples": [
            {
                "title": "Una neurona: suma ponderada + escalón",
                "explain": "La neurona combina entradas con pesos y un sesgo, y decide con un escalón (1 si z ≥ 0).",
                "code": 'import numpy as np\nw = np.array([0.5, -0.3])\nb = 0.1\n\ndef neurona(x):\n    z = np.dot(w, x) + b\n    return 1 if z >= 0 else 0\n\nfor x in [[1, 1], [1, 0], [0, 1], [0, 0]]:\n    print("x =", x, "-> salida =", neurona(np.array(x)))',
            },
            {
                "title": "La función AND con pesos elegidos a mano",
                "explain": "Con los pesos correctos, una sola neurona implementa AND (solo 1+1 da 1).",
                "code": 'import numpy as np\nw = np.array([1.0, 1.0]); b = -1.5    # umbral: necesita ambas entradas en 1\n\ndef neurona(x):\n    return 1 if np.dot(w, x) + b >= 0 else 0\n\nfor x in [[0,0],[0,1],[1,0],[1,1]]:\n    print(x, "-> AND =", neurona(np.array(x)))',
            },
            {
                "title": "Entrenar un perceptrón (aprende AND solo)",
                "explain": "Partimos de pesos en cero y aplicamos la regla de aprendizaje hasta que acierta todos los casos.",
                "code": 'import numpy as np\nX = np.array([[0,0],[0,1],[1,0],[1,1]])\ny = np.array([0, 0, 0, 1])        # AND\nw = np.zeros(2); b = 0.0; lr = 0.1\n\ndef pred(x):\n    return 1 if np.dot(w, x) + b >= 0 else 0\n\nfor epoca in range(20):\n    for xi, yi in zip(X, y):\n        error = yi - pred(xi)\n        w += lr * error * xi\n        b += lr * error\nprint("pesos:", np.round(w, 2), "| sesgo:", round(b, 2))\nprint("predicciones:", [pred(x) for x in X], "| esperado:", list(y))',
            },
            {
                "title": "El mismo perceptrón aprende OR",
                "explain": "Cambiando solo las etiquetas, el perceptrón aprende OR: basta una entrada en 1.",
                "code": 'import numpy as np\nX = np.array([[0,0],[0,1],[1,0],[1,1]])\ny = np.array([0, 1, 1, 1])        # OR\nw = np.zeros(2); b = 0.0; lr = 0.1\n\ndef pred(x):\n    return 1 if np.dot(w, x) + b >= 0 else 0\n\nfor _ in range(20):\n    for xi, yi in zip(X, y):\n        e = yi - pred(xi); w += lr * e * xi; b += lr * e\nprint("predicciones OR:", [pred(x) for x in X], "| esperado:", list(y))',
            },
            {
                "title": "El perceptrón NO puede con XOR",
                "explain": "XOR no es linealmente separable: ninguna recta lo divide, así que el perceptrón nunca acierta todo.",
                "code": 'import numpy as np\nX = np.array([[0,0],[0,1],[1,0],[1,1]])\ny = np.array([0, 1, 1, 0])        # XOR\nw = np.zeros(2); b = 0.0; lr = 0.1\n\ndef pred(x):\n    return 1 if np.dot(w, x) + b >= 0 else 0\n\nfor _ in range(100):\n    for xi, yi in zip(X, y):\n        e = yi - pred(xi); w += lr * e * xi; b += lr * e\nprint("predicciones XOR:", [pred(x) for x in X], "| esperado:", list(y))\nprint("-> imposible separarlo con una recta (hace falta una capa oculta)")',
            },
            {
                "title": "La frontera de decisión (AND)",
                "explain": "Graficamos los puntos y la recta w·x + b = 0 que el perceptrón usa para separar las clases.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nX = np.array([[0,0],[0,1],[1,0],[1,1]]); y = np.array([0,0,0,1])\nw = np.array([1.0, 1.0]); b = -1.5\n\nplt.scatter(X[:,0], X[:,1], c=y, cmap="bwr", s=120, edgecolor="k")\nxx = np.linspace(-0.5, 1.5, 10)\nplt.plot(xx, -(w[0]*xx + b) / w[1], "g--", label="frontera")\nplt.xlabel("x1"); plt.ylabel("x2"); plt.title("Perceptron: frontera lineal (AND)")\nplt.legend(); plt.show()',
            },
        ],
        "dataset": "datos lógicos (AND/OR/XOR)",
        "exercises": [
            "Define una neurona con pesos <code>[0.6, 0.6]</code> y sesgo <code>-0.5</code>; evalúala en las 4 combinaciones de (0/1).",
            "Elige pesos y sesgo a mano para implementar la función OR con una neurona.",
            "Entrena un perceptrón para aprender AND partiendo de pesos aleatorios.",
            "Entrena un perceptrón para NAND (lo contrario de AND).",
            "Muestra, entrenando, que el perceptrón no logra aprender XOR.",
            "Cambia la tasa de aprendizaje (0.01 y 0.5) y observa si cambia la convergencia en AND.",
            "Grafica la frontera de decisión que aprende tu perceptrón para OR.",
            "Agrega una tercera entrada y entrena el perceptrón para una función que tú definas.",
            "Cuenta cuántas épocas necesita el perceptrón para acertar todo en AND.",
            "Explica en un comentario qué significa que un problema sea «linealmente separable».",
        ],
    },

    # ============================================================ CAP 51
    {
        "num": 51,
        "slug": "mlp-forward",
        "code": "leccion_51",
        "title": "Perceptrón multicapa y forward pass",
        "subtitle": "Capas ocultas, funciones de activación y el pase hacia adelante",
        "apunte": "Módulo M · Lección 2 - MLP y forward pass",
        "concepts": [
            ("Capa oculta", "Una capa de neuronas <b>entre</b> la entrada y la salida. Permite aprender relaciones <b>no lineales</b> (como XOR)."),
            ("Perceptrón multicapa (MLP)", "Red con una o más capas ocultas. Es la red neuronal <b>clásica</b> (<i>fully connected</i>)."),
            ("Sigmoide", "Activación suave que aplasta cualquier número al rango (0, 1): <code>1/(1+e^-z)</code>. Útil para probabilidades."),
            ("ReLU", "Activación <code>max(0, z)</code>: simple, rápida y la más usada en capas ocultas modernas."),
            ("Softmax", "Convierte un vector de números en <b>probabilidades</b> que suman 1. Se usa en la capa de salida para clasificar en varias clases."),
            ("Pase hacia adelante (forward)", "Calcular la salida de la red: aplicar capa por capa <code>z = XW + b</code> y su activación, hasta el final."),
            ("Representación matricial", "Toda una capa se calcula de una vez con <b>multiplicación de matrices</b> (numpy): rápido y compacto."),
            ("No linealidad", "Sin funciones de activación no lineales, apilar capas daría solo otra recta. La no linealidad es lo que da <b>poder</b> a la red."),
        ],
        "theory": """
<p><b>El salto: capas ocultas.</b> El perceptrón fallaba con XOR porque solo traza una recta. La
solución es poner una o más <b>capas ocultas</b> de neuronas entre la entrada y la salida. Cada capa
transforma los datos a una nueva representación donde el problema <b>sí</b> se vuelve separable. Esa red
se llama <b>perceptrón multicapa</b> (MLP).</p>

<p><b>Todo son multiplicaciones de matrices.</b> Una capa con varias neuronas se calcula de una sola
vez: si <code>X</code> son las entradas y <code>W</code> la matriz de pesos (una columna por neurona),
la capa produce <code>Z = X·W + b</code>, y luego una <b>activación</b> elemento a elemento. Con numpy
esto es una línea. Encadenar capas es encadenar estas operaciones: eso es el <b>forward pass</b>.</p>

<p><b>Las funciones de activación.</b> Entre capa y capa va una función <b>no lineal</b>. La
<b>sigmoide</b> aplasta al rango (0,1) y sirve para probabilidades. La <b>ReLU</b> (<code>max(0,z)</code>)
es la favorita moderna por simple y eficiente. En la salida de una clasificación multiclase se usa
<b>softmax</b>, que convierte números en <b>probabilidades que suman 1</b>.</p>

<p><b>¿Por qué no linealidad?</b> Aquí está la clave. Si las activaciones fueran lineales, apilar diez
capas daría exactamente lo mismo que una sola recta: nada se gana. Son las <b>funciones no lineales</b>
las que permiten a la red <b>doblar y curvar</b> el espacio y aprender fronteras complejas. Sin ellas,
no hay aprendizaje profundo.</p>

<p><b>El forward pass, paso a paso.</b> Dada una entrada: se calcula la primera capa (<code>Z1 = XW1 +
b1</code>, luego <code>A1 = activación(Z1)</code>); esa salida alimenta la segunda capa
(<code>Z2 = A1·W2 + b2</code>, <code>A2 = activación(Z2)</code>); y así hasta la capa final, que da la
<b>predicción</b>. Es puro álgebra lineal más una no linealidad.</p>

<p><b>XOR, resuelto.</b> Con una capa oculta de apenas dos neuronas y los pesos adecuados, una MLP
<b>sí</b> calcula XOR: la capa oculta crea dos «detectores» intermedios y la capa de salida los
combina. En esta lección lo veremos con el forward pass; en la próxima, la red <b>aprenderá</b> esos
pesos sola con backpropagation.</p>
""",
        "examples": [
            {
                "title": "Sigmoide y ReLU",
                "explain": "Las dos activaciones más comunes. La sigmoide aplasta a (0,1); la ReLU deja pasar lo positivo.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\n\ndef sigmoide(z): return 1 / (1 + np.exp(-z))\ndef relu(z): return np.maximum(0, z)\n\nz = np.linspace(-6, 6, 200)\nplt.plot(z, sigmoide(z), label="sigmoide")\nplt.plot(z, relu(z), label="ReLU")\nplt.axhline(0, color="gray", lw=.5); plt.axvline(0, color="gray", lw=.5)\nplt.legend(); plt.title("Funciones de activacion"); plt.show()',
            },
            {
                "title": "Una capa con álgebra matricial",
                "explain": "Toda una capa de neuronas se calcula de una vez: Z = X·W + b, y luego la activación.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\nX = np.array([[0.5, -1.0], [1.0, 2.0]])     # 2 ejemplos, 2 entradas\nW = rng.normal(0, 1, (2, 3))                # 2 entradas -> 3 neuronas\nb = np.zeros(3)\n\ndef sigmoide(z): return 1 / (1 + np.exp(-z))\nZ = X @ W + b\nA = sigmoide(Z)\nprint("salida de la capa (2 ejemplos x 3 neuronas):\\n", np.round(A, 3))',
            },
            {
                "title": "Forward pass de un MLP 2-3-1",
                "explain": "Encadenamos dos capas: entrada → oculta (3 neuronas, sigmoide) → salida (1 neurona).",
                "code": 'import numpy as np\nrng = np.random.default_rng(1)\ndef sig(z): return 1 / (1 + np.exp(-z))\n\nX = np.array([[1.0, 0.0]])\nW1 = rng.normal(0, 1, (2, 3)); b1 = np.zeros(3)\nW2 = rng.normal(0, 1, (3, 1)); b2 = np.zeros(1)\n\nA1 = sig(X @ W1 + b1)      # capa oculta\nA2 = sig(A1 @ W2 + b2)     # capa de salida\nprint("activacion oculta:", np.round(A1, 3))\nprint("salida de la red :", np.round(A2, 3))',
            },
            {
                "title": "Softmax para varias clases",
                "explain": "Convierte números (logits) en probabilidades que suman 1. Útil en la capa de salida multiclase.",
                "code": 'import numpy as np\ndef softmax(z):\n    e = np.exp(z - z.max())\n    return e / e.sum()\n\nlogits = np.array([2.0, 1.0, 0.1])\np = softmax(logits)\nprint("probabilidades:", np.round(p, 3))\nprint("suman:", round(p.sum(), 5), "| clase elegida:", int(p.argmax()))',
            },
            {
                "title": "Un MLP resuelve XOR (con pesos a mano)",
                "explain": "Con una capa oculta de 2 neuronas y pesos elegidos, el forward pass calcula XOR correctamente.",
                "code": 'import numpy as np\ndef paso(z): return (z >= 0).astype(int)\nX = np.array([[0,0],[0,1],[1,0],[1,1]])\n\n# capa oculta: h1 = OR, h2 = NAND ; salida = AND(h1, h2) = XOR\nW1 = np.array([[1, -1], [1, -1]]); b1 = np.array([-0.5, 1.5])\nW2 = np.array([[1], [1]]);         b2 = np.array([-1.5])\n\nH = paso(X @ W1 + b1)\nout = paso(H @ W2 + b2).ravel()\nprint("XOR calculado:", list(out), "| esperado: [0, 1, 1, 0]")',
            },
        ],
        "dataset": "datos generados",
        "exercises": [
            "Programa la función sigmoide y evalúala en -2, 0 y 2.",
            "Programa ReLU y grafícala entre -5 y 5.",
            "Calcula una capa <code>Z = X·W + b</code> con X de 3 ejemplos y 2 entradas, hacia 4 neuronas.",
            "Haz el forward pass de un MLP 2-4-1 con pesos aleatorios para una entrada cualquiera.",
            "Aplica softmax a <code>[1.0, 3.0, 0.2]</code> y verifica que suma 1.",
            "Usa ReLU en la capa oculta en vez de sigmoide y compara las activaciones.",
            "Verifica con el forward pass a mano que la red del ejemplo calcula XOR en los 4 casos.",
            "Agrega una segunda capa oculta (MLP 2-3-3-1) y haz el forward pass.",
            "Explica en un comentario por qué sin activación no lineal apilar capas no sirve.",
            "Cuenta cuántos pesos tiene un MLP 2-4-1 (incluye sesgos).",
        ],
    },

    # ============================================================ CAP 52
    {
        "num": 52,
        "slug": "backpropagation",
        "code": "leccion_52",
        "title": "Backpropagation y descenso de gradiente",
        "subtitle": "Cómo aprende una red: pérdida, gradientes y entrenamiento desde cero",
        "apunte": "Módulo M · Lección 3 - Backpropagation",
        "concepts": [
            ("Función de pérdida", "Mide <b>qué tan mal</b> predice la red (error cuadrático, entropía cruzada). Entrenar es <b>minimizarla</b>."),
            ("Descenso de gradiente", "Ajustar los pesos dando pasos en la dirección que <b>más reduce</b> la pérdida: <code>w -= lr·∂L/∂w</code>."),
            ("Gradiente", "La derivada de la pérdida respecto a cada peso: indica <b>cuánto y hacia dónde</b> mover cada uno."),
            ("Tasa de aprendizaje", "El tamaño del paso. Muy grande se pasa y oscila; muy chica aprende lentísimo."),
            ("Retropropagación (backprop)", "Algoritmo que calcula los gradientes de todas las capas <b>propagando el error hacia atrás</b>, usando la regla de la cadena."),
            ("Regla de la cadena", "La regla de derivadas de funciones compuestas; es el motor matemático de backprop."),
            ("Época", "Una pasada completa por todos los datos de entrenamiento. Se repiten muchas."),
            ("Convergencia", "Cuando la pérdida deja de bajar: la red encontró buenos pesos (o se estancó)."),
        ],
        "theory": """
<p><b>Aprender = minimizar una pérdida.</b> Una red predice con sus pesos actuales; una <b>función de
pérdida</b> mide cuánto se equivoca comparando la predicción con la respuesta real. Entrenar es
<b>ajustar los pesos para minimizar esa pérdida</b>. Otra vez optimización —el hilo de toda la ruta—,
pero ahora sobre miles de pesos.</p>

<p><b>Descenso de gradiente.</b> ¿Cómo mover tantos pesos? Con el <b>gradiente</b>: la derivada de la
pérdida respecto a cada peso, que dice en qué dirección <b>crece</b> el error. Si damos un pequeño paso
en la dirección <b>contraria</b>, el error baja: <code>w -= lr·∂L/∂w</code>. Repetir esto muchas veces
es el <b>descenso de gradiente</b>, el algoritmo que entrena casi toda la IA moderna.</p>

<p><b>La tasa de aprendizaje.</b> El tamaño del paso (<code>lr</code>) es crítico. Demasiado grande y
el entrenamiento <b>oscila</b> o diverge; demasiado chico y tarda una eternidad. Ajustarla bien es de
las primeras cosas que aprende quien entrena redes.</p>

<p><b>Backpropagation: el gradiente, barato.</b> Calcular el gradiente de cada peso parece carísimo en
una red con muchas capas. La <b>retropropagación</b> lo hace eficientemente: primero un forward pass
guardando los valores intermedios; luego propaga el error <b>desde la salida hacia atrás</b>, capa por
capa, aplicando la <b>regla de la cadena</b>. Así obtiene todos los gradientes en una sola pasada hacia
atrás. Es el algoritmo (Rumelhart, Hinton y Williams, 1986) que revivió las redes neuronales.</p>

<p><b>El ciclo de entrenamiento.</b> Se repite por muchas <b>épocas</b>: (1) forward pass para predecir;
(2) calcular la pérdida; (3) backprop para obtener los gradientes; (4) actualizar los pesos con
descenso de gradiente. Época tras época, la pérdida baja y las predicciones mejoran, hasta
<b>converger</b>.</p>

<p><b>XOR, ahora aprendido.</b> En la lección anterior pusimos los pesos de XOR a mano. Aquí la red los
<b>aprende sola</b>: partiendo de pesos aleatorios, backprop ajusta una capa oculta hasta resolver XOR.
Ver bajar la pérdida y aparecer la solución es ver, en pequeño, cómo aprende cualquier red profunda.</p>
""",
        "examples": [
            {
                "title": "Descenso de gradiente en una variable",
                "explain": "Minimizamos f(x)=(x-3)² dando pasos contra su derivada f'(x)=2(x-3). Converge a x=3.",
                "code": 'x = 0.0; lr = 0.1\nfor paso in range(30):\n    grad = 2 * (x - 3)      # derivada de (x-3)^2\n    x -= lr * grad\nprint("x final:", round(x, 4), "(minimo en 3)")',
            },
            {
                "title": "La derivada de la sigmoide",
                "explain": "Backprop necesita derivadas. La de la sigmoide es muy simple: s(z)·(1−s(z)).",
                "code": 'import numpy as np\ndef sig(z): return 1 / (1 + np.exp(-z))\ndef dsig(z):\n    s = sig(z); return s * (1 - s)\n\nfor z in [-2, 0, 2]:\n    print(f"z={z:>3}: sig={sig(z):.3f}  derivada={dsig(z):.3f}")',
            },
            {
                "title": "Entrenar una neurona (regresión logística)",
                "explain": "Una neurona con sigmoide aprende a clasificar con descenso de gradiente sobre el error.",
                "code": 'import numpy as np\nrng = np.random.default_rng(0)\nX = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)\ny = np.array([0, 0, 0, 1.0])              # AND\nw = rng.normal(0, 1, 2); b = 0.0; lr = 0.5\ndef sig(z): return 1 / (1 + np.exp(-z))\n\nfor epoca in range(2000):\n    z = X @ w + b; p = sig(z)\n    error = p - y                        # gradiente de la entropia\n    w -= lr * (X.T @ error) / len(X)\n    b -= lr * error.mean()\nprint("predicciones:", np.round(sig(X @ w + b), 2), "| esperado:", list(y))',
            },
            {
                "title": "Entrenar un MLP para XOR (backprop desde cero)",
                "explain": "Red 2-4-1 con sigmoide. Backprop ajusta los pesos hasta resolver XOR. Observa la pérdida bajar.",
                "code": 'import numpy as np\nrng = np.random.default_rng(1)\nX = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)\ny = np.array([[0],[1],[1],[0]], dtype=float)\ndef sig(z): return 1 / (1 + np.exp(-z))\n\nW1 = rng.normal(0, 1, (2, 4)); b1 = np.zeros((1, 4))\nW2 = rng.normal(0, 1, (4, 1)); b2 = np.zeros((1, 1))\nlr = 0.5\nfor epoca in range(6000):\n    # forward\n    A1 = sig(X @ W1 + b1)\n    A2 = sig(A1 @ W2 + b2)\n    # backprop\n    d2 = (A2 - y) * A2 * (1 - A2)\n    d1 = (d2 @ W2.T) * A1 * (1 - A1)\n    W2 -= lr * A1.T @ d2; b2 -= lr * d2.sum(0, keepdims=True)\n    W1 -= lr * X.T @ d1;  b1 -= lr * d1.sum(0, keepdims=True)\nprint("predicciones XOR:", np.round(A2.ravel(), 2), "| esperado: [0, 1, 1, 0]")',
            },
            {
                "title": "La curva de pérdida",
                "explain": "Guardamos la pérdida por época: baja a medida que la red aprende XOR.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(1)\nX = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)\ny = np.array([[0],[1],[1],[0]], dtype=float)\ndef sig(z): return 1 / (1 + np.exp(-z))\nW1 = rng.normal(0,1,(2,4)); b1 = np.zeros((1,4))\nW2 = rng.normal(0,1,(4,1)); b2 = np.zeros((1,1)); lr = 0.5\nperdidas = []\nfor _ in range(6000):\n    A1 = sig(X @ W1 + b1); A2 = sig(A1 @ W2 + b2)\n    perdidas.append(np.mean((A2 - y) ** 2))\n    d2 = (A2 - y) * A2 * (1 - A2); d1 = (d2 @ W2.T) * A1 * (1 - A1)\n    W2 -= lr * A1.T @ d2; b2 -= lr * d2.sum(0, keepdims=True)\n    W1 -= lr * X.T @ d1;  b1 -= lr * d1.sum(0, keepdims=True)\nplt.plot(perdidas); plt.xlabel("epoca"); plt.ylabel("perdida (MSE)")\nplt.title("Entrenamiento de XOR"); plt.show()',
            },
            {
                "title": "El efecto de la tasa de aprendizaje",
                "explain": "Comparamos lr pequeña, media y grande: la pérdida final tras las mismas épocas cambia mucho.",
                "code": 'import numpy as np\nX = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)\ny = np.array([[0],[1],[1],[0]], dtype=float)\ndef sig(z): return 1 / (1 + np.exp(-z))\n\ndef entrena(lr, seed=1, epocas=3000):\n    rng = np.random.default_rng(seed)\n    W1 = rng.normal(0,1,(2,4)); b1 = np.zeros((1,4))\n    W2 = rng.normal(0,1,(4,1)); b2 = np.zeros((1,1))\n    for _ in range(epocas):\n        A1 = sig(X @ W1 + b1); A2 = sig(A1 @ W2 + b2)\n        d2 = (A2 - y) * A2 * (1 - A2); d1 = (d2 @ W2.T) * A1 * (1 - A1)\n        W2 -= lr * A1.T @ d2; b2 -= lr * d2.sum(0, keepdims=True)\n        W1 -= lr * X.T @ d1;  b1 -= lr * d1.sum(0, keepdims=True)\n    return np.mean((A2 - y) ** 2)\n\nfor lr in [0.05, 0.5, 5.0]:\n    print(f"lr={lr:>4} -> perdida final {entrena(lr):.4f}")',
            },
        ],
        "dataset": "datos generados (XOR)",
        "exercises": [
            "Minimiza <code>(x-5)²</code> con descenso de gradiente partiendo de x=0.",
            "Programa la derivada de la sigmoide y evalúala en varios puntos.",
            "Entrena una neurona para la función OR con descenso de gradiente.",
            "Entrena el MLP 2-4-1 para XOR y verifica las 4 predicciones.",
            "Grafica la curva de pérdida de tu entrenamiento de XOR.",
            "Prueba 3 tasas de aprendizaje y compara la pérdida final.",
            "Cambia el tamaño de la capa oculta (2, 4, 8) y compara la convergencia.",
            "Entrena durante más épocas y observa hasta dónde baja la pérdida.",
            "Usa otra semilla de pesos iniciales: ¿siempre converge?",
            "Explica en un comentario qué hace la retropropagación en una frase.",
        ],
    },

    # ============================================================ CAP 53
    {
        "num": 53,
        "slug": "redes-sklearn",
        "code": "leccion_53",
        "title": "Redes neuronales con scikit-learn",
        "subtitle": "MLPClassifier y MLPRegressor en datos reales: escalado y regularización",
        "apunte": "Módulo M · Lección 4 - Redes con scikit-learn",
        "concepts": [
            ("MLPClassifier", "La red neuronal de scikit-learn para <b>clasificar</b>. Se usa con la misma API <code>fit</code>/<code>predict</code> que viste en el módulo H."),
            ("MLPRegressor", "La versión para <b>predecir números</b> (regresión) con una red neuronal."),
            ("hidden_layer_sizes", "Define la <b>arquitectura</b>: p. ej. <code>(16, 8)</code> son dos capas ocultas de 16 y 8 neuronas."),
            ("Escalado", "Las redes <b>exigen</b> datos escalados (<code>StandardScaler</code>). Sin eso, entrenan mal o no convergen."),
            ("max_iter", "Número máximo de épocas de entrenamiento. Si la red no converge, suele faltar escalado o iteraciones."),
            ("alpha", "Fuerza de la <b>regularización</b> (L2). Más alta combate el sobreajuste; demasiada, subajusta."),
            ("early_stopping", "Detiene el entrenamiento cuando deja de mejorar en validación: ahorra tiempo y evita sobreajustar."),
            ("loss_curve_", "La lista de pérdidas por época que guarda el modelo; útil para graficar el entrenamiento."),
        ],
        "theory": """
<p><b>De lo artesanal a lo práctico.</b> Ya sabes lo que pasa <b>por dentro</b>: forward pass, pérdida,
backprop, descenso de gradiente. En la práctica no se programa cada vez: se usa una librería. En el
navegador tenemos <b>scikit-learn</b>, con <code>MLPClassifier</code> y <code>MLPRegressor</code>, que
entrenan una red con la misma API <code>fit</code>/<code>predict</code> del módulo H.</p>

<p><b>La arquitectura.</b> El parámetro <code>hidden_layer_sizes</code> define las capas ocultas:
<code>(16,)</code> es una capa de 16 neuronas; <code>(32, 16)</code> son dos capas. Más grande puede
aprender relaciones más complejas… y también sobreajustar más fácil. Empieza pequeño y crece si hace
falta.</p>

<p><b>Escalar no es opcional.</b> Este es el error más común: las redes neuronales <b>necesitan</b> que
las variables estén en escalas parecidas. Si una columna va de 0 a 1 y otra de 0 a 100000, el
entrenamiento se descompensa. La solución es <b>StandardScaler</b> (restar media, dividir por
desviación), idealmente dentro de un <code>Pipeline</code> para no filtrar información del test.</p>

<p><b>Regularización contra el sobreajuste.</b> Una red con muchos pesos puede <b>memorizar</b> el
entrenamiento y fallar en datos nuevos. El parámetro <code>alpha</code> aplica <b>regularización
L2</b>: penaliza pesos grandes y suaviza el modelo. Súbelo si ves mucha diferencia entre el acierto en
train y en test (lo veremos a fondo en la próxima lección).</p>

<p><b>Convergencia y paciencia.</b> Si sklearn avisa que <b>no convergió</b>, casi siempre es por falta
de escalado o de <code>max_iter</code>. Con <code>early_stopping=True</code>, la red separa un trocito
de validación y <b>para sola</b> cuando deja de mejorar, lo que ahorra tiempo y reduce el sobreajuste.</p>

<p><b>Con datos reales de PyChoice.</b> Usaremos los datasets del motor: predecir el <b>churn</b> de
<code>clientes</code> (clasificación) y el <b>precio</b> de <code>viviendas</code> (regresión).
Compararemos la red con los modelos lineales del módulo H para ver cuándo vale la pena una red —no
siempre gana, y eso también es una lección importante.</p>
""",
        "examples": [
            {
                "title": "Un clasificador neuronal para el churn",
                "explain": "MLP con escalado dentro de un Pipeline, sobre el dataset clientes. Reporta la exactitud en test.",
                "code": 'import numpy as np, pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nmlp = make_pipeline(StandardScaler(),\n                    MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=7))\nmlp.fit(Xtr, ytr)\nprint("exactitud en test:", round(mlp.score(Xte, yte), 3))',
            },
            {
                "title": "Un regresor neuronal para el precio",
                "explain": "MLPRegressor predice el precio de viviendas. El escalado es imprescindible aquí.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPRegressor\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.metrics import r2_score\n\nX = pd.get_dummies(viviendas.drop(columns=["precio"]), drop_first=True)\ny = viviendas["precio"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nreg = make_pipeline(StandardScaler(),\n                    MLPRegressor(hidden_layer_sizes=(32, 16), max_iter=800, random_state=7))\nreg.fit(Xtr, ytr)\nprint("R2 en test:", round(r2_score(yte, reg.predict(Xte)), 3))',
            },
            {
                "title": "El efecto de la arquitectura",
                "explain": "Comparamos distintos tamaños de capas ocultas en el churn de clientes.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nfor arq in [(8,), (16, 8), (32, 16, 8)]:\n    m = make_pipeline(StandardScaler(),\n                      MLPClassifier(hidden_layer_sizes=arq, max_iter=500, random_state=7))\n    m.fit(Xtr, ytr)\n    print(f"capas {arq} -> exactitud {m.score(Xte, yte):.3f}")',
            },
            {
                "title": "Regularización con alpha",
                "explain": "Subir alpha regulariza más. Comparamos el acierto en train vs test para ver el sobreajuste.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nfor a in [0.0001, 0.01, 1.0]:\n    m = make_pipeline(StandardScaler(),\n                      MLPClassifier(hidden_layer_sizes=(32, 16), alpha=a,\n                                    max_iter=600, random_state=7))\n    m.fit(Xtr, ytr)\n    print(f"alpha={a:<7} train {m.score(Xtr, ytr):.3f} | test {m.score(Xte, yte):.3f}")',
            },
            {
                "title": "La curva de pérdida del entrenamiento",
                "explain": "El MLP guarda su pérdida por época en loss_curve_. La graficamos para ver cómo entrenó.",
                "code": 'import pandas as pd, matplotlib.pyplot as plt\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXs = StandardScaler().fit_transform(X)\nmlp = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=7)\nmlp.fit(Xs, y)\nplt.plot(mlp.loss_curve_); plt.xlabel("epoca"); plt.ylabel("perdida")\nplt.title("Curva de perdida (MLPClassifier)"); plt.show()',
            },
            {
                "title": "¿Gana la red a un modelo lineal?",
                "explain": "Comparamos la red con una regresión logística en el mismo problema. No siempre la red es mejor.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nlog = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)\nmlp = make_pipeline(StandardScaler(), MLPClassifier((16, 8), max_iter=500, random_state=7)).fit(Xtr, ytr)\nprint("logistica:", round(log.score(Xte, yte), 3))\nprint("red (MLP):", round(mlp.score(Xte, yte), 3))',
            },
        ],
        "dataset": "clientes, viviendas, estudiantes",
        "exercises": [
            "Entrena un <code>MLPClassifier</code> para el churn de <code>clientes</code> con escalado y reporta la exactitud.",
            "Entrena un <code>MLPRegressor</code> para el precio de <code>viviendas</code> y reporta el R².",
            "Predice la nota de <code>estudiantes</code> (nota_final) con una red y evalúala.",
            "Compara tres arquitecturas de capas ocultas en el churn.",
            "Prueba tres valores de <code>alpha</code> y observa train vs test.",
            "Entrena sin escalar y con escalado: compara el resultado (y los avisos de convergencia).",
            "Activa <code>early_stopping=True</code> y compara con el entrenamiento normal.",
            "Grafica la <code>loss_curve_</code> del entrenamiento.",
            "Compara la red con un Random Forest (módulo H) en el mismo problema.",
            "Explica en un comentario por qué el escalado es imprescindible para una red.",
        ],
    },

    # ============================================================ CAP 54
    {
        "num": 54,
        "slug": "deep-learning-panorama",
        "code": "leccion_54",
        "title": "Buenas prácticas y panorama del deep learning",
        "subtitle": "Sobreajuste, regularización y hacia dónde sigue el aprendizaje profundo",
        "apunte": "Módulo M · Lección 5 - Buenas prácticas y panorama",
        "concepts": [
            ("Sobreajuste", "La red memoriza el entrenamiento y falla en datos nuevos: acierto alto en train, bajo en test."),
            ("Subajuste", "El modelo es demasiado simple (o muy regularizado) y no capta el patrón ni en train."),
            ("Regularización", "Técnicas para combatir el sobreajuste: <code>alpha</code> (L2), redes más chicas, early stopping, más datos."),
            ("Conjunto de validación", "Datos separados para <b>elegir</b> arquitectura e hiperparámetros sin tocar el test final."),
            ("Curva de aprendizaje", "Desempeño en train y validación según el tamaño de datos o las épocas; revela sobre/subajuste."),
            ("Deep learning", "Redes con <b>muchas</b> capas que aprenden representaciones jerárquicas; dominan visión, lenguaje y más."),
            ("CNN y RNN", "Arquitecturas especializadas: <b>CNN</b> para imágenes, <b>RNN</b>/LSTM para secuencias."),
            ("Transformers", "La arquitectura detrás de los grandes modelos de lenguaje actuales (atención); el estado del arte."),
        ],
        "theory": """
<p><b>El enemigo número uno: el sobreajuste.</b> Una red con suficientes pesos puede <b>memorizar</b>
los datos de entrenamiento, logrando casi 100% de acierto ahí y fallando con datos nuevos. La señal es
clara: <b>train alto, test bajo</b>. El objetivo del aprendizaje automático no es memorizar, sino
<b>generalizar</b>. Vigilar la brecha train–test es el hábito más importante.</p>

<p><b>Las herramientas contra el sobreajuste.</b> Varias, y suelen combinarse: <b>regularización</b>
(<code>alpha</code>), usar una <b>red más pequeña</b>, <b>early stopping</b>, y —la más poderosa—
<b>más datos</b>. El subajuste es el problema opuesto: un modelo demasiado simple que no aprende ni el
entrenamiento; ahí hay que dar <b>más capacidad</b> o entrenar más.</p>

<p><b>Validar bien.</b> Para elegir arquitectura e hiperparámetros no se usa el test (eso lo
contaminaría): se usa un <b>conjunto de validación</b> aparte, o validación cruzada (módulo H). El test
se reserva para la <b>estimación final</b>, una sola vez. Las <b>curvas de aprendizaje</b> —desempeño
en train y validación según datos o épocas— son el diagnóstico visual del equilibrio.</p>

<p><b>Qué es el deep learning.</b> El <b>aprendizaje profundo</b> son redes con <b>muchas</b> capas que
aprenden representaciones por niveles: de bordes a formas a objetos, por ejemplo. Esa profundidad, más
grandes volúmenes de datos y GPUs, es lo que disparó los avances de la última década.</p>

<p><b>Las arquitecturas que cambiaron todo.</b> Las <b>CNN</b> (redes convolucionales) explotan la
estructura espacial de las <b>imágenes</b>. Las <b>RNN</b> y LSTM procesan <b>secuencias</b> (texto,
series). Y los <b>Transformers</b> —con su mecanismo de <b>atención</b>— son la base de los grandes
modelos de lenguaje actuales. El MLP que construiste es el ancestro común de todas ellas.</p>

<p><b>El siguiente paso, fuera del navegador.</b> PyChoice ejecuta todo en el navegador, y por eso las
redes profundas con <b>PyTorch</b> o <b>TensorFlow</b> (que necesitan GPU y binarios nativos) quedan
<b>fuera</b> de aquí. El camino natural para seguir: <b>Google Colab</b> (gratis, con GPU) y la
documentación de PyTorch. Lo que aprendiste —forward, pérdida, backprop, regularización, validación— es
<b>exactamente</b> lo que harás allá, solo que con más capas y una librería que calcula los gradientes
por ti. Entendiste la base; lo demás es escala.</p>
""",
        "examples": [
            {
                "title": "Ver el sobreajuste en acción",
                "explain": "Una red grande sin regularización sobre pocos datos: acierto casi perfecto en train, peor en test.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=7)\n\nm = make_pipeline(StandardScaler(),\n                  MLPClassifier((128, 64), alpha=1e-6, max_iter=1500, random_state=7))\nm.fit(Xtr, ytr)\nprint("train:", round(m.score(Xtr, ytr), 3), "| test:", round(m.score(Xte, yte), 3))\nprint("brecha =", round(m.score(Xtr, ytr) - m.score(Xte, yte), 3))',
            },
            {
                "title": "La regularización reduce la brecha",
                "explain": "La misma red grande, pero con alpha alto: train baja un poco y la brecha con test se reduce.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=7)\n\nfor a in [1e-6, 0.1, 1.0]:\n    m = make_pipeline(StandardScaler(),\n                      MLPClassifier((128, 64), alpha=a, max_iter=1500, random_state=7)).fit(Xtr, ytr)\n    print(f"alpha={a:<7} brecha train-test = {m.score(Xtr,ytr)-m.score(Xte,yte):.3f}")',
            },
            {
                "title": "Curva de aprendizaje (más datos ayudan)",
                "explain": "Entrenamos con fracciones crecientes de datos y vemos cómo mejora el test.",
                "code": 'import numpy as np, pandas as pd, matplotlib.pyplot as plt\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=7)\ntam = [30, 60, 100, len(Xtr)]; test = []\nfor n in tam:\n    m = make_pipeline(StandardScaler(), MLPClassifier((16,8), max_iter=600, random_state=7))\n    m.fit(Xtr[:n], ytr[:n]); test.append(m.score(Xte, yte))\nplt.plot(tam, test, "o-"); plt.xlabel("nº de ejemplos de entrenamiento")\nplt.ylabel("exactitud en test"); plt.title("Curva de aprendizaje"); plt.show()',
            },
            {
                "title": "Early stopping",
                "explain": "Con early_stopping la red separa validación y para sola cuando deja de mejorar.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=7)\n\nm = make_pipeline(StandardScaler(),\n                  MLPClassifier((32, 16), early_stopping=True, max_iter=1000, random_state=7))\nm.fit(Xtr, ytr)\nprint("test:", round(m.score(Xte, yte), 3))\nprint("epocas realmente usadas:", m.named_steps["mlpclassifier"].n_iter_)',
            },
            {
                "title": "¿Cuántos parámetros tiene una red?",
                "explain": "Contamos los pesos (y sesgos) de distintas arquitecturas: crecen rápido con el tamaño.",
                "code": 'def parametros(entradas, capas, salidas):\n    tam = [entradas] + list(capas) + [salidas]\n    total = 0\n    for i in range(len(tam) - 1):\n        total += tam[i] * tam[i+1] + tam[i+1]   # pesos + sesgos\n    return total\n\nprint("MLP 7-16-8-1 :", parametros(7, (16, 8), 1), "parametros")\nprint("MLP 7-128-64-1:", parametros(7, (128, 64), 1), "parametros")\nprint("-> mas parametros = mas capacidad, pero mas riesgo de sobreajuste")',
            },
        ],
        "dataset": "clientes, viviendas",
        "exercises": [
            "Entrena una red grande sin regularización y mide la brecha train–test en <code>clientes</code>.",
            "Sube <code>alpha</code> y muestra cómo baja esa brecha.",
            "Reduce el tamaño de la red y compara con la red grande.",
            "Dibuja una curva de aprendizaje variando el número de ejemplos de entrenamiento.",
            "Activa <code>early_stopping</code> y reporta cuántas épocas usó (<code>n_iter_</code>).",
            "Cuenta los parámetros de un MLP 10-64-32-1.",
            "Usa validación cruzada (módulo H) para elegir la mejor <code>alpha</code>.",
            "Compara el sobreajuste de una red vs. un Random Forest en los mismos datos.",
            "Investiga y escribe en comentarios 3 diferencias entre una CNN y un MLP.",
            "Explica en un comentario qué significa que un modelo «generaliza» bien.",
        ],
    },
]
