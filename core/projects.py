# -*- coding: utf-8 -*-
"""
Módulo de PROYECTOS de PyChoice.

Al nivel de las rutas y las lecciones: una sección propia donde el alumno
construye programas completos ("del script a la aplicación"), aplicando lo
aprendido. Se organiza en niveles (tiers):

  1. Consola            -> apps de texto, ejecutables en el navegador.
  2. Escritorio (Tkinter) -> apps con ventana; se ejecutan en el computador.
  3. Web / Full-Stack   -> apps web completas (próximamente).

Cada proyecto es una página con: qué vas a construir, conceptos que practicas,
construcción paso a paso (consolas ejecutables o bloques de código) y el código
completo, más retos para seguir.
"""

# ====================================================================
#  NIVELES (tiers)
# ====================================================================
TIERS = [
    {"key": "consola", "code": "N1", "label": "App de consola",
     "title": "Nivel 1 · Apps de consola",
     "desc": "Programas de texto que piden datos con input() y responden en la "
             "consola. Se ejecutan aquí mismo, en el navegador."},
    {"key": "escritorio", "code": "N2", "label": "App de escritorio",
     "title": "Nivel 2 · Apps de escritorio (Tkinter)",
     "desc": "Aplicaciones con ventana, botones y campos usando Tkinter (incluido "
             "en Python). Se escriben aquí y se ejecutan en tu computador."},
    {"key": "web", "code": "N3", "label": "Web / full-stack",
     "title": "Nivel 3 · Web y full-stack",
     "desc": "Aplicaciones web completas: una página (front-end) y un servidor "
             "(back-end) con Flask y una base de datos. Próximamente."},
]
TIER_LABEL = {t["key"]: t["label"] for t in TIERS}


# ====================================================================
#  SVG: mockup de la calculadora Tkinter (para "qué vas a construir")
# ====================================================================
_CALC_GUI_SVG = """
<svg viewBox="0 0 260 300" width="230" role="img" aria-label="Boceto de la calculadora con Tkinter"
     xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="2" width="256" height="296" rx="10" fill="#0f1825" stroke="#16202e"/>
  <rect x="2" y="2" width="256" height="26" rx="10" fill="#0a1320"/>
  <circle cx="18" cy="15" r="4" fill="#ff5f56"/><circle cx="32" cy="15" r="4" fill="#ffbd2e"/>
  <circle cx="46" cy="15" r="4" fill="#27c93f"/>
  <text x="130" y="19" fill="#5d7186" font-family="monospace" font-size="10" text-anchor="middle">Calculadora PyChoice</text>
  <rect x="14" y="40" width="232" height="44" rx="5" fill="#0a1320" stroke="#16202e"/>
  <text x="236" y="70" fill="#00ff9c" font-family="monospace" font-size="22" text-anchor="end">12 + 7</text>
""" + "".join(
    f'<rect x="{14 + col*59}" y="{96 + row*44}" width="51" height="38" rx="5" '
    f'fill="{"#00ff9c" if t in ("=",) else "#101a28"}" stroke="#16202e"/>'
    f'<text x="{14 + col*59 + 25}" y="{96 + row*44 + 24}" '
    f'fill="{"#06111b" if t=="=" else ("#2bd9ff" if t in "+-*/" else "#cdd9e6")}" '
    f'font-family="monospace" font-size="15" text-anchor="middle">{t}</text>'
    for row, fila in enumerate([["7","8","9","/"],["4","5","6","*"],
                                ["1","2","3","-"],["0",".","C","+"]])
    for col, t in enumerate(fila)
) + """
  <rect x="14" y="272" width="232" height="18" rx="5" fill="#00ff9c"/>
  <text x="130" y="285" fill="#06111b" font-family="monospace" font-size="12" text-anchor="middle">=</text>
</svg>
"""


