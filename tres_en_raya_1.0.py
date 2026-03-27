from typing import List , Union, Tuple
import pyfiglet
import os
#abreviaciones type_hints alias
tablero_type = list[list[Union[int,str]]] 

class Tablero:
    #self,_matriz que representan cada casilla
    def __init__(self):
        self._matriz = [[1,2,3],[4,5,6],[7,8,9]]

    @property
    def matriz(self) -> tablero_type:
        return self._matriz
    
    def cambiar_casilla(self, indice1:int, indice2:int, signo:str) -> None:
        self._matriz[indice1][indice2] = signo
    
    def vaciar_matriz(self):
        self._matriz[0] = [1,2,3]
        self._matriz[1] = [4,5,6] 
        self._matriz[2] = [7,8,9]

    def imprimir_tablero(self) -> None:
        #Imprime el tablero en pantalla
        for jugada in range(12):
            print(f"{10 * ' '}| |{10 * ' '}| |")
            match jugada:
                case 1:
                    print(f"{4 * ' '}{self._matriz[0][0]}{5 * ' '}| |{5 * ' '}{self._matriz[0][1]}{4 * ' '}| |{5 * ' '}{self._matriz[0][2]}")
                case 3 | 7:
                    print(f"{11 * '='}+{12 * '='}+{11 * '='}")
                case 5:
                    print(f"{4 * ' '}{self._matriz[1][0]}{5 * ' '}| |{5 * ' '}{self._matriz[1][1]}{4 * ' '}| |{5 * ' '}{self._matriz[1][2]}")
                case 9:
                    print(f"{4 * ' '}{self._matriz[2][0]}{5 * ' '}| |{5 * ' '}{self._matriz[2][1]}{4 * ' '}| |{5 * ' '}{self._matriz[2][2]}")
    
    def obtener_cordenadas(self,jugada:int) ->  Tuple[int,int]:
        #nos manda las cordenadas en la self,_matriz para cambiarlo por la jugada de la persona
        if 1 <= jugada <= 3 :
            return (0, self._matriz[0].index(jugada))
        if 4 <= jugada <= 6:
            return (1, self._matriz[1].index(jugada))
        if 7 <= jugada <= 9:
            return (2, self._matriz[2].index(jugada))

class LogicaJuego:
    def __init__(self, tablero: Tablero):
        self.tablero = tablero  # Guardamos el objeto Tablero, no la matriz

    def verificar_jugada(self, jugada: int) -> bool:
        matriz = self.tablero.matriz  # Obtenemos la matriz actual
        if 1 <= jugada <= 3:
            fila = matriz[0]
        elif 4 <= jugada <= 6:
            fila = matriz[1]
        elif 7 <= jugada <= 9:
            fila = matriz[2]
        else:
            return False
        return jugada in fila

    def verificar_victoria(self, usuario: str, simbolo_bot: str) -> Union[bool, None]:
        matriz = self.tablero.matriz
        for jugador in (usuario, simbolo_bot):
            # Filas
            for fila in matriz:
                if fila[0] == fila[1] == fila[2] == jugador:
                    return jugador == usuario
            # Columnas
            for columna in range(3):
                if matriz[0][columna] == matriz[1][columna] == matriz[2][columna] == jugador:
                    return jugador == usuario
            # Diagonales
            if matriz[0][0] == matriz[1][1] == matriz[2][2] == jugador:
                return jugador == usuario
            if matriz[0][2] == matriz[1][1] == matriz[2][0] == jugador:
                return jugador == usuario
        return None

    def verificar_empate(self) -> bool:
        matriz = self.tablero.matriz
        for fila in matriz:
            for celda in fila:
                if isinstance(celda, int):
                    return False
        return True

    def volver_jugar(self, vaciar_matriz_func) -> Union[bool, str]:
        while True:
            try:
                v_jugar = int(input("Quieres jugar otra partida?\n1.Sí\n2.No: "))
            except Exception as e:
                print(f"Error en volver a jugar: {type(e).__name__}")
                continue
            if v_jugar == 1:
                vaciar_matriz_func()  # Ejecuta la función (ej: tablero.vaciar_matriz)
                return True
            elif v_jugar == 2:
                return False
            else:
                print("Seleccione una opcion correcta")

    @staticmethod
    def estadisticas(nombre_usuario: str, victorias: int, empates: int, derrotas: int):
        print(f' {nombre_usuario}: {victorias} || Empates: {empates} || Máquina: {derrotas}\n')


