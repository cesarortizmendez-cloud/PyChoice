# -*- coding: utf-8 -*-
"""
Referencia rapida y COMPLETA de PyChoice.

Documenta todo lo que ofrece la plataforma: el entorno (consolas, atajos,
Excel, helpers), los datasets precargados y todo el Python que se ensena en
las 36 lecciones (de los fundamentos al machine learning).

Convencion para no romper la sintaxis: cada 'ejemplo' se delimita con
comillas simples y por dentro usa SOLO comillas dobles.
"""

# Cada grupo: {id, titulo, ref, nota, filas:[(elemento, que_hace, ejemplo)]}
REFERENCE = [
    # ------------------------------------------------------------------
    {"id": "entorno", "titulo": "Entorno PyChoice", "ref": "Toda la app",
     "nota": "Cada bloque de codigo corre Python real en tu navegador (motor Pyodide/WASM). "
             "No necesitas instalar nada.",
     "filas": [
        ("Ejecutar", "Corre el codigo del bloque", "Ctrl + Enter (o boton «ejecutar»)"),
        ("Tabular", "Inserta 4 espacios (indentacion)", "tecla Tab"),
        ("limpiar", "Borra la salida del bloque", "boton «limpiar»"),
        ("reiniciar", "Restaura el codigo original del bloque", "boton «↻»"),
        ("cargar Excel", "Sube un .xlsx/.csv al DataFrame datos", "boton «cargar excel»"),
        ("exportar Excel", "Descarga un DataFrame como .xlsx", "boton «exportar excel»"),
        ("Consola libre", "Entorno vacio para experimentar", "menu · consola libre"),
        ("Namespace comun", "Las variables se comparten entre bloques de una pagina", "x = 5  # visible en el bloque siguiente"),
     ]},

    {"id": "helpers", "titulo": "Ayudas de datos (exclusivas de PyChoice)", "ref": "Todas las lecciones",
     "nota": "Funciones y objetos que PyChoice deja listos en cada consola para practicar.",
     "filas": [
        ("catalogo()", "Lista todos los datasets disponibles", "catalogo()"),
        ("cargar(nombre)", "Copia un dataset al DataFrame datos", 'df = cargar("propinas")'),
        ("np", "NumPy ya importado", "np.mean(notas)"),
        ("pd", "pandas ya importado", "pd.DataFrame({...})"),
        ("plt", "matplotlib (se activa al primer grafico)", "plt.plot(x, y)"),
        ("notas", "Lista de 8 calificaciones de ejemplo", "sum(notas) / len(notas)"),
        ("datos", "DataFrame base (ventas por region)", "datos.describe()"),
     ]},

    {"id": "datasets", "titulo": "Datasets precargados", "ref": "Pagina · datasets",
     "nota": "Todos vienen listos por su nombre y son reproducibles. Detalle de columnas en la pagina «datasets».",
     "filas": [
        ("notas", "Lista de calificaciones (1.0-7.0), 8 valores", "max(notas)"),
        ("datos / negocio", "Ventas por mes y region, 6 filas", "datos.groupby(\"region\").sum()"),
        ("propinas", "Restaurante: cuenta, propina, dia... 120 filas", "propinas.head()"),
        ("estudiantes", "Horas, asistencia y nota final, 100 filas", 'estudiantes["nota_final"].mean()'),
        ("viviendas", "Superficie, barrio y precio, 150 filas", 'viviendas["precio"].median()'),
        ("clientes", "Gasto y fuga (churn), 200 filas", 'clientes["churn"].mean()'),
        ("empleados", "RRHH: departamento, salario, 120 filas", 'empleados.groupby("departamento").mean(numeric_only=True)'),
        ("clima", "Serie diaria: temperatura y lluvia, 90 dias", 'clima["temp_c"].max()'),
     ]},

    # ------------------------------------------------------------------
    {"id": "fundamentos", "titulo": "Fundamentos de Python", "ref": "Modulo A · Lecciones 1-2",
     "nota": "Lo primero: mostrar valores, guardar datos en variables y comentar.",
     "filas": [
        ("print()", "Muestra valores por pantalla", 'print("Hola", 2026)'),
        ("=", "Asigna un valor a una variable", "x = 42"),
        ("#", "Comentario (Python lo ignora)", "# esto es una nota"),
        ("type()", "Tipo de un objeto", "type(3.14)"),
        ("len()", "Longitud de una secuencia", "len([1, 2, 3])"),
        ("f-string", "Interpola valores en texto", 'f"total: {x}"'),
        ("+ (texto)", "Concatena cadenas", '"data" + "science"'),
        ("int() float() str()", "Convierte entre tipos", 'int("7"), float("3.5"), str(42)'),
        ("bool", "Verdadero / falso", "activo = True"),
     ]},

    {"id": "texto", "titulo": "Cadenas de texto (str)", "ref": "Modulo A · Lecciones 2-3",
     "nota": "Metodos utiles para limpiar y manipular texto.",
     "filas": [
        (".upper() .lower()", "Mayusculas / minusculas", '"Hola".upper()'),
        (".strip()", "Quita espacios de los extremos", '"  hola  ".strip()'),
        (".replace()", "Reemplaza texto", '"a-b-c".replace("-", " ")'),
        (".split()", "Divide en una lista", '"a,b,c".split(",")'),
        (".join()", "Une una lista en texto", '", ".join(["a", "b"])'),
        (".find() / in", "Busca dentro del texto", '"py" in "python"'),
        ("[i:j]", "Rebanada (slicing) de texto", '"python"[0:2]'),
        (".title() .capitalize()", "Capitaliza palabras", '"data science".title()'),
     ]},

    {"id": "numeros", "titulo": "Numeros y operadores", "ref": "Modulo A · Lecciones 2-4",
     "nota": "Aritmetica, comparaciones y logica.",
     "filas": [
        ("+ - * /", "Suma, resta, multiplica, divide", "3 + 4 * 2"),
        ("//  %  **", "Division entera, resto, potencia", "17 // 5, 17 % 5, 2 ** 10"),
        ("== != < > <= >=", "Comparaciones (dan True/False)", "x >= 4"),
        ("and or not", "Operadores logicos", "(x > 0) and (x < 10)"),
        ("round()", "Redondea", "round(3.14159, 2)"),
        ("abs()", "Valor absoluto", "abs(-7)"),
        ("min() max()", "Minimo y maximo", "max(3, 9, 5)"),
        ("sum()", "Suma de una secuencia", "sum([1, 2, 3])"),
     ]},

    {"id": "listas", "titulo": "Listas", "ref": "Modulo C · Leccion 9",
     "nota": "Coleccion ordenada y mutable: la estructura mas usada.",
     "filas": [
        ("[]", "Crea una lista", "xs = [4, 8, 15, 16]"),
        ("xs[i]", "Accede por indice (desde 0)", "xs[0], xs[-1]"),
        ("xs[i:j]", "Rebanada (sublista)", "xs[1:3]"),
        (".append()", "Agrega al final", "xs.append(23)"),
        (".extend()", "Agrega varios", "xs.extend([1, 2])"),
        (".insert() .remove() .pop()", "Inserta / elimina", "xs.pop()"),
        ("sorted() / .sort()", "Ordena", "sorted(xs, reverse=True)"),
        ("in", "Pertenencia", "15 in xs"),
        ("len()", "Cantidad de elementos", "len(xs)"),
     ]},

    {"id": "dicts", "titulo": "Diccionarios, tuplas y conjuntos", "ref": "Modulo C · Leccion 9",
     "nota": "Otras estructuras clave para organizar informacion.",
     "filas": [
        ("{clave: valor}", "Crea un diccionario", 'd = {"a": 1, "b": 2}'),
        ("d[clave]", "Accede a un valor", 'd["a"]'),
        (".get()", "Acceso seguro (sin error)", 'd.get("z", 0)'),
        (".keys() .values() .items()", "Recorrer un dict", "for k, v in d.items(): ..."),
        ("(a, b)", "Tupla (inmutable)", "p = (10, 20)"),
        ("{1, 2, 3}", "Conjunto (sin duplicados)", "set([1, 1, 2])"),
        ("union / intersection", "Operaciones de conjuntos", "a | b, a & b"),
     ]},

    {"id": "control", "titulo": "Control de flujo", "ref": "Modulo A-B · Lecciones 4, 6",
     "nota": "Decidir con condiciones y repetir con bucles.",
     "filas": [
        ("if / elif / else", "Decisiones", 'if x > 0: print("pos")'),
        ("for ... in", "Repite sobre una secuencia", "for n in xs: print(n)"),
        ("range()", "Secuencia de numeros", "for i in range(5): ..."),
        ("while", "Repite mientras se cumpla", "while x > 0: x -= 1"),
        ("break / continue", "Corta / salta iteracion", "if n < 0: break"),
        ("enumerate()", "Indice + valor al recorrer", "for i, v in enumerate(xs): ..."),
        ("zip()", "Recorre dos listas a la vez", "for a, b in zip(xs, ys): ..."),
     ]},

    {"id": "funciones", "titulo": "Funciones", "ref": "Modulo C · Leccion 10",
     "nota": "Empaquetar codigo reutilizable.",
     "filas": [
        ("def", "Define una funcion", "def doble(n): return n * 2"),
        ("return", "Devuelve un resultado", "return total"),
        ("parametros", "Entradas de la funcion", "def saludo(nombre): ..."),
        ("valor por defecto", "Parametro opcional", "def f(x, umbral=4.0): ..."),
        ("*args / **kwargs", "Argumentos variables", "def f(*args): ..."),
        ("lambda", "Funcion anonima de una linea", "cuadrado = lambda x: x ** 2"),
        ("docstring", "Documenta la funcion", 'def f(): "Explica que hace"'),
     ]},

    {"id": "comprensiones", "titulo": "Comprensiones", "ref": "Modulo C · Leccion 11",
     "nota": "Construir colecciones en una linea, de forma clara.",
     "filas": [
        ("lista", "Comprension de lista", "[n * 2 for n in xs]"),
        ("con condicion", "Filtra al construir", "[n for n in xs if n > 4]"),
        ("dict", "Comprension de diccionario", "{k: v for k, v in pares}"),
        ("set", "Comprension de conjunto", "{n % 3 for n in xs}"),
        ("anidada", "Doble bucle", "[i * j for i in a for j in b]"),
     ]},

    {"id": "errores", "titulo": "Errores y archivos", "ref": "Modulo C · Leccion 12",
     "nota": "Manejar fallos sin que el programa se detenga y leer/escribir archivos.",
     "filas": [
        ("try / except", "Captura errores", "try: ... except ZeroDivisionError: ..."),
        ("finally", "Se ejecuta siempre", "finally: print(\"listo\")"),
        ("raise", "Lanza un error propio", 'raise ValueError("dato invalido")'),
        ("with open()", "Abre un archivo con cierre seguro", 'with open("f.txt") as f: ...'),
        (".read() .write()", "Leer / escribir texto", "f.read()"),
        ("pd.read_csv()", "Lee un CSV como DataFrame", 'pd.read_csv("datos.csv")'),
        ("df.to_csv()", "Guarda un DataFrame", 'df.to_csv("out.csv", index=False)'),
     ]},

    # ------------------------------------------------------------------
    {"id": "numpy", "titulo": "NumPy (calculo numerico)", "ref": "Modulo D · Leccion 13",
     "nota": "Arrays y operaciones vectorizadas: rapido y sin bucles.",
     "filas": [
        ("np.array()", "Crea un array", "np.array([1, 2, 3])"),
        ("np.arange() linspace()", "Secuencias numericas", "np.arange(0, 10, 2)"),
        ("np.zeros() ones()", "Arrays de ceros/unos", "np.zeros(5)"),
        (".shape .reshape()", "Forma y redimension", "a.reshape(2, 3)"),
        ("vectorizado", "Opera sobre todo el array", "a * 2 + 1"),
        (".mean() .std() .sum()", "Estadistica rapida", "a.mean(), a.std()"),
        ("mascara booleana", "Filtra por condicion", "a[a > 5]"),
        ("np.where()", "Elige segun condicion", "np.where(a > 0, 1, 0)"),
        ("np.random", "Numeros aleatorios", "np.random.default_rng(7).normal(0, 1, 100)"),
     ]},

    {"id": "pandas-base", "titulo": "pandas · crear, leer y mirar", "ref": "Modulo B-D · Lecciones 5, 7",
     "nota": "La tabla (DataFrame) es el objeto central del analisis de datos.",
     "filas": [
        ("pd.DataFrame()", "Crea una tabla", 'pd.DataFrame({"a": [1, 2]})'),
        ("pd.Series()", "Una columna con indice", "pd.Series([1, 2, 3])"),
        ("pd.read_csv() read_excel()", "Carga datos", 'pd.read_csv("f.csv")'),
        (".head() .tail()", "Primeras / ultimas filas", "df.head(3)"),
        (".info()", "Tipos y nulos por columna", "df.info()"),
        (".describe()", "Resumen estadistico", "df.describe()"),
        (".shape .columns .dtypes", "Forma, columnas y tipos", "df.shape"),
        (".to_csv() .to_excel()", "Exporta la tabla", 'df.to_excel("out.xlsx")'),
     ]},

    {"id": "pandas-sel", "titulo": "pandas · seleccionar y filtrar", "ref": "Modulo D · Leccion 14",
     "nota": "Elegir filas y columnas con precision.",
     "filas": [
        ('df["col"]', "Una columna (Series)", 'df["edad"]'),
        ('df[["a", "b"]]', "Varias columnas", 'df[["mes", "ventas"]]'),
        ("df[condicion]", "Filtra filas", 'df[df["edad"] > 30]'),
        (".loc[]", "Por etiqueta (fila, columna)", 'df.loc[df["x"] > 5, "y"]'),
        (".iloc[]", "Por posicion", "df.iloc[0:5, 0:3]"),
        (".isin()", "Pertenece a un conjunto", 'df[df["region"].isin(["norte", "sur"])]'),
        (".query()", "Filtro tipo texto", 'df.query("ventas > 100")'),
        ("& | ~", "Combina condiciones", 'df[(df["a"] > 1) & (df["b"] < 9)]'),
     ]},

    {"id": "pandas-limpieza", "titulo": "pandas · limpieza", "ref": "Modulo D · Leccion 15",
     "nota": "Preparar datos reales: nulos, duplicados, tipos y texto.",
     "filas": [
        (".isna() .sum()", "Cuenta valores faltantes", "df.isna().sum()"),
        (".dropna()", "Elimina filas con nulos", "df.dropna()"),
        (".fillna()", "Rellena nulos", 'df["x"].fillna(df["x"].mean())'),
        (".drop_duplicates()", "Quita filas repetidas", "df.drop_duplicates()"),
        (".astype()", "Cambia el tipo", 'df["x"].astype(int)'),
        (".rename()", "Renombra columnas", 'df.rename(columns={"a": "b"})'),
        (".replace()", "Reemplaza valores", 'df.replace({"si": 1, "no": 0})'),
        (".str.lower()", "Metodos de texto en columnas", 'df["c"].str.strip()'),
     ]},

    {"id": "pandas-transf", "titulo": "pandas · transformar y ordenar", "ref": "Modulo D · Lecciones 15-16",
     "nota": "Crear columnas, aplicar funciones y ordenar.",
     "filas": [
        ("df[\"nueva\"] = ...", "Crea/actualiza columna", 'df["total"] = df["a"] + df["b"]'),
        (".assign()", "Crea columnas encadenando", 'df.assign(iva=df["p"] * 0.19)'),
        (".apply()", "Aplica una funcion", 'df["x"].apply(lambda v: v * 2)'),
        (".map()", "Mapea valores", 'df["g"].map({"F": 0, "M": 1})'),
        (".sort_values()", "Ordena por columna", 'df.sort_values("precio", ascending=False)'),
        (".nlargest() .nsmallest()", "Top-N filas", 'df.nlargest(5, "ventas")'),
        (".rank()", "Rangos", 'df["p"].rank()'),
     ]},

    {"id": "pandas-group", "titulo": "pandas · agrupar y combinar", "ref": "Modulo B-D · Lecciones 7, 16",
     "nota": "Resumir por grupos y unir tablas.",
     "filas": [
        (".groupby()", "Agrupa y resume", 'df.groupby("region")["ventas"].mean()'),
        (".agg()", "Varias metricas a la vez", 'g.agg(["mean", "count"])'),
        (".value_counts()", "Conteo de categorias", 'df["region"].value_counts()'),
        (".pivot_table()", "Tabla dinamica", 'df.pivot_table(index="dia", values="propina")'),
        ("pd.concat()", "Apila tablas", "pd.concat([a, b])"),
        ("pd.merge()", "Une por clave (JOIN)", 'pd.merge(a, b, on="id")'),
        (".melt() / .pivot()", "Reforma ancho <-> largo", 'df.melt(id_vars="mes")'),
     ]},

    {"id": "pandas-fechas", "titulo": "pandas · fechas y series de tiempo", "ref": "Modulo D · Leccion 17",
     "nota": "Trabajar con fechas y datos temporales.",
     "filas": [
        ("pd.to_datetime()", "Convierte a fecha", 'pd.to_datetime(df["fecha"])'),
        (".dt.year .month .day", "Componentes de la fecha", 'df["fecha"].dt.month'),
        (".dt.day_name()", "Nombre del dia", 'df["fecha"].dt.day_name()'),
        ("pd.date_range()", "Rango de fechas", 'pd.date_range("2024-01-01", periods=30)'),
        (".resample()", "Agrupa por periodo", 'df.resample("ME", on="fecha").sum()'),
        (".rolling()", "Media/suma movil", 'df["temp_c"].rolling(7).mean()'),
        (".dt.to_period()", "Periodo (mes, ano)", 'df["fecha"].dt.to_period("M")'),
     ]},

    # ------------------------------------------------------------------
    {"id": "estadistica", "titulo": "Estadistica descriptiva", "ref": "Modulo E · Lecciones 18-20",
     "nota": "Centro, dispersion, posicion y relaciones.",
     "filas": [
        (".mean() .median()", "Promedio y mediana", 'df["x"].mean()'),
        (".mode()", "Valor mas frecuente", 'df["x"].mode()'),
        (".std() .var()", "Desviacion y varianza", 'df["x"].std()'),
        (".min() .max()", "Extremos", 'df["x"].max()'),
        (".quantile()", "Cuantiles / percentiles", 'df["x"].quantile([.25, .5, .75])'),
        ("IQR (atipicos)", "Rango intercuartil", "q3 - q1"),
        (".corr()", "Matriz de correlacion", "df.corr(numeric_only=True)"),
        (".cov()", "Covarianza", "df.cov(numeric_only=True)"),
        (".describe()", "Resumen completo", "df.describe()"),
     ]},

    {"id": "matplotlib", "titulo": "Visualizacion · Matplotlib", "ref": "Modulo F · Leccion 21",
     "nota": "Graficos base. Recuerda terminar con plt.show().",
     "filas": [
        ("plt.plot()", "Linea", "plt.plot(x, y)"),
        ("plt.scatter()", "Nube de puntos", "plt.scatter(x, y)"),
        ("plt.hist()", "Histograma", "plt.hist(notas, bins=20)"),
        ("plt.bar()", "Barras", "plt.bar(cat, val)"),
        ("plt.subplots()", "Varios graficos", "fig, ax = plt.subplots()"),
        ("plt.title()", "Titulo", 'plt.title("Ventas")'),
        ("plt.xlabel() ylabel()", "Etiquetas de ejes", 'plt.xlabel("mes")'),
        ("plt.legend()", "Leyenda", "plt.legend()"),
        ("plt.show()", "Renderiza el grafico", "plt.show()"),
     ]},

    {"id": "seaborn", "titulo": "Visualizacion · Seaborn", "ref": "Modulo F · Leccion 22",
     "nota": "Graficos estadisticos directos desde el DataFrame (import seaborn as sns).",
     "filas": [
        ("sns.scatterplot()", "Dispersion con color por grupo", 'sns.scatterplot(data=df, x="a", y="b", hue="g")'),
        ("sns.histplot()", "Histograma / densidad", 'sns.histplot(data=df, x="x", hue="g")'),
        ("sns.boxplot()", "Cajas por categoria", 'sns.boxplot(data=df, x="dia", y="propina")'),
        ("sns.barplot()", "Barras con intervalo", 'sns.barplot(data=df, x="g", y="y")'),
        ("sns.countplot()", "Conteo de categorias", 'sns.countplot(data=df, x="region")'),
        ("sns.heatmap()", "Mapa de calor (correlacion)", "sns.heatmap(df.corr(numeric_only=True))"),
     ]},

    {"id": "probabilidad", "titulo": "Probabilidad y distribuciones", "ref": "Modulo G · Lecciones 24-25",
     "nota": "Modelar y simular la incertidumbre.",
     "filas": [
        ("rng.random()", "Numero aleatorio [0,1)", "rng = np.random.default_rng(); rng.random()"),
        ("rng.choice()", "Elige al azar", 'rng.choice(["cara", "sello"], 100)'),
        ("rng.integers()", "Enteros al azar", "rng.integers(1, 7, 10)"),
        ("rng.normal()", "Distribucion normal", "rng.normal(0, 1, 1000)"),
        ("rng.binomial()", "Distribucion binomial", "rng.binomial(10, 0.5, 1000)"),
        ("rng.poisson()", "Distribucion Poisson", "rng.poisson(3, 1000)"),
        ("frecuencia relativa", "Probabilidad empirica", '(df["churn"] == 1).mean()'),
        ("scipy.stats", "Distribuciones teoricas", "from scipy import stats; stats.norm.pdf(x)"),
     ]},

    {"id": "inferencia", "titulo": "Inferencia estadistica (scipy)", "ref": "Modulo G · Leccion 26",
     "nota": "De la muestra a la poblacion: estimar y contrastar (from scipy import stats).",
     "filas": [
        ("stats.ttest_ind()", "Compara dos medias", "stats.ttest_ind(a, b)"),
        ("stats.ttest_1samp()", "Media vs valor de referencia", "stats.ttest_1samp(x, 4.0)"),
        ("stats.norm.interval()", "Intervalo de confianza", "stats.norm.interval(0.95, media, err)"),
        ("stats.pearsonr()", "Correlacion + p-valor", "stats.pearsonr(x, y)"),
        ("stats.chi2_contingency()", "Independencia (categorias)", "stats.chi2_contingency(tabla)"),
        ("p-valor", "Evidencia contra la hipotesis nula", "if p < 0.05: rechazar"),
     ]},

    # ------------------------------------------------------------------
    {"id": "ml-flujo", "titulo": "Machine Learning · flujo y preparacion", "ref": "Modulo H · Lecciones 27-28",
     "nota": "El patron de scikit-learn: separar, escalar, entrenar, predecir (from sklearn...).",
     "filas": [
        ("X, y", "Predictoras y objetivo", 'X = df[cols]; y = df["target"]'),
        ("train_test_split()", "Divide train/test", "X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25)"),
        ("StandardScaler()", "Escala las variables", "sc = StandardScaler(); Xs = sc.fit_transform(X)"),
        ("pd.get_dummies()", "Codifica categorias (one-hot)", 'pd.get_dummies(df, columns=["ciudad"])'),
        (".fit()", "Entrena el modelo", "modelo.fit(X_tr, y_tr)"),
        (".predict()", "Predice", "modelo.predict(X_te)"),
        ("Pipeline()", "Encadena pasos", "Pipeline([(\"sc\", StandardScaler()), (\"m\", modelo)])"),
     ]},

    {"id": "ml-regresion", "titulo": "Machine Learning · regresion", "ref": "Modulo H · Lecciones 29-30",
     "nota": "Predecir numeros continuos y evaluarlos.",
     "filas": [
        ("LinearRegression()", "Regresion lineal", "m = LinearRegression().fit(X, y)"),
        (".coef_ .intercept_", "Coeficientes del modelo", "m.coef_"),
        ("Ridge() Lasso()", "Regresion regularizada", "Ridge(alpha=1.0)"),
        ("r2_score()", "Bondad de ajuste (R2)", "r2_score(y_te, pred)"),
        ("mean_absolute_error()", "Error absoluto medio (MAE)", "mean_absolute_error(y_te, pred)"),
        ("mean_squared_error()", "Error cuadratico (MSE/RMSE)", "mean_squared_error(y_te, pred)"),
        ("residuos", "Real menos predicho", "y_te - pred"),
     ]},

    {"id": "ml-clasificacion", "titulo": "Machine Learning · clasificacion", "ref": "Modulo H · Lecciones 31-33",
     "nota": "Predecir categorias y medir su calidad.",
     "filas": [
        ("LogisticRegression()", "Regresion logistica", "LogisticRegression().fit(X, y)"),
        ("KNeighborsClassifier()", "Vecinos mas cercanos (KNN)", "KNeighborsClassifier(n_neighbors=5)"),
        ("DecisionTreeClassifier()", "Arbol de decision", "DecisionTreeClassifier(max_depth=4)"),
        ("RandomForestClassifier()", "Bosque aleatorio", "RandomForestClassifier(n_estimators=200)"),
        (".predict_proba()", "Probabilidades por clase", "m.predict_proba(X_te)"),
        ("accuracy_score()", "Exactitud", "accuracy_score(y_te, pred)"),
        ("confusion_matrix()", "Matriz de confusion", "confusion_matrix(y_te, pred)"),
        ("classification_report()", "Precision, recall, F1", "print(classification_report(y_te, pred))"),
        ("roc_auc_score()", "Area bajo la curva ROC", "roc_auc_score(y_te, proba)"),
        (".feature_importances_", "Importancia de variables", "modelo.feature_importances_"),
     ]},

    {"id": "ml-avanzado", "titulo": "Machine Learning · validacion y no supervisado", "ref": "Modulo H · Lecciones 34-36",
     "nota": "Generalizar bien, y descubrir estructura sin etiquetas.",
     "filas": [
        ("cross_val_score()", "Validacion cruzada", "cross_val_score(m, X, y, cv=5)"),
        ("GridSearchCV()", "Busca hiperparametros", "GridSearchCV(m, grid, cv=5)"),
        ("sobreajuste", "Train alto, test bajo", "compara score en train vs test"),
        ("KMeans()", "Agrupamiento (clustering)", "KMeans(n_clusters=3).fit(Xs)"),
        (".labels_", "Grupo asignado a cada fila", "km.labels_"),
        ("metodo del codo", "Elegir k", "inercia vs numero de clusters"),
        ("PCA()", "Reduccion de dimensiones", "PCA(n_components=2).fit_transform(Xs)"),
        ("joblib", "Guardar/cargar un modelo", 'joblib.dump(modelo, "m.pkl")'),
     ]},
]


def reference_groups():
    """Grupos de la referencia (para la vista/plantilla)."""
    return REFERENCE


def reference_index():
    """Indice ligero (id + titulo) para la navegacion superior."""
    return [{"id": g["id"], "titulo": g["titulo"]} for g in REFERENCE]