# ====================================================================
#  PROYECTOS
# ====================================================================
PROJECTS = [

# -------------------------------------------------- 1) Calculadora de consola
{
 "slug": "calculadora-consola",
 "title": "Calculadora de consola",
 "short": "calculadora de consola",
 "subtitle": "Tu primera app interactiva: pide números y opera con ellos",
 "tier": "consola", "level": "básico", "status": "listo",
 "runnable": True, "desktop": False,
 "fname": "calculadora.py",
 "icon": "=",
 "tagline": "Lee datos con input(), opera con funciones y repite con un menú.",
 "tags": ["input()", "float()", "funciones", "if / elif / else", "while", "try / except"],
 "intro": """
<p>Vas a construir una <b>calculadora interactiva</b> que funciona en la consola: le pides al usuario
una operación y dos números, y el programa muestra el resultado. Luego vuelve a preguntar, en un
<b>menú</b> que se repite hasta que el usuario escribe <code>salir</code>.</p>
<p>Es el proyecto perfecto para estrenar <code>input()</code> (capturar lo que el usuario escribe) y
combinarlo con todo lo aprendido: variables, funciones, condicionales y bucles.</p>
""",
 "goals": [
   "Capturar lo que el usuario escribe con <code>input()</code> y convertirlo a número con <code>float()</code>.",
   "Separar la lógica en una <b>función</b> <code>operar()</code> reutilizable.",
   "Elegir qué hacer con <code>if / elif / else</code>.",
   "Repetir con un <b>menú</b> usando <code>while</code>, <code>break</code> y <code>continue</code>.",
   "Evitar que el programa se caiga con <code>try / except</code>.",
 ],
 "steps": [
   {"title": "Capturar un dato con input()", "run": True,
    "explain": "<p><code>input()</code> muestra un mensaje, espera a que el usuario escriba y "
               "devuelve siempre <b>texto</b>. Para calcular, convertimos ese texto a número con "
               "<code>float()</code>. En PyChoice, al ejecutar, aparecerá un cuadro para escribir.</p>",
    "code": 'nombre = input("¿Cómo te llamas? ")\n'
            'print("Hola,", nombre)\n\n'
            'edad = int(input("¿Cuántos años tienes? "))\n'
            'print("El próximo año tendrás", edad + 1)'},
   {"title": "La operación, en una función", "run": True,
    "explain": "<p>Una <b>función</b> agrupa una tarea con un nombre. <code>operar(a, b, op)</code> "
               "recibe dos números y el símbolo de la operación, y devuelve el resultado. Fíjate en "
               "cómo protegemos la división por cero.</p>",
    "code": 'def operar(a, b, op):\n'
            '    if op == "+":\n'
            '        return a + b\n'
            '    elif op == "-":\n'
            '        return a - b\n'
            '    elif op == "*":\n'
            '        return a * b\n'
            '    elif op == "/":\n'
            '        if b == 0:\n'
            '            return "Error: no se puede dividir por cero"\n'
            '        return a / b\n'
            '    else:\n'
            '        return "Operación no válida"\n\n'
            'print(operar(10, 5, "+"))\n'
            'print(operar(10, 0, "/"))'},
   {"title": "Pedir la operación y los números", "run": True,
    "explain": "<p>Ahora unimos las piezas: pedimos la operación y los dos números con "
               "<code>input()</code>, llamamos a <code>operar()</code> y mostramos el resultado.</p>",
    "code": 'def operar(a, b, op):\n'
            '    if op == "+": return a + b\n'
            '    if op == "-": return a - b\n'
            '    if op == "*": return a * b\n'
            '    if op == "/": return a / b if b != 0 else "no se divide por cero"\n'
            '    return "operación no válida"\n\n'
            'op = input("Operación (+, -, *, /): ")\n'
            'a = float(input("Primer número: "))\n'
            'b = float(input("Segundo número: "))\n'
            'print("Resultado:", operar(a, b, op))'},
   {"title": "Repetir con un menú (while)", "run": True,
    "explain": "<p>Una calculadora de verdad no se usa una sola vez. Con <code>while True</code> "
               "repetimos el menú; <code>break</code> termina el bucle cuando el usuario escribe "
               "<code>salir</code> y <code>continue</code> salta a la siguiente vuelta.</p>",
    "code": 'while True:\n'
            '    op = input("Operación (+, -, *, / o salir): ")\n'
            '    if op == "salir":\n'
            '        print("¡Hasta pronto!")\n'
            '        break\n'
            '    print("Elegiste:", op)'},
 ],
 "full_code":
    '# Calculadora de consola - PyChoice\n'
    '\n'
    'def operar(a, b, op):\n'
    '    if op == "+":\n'
    '        return a + b\n'
    '    elif op == "-":\n'
    '        return a - b\n'
    '    elif op == "*":\n'
    '        return a * b\n'
    '    elif op == "/":\n'
    '        if b == 0:\n'
    '            return "Error: no se puede dividir por cero"\n'
    '        return a / b\n'
    '    else:\n'
    '        return "Operación no válida"\n'
    '\n'
    'print("=== Calculadora PyChoice ===")\n'
    'print("Operaciones: +  -  *  /    (escribe \'salir\' para terminar)")\n'
    '\n'
    'while True:\n'
    '    op = input("Operación (+, -, *, / o salir): ")\n'
    '    if op == "salir":\n'
    '        print("¡Hasta pronto!")\n'
    '        break\n'
    '    try:\n'
    '        a = float(input("Primer número: "))\n'
    '        b = float(input("Segundo número: "))\n'
    '    except ValueError:\n'
    '        print("Eso no es un número válido. Intenta de nuevo.")\n'
    '        continue\n'
    '    resultado = operar(a, b, op)\n'
    '    print("Resultado:", resultado)\n'
    '    print()\n',
 "retos": [
   "Agrega la operación <b>potencia</b> (<code>**</code>) y el <b>resto</b> (<code>%</code>).",
   "Lleva un historial: guarda cada operación en una lista y muéstralo al salir.",
   "Valida que la operación sea una de las permitidas antes de pedir los números.",
   "Muestra el resultado con 2 decimales usando un f-string: <code>f\"{resultado:.2f}\"</code>.",
 ],
},

# -------------------------------------------------- 2) Adivina el número
{
 "slug": "adivina-el-numero",
 "title": "Juego: adivina el número",
 "short": "adivina el número",
 "subtitle": "Un juego para dominar bucles, condiciones y números aleatorios",
 "tier": "consola", "level": "básico", "status": "listo",
 "runnable": True, "desktop": False,
 "fname": "adivina.py",
 "icon": "?",
 "tagline": "El computador piensa un número y tú lo adivinas con pistas.",
 "tags": ["random", "input()", "int()", "while", "comparaciones", "contador"],
 "intro": """
<p>El computador elige al azar un número secreto entre 1 y 100 y tú tienes que adivinarlo. En cada
intento, el programa te dice si tu número es <b>muy alto</b> o <b>muy bajo</b>, hasta que aciertas.
Al final te dice en cuántos intentos lo lograste.</p>
<p>Es un clásico para entender de verdad los <b>bucles</b> y las <b>decisiones</b>: el programa
repite mientras no aciertes, y decide qué pista darte comparando números.</p>
""",
 "goals": [
   "Generar un número al azar con el módulo <code>random</code>.",
   "Leer cada intento con <code>input()</code> y convertirlo con <code>int()</code>.",
   "Comparar con <code>if / elif / else</code> para dar pistas.",
   "Repetir hasta acertar con <code>while</code> y <code>break</code>.",
   "Contar los intentos con un <b>acumulador</b>.",
 ],
 "steps": [
   {"title": "Un número al azar", "run": True,
    "explain": "<p>El módulo <code>random</code> (incluido en Python) genera azar. "
               "<code>random.randint(1, 100)</code> devuelve un entero entre 1 y 100, ambos "
               "incluidos. Lo mostramos solo para probar; en el juego final quedará oculto.</p>",
    "code": 'import random\n\n'
            'secreto = random.randint(1, 100)\n'
            'print("El número secreto es:", secreto)'},
   {"title": "Un intento y su pista", "run": True,
    "explain": "<p>Leemos un intento con <code>input()</code>, lo convertimos a entero con "
               "<code>int()</code> y lo comparamos con el secreto para decidir la pista.</p>",
    "code": 'secreto = 42\n\n'
            'intento = int(input("Adivina el número (1 a 100): "))\n'
            'if intento < secreto:\n'
            '    print("Muy bajo")\n'
            'elif intento > secreto:\n'
            '    print("Muy alto")\n'
            'else:\n'
            '    print("¡Correcto!")'},
   {"title": "Repetir hasta acertar y contar intentos", "run": True,
    "explain": "<p>Con <code>while True</code> repetimos hasta acertar. Un contador "
               "<code>intentos</code> suma 1 en cada vuelta, y <code>break</code> corta el bucle "
               "cuando el número es correcto.</p>",
    "code": 'import random\n\n'
            'secreto = random.randint(1, 100)\n'
            'intentos = 0\n'
            'while True:\n'
            '    intento = int(input("Tu intento: "))\n'
            '    intentos += 1\n'
            '    if intento < secreto:\n'
            '        print("Muy bajo")\n'
            '    elif intento > secreto:\n'
            '        print("Muy alto")\n'
            '    else:\n'
            '        print("¡Correcto en", intentos, "intentos!")\n'
            '        break'},
 ],
 "full_code":
    '# Adivina el número - PyChoice\n'
    'import random\n'
    '\n'
    'secreto = random.randint(1, 100)\n'
    'intentos = 0\n'
    'print("Adivina el número secreto entre 1 y 100.")\n'
    'print("(escribe \'salir\' para rendirte)")\n'
    '\n'
    'while True:\n'
    '    dato = input("Tu intento: ")\n'
    '    if dato == "salir":\n'
    '        print("El número era", secreto, "- ¡vuelve pronto!")\n'
    '        break\n'
    '    if not dato.isdigit():\n'
    '        print("Escribe un número entero válido.")\n'
    '        continue\n'
    '    intento = int(dato)\n'
    '    intentos += 1\n'
    '    if intento < secreto:\n'
    '        print("Muy bajo")\n'
    '    elif intento > secreto:\n'
    '        print("Muy alto")\n'
    '    else:\n'
    '        print("¡Correcto! Lo lograste en", intentos, "intentos.")\n'
    '        break\n',
 "retos": [
   "Limita el juego a <b>7 intentos</b>: si se acaban, pierde y se revela el número.",
   "Deja que el usuario elija el rango (por ejemplo, 1 a 1000) con <code>input()</code>.",
   "Lleva el récord de la <b>menor cantidad de intentos</b> entre varias partidas.",
   "Invierte los papeles: tú piensas el número y el programa lo adivina a la mitad del rango.",
 ],
},

# -------------------------------------------------- 3) Calculadora Tkinter
{
 "slug": "calculadora-tkinter",
 "title": "Calculadora con interfaz gráfica (Tkinter)",
 "short": "calculadora con Tkinter",
 "subtitle": "De la consola a una ventana con botones, usando Tkinter",
 "tier": "escritorio", "level": "intermedio", "status": "listo",
 "runnable": False, "desktop": True,
 "fname": "calculadora_gui.py",
 "icon": "▭",
 "tagline": "Una app de escritorio real: pantalla, botones y clics con Tkinter.",
 "tags": ["tkinter", "Tk()", "Entry", "Button", "grid()", "funciones callback", "eval()"],
 "gui_svg": _CALC_GUI_SVG,
 "intro": """
<p>Ahora damos el salto de la consola a una <b>aplicación de escritorio con ventana</b>. Construirás
una calculadora con su pantalla y una grilla de botones, igual que la de tu teléfono, usando
<b>Tkinter</b>, la librería de interfaces gráficas que viene incluida con Python.</p>
<p>Aprenderás las tres ideas centrales de cualquier interfaz gráfica: crear una <b>ventana</b>,
colocar <b>widgets</b> (pantalla y botones) con un <b>layout</b>, y conectar cada botón a una
<b>función</b> que se ejecuta al hacer clic.</p>
""",
 "goals": [
   "Crear una ventana con <code>tkinter.Tk()</code> y <code>mainloop()</code>.",
   "Agregar una pantalla con <code>Entry</code> y botones con <code>Button</code>.",
   "Ubicar los widgets en filas y columnas con <code>grid()</code>.",
   "Conectar cada botón a una función (<code>command=</code>).",
   "Calcular la expresión escrita y manejar errores.",
 ],
 "local_run": """
<b>Cómo ejecutarlo en tu computador:</b> Tkinter viene incluido con Python, no se instala nada.
Copia el <b>código completo</b>, guárdalo en un archivo llamado <code>calculadora_gui.py</code> y
ejecútalo desde la terminal con <code>python calculadora_gui.py</code> (en Windows también puedes
hacer doble clic en el archivo). Se abrirá la ventana de la calculadora.
""",
 "steps": [
   {"title": "La ventana", "run": False,
    "explain": "<p>Todo parte creando la ventana principal con <code>tk.Tk()</code>. "
               "<code>title()</code> le pone nombre y <code>mainloop()</code> la mantiene abierta, "
               "atenta a los clics. <b>Siempre</b> va al final.</p>",
    "code": 'import tkinter as tk\n\n'
            'ventana = tk.Tk()\n'
            'ventana.title("Calculadora PyChoice")\n'
            'ventana.resizable(False, False)\n\n'
            'ventana.mainloop()'},
   {"title": "La pantalla (Entry) y el layout con grid", "run": False,
    "explain": "<p>El widget <code>Entry</code> es la pantalla donde se ve la operación. Con "
               "<code>grid(row, column)</code> ubicamos los widgets en una cuadrícula; "
               "<code>columnspan=4</code> hace que la pantalla ocupe las 4 columnas de botones.</p>",
    "code": 'import tkinter as tk\n\n'
            'ventana = tk.Tk()\n'
            'ventana.title("Calculadora PyChoice")\n\n'
            'pantalla = tk.Entry(ventana, font=("Consolas", 22), justify="right")\n'
            'pantalla.grid(row=0, column=0, columnspan=4, ipady=10)\n\n'
            'ventana.mainloop()'},
   {"title": "Los botones y su función (callback)", "run": False,
    "explain": "<p>Cada <code>Button</code> ejecuta una función al hacer clic (parámetro "
               "<code>command</code>). <code>escribir()</code> añade un carácter a la pantalla con "
               "<code>insert()</code>. Usamos <code>lambda c=texto: escribir(c)</code> para que "
               "cada botón recuerde su propio carácter dentro del bucle.</p>",
    "code": 'def escribir(caracter):\n'
            '    pantalla.insert(tk.END, caracter)\n\n'
            'botones = [\n'
            '    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),\n'
            '    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),\n'
            '    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),\n'
            '    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),\n'
            ']\n\n'
            'for (texto, fila, col) in botones:\n'
            '    tk.Button(ventana, text=texto, width=4, height=2,\n'
            '              command=lambda c=texto: escribir(c)).grid(row=fila, column=col)'},
   {"title": "Calcular y limpiar", "run": False,
    "explain": "<p><code>calcular()</code> toma el texto de la pantalla con <code>get()</code>, lo "
               "evalúa con <code>eval()</code> y muestra el resultado; si hay un error (por ejemplo "
               "<code>5/0</code>), muestra <i>Error</i>. <code>limpiar()</code> borra la pantalla. "
               "<b>Nota:</b> <code>eval()</code> es cómodo para aprender, pero no se usa con texto "
               "de origen desconocido.</p>",
    "code": 'def calcular():\n'
            '    try:\n'
            '        resultado = eval(pantalla.get())\n'
            '    except Exception:\n'
            '        resultado = "Error"\n'
            '    pantalla.delete(0, tk.END)\n'
            '    pantalla.insert(0, str(resultado))\n\n'
            'def limpiar():\n'
            '    pantalla.delete(0, tk.END)'},
 ],
 "full_code":
    '# Calculadora con interfaz grafica (Tkinter) - PyChoice\n'
    '# Ejecutar en tu computador:  python calculadora_gui.py\n'
    'import tkinter as tk\n'
    '\n'
    'ventana = tk.Tk()\n'
    'ventana.title("Calculadora PyChoice")\n'
    'ventana.resizable(False, False)\n'
    'ventana.configure(bg="#0f1825")\n'
    '\n'
    '# --- Pantalla ---\n'
    'pantalla = tk.Entry(ventana, font=("Consolas", 22), justify="right",\n'
    '                    bg="#0a1320", fg="#00ff9c", bd=0, insertbackground="#00ff9c")\n'
    'pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8, ipady=10)\n'
    '\n'
    '# --- Funciones (lo que hacen los botones) ---\n'
    'def escribir(caracter):\n'
    '    pantalla.insert(tk.END, caracter)\n'
    '\n'
    'def limpiar():\n'
    '    pantalla.delete(0, tk.END)\n'
    '\n'
    'def calcular():\n'
    '    try:\n'
    '        resultado = eval(pantalla.get())\n'
    '    except Exception:\n'
    '        resultado = "Error"\n'
    '    pantalla.delete(0, tk.END)\n'
    '    pantalla.insert(0, str(resultado))\n'
    '\n'
    '# --- Botones de digitos y operadores ---\n'
    'botones = [\n'
    '    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),\n'
    '    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),\n'
    '    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),\n'
    '    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),\n'
    ']\n'
    '\n'
    'for (texto, fila, col) in botones:\n'
    '    accion = limpiar if texto == "C" else (lambda c=texto: escribir(c))\n'
    '    tk.Button(ventana, text=texto, font=("Consolas", 16), width=4, height=2,\n'
    '              bg="#101a28", fg="#cdd9e6", activebackground="#00ff9c",\n'
    '              bd=0, command=accion).grid(row=fila, column=col, padx=4, pady=4)\n'
    '\n'
    '# --- Boton igual (=) ---\n'
    'tk.Button(ventana, text="=", font=("Consolas", 16), height=2,\n'
    '          bg="#00ff9c", fg="#06111b", activebackground="#2bd9ff",\n'
    '          bd=0, command=calcular).grid(row=5, column=0, columnspan=4,\n'
    '                                       sticky="nsew", padx=4, pady=(4, 8))\n'
    '\n'
    'ventana.mainloop()\n',
 "retos": [
   "Agrega soporte para el <b>teclado</b>: enlaza las teclas con <code>ventana.bind()</code>.",
   "Añade un botón de <b>borrar último dígito</b> (retroceso).",
   "Cambia <code>eval()</code> por tu propia función de cálculo, más segura.",
   "Dale estilo: colores distintos para números, operadores y el botón igual.",
 ],
},

# ======================= PRÓXIMAMENTE (scaffolding) =======================
{"slug": "gestor-tareas-consola", "title": "Gestor de tareas (lista de pendientes)",
 "short": "gestor de tareas", "subtitle": "Agrega, lista y completa tareas en la consola",
 "tier": "consola", "level": "básico", "status": "proximamente", "runnable": True,
 "desktop": False, "icon": "✓",
 "tagline": "Listas, funciones y un menú para administrar tus pendientes.",
 "tags": ["listas", "funciones", "while", "diccionarios"]},

{"slug": "conversor-unidades", "title": "Conversor de unidades",
 "short": "conversor de unidades", "subtitle": "Convierte temperatura, moneda y medidas",
 "tier": "consola", "level": "básico", "status": "proximamente", "runnable": True,
 "desktop": False, "icon": "⇄",
 "tagline": "Un menú que convierte entre distintas unidades con fórmulas.",
 "tags": ["funciones", "input()", "if / elif", "formato de números"]},

{"slug": "agenda-contactos-tkinter", "title": "Agenda de contactos (Tkinter + archivos)",
 "short": "agenda de contactos", "subtitle": "Una app de escritorio que guarda datos en un archivo",
 "tier": "escritorio", "level": "intermedio", "status": "proximamente", "runnable": False,
 "desktop": True, "icon": "☎",
 "tagline": "CRUD con ventana: crear, ver y borrar contactos que persisten en disco.",
 "tags": ["tkinter", "Listbox", "archivos", "json", "funciones"]},

{"slug": "pomodoro-tkinter", "title": "Temporizador Pomodoro (Tkinter)",
 "short": "pomodoro", "subtitle": "Un cronómetro de estudio con cuenta regresiva",
 "tier": "escritorio", "level": "intermedio", "status": "proximamente", "runnable": False,
 "desktop": True, "icon": "◴",
 "tagline": "Ventana con cuenta regresiva usando after() y eventos de tiempo.",
 "tags": ["tkinter", "after()", "Label", "estados"]},

{"slug": "encuesta-flask", "title": "Encuesta con Flask (full-stack)",
 "short": "encuesta web", "subtitle": "Tu primera app web: formulario, servidor y resultados",
 "tier": "web", "level": "avanzado", "status": "proximamente", "runnable": False,
 "desktop": False, "icon": "◧",
 "tagline": "Front-end (HTML) + back-end (Flask) que recibe y muestra respuestas.",
 "tags": ["flask", "rutas", "HTML", "formularios", "back-end"]},

{"slug": "todo-fullstack-flask", "title": "Lista de tareas full-stack (Flask + SQLite)",
 "short": "to-do full-stack", "subtitle": "App web completa con base de datos",
 "tier": "web", "level": "avanzado", "status": "proximamente", "runnable": False,
 "desktop": False, "icon": "▤",
 "tagline": "El combo completo: interfaz, servidor y base de datos SQLite.",
 "tags": ["flask", "SQLite", "CRUD", "base de datos", "full-stack"]},
]

BY_SLUG = {p["slug"]: p for p in PROJECTS}


# ====================================================================
#  API
# ====================================================================
def get_project(slug):
    return BY_SLUG.get(slug)


def project_list():
    """Lista ligera (para el índice, el home y utilidades)."""
    return [{"slug": p["slug"], "title": p["title"], "short": p["short"],
             "subtitle": p["subtitle"], "level": p["level"], "tier": p["tier"],
             "status": p["status"]} for p in PROJECTS]


def sidebar_projects():
    """Proyectos listos para el menú lateral (// proyectos)."""
    return [{"slug": p["slug"], "short": p["short"], "title": p["title"]}
            for p in PROJECTS if p["status"] == "listo"]


def project_groups():
    """Agrupa los proyectos por nivel (tier) para la página índice."""
    out = []
    total = done = 0
    for t in TIERS:
        items = [p for p in PROJECTS if p["tier"] == t["key"]]
        ready = [p for p in items if p["status"] == "listo"]
        total += len(items)
        done += len(ready)
        out.append({"code": t["code"], "title": t["title"], "desc": t["desc"],
                    "key": t["key"], "projects": items,
                    "has_ready": bool(ready)})
    return out, done, total


def tier_label(key):
    return TIER_LABEL.get(key, "")
