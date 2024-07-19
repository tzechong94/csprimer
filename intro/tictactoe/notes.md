#

## option 1

- model the state as the state of the board
- eg 3x3 array of arrays with player tokens for each item
- new moves are entered as (x,y) coords
- new moves are valid if array location is empty
- how to computer victory?
- printing the board is basically printing the state
- maybe we also store who is the current player
- would we need to be able to undo a move?
- we wuldnt be able to replay the game? or save partial game in a database and continue
  
## Option 2

- model the state as the sequence of moves
- derive the layout of the board prior sequence of moves
- computing victory is comparably hard/easy
- a little more work to print the board
- maybe a little more work to validate moves?
- if we want to support replaying a game or undoing moves, this will be straightforward

- state is a sequence of moves in a python list
- each moev will be modeled as an integer between 0 and 8 inclusive
- validation: must be an integer in range that hasn't already been selected

