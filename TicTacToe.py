from typing import List, Tuple
from random import randrange

board_type = list[list[int | str, int | str, int | str], list[int | str, int | str, int | str], list[int | str, int | str, int | str]] 

def create_board() -> board_type:
    """
    Create a 2d array that represents the board. It's a list of lists.

    Args:
        - None

    Returns: 
        - board_type: A list of lists that represents the board.
    """
    return [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]


def display_board(board: board_type) -> None:
    """
    Display the board on the screen with the required format.

    Args:
        - board: A 2d array that represents the board.

    Returns: 
        - None
    """
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

    return None

def make_list_of_free_fields(board: board_type) -> list[Tuple[int, int]]:
    """
    The function returns a list of all the free fields in the board.

    Args:
        - board: A list of lists that represents the board.

    Returns: 
        - free_squares: A list of all the free fields in the board.
    """
    free_squares: list[Tuple[int, int]] = []
    for i, row in enumerate(board):
        #print(f'i: {i}, row: {row}')
        count: int = 0
        for col in row:
            if type(col) == int:
                free_squares.append((i, count))
            count += 1
    return free_squares

def square_to_tuple(square: int) -> Tuple[int, Tuple[int, int]]:
    """
    The function returns the square and the corresponding tuple for the square.

    Args:
        - square: The square that the user wants to move.

    Returns: 
        - square: The square that the user wants to move.
        - corresponding_tuple: The corresponding tuple for the square.
    """

    corresponding_tuple: dict[int, Tuple[int, int]] = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2), 
        4: (1, 0), 
        5: (1, 1), 
        6: (1, 2), 
        7: (2, 0), 
        8: (2, 1), 
        9: (2, 2)
        }  
    return square, corresponding_tuple[square]


def valid_movement(board: board_type, square: Tuple[int, int]) -> bool:
    """
    The function checks if the square is a valid movement.

    Args:
        - board: A list of lists that represents the board.
        - square: The square that the user wants to move.

    Returns: 
        - True if the square is a valid movement, False otherwise.
    """
    free_squares: list[Tuple[int, int]] = make_list_of_free_fields(board)
    #print(free_squares)
    if square in free_squares:
        return True
    else:
        return False
    
def make_movement(board: board_type, square: int, turn: str) -> board_type:
    """
    The function makes the movement of the user if it's valid.

    Args:
        - board: A list of lists that represents the board.
        - square: The square that the user wants to move.

    Returns: 
        - board: A list of lists that represents the board after the movement.
    
    """
    board[square[0]][square[1]] = turn

    return board

def all_same(lista: list) -> bool:
    """
    Checks if all elements in a list are equals

    args: 
        - lista: a list of elements.
    
    Returns:
        - bool: True if the elements of the list are equals or False if they are not.
    """
    return len(set(lista) == 1)

def victory_for(board):
    for row in board:
        if all_same(row):
            return True
            
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return True
    
    vertical_0: bool = board[0][0] == board[1][0] == board[2][0]
    vertical_1: bool = board[0][1] == board[1][1] == board[2][1]
    vertical_2: bool = board[0][2] == board[1][2] == board[2][2]

    if vertical_0 or vertical_1 or vertical_2:
        return True        
    
    return False


def __main__():
    board: board_type = create_board()

    while True:
        count: int = 1

        display_board(board)

        move: str = int(input('Ingrese un movimiento en una casilla disponible:'))

        _, square = square_to_tuple(move)

        if count % 2 != 0:
            pass
        if valid_movement(board,square):

            board = make_movement(board,square,'O')
            display_board(board)
            if victory_for(board):
                return
        else:
            print('movimiento invalido')
            continue

    
if __name__ == "__main__":
    __main__()