class MaquinaInvencible:
    def __init__(self, simbolo: str, logica: LogicaJuego, tablero: Tablero) -> None:
        self.simbolo = simbolo
        self.logica = logica
        self.tablero = tablero
        self.oponente = "\b❌" if simbolo == "\b⭕" else "\b⭕"
    
    def jugar(self) -> int:
        _, mejor_jugada = self._minimax(self.simbolo, True)
        return mejor_jugada if mejor_jugada is not None else -1
    
    def _minimax(self, jugador_actual: str, es_max: bool) -> tuple:
        resultado = self.logica.verificar_victoria(self.oponente, self.simbolo)
        
        if resultado is True:
            return (-1, None)
        elif resultado is False:
            return (1, None)
        elif self.logica.verificar_empate():
            return (0, None)
        
        mejor_puntaje = float('-inf') if es_max else float('inf')
        mejor_jugada = None
        
        for jugada in range(1, 10):
            if self.logica.verificar_jugada(jugada):
                # 🔽 Aquí usamos 'obtener_cordenadas' (con una 'r')
                fila, col = self.tablero.obtener_cordenadas(jugada)
                original = self.tablero.matriz[fila][col]
                self.tablero.cambiar_casilla(fila, col, jugador_actual)
                
                siguiente_jugador = self.oponente if jugador_actual == self.simbolo else self.simbolo
                puntaje, _ = self._minimax(siguiente_jugador, not es_max)
                
                self.tablero.cambiar_casilla(fila, col, original)
                
                if es_max and puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_jugada = jugada
                elif not es_max and puntaje < mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_jugada = jugada
        
        return (mejor_puntaje, mejor_jugada)


class CrearJugador:
    def obtener_datos_usuario(self) ->Tuple[str,str,str]:
        nombre_usuario = input("Para continuar introduzca su nombre: ")
        while True:
            eleccion_usuario = input("Escriba una X o un 0 segun lo que quiera ser: ")
            if eleccion_usuario.upper() == "X":
                simbolo_usuario = "\b❌"
                simbolo_bot = "\b⭕"
                return nombre_usuario, simbolo_usuario,simbolo_bot
            elif eleccion_usuario.upper() == "0":
                simbolo_usuario = "\b⭕"
                simbolo_bot = "\b❌"
                return nombre_usuario,simbolo_usuario,simbolo_bot
            else:
                print("Debes elegir una X o un 0 \n")

    def elegir_casilla(self) -> int:
        while True:
            try:
                return int(input("Tu turno: "))
            except ValueError:
                print(f'Erorr elegiendo casilla\n ')

