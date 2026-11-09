# -*- coding: utf-8 -*-
"""
Modulo I - Proyecto y cierre (ruta Cientifico de datos).

Leccion 38: Proyecto integrador de data science. El alumno construye, de forma
GRADUAL y didactica, un PANEL DE ANALISIS con menu interactivo para las ventas
de un negocio (ferreteria + 4 negocios con el MISMO esquema).

CLAVE UX: en las consolas de PyChoice la salida (print) se muestra al TERMINAR
la ejecucion, no durante el bucle. Por eso el MENU va DENTRO de input() (como un
texto), asi sus opciones se ven en el cuadro emergente al elegir. Los resultados
aparecen en la consola de abajo cuando el alumno sale del menu (transcripcion).

Estructura:
  - Pasos 1-4: las PIEZAS por separado (cargar, totales, promedios, grafico).
  - Practicas 1-3: construir el menu PASO A PASO (1 opcion -> varias -> + grafico).
  - Paso final: CONSOLA LIBRE en blanco para que el alumno arme/ample el suyo.

Dataset `ferreteria` (y panaderia/farmacia/libreria/minimarket, mismo esquema)
sembrado en pyengine.js; descargable en Excel.
"""

_XLSX = "/static/core/datasets/ventas_ferreteria.xlsx"

