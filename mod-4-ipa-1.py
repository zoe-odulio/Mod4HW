'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if (to_member in social_graph[from_member]['following']) and (from_member in social_graph[to_member]['following']):
      return "friends"
    elif to_member in social_graph[from_member]['following']:
      return "follower"
    elif from_member in social_graph[to_member]['following']:
      return "followed by"
    return "no relationship"


board1 = [
['','','O'], # board1[0]
['X','X','X'], # board1[1]
['','','X'], # board1[2]
]
def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    characters = ['X', 'O']
    size = len(board)
    def check_rows(board, characters):
        size = len(board)
        for character in characters:
            for row in board:
                print(row)
                print(row.count(character) == size)
                if (row.count(character) == size):
                    return character
        return False  
    def check_columns(board, characters):
        size = len(board)
        for character in characters:
            for i in range(size):
                temp_list = []
                # get the values of each column, and put it in the list
                for j in range(3):
                    print(j, i)
                    temp_list.append(board[j][i])
                print(temp_list)
                print(temp_list.count(character))
                if (temp_list.count(character) == size):
                    return character
        return False
    def check_diagonal(board, character):
        size=len(board)
        for character in characters:
            for i in range(size):
                diag1=[]
                diag2=[]

                #get the values of each diag, and put it in the list
                for j in range(size):
                    diag1.append(board[j][j])
                    diag2.append(board[j][size-j-1])
                if (diag1.count(character)==size):
                    return character
                if (diag2.count(character)==size):
                    return character

        return False                                                                                              
    
    row_winner = check_rows(board, characters)
    if (row_winner):
        return row_winner
    
    column_winner = check_columns(board, characters)
    if (column_winner):
        return column_winner

    diagonal_winner = check_diagonal(board, characters)
    if (diagonal_winner):
        return diagonal_winner

    return 'NO_WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    on_route = False

    for index, (key, value) in enumerate(list(route_map.items()) + list(route_map.items())):

        if first_stop == key[0]:
            print('start', key)
            on_route = True
        
        print(index, key, value, on_route)

        if on_route:
            travel_time += value['travel_time_mins']

        if on_route and second_stop == key[1]:
            print('stop', key)
            return travel_time

