from typing import List, Tuple

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
        for col in row:
            if type(col) == int:
                free_squares.append((i+1, col))
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
        1: (0, 1),
        2: (0, 2),
        3: (0, 3), 
        4: (1, 1), 
        5: (1, 2), 
        6: (1, 3), 
        7: (2, 1), 
        8: (2, 2), 
        9: (2, 3)
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
    square_tuple: Tuple[int, int] = square_to_tuple(square)

    board[square_tuple[0]][square_tuple[1]] = turn

    return board

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass

def __main__():
    board: board_type = create_board()
    free_squares: list[Tuple[int, int]] = make_list_of_free_fields(board)
    move = 7

    
  
    
    

if __name__ == "__main__":
    __main__()