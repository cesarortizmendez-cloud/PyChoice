# -*- coding: utf-8 -*-
"""
Catalogo de datasets de practica y su asignacion por leccion.

Los DataFrames se generan (reproducibles) en el motor del navegador
(pyengine.js -> _seed / cargar / catalogo). Aqui vive la METADATA que
usa la web: la ficha de cada dataset y, para cada leccion, que datasets
sugerir y con que retos concretos practicar ("aprender haciendo").
"""

# --------------------------------------------------------------------
#  FICHAS DE DATASETS
#  key -> {var, titulo, filas, desc, cols:[(col, tipo, desc)]}
#  Todos vienen precargados por su nombre; ademas cargar('key') los
#  copia a `datos` para reutilizar el codigo de las lecciones.
# --------------------------------------------------------------------
DATASETS = {
    "notas": {
        "var": "notas", "titulo": "notas", "filas": "8 valores", "tipo": "lista",
        "desc": "Lista simple de calificaciones (1.0–7.0). Ideal para primeros pasos, "
                "bucles y estadistica manual.",
        "cols": [("notas", "list[float]", "8 calificaciones de ejemplo")],
    },
    "negocio": {
        "var": "datos", "titulo": "negocio", "filas": "6 filas", "tipo": "DataFrame",
        "desc": "Ventas mensuales por region. Es el DataFrame base `datos`; tabla "
                "pequena y facil de leer completa.",
        "cols": [("mes", "texto", "mes abreviado (ene…jun)"),
                 ("region", "texto", "norte / sur / centro"),
                 ("ventas", "entero", "ventas del mes (miles $)"),
                 ("unidades", "entero", "unidades vendidas"),
                 ("costo", "entero", "costo asociado (miles $)")],
    },
    "propinas": {
        "var": "propinas", "titulo": "propinas", "filas": "120 filas", "tipo": "DataFrame",
        "desc": "Cuentas y propinas de un restaurante. Mezcla de numeros y categorias: "
                "perfecta para agrupar, comparar grupos y graficar.",
        "cols": [("cuenta", "decimal", "total de la cuenta ($)"),
                 ("propina", "decimal", "propina dejada ($)"),
                 ("sexo", "texto", "Mujer / Hombre"),
                 ("fumador", "texto", "si / no"),
                 ("dia", "texto", "jue / vie / sab / dom"),
                 ("momento", "texto", "almuerzo / cena"),
                 ("personas", "entero", "comensales en la mesa")],
    },
    "estudiantes": {
        "var": "estudiantes", "titulo": "estudiantes", "filas": "100 filas", "tipo": "DataFrame",
        "desc": "Horas de estudio, asistencia y nota final. Relacion clara entre "
                "variables: ideal para correlacion, condicionales y regresion.",
        "cols": [("edad", "entero", "17–26 anios"),
                 ("genero", "texto", "F / M"),
                 ("horas_estudio", "decimal", "horas semanales de estudio"),
                 ("asistencia", "decimal", "proporcion de clases (0–1)"),
                 ("nota_final", "decimal", "nota 1.0–7.0"),
                 ("aprobado", "booleano", "True si nota_final ≥ 4.0")],
    },
    "viviendas": {
        "var": "viviendas", "titulo": "viviendas", "filas": "150 filas", "tipo": "DataFrame",
        "desc": "Superficie, barrio y precio de viviendas. Dataset clasico de "
                "regresion: predecir el precio a partir de sus caracteristicas.",
        "cols": [("superficie", "decimal", "metros cuadrados"),
                 ("habitaciones", "entero", "numero de dormitorios"),
                 ("antiguedad", "entero", "anios desde construccion"),
                 ("barrio", "texto", "centro / norte / sur / oriente"),
                 ("precio", "decimal", "precio (unidades $)")],
    },
    "clientes": {
        "var": "clientes", "titulo": "clientes", "filas": "200 filas", "tipo": "DataFrame",
        "desc": "Clientes de un servicio con su gasto y si se fueron (churn). "
                "Dataset estrella para clasificacion y segmentacion.",
        "cols": [("edad", "entero", "18–74 anios"),
                 ("genero", "texto", "F / M"),
                 ("ciudad", "texto", "ciudad del cliente"),
                 ("ingresos", "decimal", "ingreso mensual estimado"),
                 ("antiguedad_meses", "entero", "meses como cliente"),
                 ("gasto_mensual", "decimal", "gasto promedio ($)"),
                 ("churn", "0/1", "1 = se dio de baja")],
    },
    "empleados": {
        "var": "empleados", "titulo": "empleados", "filas": "120 filas", "tipo": "DataFrame",
        "desc": "Datos de RRHH: departamento, salario y satisfaccion. Excelente para "
                "agrupar, comparar y detectar diferencias entre grupos.",
        "cols": [("departamento", "texto", "Ventas / TI / RRHH / Finanzas / Operaciones"),
                 ("edad", "entero", "22–62 anios"),
                 ("genero", "texto", "F / M"),
                 ("antiguedad", "entero", "anios en la empresa"),
                 ("salario", "decimal", "salario mensual"),
                 ("satisfaccion", "decimal", "encuesta 1–5")],
    },
    "clima": {
        "var": "clima", "titulo": "clima", "filas": "90 dias", "tipo": "DataFrame",
        "desc": "Serie diaria de temperatura, humedad y lluvia. Pensado para fechas, "
                "series de tiempo y graficos de linea.",
        "cols": [("fecha", "fecha", "un dia por fila (2024)"),
                 ("ciudad", "texto", "ciudad de la medicion"),
                 ("temp_c", "decimal", "temperatura media (°C)"),
                 ("humedad", "decimal", "humedad relativa (%)"),
                 ("lluvia_mm", "decimal", "lluvia caida (mm)")],
    },
}


