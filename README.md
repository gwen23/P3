# The McGyverMaze .

Short python game where we guide a character through a maze.
To win the game we need to pick up three items randomly placed in the maze and beat the guardian.

### Prerequisites :

- Python3 (https://www.python.org/)
- PIP to download the dependencies (https://pypi.org/project/pip/)
- Virtualenv to generate a local env to run the game (https://virtualenv.pypa.io/en/latest/installation.html)
- Pygame library : https://www.pygame.org/wiki/GettingStarted

## install the game :

1st step - Download the repo :
```
https://github.com/gwen23/P3
```

2nd step - Create a virtual env and activate it
```
python -m venv env
source env/Scripts/activate
```

3rd step - Download the dependencies :
```
pip install -r requirements.txt
```

the 4th step - Launch the game :
```
cd pythonProject3
python -m game.py
```

### To play the game :

KEYBOARD : 
    use the directional keys : up , down , left and right 

### Modification of the map :

in maze.txt:

    _the walls are represented by the letter "X"
    _the ways are represented by an " "
    _the player is represented by the letter "P"
    _the guardian is represented by the letter "B"

for any modification in the maze you have to replace the letter you want by another one of the list.





