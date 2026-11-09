# -*- coding: utf-8 -*-
"""
Modulo I - Proyecto y cierre (ruta Cientifico de datos).

Leccion 38: Proyecto integrador de data science. Un primer proyecto completo
que aplica TODO lo aprendido en las lecciones 1 a 9 (variables, tipos, input,
cargar Excel, bucles for/while, condiciones y estadistica con pandas) sobre un
caso real: las ventas de una ferreteria. El alumno describe los datos, los
agrupa y realiza calculos con ciclos para, al final, decidir con datos.

El dataset `ferreteria` (500 filas) viene sembrado en el motor del navegador
(pyengine.js) y ademas se puede descargar en Excel.
"""

_XLSX = "/static/core/datasets/ventas_ferreteria.xlsx"

CHAPTERS_I = [
    {
        "num": 38,
        "slug": "proyecto-integrador-ds",
        "code": "leccion_38",
        "title": "Proyecto integrador de data science",
        "subtitle": "Analiza las ventas de una ferretería aplicando todo lo de las lecciones 1 a 9",
        "apunte": "Módulo I · Proyecto - Ciencia de datos",
        "concepts": [
            ("Cargar los datos", "Traer una planilla a Python como DataFrame con <code>cargar(\"ferreteria\")</code> y mirarla con <code>head()</code>, <code>shape</code> y <code>columns</code>. (Lección 6)"),
            ("Describir", "Resumir los números con <code>describe()</code> y contar categorías con <code>value_counts()</code>. (Lección 8)"),
            ("Agrupar", "Responder preguntas de negocio con <code>groupby()</code>: ingreso por categoría, ticket por sucursal. (Lección 8)"),
            ("Calcular con ciclos", "Recorrer fila por fila con <code>for … in iterrows()</code> y acumular con un contador o un diccionario. (Lección 7)"),
            ("Condiciones", "Decidir dentro del bucle con <code>if</code>: contar y sumar solo lo que cumple una regla. (Lecciones 4 y 9)"),
            ("Entrada del usuario", "Hacer el análisis interactivo con <code>input()</code>: el usuario elige el umbral. (Lección 5)"),
            ("Del dato a la decisión", "Cerrar con una conclusión accionable: qué categoría reforzar. Es el propósito de PyChoice."),
        ],
        "theory": """
<p>Llegaste al <b>primer proyecto integrador</b> de la ruta. Hasta aquí aprendiste las piezas por
separado; ahora las vas a <b>juntar todas</b> en un caso real, igual que lo haría un analista de
datos en su trabajo. No hay conceptos nuevos: solo las lecciones <b>1 a 9</b> puestas a trabajar
sobre un problema concreto.</p>

<p><b>El caso.</b> Una <b>ferretería</b> registró sus ventas y quiere entenderlas: ¿qué se vende
más?, ¿qué categoría deja más ingreso?, ¿cuánto pesan las ventas grandes?, ¿en qué sucursal el
ticket es más alto? Tu trabajo es responder con datos y terminar con una <b>recomendación</b>.</p>

<p><b>Los datos.</b> Trabajarás con <code>ferreteria</code>, una tabla de <b>500 ventas</b> con la
fecha, la boleta, la sucursal, la categoría y el producto, la cantidad, el precio unitario, el total
(en pesos), el medio de pago y el vendedor. Ya viene cargada en cada consola; también puedes
<a href="%s" download><b>descargar el archivo Excel</b></a> para mirarlo como lo verías en tu
computador.</p>

<p><b>El plan (como un analista de verdad).</b> Un análisis de datos sigue siempre los mismos pasos,
y cada uno usa algo que ya sabes:</p>

<p>1) <b>Cargar y conocer</b> los datos (lección 6): cuántas filas y columnas, qué significan.<br>
2) <b>Describir</b> (lección 8): promedios, mínimos, máximos y conteos para tener una foto general.<br>
3) <b>Agrupar</b> (lección 8): comparar por categoría y por sucursal con <code>groupby</code>.<br>
4) <b>Calcular con ciclos</b> (lecciones 7 y 9): recorrer la tabla fila por fila con un
<code>for</code> y acumular resultados, incluso decidiendo con <code>if</code> dentro del bucle.<br>
5) <b>Decidir</b>: convertir los números en una conclusión para la ferretería.</p>

<p><b>Por qué calcular "a mano" con un ciclo si pandas ya lo hace.</b> Porque entender el
<b>mecanismo</b> es lo que te hace analista y no solo usuario de una librería. Verás que el ingreso
total calculado con un <code>for</code> da <b>exactamente lo mismo</b> que <code>datos["total"].sum()</code>:
la vectorización de pandas es el atajo rápido del ciclo que tú ya sabes escribir. Aprende las dos
formas; usa el ciclo para pensar y pandas para producir.</p>

<p>Trabaja los bloques en orden: cada uno es un paso del análisis. Al final tendrás un informe
pequeño y una recomendación, que es justo lo que se espera de un proyecto de ciencia de datos.</p>
""" % _XLSX,
        "examples": [
            {
                "title": "Paso 1 · Cargar y conocer los datos",
                "explain": "Traemos la planilla a Python con <code>cargar()</code> (lección 6). "
                           "También queda disponible por su nombre, <code>ferreteria</code>. "
                           "Miramos su tamaño, sus columnas y sus primeras filas.",
                "code": '# Cargar las ventas de la ferreteria en `datos` (asi puedes exportarlas a Excel)\n'
                        'datos = cargar("ferreteria")\n\n'
                        'print("Filas y columnas:", ferreteria.shape)\n'
                        'print("Columnas:", list(ferreteria.columns))\n'
                        'print()\n'
                        'print(ferreteria.head())',
            },
            {
                "title": "Paso 2 · Describir los datos",
                "explain": "Una foto general: <code>dtypes</code> dice el tipo de cada columna y "
                           "<code>describe()</code> resume las numéricas (promedio, mínimo, máximo). (Lección 8)",
                "code": '# ¿Que tipo de dato tiene cada columna?\n'
                        'print(ferreteria.dtypes)\n\n'
                        'print("\\nResumen de las columnas numericas:")\n'
                        'print(ferreteria[["cantidad", "precio_unit", "total"]].describe().round(0))',
            },
            {
                "title": "Paso 3 · Contar categorías (value_counts)",
                "explain": "Para las columnas de texto, <code>value_counts()</code> cuenta cuántas "
                           "veces aparece cada valor. Así vemos qué se vende y dónde. (Lección 8)",
                "code": '# ¿Cuantas ventas hay por categoria, por sucursal y por medio de pago?\n'
                        'print("Ventas por categoria:")\n'
                        'print(ferreteria["categoria"].value_counts())\n\n'
                        'print("\\nVentas por sucursal:")\n'
                        'print(ferreteria["sucursal"].value_counts())\n\n'
                        'print("\\nMedio de pago mas usado:", ferreteria["medio_pago"].mode()[0])',
            },
            {
                "title": "Paso 4 · Agrupar para responder preguntas (groupby)",
                "explain": "La pregunta clave del negocio: ¿qué categoría deja más ingreso? "
                           "<code>groupby</code> agrupa y suma por categoría; luego ordenamos. (Lección 8)",
                "code": '# Ingreso total ($) por categoria, de mayor a menor\n'
                        'ingresos = ferreteria.groupby("categoria")["total"].sum().sort_values(ascending=False)\n'
                        'print("Ingreso por categoria ($):")\n'
                        'print(ingresos)\n\n'
                        'print("\\nTicket promedio por sucursal ($):")\n'
                        'print(ferreteria.groupby("sucursal")["total"].mean().round(0))',
            },
            {
                "title": "Paso 5 · Un cálculo con un CICLO (for + if)",
                "explain": "El mismo ingreso total, pero calculado <b>a mano</b> recorriendo fila por "
                           "fila con <code>for … in iterrows()</code> y acumulando. De paso contamos las "
                           "ventas grandes con un <code>if</code>. Compara: da lo mismo que pandas. (Lecciones 7 y 9)",
                "code": '# Recorremos la tabla fila por fila y vamos acumulando\n'
                        'ingreso_total = 0\n'
                        'ventas_grandes = 0\n'
                        'for i, fila in ferreteria.iterrows():\n'
                        '    ingreso_total += fila["total"]\n'
                        '    if fila["total"] > 50000:\n'
                        '        ventas_grandes += 1\n\n'
                        'print("Ingreso total (con ciclo): ", ingreso_total)\n'
                        'print("Comprobacion con pandas:   ", ferreteria["total"].sum())\n'
                        'print("Ventas sobre $50.000:", ventas_grandes)',
            },
            {
                "title": "Paso 6 · Ciclo + diccionario: la categoría estrella",
                "explain": "Acumulamos el ingreso por categoría en un <b>diccionario</b> con un "
                           "<code>for</code>, y luego recorremos el diccionario para encontrar el máximo. "
                           "Así se piensa un cálculo antes de conocer <code>groupby</code>.",
                "code": '# Acumular el ingreso de cada categoria en un diccionario\n'
                        'acum = {}\n'
                        'for i, fila in ferreteria.iterrows():\n'
                        '    cat = fila["categoria"]\n'
                        '    acum[cat] = acum.get(cat, 0) + fila["total"]\n\n'
                        '# Buscar la categoria con mas ingreso recorriendo el diccionario\n'
                        'mejor = ""\n'
                        'mejor_monto = 0\n'
                        'for cat, monto in acum.items():\n'
                        '    if monto > mejor_monto:\n'
                        '        mejor_monto = monto\n'
                        '        mejor = cat\n\n'
                        'print("Ingreso por categoria:")\n'
                        'for cat, monto in acum.items():\n'
                        '    print("  ", cat, "->", monto)\n'
                        'print("\\nCategoria estrella:", mejor, "con $", mejor_monto)',
            },
            {
                "title": "Paso 7 · Análisis interactivo con input()",
                "explain": "Hacemos el análisis a la medida: el usuario escribe desde qué monto "
                           "considera una «venta grande» y contamos cuántas hay. Integra "
                           "<code>input()</code>, el ciclo y la condición. (Lecciones 5, 7 y 9)",
                "code": '# Al ejecutar, aparece un cuadro para escribir el monto\n'
                        'umbral = int(input("¿Desde que monto es una venta grande? (ej: 40000) "))\n\n'
                        'cuenta = 0\n'
                        'suma = 0\n'
                        'for i, fila in ferreteria.iterrows():\n'
                        '    if fila["total"] >= umbral:\n'
                        '        cuenta += 1\n'
                        '        suma += fila["total"]\n\n'
                        'print("Ventas desde $", umbral, "->", cuenta, "boletas")\n'
                        'print("Suman en total: $", suma)\n'
                        'print("Son el", round(100 * cuenta / len(ferreteria), 1), "% de las ventas")',
            },
            {
                "title": "Paso 8 · Informe final y recomendación",
                "explain": "Cerramos como un analista: un resumen por categoría (número de ventas, "
                           "ingreso y ticket promedio) y una <b>recomendación</b>. Prueba el botón "
                           "<b>exportar excel</b> con el objeto <code>resumen</code>.",
                "code": '# Resumen por categoria: cuantas ventas, cuanto ingreso y ticket promedio\n'
                        'resumen = ferreteria.groupby("categoria")["total"].agg(["count", "sum", "mean"]).round(0)\n'
                        'resumen = resumen.sort_values("sum", ascending=False)\n'
                        'resumen.columns = ["ventas", "ingreso_$", "ticket_prom_$"]\n'
                        'print(resumen)\n\n'
                        'top = resumen.index[0]\n'
                        'print("\\nRecomendacion: reforzar el stock y la promocion de la categoria")\n'
                        'print("\'" + top + "\', que es la que mas ingreso genera para la ferreteria.")',
            },
        ],
        "dataset": "ferreteria",
        "exercises": [
            "Muestra las <b>últimas</b> 10 filas con <code>ferreteria.tail(10)</code> y di qué fechas abarca.",
            "¿Cuál es el <b>producto</b> más vendido (por número de ventas)? Usa <code>value_counts()</code> sobre la columna <code>producto</code>.",
            "Crea una columna nueva <code>precio_con_iva = precio_unit * 1.19</code> y muéstrala junto a <code>producto</code>.",
            "Con un <b>ciclo <code>for</code> y un <code>if</code></b>, cuenta cuántas ventas se pagaron con <code>\"Efectivo\"</code>.",
            "Con <code>groupby</code>, calcula el <b>ingreso total por sucursal</b> y ordénalo de mayor a menor.",
            "Con un <b>acumulador y un ciclo</b>, suma el <code>total</code> solo de las ventas de la categoría <code>\"Pinturas\"</code>.",
            "Filtra las ventas con <code>total &gt; 100000</code> (condición booleana) y cuenta cuántas hay con <code>len()</code>.",
            "Usando <code>input()</code>, pide una <b>categoría</b> al usuario y muestra cuántas ventas y cuánto ingreso tuvo esa categoría.",
            "Reto final: arma un <b>informe por vendedor</b> (número de ventas e ingreso total) con <code>groupby</code>, ordénalo y escribe en un comentario quién fue el mejor vendedor.",
        ],
    },
]
