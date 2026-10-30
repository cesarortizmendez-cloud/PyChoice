# -*- coding: utf-8 -*-
"""
PyChoice - Ruta "Ingeniero de IA con Python".
Modulo O - Proyecto y cierre (lecciones 60-61).

Integra toda la ruta en un proyecto de punta a punta y cierra con los
siguientes pasos profesionales. Todo corre en el navegador (numpy, sklearn).
Datasets del motor: clientes, viviendas.
"""

CHAPTERS_O = [

    # ============================================================ CAP 59
    {
        "num": 60,
        "slug": "proyecto-integrador-ia",
        "code": "leccion_60",
        "title": "Proyecto integrador de Ingeniería de IA",
        "subtitle": "Del problema a la solución: un flujo completo que junta toda la ruta",
        "apunte": "Módulo O · Lección 1 - Proyecto integrador",
        "concepts": [
            ("Definir el problema", "Antes de programar: ¿qué se quiere lograr?, ¿es optimización o predicción?, ¿cómo se mide el éxito? El modelado empieza aquí."),
            ("Línea base (baseline)", "Un modelo trivial (la clase mayoritaria, el promedio) contra el cual <b>comparar</b>. Si no le ganas, tu solución no aporta."),
            ("Pipeline de solución", "El flujo ordenado: datos → preparación → modelo/optimización → evaluación → interpretación → decisión."),
            ("Elegir el enfoque", "Según el problema: una <b>metaheurística</b> (optimización combinatoria) o un <b>modelo de ML</b> (predicción), o ambos combinados."),
            ("Optimizar la solución", "Afinar el modelo: hiperparámetros (malla, aleatoria, genético) o los parámetros de la metaheurística."),
            ("Evaluación honesta", "Medir en datos no vistos, con la métrica adecuada al problema y el <b>costo</b> real de los errores."),
            ("Interpretación", "Explicar <b>por qué</b> decide el modelo (importancias, coeficientes) y revisar sesgos: IA responsable."),
            ("Comunicar resultados", "Traducir los números a una <b>recomendación</b> clara para quien debe decidir. El objetivo final de PyChoice."),
        ],
        "theory": """
<p><b>Juntar todas las piezas.</b> A lo largo de la ruta aprendiste a buscar, optimizar con
metaheurísticas, construir redes y aplicar IA moderna. Un ingeniero de IA no usa esas piezas por
separado: las <b>integra</b> en un flujo para resolver un problema real de principio a fin. Esta
lección es ese flujo completo, con un proyecto que puedes ejecutar y adaptar.</p>

<p><b>Primero el problema, no el algoritmo.</b> El error más común es empezar eligiendo la técnica de
moda. Al revés: primero define <b>qué quieres lograr</b> y <b>cómo medirás el éxito</b>. ¿Es un
problema de <b>optimización</b> (encontrar la mejor combinación: rutas, asignación) o de
<b>predicción</b> (estimar un valor o una clase)? Esa pregunta decide todo el resto.</p>

<p><b>Siempre una línea base.</b> Antes de modelos sofisticados, mide una <b>línea base</b> trivial:
para clasificar, predecir siempre la clase mayoritaria; para regresión, el promedio. Es la vara contra
la que se compara todo. Si tu red neuronal no le gana a «siempre predigo que no se va el cliente», algo
anda mal o el problema no necesita una red.</p>

<p><b>El flujo de trabajo.</b> Un proyecto de IA sigue siempre los mismos pasos: (1) <b>definir</b> el
problema y la métrica; (2) <b>preparar</b> los datos (limpieza, escalado, codificación); (3) una
<b>línea base</b>; (4) el <b>modelo o la optimización</b>, afinado; (5) <b>evaluación honesta</b> en
datos no vistos; (6) <b>interpretación</b> y revisión de sesgos; (7) <b>comunicación</b> de una
recomendación. En este orden, y sin saltarse pasos.</p>

<p><b>El proyecto de esta lección.</b> Resolveremos un caso de negocio completo: <b>predecir y entender
la fuga de clientes (churn)</b>. Construiremos una línea base, un modelo, lo <b>optimizaremos con un
algoritmo genético</b> (uniendo el módulo L con el ML), lo <b>evaluaremos</b> con las métricas
correctas, lo <b>interpretaremos</b> y terminaremos con una <b>recomendación de negocio</b>. Es el
patrón que repetirás en cualquier proyecto.</p>

<p><b>Optimización, el hilo de toda la ruta.</b> Fíjate que el proyecto usa la optimización en dos
niveles: el modelo aprende sus pesos minimizando una pérdida, y nosotros optimizamos sus hiperparámetros
con una metaheurística. Esa es la gran idea que conecta la ruta entera: <b>casi toda la IA es buscar la
mejor solución según un objetivo</b>. En los ejercicios podrás repetir el flujo con un problema de
<b>optimización logística</b> (rutas) en vez de predicción.</p>
""",
        "examples": [
            {
                "title": "Paso 1-2: definir el problema y la línea base",
                "explain": "Objetivo: predecir churn. Preparamos los datos y medimos una línea base (clase mayoritaria).",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.dummy import DummyClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nbase = DummyClassifier(strategy="most_frequent").fit(Xtr, ytr)\nprint("proporcion de churn:", round(y.mean(), 3))\nprint("linea base (clase mayoritaria) -> exactitud:", round(base.score(Xte, yte), 3))',
            },
            {
                "title": "Paso 3: un modelo que supere la base",
                "explain": "Entrenamos una regresión logística con escalado y comprobamos que mejora la línea base.",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.pipeline import make_pipeline\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\n\nmodelo = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)\nprint("modelo base -> exactitud:", round(modelo.score(Xte, yte), 3))',
            },
            {
                "title": "Paso 4: optimizar con un algoritmo genético",
                "explain": "Usamos un genético (módulo L) para elegir los hiperparámetros de un Random Forest: une optimización y ML.",
                "code": 'import numpy as np, pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\nrng = np.random.default_rng(7)\n\ncache = {}\ndef fitness(g):\n    clave = (int(g[0]), int(g[1]))        # memoizar: no reentrenar lo ya visto\n    if clave not in cache:\n        n, d = clave\n        cache[clave] = RandomForestClassifier(n_estimators=n, max_depth=d,\n                                              random_state=7).fit(Xtr, ytr).score(Xte, yte)\n    return cache[clave]\n\npob = [np.array([rng.integers(20, 60), rng.integers(2, 10)]) for _ in range(5)]\nfor gen in range(3):\n    pob = sorted(pob, key=fitness, reverse=True)\n    p = pob[:2]                            # elitismo: los 2 mejores\n    pob = p + [np.array([max(10, (p[0][0]+p[1][0])//2 + rng.integers(-8, 9)),\n                         max(2, (p[0][1]+p[1][1])//2 + rng.integers(-1, 2))]) for _ in range(3)]\nmejor = max(pob, key=fitness)\nprint("mejores hiperparametros (n_estimators, max_depth):", mejor.tolist())\nprint("exactitud optimizada:", round(fitness(mejor), 3))',
            },
            {
                "title": "Paso 5: evaluación honesta",
                "explain": "Métricas que importan en churn: matriz de confusión, precision/recall/F1 y AUC (no solo exactitud).",
                "code": 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import confusion_matrix, classification_report, roc_auc_score\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nXtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)\nm = RandomForestClassifier(n_estimators=120, max_depth=6, random_state=7).fit(Xtr, ytr)\n\npred = m.predict(Xte); proba = m.predict_proba(Xte)[:, 1]\nprint("matriz de confusion:\\n", confusion_matrix(yte, pred))\nprint(classification_report(yte, pred, zero_division=0))\nprint("AUC:", round(roc_auc_score(yte, proba), 3))',
            },
            {
                "title": "Paso 6-7: interpretar y recomendar",
                "explain": "Qué variables explican el churn, y la traducción a una recomendación de negocio.",
                "code": 'import pandas as pd\nfrom sklearn.ensemble import RandomForestClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nm = RandomForestClassifier(n_estimators=120, max_depth=6, random_state=7).fit(X, y)\nimp = pd.Series(m.feature_importances_, index=X.columns).sort_values(ascending=False)\n\nprint("factores mas asociados a la fuga:")\nprint(imp.head(3).round(3))\nprint("\\nRECOMENDACION: enfocar retencion en los clientes con mayor")\nprint("riesgo segun estas variables; medir el impacto antes de escalar.")',
            },
            {
                "title": "El proyecto, de un vistazo",
                "explain": "Resumen del flujo completo, el patrón que repetirás en cualquier proyecto de IA.",
                "code": 'pasos = [\n    "1. Definir problema y metrica de exito",\n    "2. Preparar datos (limpieza, escalado, codificacion)",\n    "3. Linea base trivial para comparar",\n    "4. Modelo / optimizacion, afinado (metaheuristica)",\n    "5. Evaluacion honesta en datos no vistos",\n    "6. Interpretacion y revision de sesgos",\n    "7. Comunicar una recomendacion clara",\n]\nfor p in pasos:\n    print(p)',
            },
        ],
        "dataset": "clientes, viviendas",
        "exercises": [
            "Define el problema de predecir el precio de <code>viviendas</code>: variable objetivo y métrica (R²).",
            "Calcula una línea base para viviendas (predecir siempre el precio promedio) y su R².",
            "Entrena un modelo de regresión que supere esa línea base.",
            "Optimiza sus hiperparámetros con búsqueda aleatoria o un genético.",
            "Evalúa el modelo final con MAE y RMSE, no solo R².",
            "Interpreta qué variables influyen más en el precio.",
            "Escribe una recomendación de negocio a partir de tus resultados.",
            "Proyecto alternativo: optimiza una ruta con <code>ciudades(12)</code> usando un genético o ACO (módulo L).",
            "Para ese proyecto de rutas, compara tu solución con una línea base (ruta al azar).",
            "Documenta tu proyecto completo en comentarios siguiendo los 7 pasos del flujo.",
        ],
    },

    # ============================================================ CAP 60
    {
        "num": 61,
        "slug": "cierre-siguientes-pasos",
        "code": "leccion_61",
        "title": "Cierre y siguientes pasos",
        "subtitle": "Guardar modelos, armar tu portafolio y escalar más allá del navegador",
        "apunte": "Módulo O · Lección 2 - Cierre de la ruta",
        "concepts": [
            ("Persistencia del modelo", "Guardar un modelo entrenado en disco (<code>joblib</code>) para reutilizarlo sin volver a entrenar."),
            ("Reproducibilidad", "Que tu proyecto se pueda repetir: semillas fijas, versiones, datos y pasos documentados."),
            ("Ficha del modelo (model card)", "Documento breve que describe qué hace el modelo, con qué datos se entrenó, sus límites y su desempeño."),
            ("Portafolio", "Colección de proyectos que demuestran lo que sabes hacer. La mejor carta de presentación de un ingeniero de IA."),
            ("Escalar fuera del navegador", "Para datos grandes o deep learning: salir de Pyodide hacia Colab, servidores o la nube con GPU."),
            ("Frameworks de deep learning", "<b>PyTorch</b> y <b>TensorFlow</b>: construyen y entrenan redes profundas con aceleración por GPU."),
            ("Despliegue (deployment)", "Poner un modelo a funcionar de verdad: una API, una app, o integrado en un producto como PyChoice."),
            ("Aprendizaje continuo", "La IA avanza rápido: la base que aprendiste no cambia, pero las herramientas sí. Seguir aprendiendo es parte del oficio."),
        ],
        "theory": """
<p><b>Llegaste al final de la ruta.</b> Recorriste de la función objetivo a las metaheurísticas, de la
neurona al backpropagation, y de ahí a RL, NLP, recomendadores e IA responsable. Más importante que
cualquier algoritmo: aprendiste a <b>pensar como ingeniero de IA</b> —modelar un problema, elegir una
estrategia de búsqueda u optimización, evaluar con honestidad y comunicar—. Esta lección cierra con lo
que viene después.</p>

<p><b>Guardar lo que entrenas.</b> Entrenar un modelo puede tomar tiempo; no querrás repetirlo cada
vez. Con <b>joblib</b> se <b>guarda</b> un modelo entrenado en un archivo y se <b>carga</b> después,
listo para predecir. Es el primer paso para reutilizar o desplegar un modelo.</p>

<p><b>Reproducibilidad y documentación.</b> Un proyecto serio se puede <b>repetir</b>: semillas fijas,
versiones de librerías anotadas, datos y pasos documentados. Una <b>ficha del modelo</b> (model card)
—qué hace, con qué datos, qué desempeño, qué límites y sesgos— es una práctica profesional cada vez más
esperada, sobre todo por la IA responsable que viste en el módulo N.</p>

<p><b>Arma tu portafolio.</b> La mejor forma de demostrar lo que sabes no es un certificado, sino
<b>proyectos</b>. Toma los problemas de esta ruta —un TSP resuelto con colonia de hormigas, una red que
clasifica, un recomendador— y conviértelos en proyectos limpios y documentados. Un buen portafolio
abre más puertas que cualquier currículum.</p>

<p><b>Escalar fuera del navegador.</b> PyChoice es ideal para <b>aprender</b> ejecutando, pero tiene
límites: todo corre en tu navegador. Para datos grandes, entrenamientos largos o <b>deep learning</b>,
el siguiente paso es salir a <b>Google Colab</b> (gratis, con GPU), a tu propio computador con un
entorno Python, o a la nube. Ahí entran <b>PyTorch</b> y <b>TensorFlow</b>, que construyen redes
profundas con aceleración por GPU. Lo esencial —forward, pérdida, backprop, validación— es idéntico; lo
que aprendiste aquí es exactamente lo que harás allá, a mayor escala.</p>

<p><b>Del modelo al producto.</b> Un modelo entrenado solo sirve si <b>se usa</b>. El <b>despliegue</b>
lo pone a funcionar: una API que responde predicciones, una app, o integrado en un producto —como las
consolas de PyChoice integran Python—. Ese es el salto de «entrené un modelo» a «construí algo que
ayuda a decidir».</p>

<p><b>El oficio continúa.</b> La IA cambia rápido, pero las <b>bases no</b>: optimización, modelos,
evaluación, criterio. Con eso puedes aprender cualquier herramienta nueva. Gracias por recorrer la
ruta; ahora tienes con qué seguir construyendo. <b>El mejor momento para empezar tu próximo proyecto es
ahora.</b></p>
""",
        "examples": [
            {
                "title": "Guardar y cargar un modelo (joblib)",
                "explain": "Entrenamos, guardamos en un archivo y volvemos a cargar el modelo para predecir sin reentrenar.",
                "code": 'import joblib, pandas as pd\nfrom sklearn.ensemble import RandomForestClassifier\n\nX = pd.get_dummies(clientes.drop(columns=["churn"]), drop_first=True)\ny = clientes["churn"]\nmodelo = RandomForestClassifier(n_estimators=100, random_state=7).fit(X, y)\n\njoblib.dump(modelo, "modelo_churn.pkl")      # guardar\ncargado = joblib.load("modelo_churn.pkl")     # cargar\nprint("modelo recargado -> exactitud:", round(cargado.score(X, y), 3))',
            },
            {
                "title": "Una ficha del modelo (model card)",
                "explain": "Un resumen estructurado de qué hace el modelo, cómo se entrenó y sus límites.",
                "code": 'ficha = {\n    "nombre": "Predictor de churn",\n    "tipo": "clasificacion (Random Forest)",\n    "datos": "clientes (200 filas, sinteticos)",\n    "metrica": "AUC ~0.8 en test",\n    "limites": "datos pequenos; revisar sesgo por ciudad/genero",\n    "uso_responsable": "apoyar retencion, no decidir sin revision humana",\n}\nfor k, v in ficha.items():\n    print(f"{k:>16}: {v}")',
            },
            {
                "title": "Checklist de IA responsable",
                "explain": "Preguntas que todo ingeniero de IA debería responder antes de desplegar un modelo.",
                "code": 'checklist = [\n    "¿Supera el modelo a una linea base razonable?",\n    "¿Evalue en datos NO vistos, con la metrica correcta?",\n    "¿Revise el desempeno por grupos (sesgo)?",\n    "¿Puedo explicar por que decide (interpretabilidad)?",\n    "¿Que pasa si se equivoca? ¿cual es el costo?",\n    "¿Hay una persona revisando las decisiones importantes?",\n]\nfor i, q in enumerate(checklist, 1):\n    print(f"[ ] {i}. {q}")',
            },
            {
                "title": "La ruta, de un vistazo",
                "explain": "Un recorrido por todo lo que construiste: de la búsqueda a la IA aplicada.",
                "code": 'ruta = {\n    "J": "Fundamentos: funcion objetivo, busqueda, evaluacion",\n    "K": "Busqueda local: hill climbing, recocido, tabu",\n    "L": "Bioinspiradas: geneticos, PSO, hormigas",\n    "M": "Redes neuronales: perceptron -> backprop -> MLP",\n    "N": "Aplicada: RL, NLP, recomendadores, IA responsable",\n    "O": "Proyecto y cierre: integrar y comunicar",\n}\nprint("Ruta Ingeniero de IA con Python\\n" + "-" * 34)\nfor k, v in ruta.items():\n    print(f"  Modulo {k}: {v}")\nprint("\\nTodo con numpy, scipy y scikit-learn, en el navegador.")',
            },
            {
                "title": "Tu próximo paso",
                "explain": "Ideas concretas para seguir, dentro y fuera de PyChoice.",
                "code": 'siguientes = [\n    "Arma un portafolio con 2-3 proyectos de esta ruta",\n    "Repite un proyecto en Google Colab (gratis, con GPU)",\n    "Aprende PyTorch siguiendo su tutorial oficial",\n    "Explora un dataset real que te interese de verdad",\n    "Combina rutas: usa IO (optimizacion) + IA (prediccion)",\n]\nprint("Siguientes pasos sugeridos:")\nfor s in siguientes:\n    print("  ->", s)',
            },
        ],
        "dataset": "clientes",
        "exercises": [
            "Entrena un modelo, guárdalo con <code>joblib</code> y vuelve a cargarlo.",
            "Verifica que el modelo cargado predice igual que el original.",
            "Escribe una ficha (model card) para un modelo que hayas entrenado en la ruta.",
            "Completa el checklist de IA responsable para tu proyecto de la lección 60.",
            "Haz un resumen en comentarios de los 3 conceptos que más te marcaron de la ruta.",
            "Elige un proyecto de la ruta y escribe cómo lo llevarías a Google Colab.",
            "Investiga y anota en comentarios qué es PyTorch y para qué se usa.",
            "Propón un proyecto que combine la ruta de IA con la de Investigación de Operaciones.",
            "Guarda también el escalador (StandardScaler) junto al modelo y explica por qué es necesario.",
            "Escribe tu plan de aprendizaje para los próximos 3 meses como ingeniero de IA.",
        ],
    },
]