#variables globales
victorias:int = 0
empates:int = 0
derrotas:int = 0
#Objetos y instancias
jugador = CrearJugador()
tablero = Tablero()
logica_del_juego = LogicaJuego(tablero)
nombre_usuario, simbolo_usuario, simbolo_bot = jugador.obtener_datos_usuario()
#flujo principal del juego
def main():
    global victorias, empates, derrotas
    bienvenida = pyfiglet.figlet_format(f"Hola {nombre_usuario} bienvenido", font="slant")
    print(bienvenida)
    print(f"\n{16 * ' '} X'0")
    logica_del_juego.estadisticas(nombre_usuario, victorias, empates, derrotas)
    tablero.imprimir_tablero()
    maquina = MaquinaInvencible(simbolo_bot, logica_del_juego, tablero)

    while True:
        # --- Turno del humano ---
        jugada = jugador.elegir_casilla()
        if not logica_del_juego.verificar_jugada(jugada):
            print("Casilla no disponible, elige otra.\n")
            continue

        fila, col = tablero.obtener_cordenadas(jugada)
        tablero.cambiar_casilla(fila, col, simbolo_usuario)
        os.system("cls")
        print(pyfiglet.figlet_format(f"{4 * ' '} X'0", font='slant'))
        logica_del_juego.estadisticas(nombre_usuario, victorias, empates, derrotas)
        tablero.imprimir_tablero()

        # Verificar tras jugada humana
        hay_victoria = logica_del_juego.verificar_victoria(simbolo_usuario, simbolo_bot)
        hay_empate = logica_del_juego.verificar_empate()

        if hay_victoria is not None or hay_empate:
            if hay_victoria:
                mensaje = "\n Felicidades, has ganado😎🥳☆*: .｡. o(≧▽≦)o .｡.:*☆ "
                victorias += 1
            elif hay_victoria == False:
                mensaje = "\n Vaya! Parece que has perdido😓(┬┬﹏┬┬) "
                derrotas += 1
            elif hay_empate:
                mensaje = "\n Vaya!!!, Esto es un empate🤔O.O "
                empates += 1
            os.system('cls')
            print(pyfiglet.figlet_format(f"{4 * ' '} X'0", font='slant'))
            logica_del_juego.estadisticas(nombre_usuario, victorias, empates, derrotas)
            tablero.imprimir_tablero()
            print(mensaje)
            if logica_del_juego.volver_jugar(tablero.vaciar_matriz):
                os.system('cls')
                print(pyfiglet.figlet_format(f"{4 * ' '} X'0", font='slant'))
                logica_del_juego.estadisticas(nombre_usuario, victorias, empates, derrotas)
                tablero.imprimir_tablero()
                continue
            else:
                print('\nGracias por jugar T_T')
                break

        # --- Turno de la máquina ---
        jugada_maquina = maquina.jugar()
        if jugada_maquina == -1:
            print("Error: no hay jugadas disponibles")
            break
        fila, col = tablero.obtener_cordenadas(jugada_maquina)
        tablero.cambiar_casilla(fila, col, simbolo_bot)
        os.system("cls")
        print(pyfiglet.figlet_format(f"{4 * ' '} X'0", font='slant'))
        logica_del_juego.estadisticas(nombre_usuario, victorias, empates, derrotas)
        tablero.imprimir_tablero()
        print(f"La máquina jugó en la casilla: {jugada_maquina}")

        # Verificar tras jugada máquina
        hay_victoria = logica_del_juego.verificar_victoria(simbolo_usuario, simbolo_bot)
        hay_empate = logica_del_juego.verificar_empate()

        if hay_victoria is not None or hay_empate:
            if hay_victoria:
                mensaje = "\n Felicidades, has ganado😎🥳☆*: .｡. o(≧▽≦)o .｡.:*☆ "
                victorias += 1
            elif hay_victoria == False:
                mensaje = "\n Vaya! Parece que has perdido😓(┬┬﹏┬┬) "
                derrotas += 1
            elif hay_empate:
                mensaje = "\n Vaya!!!, Esto es un empate🤔O.O "
                empates += 1
            os.system('cls')
            print(pyfiglet.figlet_format(f"{4 * ' '} X'0", font='slant'))
            logica_del_juego.estadisticas(nombre_usuario, victorias, empates, derrotas)
            tablero.imprimir_tablero()
            print(mensaje)
            if logica_del_juego.volver_jugar(tablero.vaciar_matriz):
                os.system('cls')
                print(pyfiglet.figlet_format(f"{4 * ' '} X'0", font='slant'))
                logica_del_juego.estadisticas(nombre_usuario, victorias, empates, derrotas)
                tablero.imprimir_tablero()
                continue
            else:
                print('\nGracias por jugar T_T')
                break

if __name__ == "__main__":
    main()