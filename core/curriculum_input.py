# -*- coding: utf-8 -*-
"""
PyChoice - Leccion 5: Entrada de datos con input().
Se intercala tras los condicionales (leccion 4), antes de los bucles, como leccion principal:
capturar lo que el usuario escribe es la base de los programas interactivos
(y de los proyectos de consola). En PyChoice, input() abre un cuadro de
dialogo del navegador para escribir el valor.
"""

CHAPTERS_INPUT = [
    {
        "num": 5,
        "slug": "entrada-input",
        "code": "leccion_05",
        "title": "Entrada de datos con input()",
        "subtitle": "Pedir y capturar lo que el usuario escribe",
        "apunte": "Lección 5 - Entrada de datos",
        "dataset": "notas, datos",
        "concepts": [
            ("input()", "Función que muestra un mensaje, espera a que el usuario escriba y "
                        "<b>devuelve siempre texto</b> (<code>str</code>). En PyChoice abre un "
                        "cuadro de diálogo del navegador."),
            ("Prompt", "El mensaje que se pone dentro de <code>input(\"...\")</code> para indicarle "
                       "al usuario qué debe escribir. Conviene terminarlo con un espacio."),
            ("Conversión de tipo", "Como <code>input()</code> entrega texto, para calcular hay que "
                                   "convertir: <code>int()</code> para enteros y <code>float()</code> "
                                   "para decimales."),
            ("int() / float()", "<code>int(\"5\")</code> → 5; <code>float(\"3.2\")</code> → 3.2. Si el "
                                "texto no representa un número, se produce un error (<code>ValueError</code>)."),
            ("str()", "Convierte un número a texto; útil para unirlo con otro texto usando <code>+</code>."),
            (".strip()", "Quita los espacios al inicio y al final de lo ingresado; evita errores por "
                         "espacios escritos sin querer."),
            ("Validar la entrada", "Comprobar que lo ingresado sirve antes de usarlo, por ejemplo con "
                                   "<code>.isdigit()</code> o con <code>try / except</code>."),
            ("input() + f-string", "Se combinan para armar mensajes con lo capturado: "
                                   "<code>f\"Hola {nombre}\"</code>."),
        ],
        "theory": """
<p><b>Hasta ahora tus programas decidían solos.</b> Usaban datos que estaban escritos en el código o
los de ejemplo de PyChoice. Pero un programa <b>interactivo</b> le pregunta cosas a la persona que lo
usa y responde según lo que ella escriba. Esa es la puerta de entrada a las aplicaciones de verdad: una
calculadora, un formulario, un juego. La herramienta para lograrlo es <code>input()</code>.</p>

<p><b>Qué hace input().</b> La función <code>input()</code> muestra un mensaje (el <i>prompt</i>),
<b>detiene el programa</b> hasta que el usuario escribe algo y presiona Enter, y <b>devuelve lo
escrito</b>. En PyChoice, al ejecutar un bloque con <code>input()</code> se abre un pequeño cuadro de
diálogo en el navegador para que escribas el valor. Se usa así:
<code>nombre = input("¿Cómo te llamas? ")</code>. Lo que escribas queda guardado en la variable
<code>nombre</code>.</p>

<p><b>La regla de oro: input() SIEMPRE devuelve texto.</b> Aunque escribas <code>25</code>,
<code>input()</code> te entrega el <b>texto</b> <code>"25"</code>, no el número 25. Por eso
<code>input("Edad: ") + 1</code> da error: no se puede sumar 1 a un texto. Esta es una de las
confusiones más comunes al empezar, y entenderla aquí te ahorra muchos dolores de cabeza.</p>

<p><b>Convertir el texto a número.</b> Cuando necesitas calcular, conviertes lo ingresado al tipo
correcto: <code>int()</code> si es un número entero (una edad, una cantidad) o <code>float()</code> si
puede tener decimales (un precio, una temperatura). El patrón típico es envolver el
<code>input()</code> en la conversión: <code>edad = int(input("Tu edad: "))</code>. Así
<code>edad</code> ya es un número y puedes operar con él.</p>

<p><b>Limpiar y validar.</b> Los datos que escribe una persona vienen "sucios": a veces con espacios
de más o mal escritos. <code>.strip()</code> quita los espacios sobrantes
(<code>input("...").strip()</code>). Y antes de confiar en un dato conviene <b>validarlo</b>: por
ejemplo, <code>dato.isdigit()</code> dice si el texto son solo dígitos, y <code>try / except</code>
permite intentar la conversión y reaccionar si falla, en lugar de que el programa se caiga.</p>

<p><b>El patrón completo.</b> Casi todo programa interactivo sigue la misma receta: <b>pedir</b> con
<code>input()</code>, <b>convertir</b> con <code>int()</code>/<code>float()</code> si hace falta,
<b>validar</b>, y <b>usar</b> el dato (calcular, decidir, mostrar con un f-string). Con esto ya puedes
construir pequeñas aplicaciones; de hecho, es justo lo que usarás en los <b>proyectos de consola</b> de
PyChoice, como la calculadora.</p>
""",
        "examples": [
            {"title": "Tu primer input",
             "explain": "<code>input()</code> muestra el mensaje, espera lo que escribas y lo guarda en "
                        "la variable. Al ejecutar, aparecerá un cuadro para escribir.",
             "code": 'nombre = input("¿Cómo te llamas? ")\nprint(f"¡Hola, {nombre}!")'},
            {"title": "input() siempre entrega texto",
             "explain": "Aunque escribas un número, lo que vuelve es <b>texto</b> (str). Compruébalo con "
                        "<code>type()</code>.",
             "code": 'edad_texto = input("¿Cuántos años tienes? ")\n'
                     'print("Escribiste:", edad_texto)\n'
                     'print("Su tipo es:", type(edad_texto))'},
            {"title": "Convertir a número para calcular",
             "explain": "Con <code>int()</code> convertimos el texto a entero y ya podemos operar.",
             "code": 'edad = int(input("Tu edad: "))\n'
                     'print("En 10 años tendrás", edad + 10, "años")'},
            {"title": "Decimales con float() y un cálculo",
             "explain": "Para precios usamos <code>float()</code>. Luego combinamos todo en un f-string.",
             "code": 'precio = float(input("Precio del producto: "))\n'
                     'cantidad = int(input("¿Cuántas unidades? "))\n'
                     'total = precio * cantidad\n'
                     'print(f"Total a pagar: ${total:.0f}")'},
            {"title": "Limpiar y dar formato al texto",
             "explain": "<code>.strip()</code> quita espacios sobrantes; luego damos formato con "
                        "métodos de texto y un f-string.",
             "code": 'ciudad = input("¿De qué ciudad eres? ").strip()\n'
                     'print(f"{ciudad.upper()} — ¡buena elección!")'},
            {"title": "Validar lo que se ingresa",
             "explain": "<code>.isdigit()</code> comprueba que sean solo dígitos antes de convertir, "
                        "evitando que el programa se caiga.",
             "code": 'dato = input("Escribe un número entero: ").strip()\n'
                     'if dato.isdigit():\n'
                     '    n = int(dato)\n'
                     '    print("El doble es", n * 2)\n'
                     'else:\n'
                     '    print("Eso no es un número entero válido.")'},
        ],
        "exercises": [
            "Pide el <b>nombre</b> y la <b>edad</b> del usuario y muestra un saludo con un f-string "
            "(por ejemplo: «Hola Ana, tienes 20 años»).",
            "Pide <b>dos números</b> con <code>input()</code> y <code>float()</code> y muestra su suma.",
            "Pide el <b>radio</b> de un círculo y calcula su área con <code>math.pi * r ** 2</code> "
            "(recuerda <code>import math</code>).",
            "Pide una temperatura en <b>°C</b> (float) y conviértela a °F con la fórmula "
            "<code>C * 9/5 + 32</code>.",
            "Pide una <b>palabra</b> y muestra cuántas letras tiene con <code>len()</code>.",
            "Pide un <b>precio</b> y un <b>descuento</b> (%) y muestra el precio final a pagar.",
            "Pide un número entero y di si es <b>par o impar</b> (usa <code>int()</code> y <code>%</code>).",
            "Pide <b>tres notas</b>, calcula el promedio y di si el alumno aprueba (promedio ≥ 4).",
            "Valida con <code>.isdigit()</code>: pide una edad; si no es un entero válido, muestra un "
            "aviso en lugar de calcular.",
        ],
    },
]
