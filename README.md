# Juego-X-0
Juego sencillo de X-0 en la terminal con bot inteligente
# Tres en Raya - IA Invencible 🎮

Un clásico juego de Tres en Raya donde te enfrentas a una máquina que **NUNCA PIERDE**. Desarrollado con Python y algoritmo Minimax.

## 🎯 Características

- 🧠 **IA invencible**: Utiliza el algoritmo Minimax para elegir la mejor jugada
- 🎨 **Interfaz visual**: Tablero estilizado con emojis y fuentes ASCII (`pyfiglet`)
- 📊 **Estadísticas**: Lleva el registro de tus victorias, derrotas y empates
- 🔄 **Rejugabilidad**: Opción de jugar múltiples partidas sin reiniciar
- ⌨️ **Jugabilidad fluida**: Limpieza de pantalla entre turnos

## 🚀 Cómo jugar

1. **Ejecuta el programa**
2. **Ingresa tu nombre**
3. **Elige tu símbolo**: `X` o `0`
4. **Selecciona una casilla** del 1 al 9 (como se muestra en el tablero)
5. **La máquina responderá** con su jugada

### 🧩 Distribución del tablero
1 | 2 | 3
=====+=====+=====
4 | 5 | 6
=====+=====+=====
7 | 8 | 9


## 🧠 Cómo funciona la IA

La máquina usa el algoritmo **Minimax**:
- **Evalúa TODAS las jugadas posibles** hasta el final de la partida
- **Maximiza** sus oportunidades de ganar
- **Minimiza** las del oponente
- **Resultado**: Si juegas perfecto → empate. Si te equivocas → la máquina gana.

## 💻 Requisitos

- Python 3.7+
- Librerías: `pyfiglet` (instalación: `pip install pyfiglet`)

## 📁 Estructura del proyecto
tres_en_raya_1.0.py
├── Tablero # Manejo del tablero (visualización, coordenadas, reset)
├── LogicaJuego # Reglas del juego (victoria, empate, jugada válida)
├── MaquinaInvencible # IA con algoritmo Minimax
├── CrearJugador # Interacción con el usuario (nombre, símbolo, jugadas)
└── main() # Flujo principal del juego


## 🏆 ¿Puedes ganarle?

**No.** Si la IA juega correctamente, el mejor resultado posible es un **empate**.  
Pero hey... si encuentras la forma de ganarle, ¡avísame! 😅

---

_Proyecto creado con fines educativos y diversión_ 🎲
