# -*- coding: utf-8 -*-
"""
PyChoice - Modulo H (parte 2): Machine Learning (Lecciones 32 a 36).
Nivel profesional. scikit-learn se carga bajo demanda al importarlo.
"""

CHAPTERS_H2 = [

    # ============================================================ CAP 32
    {
        "num": 32,
        "slug": "evaluar-clasificacion",
        "code": "leccion_32",
        "title": "Evaluar una clasificación",
        "subtitle": "Más allá de la precisión: matriz de confusión, precision, recall, F1 y AUC",
        "apunte": "Lección 32 - Métricas de clasificación",
        "concepts": [
            ("Accuracy", "Proporción de aciertos. Útil, pero engañosa con clases desbalanceadas."),
            ("Matriz de confusión", "Tabla de aciertos y errores por clase (verdaderos/falsos positivos y negativos)."),
            ("Precision", "De lo que predije positivo, ¿cuánto lo era de verdad? Mide falsos positivos."),
            ("Recall (sensibilidad)", "De todos los positivos reales, ¿cuántos detecté? Mide falsos negativos."),
            ("F1", "La media armónica de precision y recall: un balance entre ambas."),
            ("Clases desbalanceadas", "Cuando una clase es mucho más frecuente; la accuracy deja de ser fiable."),
            ("ROC-AUC", "Mide la capacidad de separar clases considerando todos los umbrales (1 = perfecto, 0.5 = azar)."),
            ("classification_report", "Resumen con precision, recall y F1 por clase, todo de una vez."),
        ],
        "theory": """
<p>Medir bien una clasificación es más sutil de lo que parece. La métrica obvia —la <b>accuracy</b>
(proporción de aciertos)— puede ser profundamente engañosa, y confiar solo en ella es un error de
principiante que un profesional evita.</p>

<p><b>El problema del desbalance.</b> Imagina detectar fraude, donde solo el 1% de las transacciones
son fraudulentas. Un modelo que <b>siempre</b> dice "no es fraude" acierta el 99% de las veces:
¡accuracy 0.99! Y es completamente inútil, porque no detecta ningún fraude. Cuando las clases están
<b>desbalanceadas</b>, la accuracy miente. Necesitamos métricas que miren cada clase por separado.</p>

<p><b>La matriz de confusión.</b> Es el punto de partida: una tabla que cruza lo real con lo predicho,
mostrando <b>verdaderos positivos</b>, <b>falsos positivos</b>, <b>verdaderos negativos</b> y
<b>falsos negativos</b>. De ella salen las métricas clave. La <b>precision</b> responde "de lo que
marqué como positivo, ¿cuánto acerté?" (penaliza falsos positivos). El <b>recall</b> responde "de todos
los positivos reales, ¿cuántos encontré?" (penaliza falsos negativos). Según el problema, importa más
una u otra: en un filtro de spam duele el falso positivo (correo bueno perdido); en un test médico duele
el falso negativo (enfermo no detectado).</p>

<p><b>F1 y AUC.</b> El <b>F1</b> combina precision y recall en un solo número (su media armónica),
útil cuando quieres balance. El <b>ROC-AUC</b> mide algo distinto: qué tan bien el modelo <b>ordena</b>
los casos por probabilidad, considerando todos los umbrales posibles; va de 0.5 (azar) a 1 (perfecto).
El <code>classification_report</code> de scikit-learn entrega precision, recall y F1 por clase de un
vistazo. Elegir y reportar las métricas correctas —no solo la accuracy— es la diferencia entre un
modelo que parece bueno y uno que <b>es</b> bueno.</p>
""",
        "examples": [
            {
                "title": "Accuracy y matriz de confusión",
                "explain": "Los aciertos totales y el detalle de errores por clase.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score, confusion_matrix\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = LogisticRegression(max_iter=1000).fit(Xtr, ytr)\npred = m.predict(Xte)\nprint("accuracy:", round(accuracy_score(yte, pred), 3))\nprint("matriz de confusión:\\n", confusion_matrix(yte, pred))',
            },
            {
                "title": "Reporte completo (precision, recall, F1)",
                "explain": "<code>classification_report</code> resume todo por clase.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import classification_report\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = LogisticRegression(max_iter=1000).fit(Xtr, ytr)\nprint(classification_report(yte, m.predict(Xte), target_names=load_iris().target_names))',
            },
            {
                "title": "Precision, recall y F1 (problema binario)",
                "explain": "Cada métrica por separado en un problema de dos clases.",
                "code": 'from sklearn.datasets import make_classification\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import precision_score, recall_score, f1_score\nX, y = make_classification(n_samples=300, random_state=0)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\npred = LogisticRegression().fit(Xtr, ytr).predict(Xte)\nprint("precision:", round(precision_score(yte, pred), 3))\nprint("recall   :", round(recall_score(yte, pred), 3))\nprint("f1       :", round(f1_score(yte, pred), 3))',
            },
            {
                "title": "ROC-AUC",
                "explain": "Capacidad de ordenar los casos por probabilidad de ser positivos.",
                "code": 'from sklearn.datasets import make_classification\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import roc_auc_score\nX, y = make_classification(n_samples=300, random_state=0)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nm = LogisticRegression().fit(Xtr, ytr)\nproba = m.predict_proba(Xte)[:, 1]\nprint("ROC-AUC:", round(roc_auc_score(yte, proba), 3))',
            },
            {
                "title": "Por qué la accuracy engaña",
                "explain": "Con 95% de una clase, un modelo que siempre dice '0' tiene 0.95 de accuracy y recall 0.",
                "code": 'import numpy as np\nfrom sklearn.metrics import accuracy_score, recall_score\ny_real = np.array([0]*95 + [1]*5)\ny_pred = np.zeros(100, dtype=int)   # predice SIEMPRE la clase mayoritaria\nprint("accuracy:", accuracy_score(y_real, y_pred))\nprint("recall clase 1:", recall_score(y_real, y_pred))\nprint("=> alta accuracy, pero no detecta ni un positivo")',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Calcula accuracy y matriz de confusión de un clasificador en iris.",
            "Muestra el <code>classification_report</code> de un modelo.",
            "En un problema binario, calcula precision, recall y F1.",
            "Calcula el ROC-AUC de una regresión logística binaria.",
            "Construye un caso desbalanceado y muestra cómo la accuracy engaña.",
            "Explica en un comentario cuándo importa más el recall que la precision.",
            "Compara el F1 de dos modelos distintos en el mismo problema.",
            "Interpreta una matriz de confusión: ¿dónde están los falsos positivos?",
            "Investiga: ¿qué mide exactamente un AUC de 0.5?",
        ],
    },

    # ============================================================ CAP 33
    {
        "num": 33,
        "slug": "ensembles",
        "code": "leccion_33",
        "title": "Árboles y ensembles: Random Forest",
        "subtitle": "De un árbol a un bosque: modelos potentes e importancia de variables",
        "apunte": "Lección 33 - Ensembles",
        "concepts": [
            ("Árbol de decisión", "Preguntas sí/no encadenadas; interpretable pero tiende a sobreajustar."),
            ("max_depth", "Límite de profundidad del árbol: controla su complejidad."),
            ("Ensemble", "Combinar muchos modelos para obtener uno mejor que cualquiera por separado."),
            ("Random Forest", "Un <b>bosque</b> de muchos árboles distintos que votan; robusto y muy usado."),
            ("Bagging", "Entrenar cada árbol con una muestra aleatoria: da diversidad al bosque."),
            ("n_estimators", "Número de árboles del bosque."),
            ("Importancia de variables", "<code>feature_importances_</code>: cuánto aporta cada feature a las predicciones."),
            ("Boosting", "Otra familia de ensembles que construye modelos en secuencia corrigiendo errores (XGBoost, etc.)."),
        ],
        "theory": """
<p>Los modelos lineales son interpretables, pero muchas relaciones del mundo real no son lineales. Los
<b>árboles de decisión</b> capturan relaciones complejas con una serie de preguntas sí/no, y son muy
fáciles de interpretar. Su debilidad: un árbol sin límite tiende a <b>memorizar</b> los datos de
entrenamiento (sobreajuste). Controlar su <code>max_depth</code> ayuda, pero hay algo mejor.</p>

<p><b>La sabiduría de las multitudes.</b> Un <b>ensemble</b> combina muchos modelos para lograr uno
más preciso y estable que cualquiera individual. La intuición: si muchos expertos con puntos de vista
distintos votan, la decisión conjunta suele ser mejor que la de uno solo. El <b>Random Forest</b>
(bosque aleatorio) aplica esta idea: entrena <b>decenas o cientos de árboles</b>, cada uno con una
muestra aleatoria de los datos y de las variables (una técnica llamada <b>bagging</b>), y promedia sus
votos. El resultado es robusto, potente y difícil de sobreajustar.</p>

<p><b>Fácil y efectivo.</b> El Random Forest es uno de los modelos favoritos de los profesionales
porque funciona muy bien "de fábrica", con poco ajuste, en una enorme variedad de problemas. Sus
parámetros principales son <code>n_estimators</code> (cuántos árboles) y <code>max_depth</code>
(profundidad de cada uno). Más árboles suele ser mejor (hasta un punto), a costa de más cómputo.</p>

<p><b>Bonus: qué variables importan.</b> Además de predecir bien, el Random Forest te dice
<code>feature_importances_</code>: cuánto contribuye cada variable a las decisiones. Esto es oro para el
análisis: no solo obtienes un buen modelo, sino <b>entendimiento</b> sobre qué factores mueven el
resultado. Existen ensembles aún más potentes basados en <b>boosting</b> (como XGBoost o
LightGBM), que construyen los árboles en secuencia corrigiendo los errores del anterior; son el estándar
en competencias, y un paso natural cuando domines el Random Forest.</p>
""",
        "examples": [
            {
                "title": "Un árbol con profundidad limitada",
                "explain": "Limitar la profundidad controla la complejidad.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=1)\nm = DecisionTreeClassifier(max_depth=2, random_state=0).fit(Xtr, ytr)\nprint("precisión (prof=2):", round(m.score(Xte, yte), 3))',
            },
            {
                "title": "Random Forest",
                "explain": "Un bosque de 100 árboles que votan.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=1)\nm = RandomForestClassifier(n_estimators=100, random_state=0).fit(Xtr, ytr)\nprint("precisión bosque:", round(m.score(Xte, yte), 3))',
            },
            {
                "title": "Árbol vs bosque",
                "explain": "El ensemble suele generalizar mejor que un solo árbol.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.ensemble import RandomForestClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=1)\nt = DecisionTreeClassifier(random_state=0).fit(Xtr, ytr)\nf = RandomForestClassifier(random_state=0).fit(Xtr, ytr)\nprint("árbol :", round(t.score(Xte, yte), 3))\nprint("bosque:", round(f.score(Xte, yte), 3))',
            },
            {
                "title": "Importancia de variables",
                "explain": "El bosque revela qué features pesan más en sus decisiones.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.ensemble import RandomForestClassifier\nd = load_iris()\nm = RandomForestClassifier(random_state=0).fit(d.data, d.target)\nfor nombre, imp in sorted(zip(d.feature_names, m.feature_importances_), key=lambda p: -p[1]):\n    print(f"{nombre:>20}: {imp:.3f}")',
            },
            {
                "title": "Señal de sobreajuste en un árbol profundo",
                "explain": "Train perfecto y test menor = memorizó en vez de generalizar.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=1)\nm = DecisionTreeClassifier(random_state=0).fit(Xtr, ytr)  # sin límite\nprint("train:", round(m.score(Xtr, ytr), 3), "| test:", round(m.score(Xte, yte), 3))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Entrena un árbol con <code>max_depth=1</code> y con <code>max_depth=5</code>; compara en test.",
            "Entrena un Random Forest de 50 árboles y reporta su precisión.",
            "Compara un solo árbol contra un bosque en el mismo split.",
            "Muestra la importancia de variables de un Random Forest sobre iris.",
            "Grafica en barras las importancias de las features.",
            "Muestra la señal de sobreajuste comparando train y test en un árbol sin límite.",
            "Prueba distintos <code>n_estimators</code> (10, 100, 300) y observa la precisión.",
            "Usa un Random Forest de regresión (<code>RandomForestRegressor</code>) sobre diabetes.",
            "Investiga en un comentario la diferencia entre bagging y boosting.",
        ],
    },

    # ============================================================ CAP 34
    {
        "num": 34,
        "slug": "validacion-cruzada",
        "code": "leccion_34",
        "title": "Sobreajuste, validación cruzada y regularización",
        "subtitle": "Que el modelo generalice: medir bien y controlar la complejidad",
        "apunte": "Lección 34 - Generalización",
        "concepts": [
            ("Sobreajuste (overfitting)", "El modelo memoriza el entrenamiento y falla con datos nuevos (train alto, test bajo)."),
            ("Subajuste (underfitting)", "El modelo es demasiado simple y no capta el patrón (train y test bajos)."),
            ("Validación cruzada", "Entrenar y evaluar en varias particiones para una estimación más fiable."),
            ("cross_val_score", "Ejecuta la validación cruzada y devuelve el desempeño en cada partición (fold)."),
            ("KFold", "Divide los datos en k bloques; cada uno es test una vez."),
            ("Regularización", "Penalizar la complejidad del modelo para evitar el sobreajuste (Ridge, Lasso)."),
            ("Hiperparámetro", "Un ajuste del modelo que se elige antes de entrenar (k de KNN, profundidad, alpha)."),
            ("GridSearchCV", "Prueba automáticamente combinaciones de hiperparámetros con validación cruzada."),
        ],
        "theory": """
<p>El objetivo del ML no es acertar con los datos conocidos, sino <b>generalizar</b> a los nuevos. Los
dos enemigos de la generalización tienen nombre. El <b>sobreajuste</b> (overfitting) ocurre cuando el
modelo es tan complejo que <b>memoriza</b> el entrenamiento, incluyendo su ruido: brilla en train y
fracasa en test. El <b>subajuste</b> (underfitting) es lo contrario: un modelo tan simple que no capta
el patrón, y falla en ambos. El arte está en el equilibrio.</p>

<p><b>Validación cruzada.</b> Evaluar con una sola partición train/test tiene un problema: el resultado
depende de <b>qué</b> datos cayeron en test (mala o buena suerte). La <b>validación cruzada</b> lo
resuelve: divide los datos en <code>k</code> bloques (folds), entrena <code>k</code> veces usando cada
bloque como test una vez, y promedia. Así obtienes una estimación mucho más <b>fiable</b> del
desempeño, con su variabilidad incluida. <code>cross_val_score</code> lo hace en una línea, y es el
estándar profesional para comparar modelos.</p>

<p><b>Regularización.</b> Una forma directa de combatir el sobreajuste es <b>penalizar la
complejidad</b>. En regresión, <b>Ridge</b> y <b>Lasso</b> añaden una penalización que "encoge" los
coeficientes, evitando que el modelo se ajuste demasiado a los datos; Lasso incluso puede llevar
coeficientes a cero (selección de variables). El parámetro <code>alpha</code> controla la fuerza de la
penalización: es un <b>hiperparámetro</b> que hay que elegir.</p>

<p><b>Ajustar hiperparámetros.</b> Los modelos tienen <b>hiperparámetros</b> (el <code>k</code> de
KNN, la profundidad de un árbol, el <code>alpha</code> de Ridge) que no se aprenden solos: hay que
elegirlos. Probar a mano es tedioso y arriesgado. <b>GridSearchCV</b> automatiza la búsqueda: prueba
todas las combinaciones que le indiques, cada una con validación cruzada, y te dice la mejor. Combinar
validación cruzada, regularización y búsqueda de hiperparámetros es lo que convierte un modelo que
"funciona" en uno realmente sólido y confiable.</p>
""",
        "examples": [
            {
                "title": "Ver el sobreajuste según la complejidad",
                "explain": "Al aumentar la profundidad, train sube pero test se estanca o baja.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\nX, y = load_iris(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=1)\nfor d in [1, 2, 3, None]:\n    m = DecisionTreeClassifier(max_depth=d, random_state=0).fit(Xtr, ytr)\n    print(f"prof={str(d):>4}  train={m.score(Xtr,ytr):.3f}  test={m.score(Xte,yte):.3f}")',
            },
            {
                "title": "Validación cruzada",
                "explain": "Cinco evaluaciones dan una estimación fiable, con su variabilidad.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import cross_val_score\nfrom sklearn.ensemble import RandomForestClassifier\nX, y = load_iris(return_X_y=True)\nscores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=5)\nprint("por fold:", scores.round(3))\nprint("media:", round(scores.mean(), 3), "±", round(scores.std(), 3))',
            },
            {
                "title": "Cómo divide KFold",
                "explain": "Cada bloque es test una vez; el resto, entrenamiento.",
                "code": 'import numpy as np\nfrom sklearn.model_selection import KFold\nX = np.arange(10)\nfor i, (tr, te) in enumerate(KFold(n_splits=5).split(X)):\n    print(f"fold {i+1}: test = {te}")',
            },
            {
                "title": "Regularización: Ridge y Lasso",
                "explain": "Penalizan la complejidad para mejorar la generalización.",
                "code": 'from sklearn.datasets import load_diabetes\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression, Ridge, Lasso\nX, y = load_diabetes(return_X_y=True)\nXtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)\nfor nombre, mod in [("lineal", LinearRegression()), ("ridge", Ridge(alpha=1.0)), ("lasso", Lasso(alpha=0.1))]:\n    mod.fit(Xtr, ytr)\n    print(f"{nombre:>7}: R² test = {mod.score(Xte, yte):.3f}")',
            },
            {
                "title": "Buscar el mejor hiperparámetro (GridSearchCV)",
                "explain": "Prueba varios valores de k con validación cruzada y elige el mejor.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.neighbors import KNeighborsClassifier\nX, y = load_iris(return_X_y=True)\ngrid = GridSearchCV(KNeighborsClassifier(), {"n_neighbors": [1, 3, 5, 7, 9]}, cv=5)\ngrid.fit(X, y)\nprint("mejor k:", grid.best_params_)\nprint("mejor precisión CV:", round(grid.best_score_, 3))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Muestra train vs test de un árbol para profundidades 1, 3 y sin límite.",
            "Aplica <code>cross_val_score</code> con cv=5 a un modelo y muestra la media.",
            "Cambia el número de folds a 10 y compara la estimación.",
            "Compara LinearRegression, Ridge y Lasso en diabetes por su R² en test.",
            "Prueba distintos <code>alpha</code> en Ridge y observa el efecto.",
            "Usa <code>GridSearchCV</code> para elegir la mejor profundidad de un árbol.",
            "Explica en un comentario la diferencia entre sobreajuste y subajuste.",
            "Muestra la variabilidad (desviación) de la validación cruzada de dos modelos.",
            "Investiga: ¿por qué la validación cruzada es más fiable que un solo split?",
        ],
    },

    # ============================================================ CAP 35
    {
        "num": 35,
        "slug": "no-supervisado",
        "code": "leccion_35",
        "title": "Aprendizaje no supervisado: clustering y PCA",
        "subtitle": "Descubrir grupos y reducir dimensiones sin etiquetas",
        "apunte": "Lección 35 - No supervisado",
        "concepts": [
            ("No supervisado", "Aprender sin etiquetas: se busca estructura oculta en los datos."),
            ("Clustering", "Agrupar observaciones parecidas en grupos (clusters)."),
            ("k-means", "El algoritmo de clustering más común: forma k grupos alrededor de centros."),
            ("Inercia", "Qué tan compactos son los grupos; baja al aumentar k."),
            ("Método del codo", "Graficar la inercia vs k para elegir un buen número de grupos."),
            ("PCA", "Análisis de componentes principales: reduce muchas variables a unas pocas."),
            ("Reducción de dimensionalidad", "Comprimir los datos conservando la mayor información posible."),
            ("Varianza explicada", "Cuánta información retiene cada componente del PCA."),
        ],
        "theory": """
<p>Hasta ahora, el aprendizaje supervisado tenía siempre una respuesta correcta (el target). En el
<b>aprendizaje no supervisado</b> no hay etiquetas: el objetivo es <b>descubrir estructura</b> por sí
mismo. Es fundamental cuando tienes muchos datos pero nadie los ha clasificado, que es lo más común en
la práctica.</p>

<p><b>Clustering con k-means.</b> El <b>clustering</b> agrupa observaciones <b>parecidas</b>. El
algoritmo <b>k-means</b> es el más usado: le indicas cuántos grupos (<code>k</code>) quieres y él
ubica <code>k</code> centros, asignando cada punto al más cercano y reajustando los centros hasta que
se estabilizan. Sirve para segmentar clientes, agrupar productos, detectar perfiles… sin necesidad de
etiquetas previas. Su medida de calidad es la <b>inercia</b>: qué tan compactos quedan los grupos.</p>

<p><b>¿Cuántos grupos?</b> El desafío de k-means es elegir <code>k</code>. La inercia siempre baja al
aumentar k (con k = nº de puntos, cada punto es su propio grupo, inercia 0), así que no se puede
minimizar sin más. El <b>método del codo</b> ayuda: se grafica la inercia frente a k y se busca el
"codo", el punto donde añadir más grupos ya no mejora mucho. Ese quiebre suele indicar un buen número
de grupos.</p>

<p><b>Reducir dimensiones con PCA.</b> Cuando hay <b>muchas</b> variables, cuesta visualizar y los
modelos se complican (la "maldición de la dimensionalidad"). El <b>PCA</b> (análisis de componentes
principales) <b>comprime</b> muchas variables en unas pocas <b>componentes</b> que conservan la mayor
parte de la información (la <b>varianza</b>). Es ideal para <b>visualizar</b> datos de alta dimensión en
2D y para acelerar y estabilizar otros modelos. Combinado con clustering, permite explorar y entender
conjuntos de datos complejos que de otro modo serían una caja negra. Con esto cierras el repertorio
esencial de un científico de datos.</p>
""",
        "examples": [
            {
                "title": "k-means: encontrar grupos",
                "explain": "Agrupamos datos sin etiquetas en 3 clusters.",
                "code": 'from sklearn.datasets import make_blobs\nfrom sklearn.cluster import KMeans\nX, _ = make_blobs(n_samples=200, centers=3, random_state=0)\nkm = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)\nprint("etiquetas:", km.labels_[:20])\nprint("inercia:", round(km.inertia_, 1))',
            },
            {
                "title": "Visualizar los clusters",
                "explain": "Cada color es un grupo; las X son los centros.",
                "code": 'import matplotlib.pyplot as plt\nfrom sklearn.datasets import make_blobs\nfrom sklearn.cluster import KMeans\nX, _ = make_blobs(n_samples=200, centers=3, random_state=0)\nkm = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)\nplt.scatter(X[:, 0], X[:, 1], c=km.labels_, cmap="viridis", s=25)\nplt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], c="#ff2e97", marker="X", s=200)\nplt.title("k-means (3 grupos)")\nplt.show()',
            },
            {
                "title": "Método del codo",
                "explain": "La inercia vs k; el 'codo' sugiere un buen número de grupos.",
                "code": 'import matplotlib.pyplot as plt\nfrom sklearn.datasets import make_blobs\nfrom sklearn.cluster import KMeans\nX, _ = make_blobs(n_samples=200, centers=3, random_state=0)\ninercias = [KMeans(n_clusters=k, n_init=10, random_state=0).fit(X).inertia_ for k in range(1, 7)]\nplt.plot(range(1, 7), inercias, marker="o", color="#00ff9c")\nplt.xlabel("k"); plt.ylabel("inercia"); plt.title("Método del codo")\nplt.show()',
            },
            {
                "title": "PCA: reducir iris a 2D",
                "explain": "Comprimimos 4 variables en 2 componentes para visualizar.",
                "code": 'import matplotlib.pyplot as plt\nfrom sklearn.datasets import load_iris\nfrom sklearn.decomposition import PCA\nd = load_iris()\nX2 = PCA(n_components=2).fit_transform(d.data)\nplt.scatter(X2[:, 0], X2[:, 1], c=d.target, cmap="viridis")\nplt.title("Iris en 2D (PCA)")\nplt.show()',
            },
            {
                "title": "Varianza explicada por el PCA",
                "explain": "Cuánta información retiene cada componente.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.decomposition import PCA\nd = load_iris()\np = PCA().fit(d.data)\nprint("varianza por componente:", p.explained_variance_ratio_.round(3))\nprint("acumulada con 2 comp:", round(p.explained_variance_ratio_[:2].sum(), 3))',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Aplica k-means con 4 grupos a datos de <code>make_blobs</code> y muestra la inercia.",
            "Grafica los clusters y sus centros.",
            "Dibuja el método del codo para k de 1 a 8.",
            "Aplica k-means a iris (sin usar etiquetas) y compara con las especies reales (crosstab).",
            "Reduce iris a 2 dimensiones con PCA y grafícalo.",
            "Muestra la varianza explicada por cada componente del PCA.",
            "Estandariza los datos antes de aplicar k-means y observa si cambian los grupos.",
            "Con PCA, averigua cuántas componentes se necesitan para retener el 95% de la varianza.",
            "Explica en un comentario para qué sirve reducir dimensiones.",
        ],
    },

    # ============================================================ CAP 36
    {
        "num": 36,
        "slug": "proyecto-ml",
        "code": "leccion_36",
        "title": "Proyecto de ML de punta a punta",
        "subtitle": "Del problema al modelo: el flujo completo integrado",
        "apunte": "Lección 36 - Proyecto de ML",
        "concepts": [
            ("Flujo de ML", "Cargar → preparar → dividir → entrenar → evaluar → interpretar → usar."),
            ("Pipeline", "Encadena preparación y modelo en un solo objeto reproducible."),
            ("Selección de modelo", "Comparar candidatos con validación cruzada y elegir el mejor."),
            ("Evaluación final", "Medir el modelo elegido en el conjunto de test reservado, una sola vez."),
            ("Interpretación", "Explicar qué aprendió el modelo (importancias, coeficientes)."),
            ("Persistencia (joblib)", "Guardar el modelo entrenado para reutilizarlo sin re-entrenar."),
            ("Reproducibilidad", "Fijar semillas y encadenar pasos para obtener siempre el mismo resultado."),
            ("Puesta en uso", "Cargar el modelo guardado y predecir sobre casos nuevos."),
        ],
        "theory": """
<p>Has aprendido las piezas; ahora las <b>integras</b>. Un proyecto real de Machine Learning sigue un
<b>flujo</b> ordenado, y saber ejecutarlo de principio a fin —no solo entrenar un modelo suelto— es lo
que define a un profesional. Esta lección junta todo lo anterior en un proceso coherente.</p>

<p><b>El flujo completo.</b> Los pasos son siempre los mismos: <b>1)</b> entender el problema y cargar
los datos; <b>2)</b> explorarlos y prepararlos (limpiar, escalar, codificar); <b>3)</b> separar
train/test; <b>4)</b> entrenar varios modelos candidatos; <b>5)</b> compararlos con <b>validación
cruzada</b> y elegir el mejor; <b>6)</b> evaluarlo <b>una sola vez</b> en el test reservado; <b>7)</b>
interpretar qué aprendió; y <b>8)</b> guardarlo para usarlo. Un <b>Pipeline</b> encapsula la preparación
y el modelo, garantizando que el mismo proceso se aplique siempre igual, sin fugas.</p>

<p><b>Elegir y evaluar honestamente.</b> La comparación entre modelos se hace con validación cruzada
<b>sobre los datos de entrenamiento</b>. El conjunto de <b>test</b> se guarda como un examen final:
se usa <b>una única vez</b>, con el modelo ya elegido, para estimar cómo se comportará en la realidad.
Mirar el test muchas veces para elegir es una forma sutil de sobreajuste. Esta disciplina es lo que
hace creíbles tus resultados.</p>

<p><b>Interpretar y persistir.</b> Un modelo no termina al predecir bien: hay que <b>explicarlo</b>
(qué variables importan, cómo decide) para que el negocio confíe y actúe. Y hay que <b>guardarlo</b>
(con <code>joblib</code>) para no re-entrenarlo cada vez: se entrena una vez, se guarda, y en producción
solo se carga y se usa para predecir. Con este flujo dominado, tienes la base completa de un científico
de datos: puedes tomar un problema, unos datos, y llevarlos hasta un modelo útil, evaluado y explicable.
El resto es práctica, profundidad y experiencia.</p>
""",
        "examples": [
            {
                "title": "1) Cargar y dividir",
                "explain": "Partimos del dataset y reservamos el test.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nX, y = load_iris(return_X_y=True)\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)\nprint("train:", X_tr.shape[0], "| test:", X_te.shape[0])',
            },
            {
                "title": "2) Comparar modelos con validación cruzada",
                "explain": "Elegimos el mejor candidato sin tocar el test.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split, cross_val_score\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.ensemble import RandomForestClassifier\nX, y = load_iris(return_X_y=True)\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)\ncandidatos = {\n    "logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),\n    "bosque": RandomForestClassifier(random_state=0),\n}\nfor nombre, mod in candidatos.items():\n    s = cross_val_score(mod, X_tr, y_tr, cv=5)\n    print(f"{nombre:>10}: CV = {s.mean():.3f}")',
            },
            {
                "title": "3) Entrenar el elegido y evaluar en test",
                "explain": "El test se usa una sola vez, con el modelo final.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import classification_report\nX, y = load_iris(return_X_y=True)\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)\nmodelo = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(X_tr, y_tr)\nprint(classification_report(y_te, modelo.predict(X_te), target_names=load_iris().target_names))',
            },
            {
                "title": "4) Interpretar el modelo",
                "explain": "Qué variables pesan más (con un bosque).",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.ensemble import RandomForestClassifier\nd = load_iris()\nm = RandomForestClassifier(random_state=0).fit(d.data, d.target)\nfor nombre, imp in sorted(zip(d.feature_names, m.feature_importances_), key=lambda p: -p[1]):\n    print(f"{nombre:>20}: {imp:.3f}")',
            },
            {
                "title": "5) Guardar y volver a usar el modelo",
                "explain": "Se entrena una vez, se guarda y luego solo se carga para predecir.",
                "code": 'import joblib\nfrom sklearn.datasets import load_iris\nfrom sklearn.ensemble import RandomForestClassifier\nd = load_iris()\nmodelo = RandomForestClassifier(random_state=0).fit(d.data, d.target)\njoblib.dump(modelo, "/tmp/modelo_iris.joblib")\ncargado = joblib.load("/tmp/modelo_iris.joblib")\npred = cargado.predict([[5.1, 3.5, 1.4, 0.2]])\nprint("modelo cargado; especie predicha:", d.target_names[pred[0]])',
            },
            {
                "title": "6) Predecir varios casos nuevos",
                "explain": "El modelo final en acción sobre datos inventados.",
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.ensemble import RandomForestClassifier\nd = load_iris()\nm = RandomForestClassifier(random_state=0).fit(d.data, d.target)\nnuevos = [[5.1, 3.5, 1.4, 0.2], [6.7, 3.0, 5.2, 2.3], [5.9, 3.0, 4.2, 1.5]]\nfor flor, pred in zip(nuevos, m.predict(nuevos)):\n    print(flor, "->", d.target_names[pred])',
            },
        ],
        "dataset": "notas, datos",
        "exercises": [
            "Carga iris, divídelo en train/test (25% test) y muestra los tamaños.",
            "Compara dos modelos con <code>cross_val_score</code> sobre el train.",
            "Entrena el mejor modelo y evalúalo en el test con <code>classification_report</code>.",
            "Construye un <code>Pipeline</code> de escalado + modelo para todo el flujo.",
            "Interpreta el modelo mostrando las importancias de variables.",
            "Guarda un modelo con <code>joblib</code> y vuelve a cargarlo.",
            "Con el modelo cargado, predice 3 casos nuevos inventados por ti.",
            "Repite el flujo completo con el dataset <code>load_wine</code> en lugar de iris.",
            "Escribe, en comentarios, los 8 pasos de un proyecto de ML de punta a punta.",
        ],
    },
]
