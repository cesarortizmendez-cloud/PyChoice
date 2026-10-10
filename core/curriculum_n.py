# -*- coding: utf-8 -*-
"""
PyChoice - Ruta "Ingeniero de IA con Python".
Modulo N - IA moderna aplicada (lecciones 55-58):
aprendizaje por refuerzo, NLP clasico, recomendadores y
metaheuristicas para ML + IA responsable.

Todo corre en el navegador (numpy; sklearn se autocarga al usarse).
Datasets del motor: clientes, estudiantes.
"""

CHAPTERS_N = [

    # ============================================================ CAP 55
    {
        "num": 55,
        "slug": "aprendizaje-refuerzo",
        "code": "leccion_55",
        "title": "Aprendizaje por refuerzo básico (Q-learning)",
        "subtitle": "Un agente que aprende a decidir probando y recibiendo recompensas",
        "apunte": "Módulo N · Lección 1 - Aprendizaje por refuerzo",
        "concepts": [
            ("Aprendizaje por refuerzo (RL)", "Un <b>agente</b> aprende a actuar en un <b>entorno</b> probando acciones y recibiendo <b>recompensas</b>, sin que nadie le dé las respuestas correctas."),
            ("Agente y entorno", "El <b>agente</b> decide y actúa; el <b>entorno</b> responde con un nuevo estado y una recompensa. Interactúan en un ciclo."),
            ("Estado y acción", "El <b>estado</b> describe la situación actual; la <b>acción</b> es lo que el agente elige hacer en ese estado."),
            ("Recompensa", "La señal numérica que le dice al agente qué tan buena fue su acción. El objetivo es <b>maximizar la recompensa total</b>."),
            ("Política", "La <b>estrategia</b> del agente: qué acción tomar en cada estado. Aprender es mejorar la política."),
            ("Valor Q", "<code>Q(s, a)</code> estima la <b>recompensa futura</b> esperada de tomar la acción <code>a</code> en el estado <code>s</code>. El agente aprende estos valores."),
            ("Exploración vs. explotación", "Equilibrio entre <b>probar</b> acciones nuevas (explorar) y <b>usar</b> lo que ya se sabe que funciona (explotar). Se maneja con <b>ε-greedy</b>."),
            ("Factor de descuento (γ)", "Cuánto valora el agente las recompensas <b>futuras</b> frente a las inmediatas (0 = cortoplacista, cercano a 1 = previsor)."),
        ],
        "theory": """
<p><b>Aprender actuando.</b> El <b>aprendizaje por refuerzo</b> es distinto de todo lo anterior: no hay
un conjunto de datos con respuestas. Un <b>agente</b> está en un <b>entorno</b>, toma <b>acciones</b>,
y el entorno le devuelve un nuevo <b>estado</b> y una <b>recompensa</b>. A fuerza de prueba y error, el
agente descubre qué conviene hacer. Es como aprende un niño a andar en bici, o una IA a jugar.</p>

<p><b>El objetivo: maximizar la recompensa total.</b> El agente no busca acertar una etiqueta, sino
<b>acumular la mayor recompensa</b> a lo largo del tiempo. Eso lo obliga a pensar en el futuro: a veces
conviene una recompensa pequeña ahora para lograr una grande después. El <b>factor de descuento</b> γ
regula cuánto pesa el futuro.</p>

<p><b>El bandido multibrazo.</b> El caso más simple: varias «máquinas tragamonedas», cada una con una
recompensa media desconocida. El agente debe <b>descubrir cuál es la mejor</b> jugando. Aquí aparece el
dilema central del RL: <b>explorar</b> (probar máquinas para aprender) vs. <b>explotar</b> (jugar la
que parece mejor). La estrategia <b>ε-greedy</b> lo resuelve: con probabilidad ε explora al azar, y el
resto del tiempo explota la mejor conocida.</p>

<p><b>Valores Q y la ecuación de aprendizaje.</b> Para problemas con <b>estados</b>, el agente aprende
una tabla <b>Q(s, a)</b>: cuánta recompensa futura espera por tomar la acción <code>a</code> en el
estado <code>s</code>. La regla de <b>Q-learning</b> la actualiza con cada experiencia:
<code>Q(s,a) ← Q(s,a) + α·[r + γ·max Q(s',·) − Q(s,a)]</code>. En palabras: ajusta la estimación hacia
la recompensa recibida más lo mejor que se puede lograr desde el estado siguiente.</p>

<p><b>Un mundo de cuadrícula (gridworld).</b> El ejemplo clásico: una grilla donde el agente se mueve
(arriba, abajo, izquierda, derecha) buscando una meta con recompensa, evitando castigos. Con
Q-learning, tras muchos <b>episodios</b>, la tabla Q revela la <b>mejor ruta</b> a la meta: el agente
aprendió una política óptima sin que nadie se la enseñara.</p>

<p><b>Por qué importa.</b> El RL está detrás de logros famosos (juegos, robótica, control) y se combina
hoy con redes neuronales (deep RL). Aquí lo vemos en su forma <b>tabular</b> con numpy, que es la mejor
manera de entender la idea antes de escalarla. Es, de nuevo, optimización: maximizar recompensa
ajustando una política.</p>
""",
        "examples": [
            {
                "title": "El bandido multibrazo (ε-greedy)",
                "explain": "Tres máquinas con recompensa media desconocida. El agente las descubre explorando y explotando.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\nmedias = [0.2, 0.5, 0.8]        # desconocidas para el agente\nQ = np.zeros(3); conteo = np.zeros(3); eps = 0.1\n\nfor t in range(1000):\n    a = rng.integers(3) if rng.random() < eps else int(Q.argmax())\n    r = 1.0 if rng.random() < medias[a] else 0.0   # recompensa 0/1\n    conteo[a] += 1\n    Q[a] += (r - Q[a]) / conteo[a]                 # media incremental\nprint("Q estimada:", np.round(Q, 3))\nprint("mejor brazo segun el agente:", int(Q.argmax()), "| real:", int(np.argmax(medias)))',
            },
            {
                "title": "Definir un gridworld",
                "explain": "Una fila de 6 casillas: el agente parte en 0 y la meta (recompensa 1) está en la 5.",
                "code": 'import numpy as np\nN = 6                      # casillas 0..5, meta en 5\nacciones = [-1, +1]        # izquierda, derecha\n\ndef paso(s, a):\n    s2 = min(max(s + acciones[a], 0), N - 1)\n    r = 1.0 if s2 == N - 1 else 0.0\n    fin = (s2 == N - 1)\n    return s2, r, fin\n\nprint("desde s=3, accion derecha ->", paso(3, 1))\nprint("desde s=4, accion derecha ->", paso(4, 1))',
            },
            {
                "title": "Una actualización de Q (Bellman)",
                "explain": "La regla de Q-learning ajusta Q(s,a) hacia la recompensa más el mejor valor del estado siguiente.",
                "code": 'import numpy as np\nQ = np.zeros((6, 2)); alpha, gamma = 0.5, 0.9\ns, a, r, s2 = 4, 1, 1.0, 5      # transicion que llega a la meta\n\nQ[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])\nprint("Q tras una actualizacion:\\n", np.round(Q, 2))',
            },
            {
                "title": "Q-learning completo en el gridworld",
                "explain": "Tras varios episodios, el agente aprende que conviene ir siempre a la derecha hacia la meta.",
                "code": 'import numpy as np\nrng = np.random.default_rng(7)\nN = 6; acciones = [-1, +1]\ndef paso(s, a):\n    s2 = min(max(s + acciones[a], 0), N - 1)\n    return s2, (1.0 if s2 == N-1 else 0.0), (s2 == N-1)\n\nQ = np.zeros((N, 2)); alpha, gamma, eps = 0.5, 0.9, 0.2\nfor ep in range(300):\n    s = 0; fin = False\n    while not fin:\n        a = rng.integers(2) if rng.random() < eps else int(Q[s].argmax())\n        s2, r, fin = paso(s, a)\n        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])\n        s = s2\npolitica = ["derecha" if Q[s].argmax() == 1 else "izquierda" for s in range(N)]\nprint("politica aprendida por casilla:", politica[:5])',
            },
            {
                "title": "Curva de aprendizaje (pasos hasta la meta)",
                "explain": "A medida que aprende, el agente llega a la meta en menos pasos por episodio.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nrng = np.random.default_rng(7)\nN = 6; acciones = [-1, +1]\ndef paso(s, a):\n    s2 = min(max(s + acciones[a], 0), N - 1)\n    return s2, (1.0 if s2 == N-1 else 0.0), (s2 == N-1)\n\nQ = np.zeros((N, 2)); alpha, gamma, eps = 0.5, 0.9, 0.2; largos = []\nfor ep in range(200):\n    s = 0; fin = False; pasos = 0\n    while not fin and pasos < 100:\n        a = rng.integers(2) if rng.random() < eps else int(Q[s].argmax())\n        s2, r, fin = paso(s, a)\n        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])\n        s = s2; pasos += 1\n    largos.append(pasos)\nplt.plot(largos); plt.xlabel("episodio"); plt.ylabel("pasos hasta la meta")\nplt.title("El agente aprende a llegar mas rapido"); plt.show()',
            },
        ],
        "dataset": "entorno generado (bandido / gridworld)",
        "exercises": [
            "Programa un bandido de 4 brazos con medias a tu elección y encuentra el mejor con ε-greedy.",
            "Prueba ε = 0.0, 0.1 y 0.5 en el bandido: ¿cómo cambia lo que aprende?",
            "Define un gridworld de 8 casillas y prueba la función <code>paso</code>.",
            "Aplica una actualización de Q a mano para una transición que elijas.",
            "Entrena Q-learning en tu gridworld y muestra la política aprendida.",
            "Grafica los pasos por episodio y observa cómo bajan.",
            "Cambia el factor de descuento γ (0.5 y 0.99) y compara.",
            "Agrega un castigo (recompensa −1) en una casilla y vuelve a entrenar.",
            "Reduce ε con el tiempo (más exploración al inicio) y compara.",
            "Explica en un comentario el dilema exploración vs. explotación.",
        ],
    },

    # ============================================================ CAP 56
    {
        "num": 56,
        "slug": "nlp-clasico",
        "code": "leccion_56",
        "title": "NLP clásico: convertir texto en números",
        "subtitle": "Bolsa de palabras, TF-IDF y clasificación de texto con scikit-learn",
        "apunte": "Módulo N · Lección 2 - NLP clásico",
        "concepts": [
            ("Procesamiento de lenguaje (NLP)", "Hacer que la computadora <b>trabaje con texto</b>: clasificarlo, buscar, analizar sentimiento. El primer reto es convertir palabras en <b>números</b>."),
            ("Tokenización", "Partir el texto en <b>unidades</b> (palabras o tokens). Es el primer paso de casi todo NLP."),
            ("Bolsa de palabras (BoW)", "Representar un texto por <b>cuántas veces</b> aparece cada palabra, ignorando el orden. Simple y sorprendentemente útil."),
            ("TF-IDF", "Pondera cada palabra por su frecuencia en el documento (TF) y su <b>rareza</b> en el conjunto (IDF). Resalta las palabras <b>distintivas</b>."),
            ("Vectorización", "Convertir cada texto en un <b>vector</b> de números para poder aplicarle un modelo de ML."),
            ("Stopwords", "Palabras muy comunes (el, la, de, que…) que aportan poco y a menudo se <b>eliminan</b>."),
            ("Clasificación de texto", "Entrenar un modelo para asignar una <b>categoría</b> a un texto (spam/no spam, positivo/negativo)."),
            ("Análisis de sentimiento", "Caso típico: decidir si un texto expresa una opinión <b>positiva o negativa</b>."),
        ],
        "theory": """
<p><b>El puente entre texto y modelos.</b> Los modelos de machine learning solo entienden
<b>números</b>. El NLP clásico resuelve esto convirtiendo cada texto en un <b>vector numérico</b>, y
luego aplica los mismos clasificadores que ya conoces. Aunque hoy dominan los grandes modelos de
lenguaje, estas técnicas siguen siendo rápidas, interpretables y muy usadas.</p>

<p><b>Bolsa de palabras.</b> La idea más simple: listar todas las palabras del vocabulario y
representar cada texto por <b>cuántas veces</b> aparece cada una. Se pierde el orden, pero se conserva
<b>de qué trata</b>. En scikit-learn lo hace <code>CountVectorizer</code>: convierte una lista de
frases en una matriz donde cada fila es un texto y cada columna una palabra.</p>

<p><b>El problema de las palabras comunes.</b> En bolsa de palabras, «el» o «de» aparecen muchísimo
pero no dicen nada del tema. Las <b>stopwords</b> se pueden eliminar, pero hay una idea mejor:
<b>pesar</b> cada palabra según lo informativa que sea.</p>

<p><b>TF-IDF: resaltar lo distintivo.</b> <b>TF-IDF</b> multiplica dos factores. <b>TF</b> (frecuencia
del término) sube con lo repetida que está la palabra en el documento. <b>IDF</b> (frecuencia inversa
de documento) sube con lo <b>rara</b> que es en el conjunto: una palabra que aparece en todos los
textos pesa poco; una que aparece solo en algunos, mucho. Así, TF-IDF da más peso a las palabras que
<b>caracterizan</b> cada texto. <code>TfidfVectorizer</code> lo calcula en una línea.</p>

<p><b>Clasificar texto.</b> Con los textos ya vectorizados, aplicamos un clasificador —una
<b>regresión logística</b> funciona muy bien—. El ejemplo clásico es el <b>análisis de sentimiento</b>:
entrenar con frases etiquetadas como positivas o negativas, y luego predecir el sentimiento de una
frase nueva. También spam, categorización de noticias, etc.</p>

<p><b>Interpretabilidad.</b> Una ventaja enorme de este enfoque: es <b>transparente</b>. Mirando los
coeficientes del modelo podemos ver <b>qué palabras</b> empujan hacia «positivo» y cuáles hacia
«negativo». Esa claridad —saber por qué el modelo decide— es cada vez más valiosa, y conecta con la IA
responsable de la próxima lección.</p>
""",
        "examples": [
            {
                "title": "Bolsa de palabras con CountVectorizer",
                "explain": "Convierte frases en una matriz de conteos: cada columna es una palabra del vocabulario.",
                "code": 'from sklearn.feature_extraction.text import CountVectorizer\ntextos = ["el curso es bueno", "el curso es malo", "muy buen curso"]\nvec = CountVectorizer()\nX = vec.fit_transform(textos)\nprint("vocabulario:", vec.get_feature_names_out())\nprint("matriz de conteos:\\n", X.toarray())',
            },
            {
                "title": "TF-IDF: pesar las palabras",
                "explain": "TfidfVectorizer da más peso a las palabras distintivas y menos a las muy comunes.",
                "code": 'from sklearn.feature_extraction.text import TfidfVectorizer\ntextos = ["el curso es bueno", "el curso es malo", "muy buen curso"]\nvec = TfidfVectorizer()\nX = vec.fit_transform(textos)\nimport numpy as np\nprint("vocabulario:", vec.get_feature_names_out())\nprint("pesos TF-IDF (redondeados):\\n", np.round(X.toarray(), 2))',
            },
            {
                "title": "Análisis de sentimiento",
                "explain": "Entrenamos un clasificador con frases positivas y negativas, y predecimos una frase nueva.",
                "code": 'from sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.pipeline import make_pipeline\n\ntextos = ["excelente producto", "muy buena calidad", "me encanta",\n          "lo recomiendo", "pesimo servicio", "muy mala calidad",\n          "no lo recomiendo", "una perdida de dinero"]\ny = [1, 1, 1, 1, 0, 0, 0, 0]       # 1 = positivo, 0 = negativo\n\nmodelo = make_pipeline(TfidfVectorizer(), LogisticRegression())\nmodelo.fit(textos, y)\nfor frase in ["buena calidad", "pesimo producto"]:\n    print(frase, "->", "positivo" if modelo.predict([frase])[0] == 1 else "negativo")',
            },
            {
                "title": "¿Qué palabras pesan más?",
                "explain": "Los coeficientes del modelo revelan qué palabras empujan hacia positivo o negativo.",
                "code": 'import numpy as np\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\n\ntextos = ["excelente producto", "muy buena calidad", "me encanta", "lo recomiendo",\n          "pesimo servicio", "muy mala calidad", "no lo recomiendo", "perdida de dinero"]\ny = [1,1,1,1,0,0,0,0]\nvec = TfidfVectorizer(); X = vec.fit_transform(textos)\nclf = LogisticRegression().fit(X, y)\npalabras = vec.get_feature_names_out(); coef = clf.coef_[0]\norden = np.argsort(coef)\nprint("mas negativas:", [palabras[i] for i in orden[:3]])\nprint("mas positivas:", [palabras[i] for i in orden[-3:]])',
            },
            {
                "title": "Similitud entre textos",
                "explain": "Con TF-IDF y similitud coseno medimos qué tan parecidos son dos textos (base de los buscadores).",
                "code": 'from sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.metrics.pairwise import cosine_similarity\ntextos = ["el gato duerme en el sofa", "un gato descansa en el sillon",\n          "el equipo gano el partido"]\nX = TfidfVectorizer().fit_transform(textos)\nS = cosine_similarity(X)\nimport numpy as np\nprint("similitud texto 0 vs 1:", round(S[0, 1], 3), "(parecidos)")\nprint("similitud texto 0 vs 2:", round(S[0, 2], 3), "(distintos)")',
            },
        ],
        "dataset": "corpus de texto (en el código)",
        "exercises": [
            "Usa <code>CountVectorizer</code> sobre 4 frases tuyas y muestra el vocabulario y la matriz.",
            "Repite con <code>TfidfVectorizer</code> y compara los pesos.",
            "Elimina stopwords con <code>TfidfVectorizer(stop_words=[...])</code> y observa el cambio.",
            "Arma un pequeño corpus de sentimiento (6+ frases) y entrena un clasificador.",
            "Predice el sentimiento de 3 frases nuevas.",
            "Muestra las 3 palabras más positivas y 3 más negativas según el modelo.",
            "Calcula la similitud coseno entre dos textos parecidos y dos distintos.",
            "Agrega bigramas con <code>ngram_range=(1,2)</code> y compara el vocabulario.",
            "Compara LogisticRegression con <code>MultinomialNB</code> (Naive Bayes) en tu corpus.",
            "Explica en un comentario qué hace el factor IDF de TF-IDF.",
        ],
    },

    # ============================================================ CAP 57
    {
        "num": 57,
        "slug": "sistemas-recomendacion",
        "code": "leccion_57",
        "title": "Sistemas de recomendación",
        "subtitle": "Filtrado colaborativo: recomendar según usuarios o ítems parecidos",
        "apunte": "Módulo N · Lección 3 - Recomendadores",
        "concepts": [
            ("Sistema de recomendación", "Modelo que sugiere <b>ítems</b> (productos, películas) a un usuario según sus gustos y los de otros. Motor de Netflix, Amazon, Spotify."),
            ("Matriz usuario-ítem", "Tabla de <b>valoraciones</b>: filas = usuarios, columnas = ítems. Suele estar <b>incompleta</b> (nadie valora todo)."),
            ("Filtrado colaborativo", "Recomendar usando el comportamiento de <b>muchos usuarios</b>: «a quienes se parecen a ti les gustó esto»."),
            ("Similitud coseno", "Mide qué tan <b>parecidos</b> son dos usuarios (o ítems) según el ángulo entre sus vectores de valoraciones."),
            ("Enfoque usuario / ítem", "<b>User-based</b>: usuarios parecidos al objetivo. <b>Item-based</b>: ítems parecidos a los que ya le gustaron."),
            ("Predicción de valoración", "Estimar qué nota le pondría un usuario a un ítem que <b>aún no ha valorado</b>."),
            ("Top-N", "La lista de las <b>N mejores</b> recomendaciones para un usuario."),
            ("Cold start", "El problema de recomendar a un usuario (o ítem) <b>nuevo</b>, del que no hay datos."),
        ],
        "theory": """
<p><b>Ayudar a elegir.</b> Un <b>sistema de recomendación</b> sugiere qué podría gustarte entre miles
de opciones. Está en todas partes: las películas que Netflix te propone, los productos de Amazon, las
canciones de Spotify. La idea central del enfoque más popular es sorprendentemente simple y muy acorde
al espíritu de PyChoice: <b>decidir con datos</b> de mucha gente.</p>

<p><b>La matriz usuario-ítem.</b> Todo parte de una tabla de <b>valoraciones</b>: cada fila es un
usuario, cada columna un ítem, y las celdas son las notas que cada usuario dio (de 1 a 5, por
ejemplo). La característica clave es que está <b>casi vacía</b>: nadie valora todo. Recomendar es, en
el fondo, <b>rellenar los huecos</b>: predecir las valoraciones que faltan y sugerir las más altas.</p>

<p><b>Filtrado colaborativo.</b> El método estrella no mira el <b>contenido</b> de los ítems, sino el
<b>comportamiento</b> de los usuarios: «personas con gustos parecidos a los tuyos disfrutaron esto, así
que probablemente a ti también». Se llama <b>colaborativo</b> porque aprovecha la sabiduría de toda la
comunidad de usuarios.</p>

<p><b>Medir parecido: similitud coseno.</b> ¿Cómo sabemos si dos usuarios se parecen? Representamos a
cada uno por su <b>vector de valoraciones</b> y medimos la <b>similitud coseno</b>: el coseno del
ángulo entre ambos vectores. Vale 1 si tienen gustos idénticos y baja a medida que difieren. Con
scikit-learn es <code>cosine_similarity</code>.</p>

<p><b>Usuario vs. ítem.</b> Hay dos enfoques simétricos. El <b>user-based</b> busca los usuarios más
parecidos al objetivo y recomienda lo que a ellos les gustó. El <b>item-based</b> busca ítems
parecidos a los que el usuario ya valoró bien. El item-based suele ser más estable (los gustos por un
ítem cambian menos que los usuarios).</p>

<p><b>Predicción y top-N.</b> Para un ítem que el usuario no ha visto, estimamos su valoración como un
<b>promedio ponderado</b> de lo que dieron los usuarios similares. Ordenando esas predicciones de mayor
a menor, obtenemos el <b>top-N</b> de recomendaciones. Un reto conocido es el <b>cold start</b>:
recomendar a alguien <b>nuevo</b>, sin historial, donde el filtrado colaborativo aún no tiene de dónde
agarrarse.</p>
""",
        "examples": [
            {
                "title": "La matriz usuario-ítem",
                "explain": "Filas = usuarios, columnas = películas. Un 0 significa «no valorada».",
                "code": 'import numpy as np, pandas as pd\nR = pd.DataFrame(\n    [[5, 4, 0, 1],\n     [4, 5, 1, 0],\n     [1, 0, 5, 4],\n     [0, 1, 4, 5]],\n    index=["Ana", "Beto", "Caro", "Dani"],\n    columns=["Accion", "Aventura", "Drama", "Romance"])\nprint(R)',
            },
            {
                "title": "Similitud entre usuarios (coseno)",
                "explain": "Medimos qué tan parecidos son los usuarios según sus valoraciones.",
                "code": 'import numpy as np, pandas as pd\nfrom sklearn.metrics.pairwise import cosine_similarity\nR = np.array([[5,4,0,1],[4,5,1,0],[1,0,5,4],[0,1,4,5]])\nusuarios = ["Ana","Beto","Caro","Dani"]\nS = cosine_similarity(R)\nprint(pd.DataFrame(np.round(S, 2), index=usuarios, columns=usuarios))',
            },
            {
                "title": "Recomendación user-based",
                "explain": "Para una película no vista por Ana, predecimos su nota con las valoraciones de usuarios similares.",
                "code": 'import numpy as np\nfrom sklearn.metrics.pairwise import cosine_similarity\nR = np.array([[5,4,0,1],[4,5,1,0],[1,0,5,4],[0,1,4,5]], dtype=float)\nS = cosine_similarity(R)\n\nu = 0            # Ana ; item 2 (Drama) no lo valoro (=0)\nitem = 2\nsimil = S[u].copy(); simil[u] = 0\nvaloraron = R[:, item] > 0\npred = np.dot(simil[valoraron], R[valoraron, item]) / simil[valoraron].sum()\nprint("prediccion de nota de Ana para Drama:", round(pred, 2))',
            },
            {
                "title": "Similitud entre ítems (item-based)",
                "explain": "Transponiendo la matriz medimos qué ítems se parecen entre sí.",
                "code": 'import numpy as np, pandas as pd\nfrom sklearn.metrics.pairwise import cosine_similarity\nR = np.array([[5,4,0,1],[4,5,1,0],[1,0,5,4],[0,1,4,5]], dtype=float)\nitems = ["Accion","Aventura","Drama","Romance"]\nSitem = cosine_similarity(R.T)\nprint(pd.DataFrame(np.round(Sitem, 2), index=items, columns=items))',
            },
            {
                "title": "Top-N recomendaciones para un usuario",
                "explain": "Predecimos todas las películas no vistas por Caro y le recomendamos las mejores.",
                "code": 'import numpy as np\nfrom sklearn.metrics.pairwise import cosine_similarity\nR = np.array([[5,4,0,1],[4,5,1,0],[1,0,5,4],[0,1,4,5]], dtype=float)\nitems = ["Accion","Aventura","Drama","Romance"]\nS = cosine_similarity(R)\n\nu = 2            # Caro\nsimil = S[u].copy(); simil[u] = 0\npreds = {}\nfor item in range(R.shape[1]):\n    if R[u, item] == 0:                       # no vista\n        quien = R[:, item] > 0\n        preds[items[item]] = np.dot(simil[quien], R[quien, item]) / simil[quien].sum()\nrank = sorted(preds.items(), key=lambda x: -x[1])\nprint("recomendaciones para Caro:", [(n, round(v, 2)) for n, v in rank])',
            },
        ],
        "dataset": "valoraciones (en el código)",
        "exercises": [
            "Crea una matriz usuario-ítem de 5 usuarios y 4 ítems con algunas valoraciones en 0.",
            "Calcula la similitud coseno entre todos los usuarios.",
            "Encuentra los 2 usuarios más parecidos a uno dado.",
            "Predice la valoración de un ítem no visto para un usuario (user-based).",
            "Calcula la similitud entre ítems (item-based).",
            "Genera el top-N de recomendaciones para un usuario.",
            "Compara la recomendación user-based con la item-based para el mismo caso.",
            "Agrega un usuario nuevo con solo una valoración (cold start) y comenta la dificultad.",
            "Normaliza restando la media de cada usuario antes de calcular similitud y compara.",
            "Explica en un comentario qué es el filtrado colaborativo en una frase.",
        ],
    },

    # ============================================================ CAP 58
    {
        "num": 58,
        "slug": "metaheuristicas-ml-etica",
        "code": "leccion_58",
        "title": "Metaheurísticas para ML e IA responsable",
        "subtitle": "Optimizar hiperparámetros y mirar los modelos con ojo crítico",
        "apunte": "Módulo N · Lección 4 - Hiperparámetros y ética",
        "concepts": [
            ("Hiperparámetros", "Los ajustes que <b>no</b> se aprenden solos (profundidad de un árbol, nº de neuronas, alpha). Hay que <b>buscarlos</b>."),
            ("Búsqueda en malla (grid)", "Probar <b>todas</b> las combinaciones de una rejilla de valores. Exhaustiva pero cara."),
            ("Búsqueda aleatoria", "Probar combinaciones <b>al azar</b>. Suele hallar buenos valores con menos pruebas que la malla."),
            ("Metaheurística para hiperparámetros", "Usar un <b>algoritmo genético</b> (u otro) para buscar hiperparámetros: une los módulos L y M/H."),
            ("Sesgo en los datos", "Si los datos reflejan desigualdades, el modelo las <b>aprende y amplifica</b>. Un modelo no es neutral por ser matemático."),
            ("Equidad (fairness)", "Que el modelo no <b>perjudique sistemáticamente</b> a un grupo. Se revisa comparando su desempeño por grupos."),
            ("Interpretabilidad", "Poder <b>explicar</b> por qué el modelo decidió algo (importancia de variables, coeficientes). Clave para confiar y auditar."),
            ("IA responsable", "Diseñar y usar modelos considerando su <b>impacto</b>: sesgos, transparencia, privacidad y consecuencias."),
        ],
        "theory": """
<p><b>Dos cierres en una lección.</b> Esta lección une los hilos de la ruta. Primero, lo técnico: cómo
<b>buscar los mejores hiperparámetros</b> de un modelo usando lo aprendido en optimización y
metaheurísticas. Segundo, lo humano: cómo mirar un modelo con <b>ojo crítico</b>, porque un buen
ingeniero de IA no solo construye modelos que funcionan, sino que entiende sus <b>límites y su
impacto</b>.</p>

<p><b>El problema de los hiperparámetros.</b> Un modelo tiene parámetros que <b>aprende</b> (los pesos)
y <b>hiperparámetros</b> que hay que <b>fijar antes</b>: la profundidad de un árbol, el nº de neuronas,
la regularización. La calidad del modelo depende mucho de ellos, y no hay fórmula: hay que
<b>buscarlos</b>. Esto es, otra vez, un problema de optimización —el gran tema de la ruta—.</p>

<p><b>Tres formas de buscar.</b> La <b>búsqueda en malla</b> prueba todas las combinaciones de una
rejilla: exhaustiva pero cara si hay muchos hiperparámetros. La <b>búsqueda aleatoria</b> prueba
combinaciones al azar y, curiosamente, suele encontrar buenos valores con <b>menos</b> pruebas. Y,
cerrando el círculo con el módulo L, se puede usar un <b>algoritmo genético</b> que evoluciona
combinaciones de hiperparámetros tratándolas como individuos cuyo fitness es el desempeño del modelo.</p>

<p><b>Los modelos no son neutrales.</b> Aquí cambia el tono. Un modelo aprende de datos, y <b>los datos
reflejan el mundo</b>, con sus desigualdades. Si históricamente un grupo fue tratado distinto, el
modelo <b>aprenderá y perpetuará</b> ese patrón —a veces amplificándolo—. Que una decisión venga de una
fórmula no la hace justa ni objetiva. Este es uno de los puntos más importantes de toda la ruta.</p>

<p><b>Revisar sesgo y equidad.</b> Una práctica básica de <b>IA responsable</b> es <b>medir el
desempeño por grupos</b>: ¿el modelo acierta igual para hombres y mujeres, para distintas regiones o
edades? Grandes diferencias son una señal de alarma. La <b>equidad</b> (fairness) busca que el modelo
no perjudique sistemáticamente a ningún grupo, y exige mirar más allá de la exactitud global.</p>

<p><b>Interpretabilidad y responsabilidad.</b> Poder <b>explicar</b> por qué un modelo decidió algo
—con la importancia de variables o los coeficientes— es esencial para <b>confiar</b> en él, auditarlo y
corregirlo. Un ingeniero de IA responsable se pregunta no solo «¿funciona?», sino «¿a quién afecta?,
¿puedo explicarlo?, ¿qué pasa si se equivoca?». Con eso cierras la parte aplicada de la ruta; lo que
queda es integrarlo todo en un proyecto.</p>
""",
        "examples": [
            {
                "title": "Búsqueda en malla de un hiperparámetro",
                "explain": "Probamos varias profundidades de un árbol y nos quedamos con la mejor en validación.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nfor d in [2, 3, 5, 8, 12]:\n    m = DecisionTreeClassifier(max_depth=d, random_state=7).fit(Xtr, ytr)\n    print(f"max_depth={d:>2} -> exactitud test {m.score(Xte, yte):.3f}")',
            },
            {
                "title": "Búsqueda aleatoria de hiperparámetros",
                "explain": "Probamos combinaciones al azar de dos hiperparámetros; a menudo basta con pocas pruebas.",
                "code": 'import numpy as np, pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\nrng = np.random.default_rng(7)\n\nmejor = (0, None)\nfor _ in range(8):\n    n = int(rng.integers(20, 200)); d = int(rng.integers(2, 10))\n    s = RandomForestClassifier(n_estimators=n, max_depth=d, random_state=7).fit(Xtr, ytr).score(Xte, yte)\n    if s > mejor[0]: mejor = (s, (n, d))\nprint("mejor exactitud:", round(mejor[0], 3), "| (n_estimators, max_depth) =", mejor[1])',
            },
            {
                "title": "Un genético para hiperparámetros",
                "explain": "Cada individuo es una combinación (profundidad). El fitness es el desempeño; evolucionamos hacia la mejor.",
                "code": 'import numpy as np, pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\nrng = np.random.default_rng(7)\n\ndef fitness(d):\n    return DecisionTreeClassifier(max_depth=int(d), random_state=7).fit(Xtr, ytr).score(Xte, yte)\n\npob = rng.integers(2, 15, 6)                 # 6 profundidades al azar\nfor gen in range(5):\n    pob = sorted(pob, key=fitness, reverse=True)\n    padres = pob[:2]                         # elitismo\n    hijos = [max(2, int((padres[0] + padres[1]) / 2 + rng.integers(-2, 3))) for _ in range(4)]\n    pob = list(padres) + hijos\nmejor = max(pob, key=fitness)\nprint("mejor max_depth:", int(mejor), "| exactitud:", round(fitness(mejor), 3))',
            },
            {
                "title": "Detectar sesgo: desempeño por grupo",
                "explain": "Comparamos la exactitud del modelo entre grupos (género). Diferencias grandes son una alerta de equidad.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\n\nd = estudiantes.copy()\nX = pd.get_dummies(d.drop(columns=["aprobado"]), drop_first=True)\ny = d["aprobado"]\nXtr, Xte, ytr, yte, gtr, gte = train_test_split(X, y, d["genero"], test_size=0.3, random_state=7)\nmodelo = RandomForestClassifier(random_state=7).fit(Xtr, ytr)\n\nfor g in ["F", "M"]:\n    masc = (gte == g).values\n    print(f"genero {g}: exactitud {modelo.score(Xte[masc], yte[masc]):.3f}  (n={masc.sum()})")',
            },
            {
                "title": "Interpretabilidad: ¿en qué se fija el modelo?",
                "explain": "La importancia de variables explica las decisiones del modelo: base de la IA responsable.",
                "code": 'import pandas as pd\nfrom sklearn.ensemble import RandomForestClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nmodelo = RandomForestClassifier(random_state=7).fit(X, y)\nimp = pd.Series(modelo.feature_importances_, index=X.columns).sort_values(ascending=False)\nprint("variables mas influyentes en la prediccion de churn:")\nprint(imp.head(5).round(3))',
            },
        ],
        "dataset": "clientes, estudiantes",
        "exercises": [
            "Haz una búsqueda en malla de <code>max_depth</code> para un árbol en <code>clientes</code>.",
            "Haz una búsqueda aleatoria de dos hiperparámetros de un Random Forest.",
            "Usa un genético para optimizar <code>max_depth</code> y compáralo con la malla.",
            "Compara cuántas pruebas necesita la malla vs. la búsqueda aleatoria para un buen resultado.",
            "Mide la exactitud del modelo por género en <code>estudiantes</code>.",
            "Mide el desempeño por otra variable (p. ej. ciudad en <code>clientes</code>).",
            "Muestra las 5 variables más importantes del modelo de churn.",
            "Reflexiona en comentarios: ¿qué harías si el modelo acierta mucho menos en un grupo?",
            "Combina validación cruzada (módulo H) con la búsqueda de hiperparámetros.",
            "Escribe en comentarios 3 principios de IA responsable que te parezcan clave.",
        ],
    },
]