CHAPTERS_I = [
    {
        "num": 38,
        "slug": "proyecto-integrador-ds",
        "code": "leccion_38",
        "title": "Proyecto integrador de data science",
        "subtitle": "Construye paso a paso un menú para analizar las ventas de una ferretería (pandas + matplotlib)",
        "apunte": "Módulo I · Proyecto - Ciencia de datos",
        "concepts": [
            ("Las piezas primero", "Antes del menú, practicas cada cálculo por separado: totales, promedios y un gráfico. Así, al armar el menú, solo los conectas."),
            ("El menú va en input()", "En estas consolas la salida se muestra al terminar. Por eso el menú se pone <b>dentro de <code>input()</code></b>: así sus opciones aparecen en el cuadro emergente cuando eliges. (Lecciones 5 y 7)"),
            ("Un menú crece con elif", "El menú parte con <b>una</b> opción y va creciendo: cada nueva opción es un <code>elif</code> más dentro del mismo bucle. (Lección 4)"),
            ("Cálculos con pandas", "Cada opción responde con <code>sum()</code>, <code>mean()</code>, <code>groupby()</code> o un ciclo <code>for</code>. (Lecciones 7, 8 y 9)"),
            ("Gráficos con matplotlib", "Una opción dibuja barras de ingreso por categoría con <code>plt.barh()</code>. El salto a la visualización."),
            ("Un panel, varios negocios", "El mismo panel sirve para otros rubros: cambia <code>cargar(\"ferreteria\")</code> por <code>cargar(\"panaderia\")</code>, <code>\"farmacia\"</code>, <code>\"libreria\"</code> o <code>\"minimarket\"</code>. Todos tienen las mismas columnas."),
            ("Consola libre", "Al final, en una consola en blanco, construyes y amplías tú tu propio panel. Cada requisito te dice qué práctica y qué lección repasar."),
        ],
        "theory": """
<p>Llegaste al <b>primer proyecto integrador</b> de la ruta. Vas a construir, <b>paso a paso</b>, un
pequeño <b>panel de análisis</b> para una ferretería: un programa con un <b>menú</b> que te deja
elegir qué calcular —totales, promedios, un gráfico, un conteo— sobre sus ventas.</p>

<p><b>El caso.</b> Una ferretería registró <b>500 ventas</b> y quiere entenderlas sin abrir una
planilla cada vez: prefiere un programa que le responda. Tú se lo vas a construir.</p>

<p><b>Los datos.</b> Trabajarás con <code>ferreteria</code>: fecha, boleta, sucursal, categoría,
producto, cantidad, precio unitario, total (en pesos), medio de pago y vendedor. Ya viene cargada en
cada consola; también puedes
<a href="%s" download><b>descargar el archivo Excel</b></a> para mirarlo en tu computador.</p>

<p><b>Importante · cómo se ve un menú aquí.</b> En las consolas de PyChoice, lo que imprimes con
<code>print()</code> aparece en la consola <b>cuando termina</b> todo el programa. Por eso, para que
veas las opciones <b>en el cuadro emergente</b> al momento de elegir, el menú se escribe <b>dentro de
<code>input()</code></b>, como un texto con varias líneas. Es decir: en vez de imprimir las opciones y
luego preguntar, pones todo junto en la pregunta. Cuando sales del menú («Salir»), la consola de abajo
te muestra el <b>resultado de cada opción</b> que elegiste, en orden (una transcripción de tu sesión).</p>

<p><b>Cómo vamos a construir el menú (de a poco).</b> Primero <b>las piezas</b> (pasos 1 a 4): cada
cálculo por separado —cargar, totales, promedios y un gráfico—. Después <b>el menú en tres prácticas</b>
que crecen: P1 el menú mínimo (una opción + salir), P2 con varias opciones, P3 con el gráfico. Y al
final, <b>tú</b>, en una consola en blanco.</p>

<p><b>Un panel que sirve para cualquier negocio.</b> Tienes otros cuatro datasets con <b>las mismas
columnas</b> —una <b>panadería</b>, una <b>farmacia</b>, una <b>librería</b> y un <b>minimarket</b>—.
Cuando tu panel funcione, cambia <code>cargar("ferreteria")</code> por <code>cargar("panaderia")</code>,
<code>cargar("farmacia")</code>, <code>cargar("libreria")</code> o <code>cargar("minimarket")</code> y
verás el <b>mismo análisis</b> sobre otro negocio. (Escribe <code>catalogo()</code> para verlos todos.)</p>

<p><b>Nota sobre los gráficos:</b> cuando elijas la opción de gráfico, la imagen se dibuja y
<b>aparece abajo al terminar</b> (cuando eliges «Salir»).</p>
""" % _XLSX,
        "examples": [
            {
                "title": "Paso 1 · Cargar y conocer los datos",
                "explain": "Traemos la planilla a Python con <code>cargar()</code> (lección 6). También "
                           "queda disponible por su nombre, <code>ferreteria</code>. Miramos su tamaño, "
                           "sus columnas y sus primeras filas.",
                "code": '# Cargar las ventas de la ferreteria en `datos`\n'
                        'datos = cargar("ferreteria")\n\n'
                        'print("Filas y columnas:", ferreteria.shape)\n'
                        'print("Columnas:", list(ferreteria.columns))\n'
                        'print()\n'
                        'print(ferreteria.head())',
            },
            {
                "title": "Paso 2 · La pieza «totales» (pandas)",
                "explain": "El cálculo que usará la opción <b>Totales</b>: el ingreso total y el ingreso "
                           "por categoría, de mayor a menor, con <code>groupby</code>. (Lección 8)",
                "code": '# Ingreso total ($)\n'
                        'print("Ingreso TOTAL: $", ferreteria["total"].sum())\n\n'
                        '# Ingreso por categoria, de mayor a menor\n'
                        'print("\\nIngreso por categoria ($):")\n'
                        'print(ferreteria.groupby("categoria")["total"].sum().sort_values(ascending=False))',
            },
            {
                "title": "Paso 3 · La pieza «promedios» (pandas)",
                "explain": "El cálculo de la opción <b>Promedios</b>: el ticket promedio (lo que gasta un "
                           "cliente por boleta) en general y por sucursal, con <code>mean()</code>. (Lección 8)",
                "code": '# Ticket promedio general\n'
                        'print("Ticket promedio general: $", round(ferreteria["total"].mean()))\n\n'
                        '# Ticket promedio por sucursal\n'
                        'print("\\nTicket promedio por sucursal ($):")\n'
                        'print(ferreteria.groupby("sucursal")["total"].mean().round(0))',
            },
            {
                "title": "Paso 4 · La pieza «gráfico» (matplotlib)",
                "explain": "El cálculo de la opción <b>Gráfico</b>: tu primer gráfico. Barras horizontales "
                           "con el ingreso por categoría usando <code>matplotlib</code>. El gráfico "
                           "aparece en el panel de abajo. (¡Nuevo!)",
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
                "title": "Práctica 1 · Tu primer menú (una opción + salir)",
                "explain": "El <b>menú más pequeño que funciona</b>: una opción real + «Salir». Fíjate en la "
                           "clave: el texto del menú va <b>dentro de <code>input()</code></b> (en la variable "
                           "<code>menu</code>), así <b>ves las opciones en el cuadro emergente</b> al elegir. "
                           "Ejecútalo, escribe <b>1</b> y luego <b>2</b>; al salir verás el resultado abajo. "
                           "(Lecciones 4, 5 y 7)",
                "code": 'datos = cargar("ferreteria")\n\n'
                        '# El menu es un TEXTO de varias lineas: va dentro de input()\n'
                        'menu = """===== PANEL FERRETERIA =====\n'
                        '1) Ver ingreso total\n'
                        '2) Salir\n'
                        'Elige una opcion (1-2): """\n\n'
                        'while True:\n'
                        '    op = input(menu)          # el menu se ve en el cuadro\n'
                        '    print(">>> Elegiste la opcion", op)\n'
                        '    if op == "1":\n'
                        '        print("Ingreso TOTAL: $", datos["total"].sum())\n'
                        '    elif op == "2":\n'
                        '        print("¡Hasta pronto!")\n'
                        '        break\n'
                        '    else:\n'
                        '        print("Opcion no valida, intenta de nuevo.")',
            },
            {
                "title": "Práctica 2 · Un menú con varias opciones de análisis",
                "explain": "Un menú <b>crece agregando <code>elif</code></b>. Sumamos opciones de análisis "
                           "(ingreso por categoría, promedios y un <b>conteo con ciclo</b>). Cada opción es un "
                           "<code>elif</code> con el cálculo de los pasos 2 y 3. Recuerda: el menú va en "
                           "<code>input()</code>, y los resultados se ven al salir. (Lecciones 7, 8 y 9)",
                "code": 'datos = cargar("ferreteria")\n\n'
                        'menu = """===== PANEL FERRETERIA =====\n'
                        '1) Ingreso total\n'
                        '2) Ingreso por categoria\n'
                        '3) Ticket promedio por sucursal\n'
                        '4) Contar ventas grandes (con un ciclo)\n'
                        '5) Salir\n'
                        'Elige una opcion (1-5): """\n\n'
                        'while True:\n'
                        '    op = input(menu)\n'
                        '    print(">>> Elegiste la opcion", op)\n'
                        '    if op == "1":\n'
                        '        print("Ingreso TOTAL: $", datos["total"].sum())\n'
                        '    elif op == "2":                       # nuevo\n'
                        '        print(datos.groupby("categoria")["total"].sum().sort_values(ascending=False))\n'
                        '    elif op == "3":                       # nuevo\n'
                        '        print(datos.groupby("sucursal")["total"].mean().round(0))\n'
                        '    elif op == "4":                       # nuevo: usa un ciclo for\n'
                        '        umbral = int(input("¿Desde que monto es una venta grande? "))\n'
                        '        n = 0\n'
                        '        for i, fila in datos.iterrows():\n'
                        '            if fila["total"] >= umbral:\n'
                        '                n += 1\n'
                        '        print("Ventas desde $", umbral, "->", n, "boletas")\n'
                        '    elif op == "5":\n'
                        '        print("¡Hasta pronto!")\n'
                        '        break\n'
                        '    else:\n'
                        '        print("Opcion no valida.")',
            },
            {
                "title": "Práctica 3 · Agrega la opción de gráfico (el panel completo)",
                "explain": "Última capa: agregamos la opción de <b>gráfico</b> con matplotlib (la pieza del "
                           "paso 4) como una opción más. Con esto queda el <b>panel completo</b>. El gráfico "
                           "aparece abajo cuando eliges «Salir». Pide el gráfico (opción 5) antes de salir.",
                "code": 'import matplotlib.pyplot as plt\n'
                        'datos = cargar("ferreteria")\n\n'
                        'menu = """===== PANEL FERRETERIA =====\n'
                        '1) Ingreso total\n'
                        '2) Ingreso por categoria\n'
                        '3) Ticket promedio por sucursal\n'
                        '4) Contar ventas grandes (con un ciclo)\n'
                        '5) Grafico: ingreso por categoria\n'
                        '6) Salir\n'
                        'Elige una opcion (1-6): """\n\n'
                        'while True:\n'
                        '    op = input(menu)\n'
                        '    print(">>> Elegiste la opcion", op)\n'
                        '    if op == "1":\n'
                        '        print("Ingreso TOTAL: $", datos["total"].sum())\n'
                        '    elif op == "2":\n'
                        '        print(datos.groupby("categoria")["total"].sum().sort_values(ascending=False))\n'
                        '    elif op == "3":\n'
                        '        print(datos.groupby("sucursal")["total"].mean().round(0))\n'
                        '    elif op == "4":\n'
                        '        umbral = int(input("¿Desde que monto es una venta grande? "))\n'
                        '        n = 0\n'
                        '        for i, fila in datos.iterrows():\n'
                        '            if fila["total"] >= umbral:\n'
                        '                n += 1\n'
                        '        print("Ventas desde $", umbral, "->", n, "boletas")\n'
                        '    elif op == "5":                       # nuevo: grafico\n'
                        '        ingresos = datos.groupby("categoria")["total"].sum().sort_values()\n'
                        '        plt.figure(figsize=(7, 4))\n'
                        '        plt.barh(ingresos.index, ingresos.values, color="#00a37a")\n'
                        '        plt.title("Ingreso por categoria ($)")\n'
                        '        plt.tight_layout()\n'
                        '        plt.show()\n'
                        '        print("(el grafico aparece abajo cuando elijas Salir)")\n'
                        '    elif op == "6":\n'
                        '        print("¡Gracias por usar el panel!")\n'
                        '        break\n'
                        '    else:\n'
                        '        print("Opcion no valida.")',
            },
            {
                "title": "Tu turno · consola libre",
                "explain": "Ahora te toca a ti. Esta consola está <b>en blanco a propósito</b>: aquí "
                           "<b>escribes tú</b> tu propio panel. Ármalo como en las prácticas (recuerda: el "
                           "menú va <b>dentro de <code>input()</code></b>) y <b>agrégale al menos 2 opciones "
                           "nuevas</b>. Si no recuerdas algo, ve a la práctica y la lección que se indica.<br><br>"
                           "<b>Tu panel debe tener, como mínimo:</b>"
                           "<ol>"
                           "<li><b>Cargar los datos</b> al inicio con <code>cargar(\"ferreteria\")</code>. "
                           "→ <b>Paso 1</b> · <b>Lección 6</b>.</li>"
                           "<li><b>El menú dentro de <code>input()</code></b> (texto de varias líneas) y un "
                           "<code>while True</code> que termine con «Salir» (<code>break</code>). "
                           "→ <b>Práctica 1</b> · <b>Lecciones 5 y 7</b>.</li>"
                           "<li><b>Elegir</b> con <code>if / elif / else</code>. → <b>Lección 4</b>.</li>"
                           "<li><b>Opción Totales</b> (ingreso total y por categoría). → <b>Paso 2</b> y <b>Práctica 2</b> · <b>Lección 8</b>.</li>"
                           "<li><b>Opción Promedios</b> (ticket por sucursal). → <b>Paso 3</b> · <b>Lección 8</b>.</li>"
                           "<li><b>Opción Gráfico</b> (ingreso por categoría). → <b>Paso 4</b> y <b>Práctica 3</b>.</li>"
                           "<li><b>Opción con un ciclo</b> (cuenta ventas sobre un monto que pidas con <code>input()</code>). "
                           "→ <b>Práctica 2</b> · <b>Lecciones 7 y 9</b>.</li>"
                           "</ol>"
                           "<b>Tus 2 opciones nuevas</b> (elige o inventa): ingreso por <b>vendedor</b>, por "
                           "<b>medio de pago</b>, el <b>producto más vendido</b>, o un <b>gráfico por "
                           "sucursal</b>. Mira los ejercicios de abajo para las pistas.<br><br>"
                           "<b>Al terminar, pruébalo con otro negocio:</b> cambia "
                           "<code>cargar(\"ferreteria\")</code> por <code>cargar(\"panaderia\")</code>, "
                           "<code>cargar(\"farmacia\")</code>, <code>cargar(\"libreria\")</code> o "
                           "<code>cargar(\"minimarket\")</code>. ¡El mismo panel funciona en todos!",
                "code": '# ===== TU PANEL: escribe aqui tu codigo =====\n'
                        '# El DataFrame `ferreteria` ya esta disponible\n'
                        '# (tambien:  datos = cargar("ferreteria")).\n'
                        '#\n'
                        '# Guia rapida (copia el patron de la Practica 1):\n'
                        '#   1) Carga los datos.\n'
                        '#   2) Escribe el menu como TEXTO dentro de input(), p. ej.:\n'
                        '#        menu = """1) Totales\n'
                        '#        2) Salir\n'
                        '#        Elige: """\n'
                        '#   3) Repite con  while True  y  op = input(menu).\n'
                        '#   4) Dentro de cada  if / elif  escribe el calculo de cada opcion.\n'
                        '#   5) Pruebalo con otro negocio: cargar("panaderia"), "farmacia", "libreria" o "minimarket".\n'
                        '#\n'
                        '# ----- TU CODIGO EMPIEZA AQUI -----\n\n',
            },
        ],
        "dataset": "ferreteria",
        "exercises": [
            "Agrega una opción <b>«ingreso por sucursal»</b>: <code>datos.groupby(\"sucursal\")[\"total\"].sum().sort_values(ascending=False)</code>. (<b>Lección 8</b>.)",
            "Agrega una opción <b>«ingreso por vendedor»</b> con <code>groupby(\"vendedor\")</code> y ordénalo de mayor a menor.",
            "Agrega una opción <b>«producto más vendido»</b>: <code>datos[\"producto\"].value_counts().head()</code>. (<b>Lección 8</b>.)",
            "Agrega una opción <b>«ventas por medio de pago»</b> con <code>datos[\"medio_pago\"].value_counts()</code>.",
            "Agrega un <b>gráfico de ventas por sucursal</b>: <code>datos[\"sucursal\"].value_counts()</code> + <code>plt.bar()</code>. (Repasa el <b>Paso 4</b>.)",
            "Agrega una opción que pida una <b>categoría</b> con <code>input()</code> y muestre sus ventas e ingreso. (<b>Lecciones 5 y 9</b>.)",
            "Con un <b>ciclo <code>for</code></b>, cuenta cuántas ventas se pagaron con <code>\"Efectivo\"</code> y ponlo como opción. (<b>Lecciones 7 y 9</b>.)",
            "Mejora la opción del ciclo: además de contar, <b>suma</b> el total de esas ventas y muestra su <b>porcentaje</b> del total.",
            "Reto final: agrega una opción <b>«informe completo»</b> que muestre de una vez el ingreso total, el ticket promedio y la categoría estrella, y termine con una recomendación para la ferretería.",
        ],
    },
]
