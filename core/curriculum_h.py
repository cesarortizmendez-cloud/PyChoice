# -*- coding: utf-8 -*-
"""
PyChoice - Modulo H: Machine Learning (Lecciones 27 a 31).
Nivel profesional. scikit-learn se carga bajo demanda al importarlo.
Se usan datasets integrados (load_iris, load_diabetes, make_*) para que
cada ejemplo sea autonomo y reproducible.
"""

CHAPTERS_H = [

    # ============================================================ CAP 27
    {
        "num": 27,
        "slug": "que-es-ml",
        "code": "leccion_27",
        "title": "¿Qué es el Machine Learning?",
        "subtitle": "Aprender de los datos: el flujo de trabajo y la API de scikit-learn",
        "apunte": "Lección 27 - Introducción al ML",
        "concepts": [
            ("Machine Learning", "Programar computadores para que <b>aprendan patrones de los datos</b> en vez de seguir reglas escritas a mano."),
            ("Supervisado", "Se aprende de ejemplos <b>etiquetados</b> (X → y): regresión (números) y clasificación (categorías)."),
            ("No supervisado", "No hay etiquetas: se buscan estructuras ocultas, como grupos (clustering)."),
            ("Features (X)", "Las variables de entrada: las columnas con las que el modelo predice."),
            ("Target (y)", "La variable objetivo que se quiere predecir."),
            ("Modelo / estimador", "El algoritmo que aprende. En scikit-learn todos comparten la misma interfaz."),
            ("fit / predict", "<code>fit(X, y)</code> entrena; <code>predict(X)</code> predice. El patrón universal de scikit-learn."),
            ("Generalización", "Lo que importa: que el modelo acierte con datos <b>nuevos</b>, no solo con los de entrenamiento."),
        ],
        "theory": """
<p>El <b>Machine Learning</b> (aprendizaje automático) es una forma distinta de programar. En la
programación tradicional escribes <b>reglas</b> y el computador las aplica. En ML le das
<b>ejemplos</b> y el computador <b>aprende las reglas solo</b>. En lugar de escribir "si el correo
contiene estas palabras, es spam", le muestras miles de correos etiquetados como spam/no-spam y el
modelo descubre el patrón. Es el motor detrás de recomendaciones, detección de fraude, diagnóstico
médico asistido y mucho más.</p>

<p><b>Dos grandes familias.</b> En el aprendizaje <b>supervisado</b>, cada ejemplo trae una
<b>etiqueta</b> conocida (la respuesta correcta): se aprende la relación entre las <b>features</b>
(las entradas, que llamamos <code>X</code>) y el <b>target</b> (la salida, <code>y</code>). Si el
target es un número, es <b>regresión</b>; si es una categoría, es <b>clasificación</b>. En el
aprendizaje <b>no supervisado</b> no hay etiquetas: el objetivo es descubrir estructura, como agrupar
clientes parecidos (<b>clustering</b>).</p>

<p><b>La API de scikit-learn.</b> La gran ventaja de <b>scikit-learn</b> (la librería estándar de ML
en Python) es su consistencia: todos los modelos, por distintos que sean, se usan igual. Creas el
modelo, lo entrenas con <code>modelo.fit(X, y)</code> y predices con <code>modelo.predict(X_nuevo)</code>.
Aprender este patrón <b>fit/predict</b> una vez te sirve para cualquier algoritmo, desde una regresión
lineal hasta un bosque aleatorio.</p>

<p><b>Lo que de verdad importa: generalizar.</b> Un modelo no sirve por acertar con los datos que ya
vio, sino por acertar con datos <b>nuevos</b>. Un estudiante que memoriza las respuestas del ejercicio
no ha aprendido; uno que entiende el concepto, sí. Por eso, en las próximas lecciones, la evaluación
honesta (separar datos de prueba, medir bien) será tan importante como entrenar. En esta lección
darás tu primer modelo funcionando; en las siguientes, aprenderás a hacerlo bien.</p>
""",
        "examples": [
            {
                "title": "Tu primer modelo en 4 líneas",
                "explain": "El patrón fit/predict de scikit-learn con el dataset iris (clasificar flores).",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.neighbors import KNeighborsClassifier\niris = load_iris()\nmodelo = KNeighborsClassifier(n_neighbors=3)\nmodelo.fit(iris.data, iris.target)\nprint("clases:", list(iris.target_names))\npred = modelo.predict([iris.data[0]])\nprint("predicción de la 1ª flor:", iris.target_names[pred[0]])',
            },
            {
                "title": "Features (X) y target (y)",
                "explain": "Inspeccionamos las entradas y la salida del problema.",
                "code": 'from sklearn.datasets import load_iris\niris = load_iris()\nprint("X (features):", iris.data.shape, "->", iris.feature_names)\nprint("y (target):", iris.target.shape, "->", list(iris.target_names))\nprint("primera fila X:", iris.data[0], "| y:", iris.target[0])',
            },
            {
                "title": "Predecir un caso nuevo",
                "explain": "El valor del modelo: responder ante datos que no había visto.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.neighbors import KNeighborsClassifier\niris = load_iris()\nm = KNeighborsClassifier().fit(iris.data, iris.target)\nflor_nueva = [[5.1, 3.5, 1.4, 0.2]]\nprint("especie predicha:", iris.target_names[m.predict(flor_nueva)[0]])',
            },
            {
                "title": "Aprender = acertar",
                "explain": "Cuántos ejemplos clasifica bien un árbol sobre los datos que vio.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.tree import DecisionTreeClassifier\niris = load_iris()\nm = DecisionTreeClassifier(random_state=0).fit(iris.data, iris.target)\nprint("aciertos en entrenamiento:", round(m.score(iris.data, iris.target), 3))',
            },
            {
                "title": "No supervisado: descubrir grupos",
                "explain": "Sin usar las etiquetas, k-means encuentra 3 grupos por sí solo.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.cluster import KMeans\niris = load_iris()\nkm = KMeans(n_clusters=3, n_init=10, random_state=0).fit(iris.data)\nprint("grupos hallados (sin etiquetas):", km.labels_[:15])',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Carga <code>load_iris()</code> y muestra la forma de <code>X</code> y de <code>y</code>.",
            "Entrena un <code>KNeighborsClassifier</code> sobre iris y predice la última flor del dataset.",
            "Cambia <code>n_neighbors</code> a 1 y a 10 y observa si cambia la predicción.",
            "Predice la especie de una flor inventada por ti (4 medidas).",
            "Entrena un <code>DecisionTreeClassifier</code> y mira su <code>score()</code> en los datos.",
            "Explica en un comentario la diferencia entre aprendizaje supervisado y no supervisado.",
            "Identifica en iris cuáles serían las <code>features</code> y cuál el <code>target</code>.",
            "Usa <code>KMeans</code> con 2 grupos sobre iris y muestra las etiquetas.",
            "Investiga: imprime <code>iris.DESCR[:500]</code> para leer la descripción del dataset.",
        ],
    },

    # ============================================================ CAP 28
    {
        "num": 28,
        "slug": "preparar-datos-ml",
        "code": "leccion_28",
        "title": "Preparar los datos para el modelo",
        "subtitle": "Train/test split, escalado, variables categóricas y pipelines",
        "apunte": "Lección 28 - Preparación de datos",
        "concepts": [
            ("Train / test split", "Separar los datos en <b>entrenamiento</b> (aprender) y <b>prueba</b> (evaluar con datos no vistos)."),
            ("X_train / X_test", "Las particiones de entrada; <code>y_train</code>/<code>y_test</code>, las de salida."),
            ("Escalado", "Poner las variables en una escala comparable (<code>StandardScaler</code>: media 0, desviación 1)."),
            ("Ajustar solo con train", "El escalador y los transformadores se <b>ajustan con train</b> y se aplican a test."),
            ("Codificar categóricas", "Convertir texto en números que el modelo entienda (<code>get_dummies</code>, one-hot)."),
            ("Pipeline", "Encadena preparación + modelo en un solo objeto, evitando errores y fugas."),
            ("Fuga de datos (leakage)", "Usar información de test al preparar: infla el resultado y engaña. Hay que evitarla."),
            ("random_state", "Fija la aleatoriedad para que los resultados sean reproducibles."),
        ],
        "theory": """
<p>Antes de entrenar, los datos casi siempre necesitan <b>preparación</b>. Hacerla bien es la
diferencia entre un modelo confiable y uno que engaña. Esta lección cubre los pasos esenciales.</p>

<p><b>Separar train y test.</b> La regla de oro del ML: <b>nunca evalúes con los mismos datos que
usaste para entrenar</b>. Se reservan unos datos de <b>prueba</b> (típicamente 20–30%) que el modelo
no verá durante el entrenamiento, y se usan solo al final para medir cómo generaliza. Es como estudiar
con unos ejercicios y rendir la prueba con otros distintos. <code>train_test_split</code> lo hace en
una línea, y <code>random_state</code> asegura que la partición sea reproducible.</p>

<p><b>Escalar.</b> Muchos algoritmos (KNN, regresión logística, redes neuronales) son sensibles a la
<b>escala</b> de las variables: si una va de 0 a 1 y otra de 0 a 100.000, la segunda domina
artificialmente. <code>StandardScaler</code> lleva cada variable a media 0 y desviación 1, poniéndolas
en igualdad de condiciones. Punto crítico: el escalador se <b>ajusta solo con los datos de
entrenamiento</b> y luego se aplica a test; ajustarlo con todo sería una <b>fuga de datos</b>.</p>

<p><b>Codificar categorías.</b> Los modelos operan con números, no con texto. Una columna como
"región" (norte/sur/centro) se convierte en columnas numéricas con <b>one-hot encoding</b>
(<code>pd.get_dummies</code>): una columna 0/1 por cada categoría. Así el modelo puede usar variables
cualitativas sin inventar un orden que no existe.</p>

<p><b>Pipelines.</b> Encadenar "escalar → entrenar" a mano es propenso a errores (sobre todo a fugas:
olvidar que el escalador debe ajustarse solo con train). Un <b>Pipeline</b> junta todos los pasos en
un solo objeto que hace <code>fit</code> y <code>predict</code> respetando el orden y las reglas
automáticamente. Es la forma profesional de trabajar: reproducible, limpia y sin fugas. En esta
lección lo usarás para construir tu primer flujo bien hecho.</p>
""",
        "examples": [
            {
                "title": "Separar entrenamiento y prueba",
                "explain": "<code>train_test_split</code> reserva datos para evaluar de forma honesta.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nX, y = load_iris(return_X_y=True)\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)\nprint("entrenamiento:", X_train.shape[0], "filas")\nprint("prueba:", X_test.shape[0], "filas")',
            },
            {
                "title": "Escalar (ajustando solo con train)",
                "explain": "El escalador se ajusta con train; tras escalar, media≈0 y desviación≈1.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nX, y = load_iris(return_X_y=True)\nX_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)\nscaler = StandardScaler().fit(X_train)   # SOLO con train\nX_train_s = scaler.transform(X_train)\nprint("media:", X_train_s.mean(axis=0).round(2))\nprint("desv :", X_train_s.std(axis=0).round(2))',
            },
            {
                "title": "Codificar categóricas (one-hot)",
                "explain": "<code>get_dummies</code> crea una columna 0/1 por categoría.",
                "code": 'import pandas as pd\ndf = pd.DataFrame({"region": ["norte", "sur", "centro", "norte"], "ventas": [120, 95, 110, 130]})\nprint(pd.get_dummies(df, columns=["region"]))',
            },
            {
                "title": "Un Pipeline: escalar + entrenar",
                "explain": "Todo el flujo en un objeto, sin fugas y en una línea de entrenamiento.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.pipeline import make_pipeline\nX, y = load_iris(return_X_y=True)\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=0)\nmodelo = make_pipeline(StandardScaler(), KNeighborsClassifier())\nmodelo.fit(X_tr, y_tr)\nprint("precisión:", round(modelo.score(X_te, y_te), 3))',
            },
            {
                "title": "Por qué escalar importa",
                "explain": "Con variables de escalas muy distintas, escalar las pone en igualdad.",
                "code": 'import numpy as np\nfrom sklearn.preprocessing import StandardScaler\nX = np.array([[1, 1000], [2, 2000], [3, 3000]], dtype=float)\nprint("original:\\n", X)\nprint("escalado:\\n", StandardScaler().fit_transform(X).round(2))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Divide iris en train/test con <code>test_size=0.25</code> y muestra los tamaños.",
            "Ajusta un <code>StandardScaler</code> con train y transforma train y test.",
            "Codifica con <code>get_dummies</code> una columna de 4 categorías.",
            "Crea un <code>make_pipeline(StandardScaler(), KNeighborsClassifier())</code> y evalúalo.",
            "Cambia el <code>random_state</code> del split y observa si cambia la precisión.",
            "Explica en un comentario qué es una fuga de datos (data leakage).",
            "Compara la precisión de KNN con y sin escalado sobre iris.",
            "Usa <code>test_size=0.5</code> y comenta qué pasa con menos datos de entrenamiento.",
            "Aplica <code>get_dummies</code> al DataFrame <code>datos</code> sobre la columna <code>region</code>.",
        ],
    },

    # ============================================================ CAP 29
    {
        "num": 29,
        "slug": "regresion",
        "code": "leccion_29",
        "title": "Regresión: predecir números",
        "subtitle": "Regresión lineal, coeficientes y predicción de valores continuos",
        "apunte": "Lección 29 - Regresión",
        "concepts": [
            ("Regresión", "Predecir un valor <b>numérico continuo</b> (un precio, una temperatura, una demanda)."),
            ("LinearRegression", "El modelo base: ajusta una recta (o plano) que mejor sigue los datos."),
            ("Coeficiente (pendiente)", "Cuánto cambia la predicción por cada unidad de una variable."),
            ("Intercepto", "El valor predicho cuando todas las variables valen 0."),
            ("Regresión múltiple", "Usar varias features a la vez para predecir el target."),
            ("predict()", "Genera la predicción para nuevos valores de entrada."),
            ("score() / R²", "El <code>score</code> de una regresión es el R²: qué fracción de la variación explica el modelo."),
            ("Recta de ajuste", "La línea que el modelo encuentra minimizando los errores."),
        ],
        "theory": """
<p>La <b>regresión</b> es el tipo de problema supervisado en el que el target es un <b>número
continuo</b>: predecir el precio de una casa, la demanda de un producto, la temperatura de mañana. Es
uno de los usos más comunes del ML en negocios y ciencia.</p>

<p><b>Regresión lineal.</b> El modelo más simple y fundamental es la <b>regresión lineal</b>: busca la
<b>recta</b> (con una variable) o el <b>plano</b> (con varias) que mejor se ajusta a los datos,
minimizando la distancia entre la recta y los puntos reales. Aunque es simple, es sorprendentemente
útil y, sobre todo, <b>interpretable</b>: puedes explicar exactamente por qué predice lo que predice.</p>

<p><b>Coeficientes e intercepto.</b> La recta ajustada se describe con dos cosas. Los
<b>coeficientes</b> (<code>coef_</code>) son las pendientes: cuánto cambia la predicción por cada
unidad que aumenta una variable (si el coeficiente de "metros cuadrados" es 20, cada m² extra suma 20
al precio predicho). El <b>intercepto</b> (<code>intercept_</code>) es el valor base cuando todas las
variables son cero. Interpretar estos números es parte del valor de la regresión: no solo predice,
también <b>explica</b>.</p>

<p><b>De simple a múltiple.</b> Rara vez una sola variable basta. La <b>regresión múltiple</b> usa
varias features a la vez, y cada una aporta su coeficiente. scikit-learn lo maneja igual:
<code>fit(X, y)</code> con X de varias columnas. Al predecir con <code>predict</code> y evaluar con el
<b>R²</b> (que el <code>score</code> devuelve: la fracción de la variación del target que el modelo
explica, de 0 a 1), obtienes un modelo listo para usar. En la próxima lección aprenderás a evaluarlo
con rigor.</p>
""",
        "examples": [
            {
                "title": "Regresión lineal simple",
                "explain": "Ajustamos una recta y leemos su pendiente e intercepto.",
                "code": 'import numpy as np\nfrom sklearn.linear_model import LinearRegression\nX = np.array([[1], [2], [3], [4], [5]])\ny = np.array([2, 4, 5, 4, 6])\nm = LinearRegression().fit(X, y)\nprint("pendiente:", round(m.coef_[0], 3))\nprint("intercepto:", round(m.intercept_, 3))',
            },
            {
                "title": "Predecir valores nuevos",
                "explain": "Con el modelo entrenado, estimamos el target para nuevas entradas.",
                "code": 'import numpy as np\nfrom sklearn.linear_model import LinearRegression\nX = np.array([[1], [2], [3], [4], [5]])\ny = np.array([2, 4, 5, 4, 6])\nm = LinearRegression().fit(X, y)\nfor x in [6, 8, 10]:\n    print(f"x={x} -> predicción {m.predict([[x]])[0]:.2f}")',
            },
            {
                "title": "Graficar la recta de ajuste",
                "explain": "Los puntos reales y la recta que el modelo aprendió.",
                "code": 'import numpy as np, matplotlib.pyplot as plt\nfrom sklearn.linear_model import LinearRegression\nX = np.array([[1], [2], [3], [4], [5]])\ny = np.array([2, 4, 5, 4, 6])\nm = LinearRegression().fit(X, y)\nplt.scatter(X, y, color="#22d3ee", s=60)\nplt.plot(X, m.predict(X), color="#ff2e97")\nplt.title("Regresión lineal")\nplt.show()',
            },
            {
                "title": "Regresión múltiple",
                "explain": "Varias features a la vez, con el dataset diabetes (10 variables).",
                "code": 'from sklearn.datasets import load_diabetes\nfrom sklearn.linear_model import LinearRegression\nX, y = load_diabetes(return_X_y=True)\nm = LinearRegression().fit(X, y)\nprint("nº de coeficientes:", len(m.coef_))\nprint("R² sobre los datos:", round(m.score(X, y), 3))',
            },
            {
                "title": "Interpretar coeficientes",
                "explain": "Cada variable aporta su coeficiente: su efecto sobre la predicción.",
                "code": 'from sklearn.datasets import load_diabetes\nfrom sklearn.linear_model import LinearRegression\nd = load_diabetes()\nm = LinearRegression().fit(d.data, d.target)\npares = sorted(zip(d.feature_names, m.coef_), key=lambda p: abs(p[1]), reverse=True)\nfor nombre, coef in pares[:5]:\n    print(f"{nombre:>4}: {coef:8.1f}")',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Ajusta una regresión lineal a <code>X=[[1],[2],[3]]</code>, <code>y=[3,5,7]</code> y muestra pendiente e intercepto.",
            "Predice el valor para x=10 con ese modelo.",
            "Grafica los puntos y la recta de ajuste de un conjunto que inventes.",
            "Entrena una regresión múltiple sobre <code>load_diabetes</code> y muestra su R².",
            "Muestra los coeficientes de la regresión de diabetes.",
            "Divide diabetes en train/test y compara el R² en cada uno.",
            "Crea datos con relación clara (y = 2x + 1) y verifica que el modelo recupera la pendiente.",
            "Predice varios valores a la vez pasando una lista de entradas a <code>predict</code>.",
            "Investiga qué feature de diabetes tiene el coeficiente más grande en valor absoluto.",
        ],
    },

    # ============================================================ CAP 30
    {
        "num": 30,
        "slug": "evaluar-regresion",
        "code": "leccion_30",
        "title": "Evaluar una regresión",
        "subtitle": "MAE, MSE, RMSE, R² y análisis de residuos",
        "apunte": "Lección 30 - Métricas de regresión",
        "concepts": [
            ("MAE", "Error absoluto medio: el promedio de las diferencias (en valor absoluto). Fácil de interpretar."),
            ("MSE", "Error cuadrático medio: penaliza más los errores grandes al elevarlos al cuadrado."),
            ("RMSE", "Raíz del MSE: vuelve a las unidades originales del target. La métrica más usada."),
            ("R²", "Coeficiente de determinación: fracción de la variación explicada (1 = perfecto, 0 = como predecir la media)."),
            ("Residuo", "La diferencia entre el valor real y el predicho (<code>y − ŷ</code>)."),
            ("Gráfico de residuos", "Los residuos vs la predicción: si no muestran patrón, el modelo es adecuado."),
            ("Train vs test", "Comparar el error en train y test revela sobreajuste."),
            ("Línea base", "Un modelo tonto (predecir siempre la media) como referencia mínima."),
        ],
        "theory": """
<p>Entrenar un modelo es fácil; saber si es <b>bueno</b> es lo que separa a un profesional. Para
regresión, "bueno" significa que sus predicciones están <b>cerca</b> de los valores reales, y para
medirlo hay varias métricas, cada una con su matiz.</p>

<p><b>MAE, MSE y RMSE.</b> El <b>MAE</b> (error absoluto medio) promedia cuánto se equivoca el modelo,
en promedio, sin importar el signo; es el más intuitivo ("me equivoco por 12 unidades en promedio").
El <b>MSE</b> eleva los errores al cuadrado antes de promediar, lo que <b>penaliza más los errores
grandes</b> (un error de 10 pesa 100). Su raíz, el <b>RMSE</b>, vuelve a las unidades del target y es
la métrica más reportada. Menor MAE/RMSE = mejor modelo.</p>

<p><b>R²: ¿mejor que adivinar?</b> El <b>R²</b> responde una pregunta distinta: ¿cuánto mejor es el
modelo que simplemente predecir siempre la media? Va de 0 a 1 (a veces negativo): 1 es perfecto, 0
significa que no aporta nada sobre la media, y negativo que es <b>peor</b> que la media. Es útil porque
es adimensional y comparable entre problemas.</p>

<p><b>Mirar los residuos.</b> Los números no bastan: hay que mirar los <b>residuos</b> (los errores
individuales). Un <b>gráfico de residuos</b> (residuo vs predicción) debería verse como una nube <b>sin
patrón</b> alrededor de cero. Si en cambio muestra una curva o un embudo, el modelo está sistemáticamente
equivocándose en algún rango: una señal de que le falta algo (quizás una relación no lineal).</p>

<p><b>Honestidad: train vs test.</b> La evaluación que importa es sobre los datos de <b>prueba</b>, no
los de entrenamiento. Un modelo puede tener R²=0.99 en train y 0.60 en test: eso es <b>sobreajuste</b>,
memorizó en vez de aprender. Comparar siempre ambos, y reportar el desempeño en test, es la marca de un
análisis riguroso. En la lección de validación cruzada profundizaremos en esto.</p>
""",
        "examples": [
            {
                "title": "MAE, MSE y RMSE",
                "explain": "Las tres métricas de error a partir de valores reales y predichos.",
                "code": 'import numpy as np\nfrom sklearn.metrics import mean_absolute_error, mean_squared_error\ny_real = np.array([100, 120, 130, 90])\ny_pred = np.array([110, 115, 125, 100])\nmae = mean_absolute_error(y_real, y_pred)\nmse = mean_squared_error(y_real, y_pred)\nrmse = np.sqrt(mse)\nprint(f"MAE={mae:.2f}  MSE={mse:.2f}  RMSE={rmse:.2f}")',
            },
            {
                "title": "R²: comparado con predecir la media",
                "explain": "Un R² alto significa que el modelo aporta sobre la media.",
                "code": 'import numpy as np\nfrom sklearn.metrics import r2_score\ny = np.array([10, 20, 30, 40, 50])\nbueno = np.array([12, 19, 33, 38, 51])\nmedia = np.full(5, y.mean())   # predecir siempre la media\nprint("R² modelo:", round(r2_score(y, bueno), 3))\nprint("R2 media constante:", round(r2_score(y, media), 3))',
            },
            {
                "title": "RMSE sobre un modelo real",
                "explain": "Entrenamos, predecimos en test y medimos el error en sus unidades.",
                "code": 'import numpy as np\nfrom sklearn.datasets import load_diabetes\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error\nX, y = load_diabetes(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = LinearRegression().fit(Xtr, ytr)\nrmse = np.sqrt(mean_squared_error(yte, m.predict(Xte)))\nprint("RMSE en test:", round(rmse, 1))',
            },
            {
                "title": "Gráfico de residuos",
                "explain": "Sin patrón alrededor de 0 = modelo adecuado.",
                "code": 'import matplotlib.pyplot as plt\nfrom sklearn.datasets import load_diabetes\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nX, y = load_diabetes(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = LinearRegression().fit(Xtr, ytr)\npred = m.predict(Xte)\nplt.scatter(pred, yte - pred, color="#a87bff")\nplt.axhline(0, color="#ff2e97")\nplt.xlabel("predicción"); plt.ylabel("residuo"); plt.title("Residuos")\nplt.show()',
            },
            {
                "title": "Train vs test (detectar sobreajuste)",
                "explain": "Una gran brecha entre train y test señala sobreajuste.",
                "code": 'from sklearn.datasets import load_diabetes\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nX, y = load_diabetes(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = LinearRegression().fit(Xtr, ytr)\nprint("R² train:", round(m.score(Xtr, ytr), 3))\nprint("R² test :", round(m.score(Xte, yte), 3))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Calcula MAE y RMSE para <code>y_real=[5,7,9]</code>, <code>y_pred=[6,7,8]</code>.",
            "Calcula el R² de esas predicciones.",
            "Entrena una regresión en diabetes y reporta su RMSE en test.",
            "Grafica los residuos de un modelo de regresión.",
            "Compara el R² en train y en test de un modelo y comenta si hay sobreajuste.",
            "Crea un 'modelo' que prediga siempre la media y calcula su R² (debería ser ~0).",
            "Explica por qué el RMSE penaliza más los errores grandes que el MAE.",
            "Reporta las 3 métricas (MAE, RMSE, R²) de un mismo modelo en test.",
            "Investiga: ¿puede el R² ser negativo? Provoca un caso y muéstralo.",
        ],
    },

    # ============================================================ CAP 31
    {
        "num": 31,
        "slug": "clasificacion",
        "code": "leccion_31",
        "title": "Clasificación: predecir categorías",
        "subtitle": "Regresión logística, KNN y árboles para asignar clases",
        "apunte": "Lección 31 - Clasificación",
        "concepts": [
            ("Clasificación", "Predecir una <b>categoría</b> (spam/no spam, aprueba/reprueba, especie de flor)."),
            ("Regresión logística", "Pese a su nombre, es un modelo de <b>clasificación</b>: estima la probabilidad de cada clase."),
            ("KNN", "K vecinos más cercanos: clasifica según las clases de los ejemplos más parecidos."),
            ("Árbol de decisión", "Serie de preguntas sí/no sobre las features que llevan a una clase."),
            ("Clases", "Las categorías posibles del target."),
            ("predict_proba", "Devuelve la <b>probabilidad</b> de cada clase, no solo la elegida."),
            ("Frontera de decisión", "La superficie que separa las regiones asignadas a cada clase."),
            ("Comparar modelos", "Distintos algoritmos rinden distinto; conviene probar varios."),
        ],
        "theory": """
<p>La <b>clasificación</b> predice una <b>categoría</b> en lugar de un número: ¿es spam o no?, ¿el
cliente se irá o se quedará?, ¿qué especie es esta flor? Es, junto con la regresión, uno de los dos
pilares del aprendizaje supervisado, y probablemente el uso más frecuente del ML en la práctica.</p>

<p><b>Regresión logística.</b> A pesar de su nombre confuso, es un modelo de <b>clasificación</b>. En
vez de predecir un número, estima la <b>probabilidad</b> de pertenecer a cada clase y elige la más
probable. Es simple, rápida, interpretable y sorprendentemente competitiva: suele ser el primer modelo
que un profesional prueba como línea base.</p>

<p><b>KNN y árboles.</b> El <b>K vecinos más cercanos</b> (KNN) clasifica un caso nuevo mirando los
<code>k</code> ejemplos más <b>parecidos</b> y votando entre sus clases: intuitivo, sin "entrenamiento"
real, pero sensible a la escala (recuerda escalar). El <b>árbol de decisión</b> aprende una serie de
preguntas sí/no sobre las features ("¿el pétalo mide más de 2.5 cm?") que llevan a una clase; es muy
interpretable y no necesita escalado. Cada modelo tiene fortalezas distintas.</p>

<p><b>Probabilidades y comparación.</b> Muchos clasificadores ofrecen <code>predict_proba</code>: en
lugar de una respuesta tajante, dan la <b>probabilidad</b> de cada clase (por ejemplo, 80% spam, 20%
no). Esto es valioso para decidir con matices o fijar umbrales. Y como ningún algoritmo es el mejor
para todo, la práctica profesional es <b>probar varios</b> y comparar su desempeño con datos de prueba.
En la próxima lección verás que medir bien una clasificación es más sutil que solo contar aciertos.</p>
""",
        "examples": [
            {
                "title": "Regresión logística",
                "explain": "El clasificador base: rápido e interpretable.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = LogisticRegression(max_iter=1000).fit(Xtr, ytr)\nprint("precisión:", round(m.score(Xte, yte), 3))',
            },
            {
                "title": "K vecinos más cercanos (KNN)",
                "explain": "Clasifica según los ejemplos más parecidos.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.neighbors import KNeighborsClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = KNeighborsClassifier(n_neighbors=5).fit(Xtr, ytr)\nprint("precisión KNN:", round(m.score(Xte, yte), 3))',
            },
            {
                "title": "Probabilidades por clase",
                "explain": "<code>predict_proba</code> da la confianza del modelo en cada clase.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.linear_model import LogisticRegression\nd = load_iris()\nm = LogisticRegression(max_iter=1000).fit(d.data, d.target)\nproba = m.predict_proba([d.data[0]])[0]\nfor clase, p in zip(d.target_names, proba):\n    print(f"{clase:>12}: {p:.3f}")',
            },
            {
                "title": "Árbol de decisión",
                "explain": "Preguntas sí/no sobre las features; muy interpretable.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)\nprint("precisión árbol:", round(m.score(Xte, yte), 3))',
            },
            {
                "title": "Comparar varios modelos",
                "explain": "Ningún algoritmo gana siempre: probamos tres y comparamos.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.tree import DecisionTreeClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nmodelos = {"logística": LogisticRegression(max_iter=1000),\n           "knn": KNeighborsClassifier(),\n           "árbol": DecisionTreeClassifier(random_state=0)}\nfor nombre, mod in modelos.items():\n    mod.fit(Xtr, ytr)\n    print(f"{nombre:>10}: {mod.score(Xte, yte):.3f}")',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Entrena una regresión logística en iris y reporta su precisión en test.",
            "Entrena un KNN con <code>n_neighbors=3</code> y compáralo con <code>n_neighbors=9</code>.",
            "Muestra las probabilidades por clase de una flor con <code>predict_proba</code>.",
            "Entrena un árbol con <code>max_depth=2</code> y otro sin límite; compara sus precisiones.",
            "Compara logística, KNN y árbol en un mismo split.",
            "Predice la clase de una muestra inventada con el mejor de tus modelos.",
            "Usa <code>make_classification</code> para crear un problema binario y entrena un clasificador.",
            "Investiga: ¿por qué KNN necesita escalado y el árbol no?",
            "Muestra la clase más probable y su probabilidad para 3 muestras distintas.",
        ],
    },
]
