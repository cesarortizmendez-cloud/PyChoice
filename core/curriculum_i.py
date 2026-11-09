# -*- coding: utf-8 -*-
"""
Modulo I - Proyecto y cierre (ruta Cientifico de datos).

Leccion 38: Proyecto integrador de data science. El alumno aprende las piezas
(cargar datos, totales, promedios, un grafico con matplotlib y la estructura de
un menu) y al final, en una CONSOLA LIBRE EN BLANCO, construye el mismo un
PANEL DE ANALISIS con menu interactivo para las ventas de una ferreteria.
Cada requisito del desafio apunta al paso y a la leccion donde repasar.

Aplica lo aprendido en las lecciones 1 a 9 (variables, tipos, input, cargar
Excel, bucles, condiciones y estadistica con pandas) y da el primer paso en
matplotlib. El dataset `ferreteria` (500 filas) viene sembrado en el motor del
navegador (pyengine.js) y se puede descargar en Excel.
"""

_XLSX = "/static/core/datasets/ventas_ferreteria.xlsx"

CHAPTERS_I = [
    {
        "num": 38,
        "slug": "proyecto-integrador-ds",
        "code": "leccion_38",
        "title": "Proyecto integrador de data science",
        "subtitle": "Construye tú un menú interactivo para analizar las ventas de una ferretería (pandas + matplotlib)",
        "apunte": "Módulo I · Proyecto - Ciencia de datos",
        "concepts": [
            ("Panel con menú", "Un programa que muestra opciones y repite con <code>while True</code> + <code>input()</code> hasta que eliges «Salir». El usuario manda. (Lecciones 5 y 7)"),
            ("Elegir con if / elif", "Cada opción del menú se ejecuta según lo que el usuario escribe, con <code>if / elif / else</code>. (Lección 4)"),
            ("Totales y promedios", "Responder con pandas: <code>sum()</code>, <code>mean()</code> y <code>groupby()</code> por categoría o sucursal. (Lecciones 8 y 9)"),
            ("Gráficos con matplotlib", "Tu primer gráfico: barras de ingreso por categoría con <code>plt.barh()</code>. El salto a la visualización."),
            ("Calcular con ciclos", "Una opción del menú recorre fila por fila con <code>for … in iterrows()</code> y cuenta con un acumulador. (Lección 7)"),
            ("Consola libre", "Al final construyes tú el panel, desde cero, en una consola en blanco. Cada requisito te dice qué paso y qué lección repasar."),
            ("Del dato a la decisión", "El panel convierte la tabla en respuestas útiles para la ferretería. Es el propósito de PyChoice."),
        ],
        "theory": """
<p>Llegaste al <b>primer proyecto integrador</b> de la ruta. Aquí vas a <b>construir tú mismo</b> un
pequeño <b>panel de análisis</b> para una ferretería: un programa con un <b>menú</b> que te deja
elegir qué calcular —totales, promedios, un gráfico, un conteo— sobre sus ventas. Es la idea de una
herramienta de análisis real, pero hecha por ti y en pocas líneas.</p>

<p><b>El caso.</b> Una ferretería registró <b>500 ventas</b> y quiere entenderlas sin abrir una
planilla cada vez: prefiere un programa que le responda al instante. Tú se lo vas a construir.</p>

<p><b>Los datos.</b> Trabajarás con <code>ferreteria</code>, una tabla con la fecha, la boleta, la
sucursal, la categoría y el producto, la cantidad, el precio unitario, el total (en pesos), el medio
de pago y el vendedor. Ya viene cargada en cada consola; también puedes
<a href="%s" download><b>descargar el archivo Excel</b></a> para mirarlo como lo verías en tu
computador.</p>

<p><b>Cómo trabaja esta lección.</b> Primero, en los pasos 1 a 5, <b>practicas cada pieza por
separado</b> y la dejas funcionando: cargar los datos, calcular totales, promedios, hacer un gráfico
y entender cómo se arma un menú. Después, en el <b>Paso 6</b>, tienes una <b>consola en blanco</b>:
ahí <b>escribes tú</b> el panel completo, juntando las piezas. Cada requisito del desafío te indica a
qué paso y a qué lección volver si no lo recuerdas. Así se aprende de verdad: aplicando.</p>

<p><b>La idea del menú.</b> Un menú es un <b>bucle</b> (<code>while True</code>) que muestra las
opciones, lee tu elección con <code>input()</code> y, según lo que escribas, ejecuta un cálculo con
<code>if / elif / else</code>. Cuando eliges «Salir», el bucle termina con <code>break</code>.</p>

<p><b>Nota sobre los gráficos:</b> dentro de un menú, cuando elijas la opción de gráfico, la imagen se
dibuja y <b>aparece abajo al terminar</b> (cuando eliges «Salir»). Es normal: el panel junta todo y
muestra el gráfico al final.</p>

<p>Al terminar tendrás una pequeña aplicación de análisis <b>hecha por ti</b>, que es justo lo que se
espera de un proyecto de ciencia de datos: convertir datos en respuestas para <b>decidir</b>.</p>
""" % _XLSX,
        "examples": [
            {
                "title": "Paso 1 · Cargar y conocer los datos",
                "explain": "Traemos la planilla a Python con <code>cargar()</code> (lección 6). "
                           "También queda disponible por su nombre, <code>ferreteria</code>. "
                           "Miramos su tamaño, sus columnas y sus primeras filas.",
                "code": '# Cargar las ventas de la ferreteria en `datos`\n'
                        'datos = cargar("ferreteria")\n\n'
                        'print("Filas y columnas:", ferreteria.shape)\n'
                        'print("Columnas:", list(ferreteria.columns))\n'
                        'print()\n'
                        'print(ferreteria.head())',
            },
            {
                "title": "Paso 2 · Calcular «totales» (pandas)",
                "explain": "La pieza para la opción <b>Totales</b> del menú: el ingreso total de la "
                           "ferretería y el ingreso por categoría, de mayor a menor, con "
                           "<code>groupby</code>. (Lección 8)",
                "code": '# Ingreso total ($)\n'
                        'print("Ingreso TOTAL: $", ferreteria["total"].sum())\n\n'
                        '# Ingreso por categoria, de mayor a menor\n'
                        'print("\\nIngreso por categoria ($):")\n'
                        'print(ferreteria.groupby("categoria")["total"].sum().sort_values(ascending=False))',
            },
            {
                "title": "Paso 3 · Calcular «promedios» (pandas)",
                "explain": "La pieza para la opción <b>Promedios</b>: el ticket promedio (lo que gasta un "
                           "cliente por boleta) en general y por sucursal, con <code>mean()</code>. (Lección 8)",
                "code": '# Ticket promedio general\n'
                        'print("Ticket promedio general: $", round(ferreteria["total"].mean()))\n\n'
                        '# Ticket promedio por sucursal\n'
                        'print("\\nTicket promedio por sucursal ($):")\n'
                        'print(ferreteria.groupby("sucursal")["total"].mean().round(0))',
            },
            {
                "title": "Paso 4 · Hacer un «gráfico» (matplotlib)",
                "explain": "La pieza para la opción <b>Gráfico</b>: tu primer gráfico. Dibujamos barras "
                           "horizontales con el ingreso por categoría usando <code>matplotlib</code>. El "
                           "gráfico aparece en el panel de abajo. (¡Nuevo!)",
                "code": '# Tu primer grafico con matplotlib\n'
                        'import matplotlib.pyplot as plt\n\n'
                        '# ingreso por categoria, ordenado de menor a mayor\n'
                        'ingresos = ferreteria.groupby("categoria")["total"].sum().sort_values()\n\n'
                        'plt.figure(figsize=(7, 4))\n'
                        'plt.barh(ingresos.index, ingresos.values, color="#00a37a")\n'
                        'plt.title("Ingreso por categoria ($)")\n'
                        'plt.xlabel("$ total")\n'
                        'plt.tight_layout()\n'
                        'plt.show()',
            },
            {
                "title": "Paso 5 · La estructura de un menú (while + input + if)",
                "explain": "La última pieza: cómo se arma un menú. Un bucle que muestra opciones, lee tu "
                           "elección con <code>input()</code> y decide con <code>if/elif</code>. Al "
                           "ejecutar, responde en los cuadros; escribe <b>3</b> para salir. Fíjate bien en "
                           "esta estructura: es el esqueleto de tu panel. (Lecciones 5 y 7)",
                "code": '# Menu de prueba (todavia sin datos): asi se repite y se elige\n'
                        'while True:\n'
                        '    print("\\n--- MENU DE PRUEBA ---")\n'
                        '    print("1) Saludar")\n'
                        '    print("2) Contar hasta 3")\n'
                        '    print("3) Salir")\n'
                        '    op = input("Elige una opcion (1-3): ")\n'
                        '    if op == "1":\n'
                        '        print("¡Hola, analista!")\n'
                        '    elif op == "2":\n'
                        '        for n in [1, 2, 3]:\n'
                        '            print("  numero", n)\n'
                        '    elif op == "3":\n'
                        '        print("Saliendo del menu...")\n'
                        '        break\n'
                        '    else:\n'
                        '        print("Opcion no valida, intenta de nuevo.")',
            },
            {
                "title": "Paso 6 · Tu desafío · consola libre",
                "explain": "Ahora te toca a ti. Esta consola está <b>en blanco a propósito</b>: aquí "
                           "<b>escribes tú</b> el panel completo, juntando las piezas de los pasos "
                           "anteriores. Hazlo paso a paso; si no recuerdas algo, ve al paso y la lección "
                           "que se indica en cada punto. No copies un bloque entero: constrúyelo tú.<br><br>"
                           "<b>Tu panel debe tener un menú que se repita con estas opciones:</b>"
                           "<ol>"
                           "<li><b>Al inicio, carga los datos</b> con <code>cargar(\"ferreteria\")</code>. "
                           "→ repasa el <b>Paso 1</b> y la <b>Lección 6</b> (cargar Excel).</li>"
                           "<li><b>Un menú que se repite</b> y lee la opción con <code>input()</code>. "
                           "→ <b>Paso 5</b>, <b>Lección 7</b> (bucle <code>while</code>) y <b>Lección 5</b> (<code>input()</code>).</li>"
                           "<li><b>Elegir qué hacer</b> según el número con <code>if / elif / else</code>. "
                           "→ <b>Lección 4</b> (condicionales).</li>"
                           "<li><b>Opción Totales</b>: ingreso total y por categoría. "
                           "→ <b>Paso 2</b> y <b>Lección 8</b> (<code>sum</code>, <code>groupby</code>).</li>"
                           "<li><b>Opción Promedios</b>: ticket promedio por sucursal. "
                           "→ <b>Paso 3</b> y <b>Lección 8</b> (<code>mean</code>).</li>"
                           "<li><b>Opción Gráfico</b>: barras de ingreso por categoría. "
                           "→ <b>Paso 4</b> (matplotlib).</li>"
                           "<li><b>Opción con un ciclo</b>: pide un monto con <code>input()</code> y cuenta "
                           "cuántas ventas lo superan recorriendo la tabla. "
                           "→ <b>Lección 7</b> (<code>for</code>) y <b>Lección 9</b> (<code>for</code> + <code>if</code>).</li>"
                           "<li><b>Opción Salir</b>: termina el menú con <code>break</code>. → <b>Lección 7</b>.</li>"
                           "</ol>"
                           "Empieza por cargar los datos y copiar el esqueleto del menú del <b>Paso 5</b>; "
                           "luego, dentro de cada <code>elif</code>, pega el cálculo del paso que corresponde.",
                "code": '# ===== TU DESAFIO: escribe aqui tu panel de analisis =====\n'
                        '# El DataFrame `ferreteria` ya esta disponible\n'
                        '# (tambien puedes hacer:  datos = cargar("ferreteria")).\n'
                        '#\n'
                        '# Sigue las instrucciones de arriba, opcion por opcion.\n'
                        '# 1) Carga los datos.\n'
                        '# 2) Crea el menu con  while True  +  input().\n'
                        '# 3) Dentro de cada  if / elif  escribe el calculo de cada opcion.\n'
                        '#\n'
                        '# ----- TU CODIGO EMPIEZA AQUI -----\n\n',
            },
        ],
        "dataset": "ferreteria",
        "exercises": [
            "Cuando tu menú funcione, agrega una opción <b>«ingreso por sucursal»</b> con <code>datos.groupby(\"sucursal\")[\"total\"].sum()</code>. (Repasa la <b>Lección 8</b>.)",
            "Agrega una opción <b>«producto más vendido»</b> usando <code>datos[\"producto\"].value_counts().head()</code>. (<b>Lección 8</b>.)",
            "Agrega una opción <b>«ingreso por vendedor»</b> ordenado de mayor a menor con <code>sort_values(ascending=False)</code>.",
            "Agrega un gráfico del <b>número de ventas por sucursal</b> (<code>value_counts()</code> + <code>plt.bar()</code>). (Repasa el <b>Paso 4</b>.)",
            "Agrega una opción que pida una <b>categoría</b> con <code>input()</code> y muestre cuántas ventas e ingreso tuvo. (<b>Lecciones 5 y 9</b>.)",
            "Con un <b>ciclo <code>for</code></b>, cuenta cuántas ventas se pagaron con <code>\"Efectivo\"</code> y agrégalo como opción. (<b>Lecciones 7 y 9</b>.)",
            "Mejora la opción del ciclo: además de contar, <b>suma</b> el total de esas ventas y muestra su <b>porcentaje</b> del total.",
            "Crea una columna <code>precio_con_iva = precio_unit * 1.19</code> y úsala en alguna opción. (<b>Lección 9</b>: columna derivada.)",
            "Reto final: agrega una opción <b>«informe completo»</b> que muestre de una vez el ingreso total, el ticket promedio y la categoría estrella, y termine con una recomendación para la ferretería.",
        ],
    },
]