# --------------------------------------------------------------------
#  ASIGNACION POR LECCION
#  num -> {"sets": [keys], "retos": [html, ...]}
#  "sets" ordena de mas simple a mas rico segun la leccion.
# --------------------------------------------------------------------
LESSON_DATASETS = {
    1: {"sets": ["notas", "negocio"], "retos": [
        "Ejecuta <code>catalogo()</code> para ver todos los datasets que ya vienen cargados.",
        "Escribe <code>type(notas)</code> y <code>type(datos)</code>: observa la diferencia entre una lista y un DataFrame.",
        "Muestra las primeras filas con <code>datos.head()</code> y cuenta cuantos datasets ofrece <code>catalogo()</code>."]},

    2: {"sets": ["notas", "propinas"], "retos": [
        "Imprime un mensaje con <code>print()</code> que incluya <code>notas[0]</code> usando una f-string.",
        "Guarda en variables el primer y ultimo valor de <code>notas</code> y muestralos concatenando texto.",
        "Con <code>propinas</code>, imprime <code>propinas.shape</code> y explica en un comentario que significan los dos numeros.",
        "Crea una variable <code>resumen</code> con texto que combine cuantas filas y columnas tiene <code>propinas</code>."]},

    3: {"sets": ["propinas", "viviendas"], "retos": [
        "Importa pandas como <code>pd</code> y muestra <code>propinas.head()</code>.",
        "Usa numpy (<code>np.mean</code>) para promediar la columna <code>propinas['cuenta']</code>.",
        "Haz un grafico rapido: <code>viviendas['precio'].plot(kind='hist')</code> y luego <code>plt.show()</code>."]},

    4: {"sets": ["estudiantes", "clientes", "propinas"], "retos": [
        "Toma la primera fila de <code>estudiantes</code> y con <code>if/elif/else</code> imprime si esta 'aprobado', 'en el limite' o 'reprobado'.",
        "Recorre nada: usa <code>estudiantes['nota_final'].mean()</code> y decide con <code>if</code> si el curso va bien.",
        "Con <code>clientes</code>, escribe una condicion que clasifique un cliente como 'VIP' si <code>gasto_mensual &gt; 100</code>.",
        "En <code>propinas</code>, decide con <code>if</code> si una cuenta de $50 corresponde a 'almuerzo' o 'cena' segun el promedio de cada grupo."]},

    5: {"sets": ["negocio", "propinas", "empleados"], "retos": [
        "Usa el boton <b>cargar Excel</b> para subir tu propia planilla a <code>datos</code>, o parte de <code>negocio</code>.",
        "Accede a una columna como variable: <code>ventas = datos['ventas']</code> y muestra su media.",
        "En <code>empleados</code>, crea una nueva columna <code>salario_anual = empleados['salario'] * 12</code>.",
        "Exporta <code>propinas</code> a Excel con el boton <b>guardar Excel</b> y revisa el archivo."]},

    6: {"sets": ["notas", "clima", "propinas"], "retos": [
        "Con un <code>for</code>, recorre <code>notas</code> e imprime cada nota con su posicion.",
        "Acumula: suma todas las <code>notas</code> con un bucle y compara con <code>sum(notas)</code>.",
        "Recorre <code>clima['temp_c']</code> con <code>for</code> y cuenta cuantos dias superaron los 15°C.",
        "Con <code>while</code>, recorre <code>propinas</code> fila a fila hasta encontrar la primera cuenta mayor a $60."]},

    7: {"sets": ["propinas", "empleados", "viviendas"], "retos": [
        "Aplica <code>propinas.describe()</code> e interpreta media, minimo y maximo de <code>cuenta</code>.",
        "Agrupa: <code>propinas.groupby('momento')['propina'].mean()</code>. ¿Se deja mas propina en la cena?",
        "En <code>empleados</code>, calcula el salario promedio por <code>departamento</code>.",
        "Cuenta categorias con <code>viviendas['barrio'].value_counts()</code>."]},

    8: {"sets": ["estudiantes", "clientes", "empleados"], "retos": [
        "Combina pandas + <code>if</code>: crea la columna <code>estado</code> en <code>estudiantes</code> con np.where segun <code>nota_final</code>.",
        "Con un <code>for</code>, recorre los departamentos de <code>empleados</code> e imprime el salario medio de cada uno.",
        "En <code>clientes</code>, usa <code>for</code> + condicion para contar cuantos clientes con churn=1 tienen ingresos bajos.",
        "Calcula el % de aprobados de <code>estudiantes</code> por <code>genero</code> combinando groupby y una condicion."]},

    9: {"sets": ["notas", "propinas"], "retos": [
        "Convierte <code>notas</code> (lista) en un diccionario {posicion: nota} con un bucle.",
        "Crea un conjunto con los dias unicos de <code>propinas['dia']</code> usando <code>set()</code>.",
        "Arma una tupla con (min, max, media) de <code>propinas['cuenta']</code>.",
        "Construye un diccionario que cuente cuantas filas hay por <code>momento</code> en <code>propinas</code>."]},

    10: {"sets": ["estudiantes", "viviendas"], "retos": [
        "Define <code>def resumen(df, col)</code> que imprima media, min y max de una columna; pruebala con <code>estudiantes</code>.",
        "Escribe una funcion que reciba una nota y devuelva 'aprobado'/'reprobado'; aplicala a <code>estudiantes['nota_final']</code>.",
        "Crea <code>def precio_m2(df)</code> que devuelva <code>precio/superficie</code> para <code>viviendas</code>.",
        "Haz una funcion con parametro por defecto <code>umbral=4.0</code> que cuente aprobados en <code>estudiantes</code>."]},

    11: {"sets": ["notas", "propinas", "clientes"], "retos": [
        "Con una comprension, crea la lista de <code>notas</code> aprobadas (≥4.0).",
        "Genera <code>[c*1.1 for c in propinas['cuenta']]</code> (cuentas con 10% extra) y compara promedios.",
        "Crea un diccionario por comprension: ciudad -> nº de clientes, desde <code>clientes</code>.",
        "Filtra con comprension los <code>clientes</code> con <code>gasto_mensual &gt; 100</code> y cuenta cuantos son."]},

    12: {"sets": ["propinas", "empleados"], "retos": [
        "Envuelve en <code>try/except</code> una division que podria fallar (por cero) al calcular propina/personas.",
        "Guarda <code>propinas.to_csv('propinas.csv', index=False)</code> y vuelve a leerlo con <code>pd.read_csv</code>.",
        "Exporta <code>empleados</code> a Excel con el boton y captura con try/except un nombre de columna inexistente.",
        "Maneja con <code>except KeyError</code> el acceso a una columna que no existe en <code>propinas</code>."]},

    13: {"sets": ["notas", "viviendas", "clima"], "retos": [
        "Convierte <code>notas</code> a un array de numpy y calcula media y desviacion estandar vectorizadas.",
        "Con <code>viviendas['superficie'].to_numpy()</code>, normaliza los valores (restar media, dividir por std).",
        "Usa operaciones vectorizadas para pasar <code>clima['temp_c']</code> de °C a °F sin bucles.",
        "Aplica una mascara booleana de numpy para contar dias de <code>clima</code> con lluvia &gt; 0."]},

    14: {"sets": ["propinas", "empleados", "clientes"], "retos": [
        "Selecciona con <code>loc</code> las filas de <code>propinas</code> donde <code>momento == 'cena'</code>.",
        "Con <code>iloc</code>, muestra las primeras 5 filas y 3 columnas de <code>empleados</code>.",
        "Filtra <code>clientes</code> con <code>loc</code>: churn=1 e ingresos &lt; 600.",
        "Selecciona con <code>loc</code> solo las columnas <code>cuenta</code> y <code>propina</code> de las mesas de 4+ personas."]},

    15: {"sets": ["clientes", "empleados", "viviendas"], "retos": [
        "Introduce nulos a proposito (<code>df.loc[0,'ingresos']=np.nan</code>) en una copia de <code>clientes</code> y detectalos con <code>isna().sum()</code>.",
        "Elimina duplicados de <code>empleados</code> con <code>drop_duplicates()</code> y compara <code>shape</code> antes/despues.",
        "Convierte <code>viviendas['habitaciones']</code> a tipo string y de vuelta a entero con <code>astype</code>.",
        "Rellena los nulos que creaste con la media de la columna usando <code>fillna</code>."]},

    16: {"sets": ["negocio", "empleados", "propinas"], "retos": [
        "Agrupa <code>empleados</code> por <code>departamento</code> y obten salario medio y conteo con <code>agg</code>.",
        "Crea una tabla dinamica: <code>propinas.pivot_table(index='dia', columns='momento', values='propina', aggfunc='mean')</code>.",
        "Concatena dos mitades de <code>negocio</code> con <code>pd.concat</code> y verifica el resultado.",
        "Haz un <code>merge</code> entre un resumen por region y <code>negocio</code> para agregar el promedio regional a cada fila."]},

    17: {"sets": ["clima"], "retos": [
        "Extrae componentes de fecha: <code>clima['fecha'].dt.month</code> y <code>.dt.day_name()</code>.",
        "Agrupa <code>clima</code> por mes y calcula la temperatura media mensual.",
        "Filtra los dias de una semana concreta usando comparaciones de fechas sobre <code>clima['fecha']</code>.",
        "Calcula la media movil de 7 dias de <code>temp_c</code> con <code>rolling(7).mean()</code>."]},

    18: {"sets": ["propinas", "clientes", "viviendas"], "retos": [
        "Haz un primer vistazo a <code>clientes</code>: <code>.info()</code>, <code>.describe()</code> y <code>.head()</code>.",
        "Pregunta a los datos: ¿el gasto promedio difiere entre clientes con y sin churn? (groupby).",
        "En <code>propinas</code>, explora si el % de propina cambia por <code>dia</code>.",
        "Detecta a ojo posibles atipicos en <code>viviendas['precio']</code> con <code>describe()</code> y ordenando de mayor a menor."]},

    19: {"sets": ["viviendas", "empleados", "propinas"], "retos": [
        "Calcula media, mediana y desviacion de <code>viviendas['precio']</code>; ¿coinciden media y mediana?",
        "Obten los cuartiles de <code>empleados['salario']</code> con <code>quantile([.25,.5,.75])</code>.",
        "Aplica la regla del rango intercuartil (IQR) para marcar atipicos en <code>propinas['cuenta']</code>.",
        "Compara la dispersion (std) del salario entre dos departamentos de <code>empleados</code>."]},

    20: {"sets": ["estudiantes", "viviendas", "propinas"], "retos": [
        "Calcula la correlacion entre <code>horas_estudio</code> y <code>nota_final</code> en <code>estudiantes</code>.",
        "Grafica la dispersion superficie vs precio de <code>viviendas</code> con <code>plt.scatter</code>.",
        "Obten la matriz de correlacion de <code>propinas</code> (solo columnas numericas) con <code>.corr()</code>.",
        "¿Que se relaciona mas con <code>propina</code>: <code>cuenta</code> o <code>personas</code>? Compara correlaciones."]},

    21: {"sets": ["clima", "propinas", "negocio"], "retos": [
        "Grafico de linea: temperatura diaria de <code>clima</code> con titulo y etiquetas de ejes.",
        "Histograma de <code>propinas['cuenta']</code> con 20 bins.",
        "Grafico de barras de <code>negocio</code>: ventas por mes.",
        "Combina dos series (temp y humedad de <code>clima</code>) en el mismo grafico con leyenda."]},

    22: {"sets": ["propinas", "estudiantes", "clientes"], "retos": [
        "Usa <code>sns.boxplot</code> para comparar <code>propina</code> por <code>momento</code> en <code>propinas</code>.",
        "Haz un <code>sns.scatterplot</code> de horas_estudio vs nota_final coloreando por <code>aprobado</code>.",
        "Dibuja un <code>sns.heatmap</code> de la correlacion de <code>clientes</code>.",
        "Crea un <code>sns.histplot</code> del gasto por <code>churn</code> (hue) en <code>clientes</code>."]},

    23: {"sets": ["clientes", "viviendas", "empleados"], "retos": [
        "Cuenta una historia con <code>clientes</code>: un solo grafico que muestre que el churn cae con la antiguedad.",
        "Elige el grafico correcto para comparar precio por <code>barrio</code> en <code>viviendas</code> y justifica.",
        "Anade un titulo con conclusion (no descriptivo) a un grafico de <code>empleados</code>.",
        "Simplifica: toma un grafico recargado y quita todo lo que no aporte al mensaje."]},

    24: {"sets": ["notas", "clientes", "propinas"], "retos": [
        "Estima la probabilidad de aprobar (nota≥4) usando la frecuencia en <code>notas</code>.",
        "Simula 1000 lanzamientos con <code>np.random</code> y compara con la probabilidad teorica.",
        "Calcula P(churn=1) en <code>clientes</code> como frecuencia relativa.",
        "Estima P(cena | fumador='si') en <code>propinas</code> con probabilidad condicional."]},

    25: {"sets": ["viviendas", "clientes", "clima"], "retos": [
        "Compara el histograma de <code>viviendas['precio']</code> con una normal ajustada (media y std).",
        "Modela el nº de eventos de lluvia por semana en <code>clima</code> con una Poisson.",
        "Simula ingresos con una normal y comparalos con <code>clientes['ingresos']</code>.",
        "Genera una binomial (nº de aprobados en 100 estudiantes) y compara con lo observado."]},

    26: {"sets": ["estudiantes", "propinas", "empleados"], "retos": [
        "Calcula un intervalo de confianza del 95% para la nota media de <code>estudiantes</code>.",
        "Prueba de hipotesis: ¿la propina media difiere entre almuerzo y cena en <code>propinas</code>? (t-test).",
        "Compara el salario medio entre dos departamentos de <code>empleados</code> con una prueba t.",
        "Interpreta el p-valor de una de las pruebas anteriores en una frase."]},

    27: {"sets": ["estudiantes", "viviendas", "clientes"], "retos": [
        "Identifica en cada dataset cual seria la variable objetivo (y) y las predictoras (X).",
        "Separa X e y en <code>viviendas</code> (objetivo: precio) y muestra sus <code>shape</code>.",
        "Explica por que <code>clientes</code> (churn) es clasificacion y <code>viviendas</code> (precio) es regresion.",
        "Prueba el flujo minimo de sklearn con <code>estudiantes</code>: fit + predict de un modelo simple."]},

    28: {"sets": ["clientes", "viviendas", "empleados"], "retos": [
        "Haz <code>train_test_split</code> sobre <code>clientes</code> (objetivo churn) con test_size=0.25.",
        "Escala las columnas numericas de <code>viviendas</code> con <code>StandardScaler</code>.",
        "Codifica <code>ciudad</code> de <code>clientes</code> con one-hot (<code>pd.get_dummies</code>).",
        "Arma un <code>Pipeline</code> que escale y ajuste un modelo sobre <code>empleados</code>."]},

    29: {"sets": ["viviendas", "estudiantes"], "retos": [
        "Ajusta una regresion lineal en <code>viviendas</code> para predecir <code>precio</code> desde <code>superficie</code>.",
        "Interpreta el coeficiente: ¿cuanto sube el precio por m² adicional?",
        "Usa varias variables (superficie, habitaciones, antiguedad) y compara.",
        "Predice la nota final de un estudiante con 8 horas de estudio y 90% de asistencia usando <code>estudiantes</code>."]},

    30: {"sets": ["viviendas", "estudiantes"], "retos": [
        "Calcula MAE, RMSE y R² del modelo de <code>viviendas</code> en el set de prueba.",
        "Grafica los residuos (real − predicho) del modelo y busca patrones.",
        "Compara R² usando 1 variable vs varias en <code>viviendas</code>.",
        "Evalua el modelo de nota de <code>estudiantes</code> e interpreta si el error es aceptable."]},

    31: {"sets": ["clientes", "estudiantes"], "retos": [
        "Entrena una regresion logistica para predecir <code>churn</code> en <code>clientes</code>.",
        "Compara logistica vs KNN vs arbol para predecir <code>aprobado</code> en <code>estudiantes</code>.",
        "Muestra las probabilidades (<code>predict_proba</code>) de churn de 5 clientes.",
        "Cambia el umbral de decision (0.5 → 0.3) y observa como cambian las predicciones."]},

    32: {"sets": ["clientes", "estudiantes"], "retos": [
        "Construye la matriz de confusion del modelo de churn en <code>clientes</code>.",
        "Calcula precision, recall y F1; ¿que importa mas si el costo de perder un cliente es alto?",
        "Dibuja la curva ROC y calcula el AUC para el modelo de <code>clientes</code>.",
        "Compara accuracy vs F1 en <code>estudiantes</code> y explica por que pueden diferir."]},

    33: {"sets": ["clientes", "viviendas"], "retos": [
        "Entrena un <code>RandomForestClassifier</code> sobre <code>clientes</code> y comparalo con la logistica.",
        "Obten la importancia de variables del bosque y grafica las top 5.",
        "Usa <code>RandomForestRegressor</code> en <code>viviendas</code> y compara su R² con la regresion lineal.",
        "Prueba variar <code>n_estimators</code> y observa el efecto en el desempeno."]},

    34: {"sets": ["viviendas", "clientes"], "retos": [
        "Compara el score en train vs test de un arbol profundo en <code>viviendas</code>: ¿hay sobreajuste?",
        "Aplica <code>cross_val_score</code> (5 folds) sobre <code>clientes</code> y reporta media ± std.",
        "Regulariza una regresion con Ridge/Lasso en <code>viviendas</code> y compara coeficientes.",
        "Ajusta <code>max_depth</code> con validacion cruzada y elige el mejor valor."]},

    35: {"sets": ["clientes", "propinas", "viviendas"], "retos": [
        "Escala y aplica <code>KMeans</code> (k=3) a <code>clientes</code>; describe cada segmento.",
        "Usa el metodo del codo para elegir k en <code>clientes</code>.",
        "Aplica <code>PCA</code> a 2 componentes en <code>viviendas</code> y grafica el resultado.",
        "Agrupa <code>propinas</code> por comportamiento (cuenta, propina, personas) y perfila los grupos."]},

    36: {"sets": ["clientes", "viviendas"], "retos": [
        "Proyecto completo con <code>clientes</code>: EDA → limpieza → split → modelo → evaluacion → conclusion.",
        "Documenta cada decision en comentarios como si fuera un informe reproducible.",
        "Compara al menos dos modelos y justifica cual elegirias para produccion.",
        "Repite el flujo con <code>viviendas</code> (regresion) y resume los aprendizajes en 3 frases."]},
}


def datasets_for(num):
    """Devuelve las fichas + retos de una leccion, listas para la plantilla."""
    entry = LESSON_DATASETS.get(num)
    if not entry:
        return None
    fichas = []
    for key in entry["sets"]:
        d = DATASETS.get(key)
        if not d:
            continue
        fichas.append({
            "key": key, "var": d["var"], "titulo": d["titulo"], "filas": d["filas"],
            "tipo": d["tipo"], "desc": d["desc"], "cols": d["cols"],
        })
    return {"fichas": fichas, "retos": entry.get("retos", [])}


def dataset_list():
    """Catalogo completo para la pagina de referencia /datasets."""
    out = []
    for key, d in DATASETS.items():
        out.append({
            "key": key, "var": d["var"], "titulo": d["titulo"], "filas": d["filas"],
            "tipo": d["tipo"], "desc": d["desc"], "cols": d["cols"],
        })
    return out
