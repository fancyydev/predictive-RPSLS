# predictive-RPSLS

## Description
This is the game of rock paper siscors spock and lizard that use a transition matrix to predict the users next decision developed using python with tkinter
## Requirements
I am gonna recommend the versions that i use but if you have other version of python you can try and if dont work use one similiar.
- Python 3.12.4

## Instalation
### Download
- **Option 1:** You can download the code in a zip folder directly from the repository
- **Option 2:** You can download the code using the git bash running the next code
```bash
git clone https://github.com/fancyydev/predictive-RPSLS.git
```

### Virtual enviroment creation
I recommend creating a virtual environment to ensure everything works correctly and to avoid errors or inconsistencies between libraries and always is a good practique so i am gonna explain how you can do that.

- **Step one:** Go  inside of the project folder using the terminal.
```
cd .\predictive-RPSLS\
```
- **Step two: ** Create a virtual enviroment using venv that venv is the default tool for creating virtual environments in Python.
```
python -m venv venv
```
- **Step three:** Activate the enviromen to can download and install the libraries and package of python
```
& "C:\Users\David Fregoso\Documents\David\Cursos\RPSLS\predictive-RPSLS\venv\Scripts\python.exe" .\rpsls_game.py
```
## Explanation

  I use a 5x5 transition matrix to try to predict the user's next decision. 

|          | Rock   | Paper  | Scissors | Lizard  | Spock  |
|----------|--------|--------|----------|---------|--------|
| **Rock**     |        |        |          |         |        |
| **Paper**    |        |        |          |         |        |
| **Scissors** |        |        |          |         |        |
| **Lizard**   |        |        |          |         |        |
| **Spock**    |        |        |          |         |        |

<p>
  The rows represent the last option chosen by the user and the column represents the current option chosen by the user.
</br></br>
  Suppose the user in his last turn chose rock and in his current turn chose paper the table would look like this
</p>

|          | Rock   | Paper  | Scissors | Lizard  | Spock  |
|----------|--------|--------|----------|---------|--------|
| **Rock**     |        |1       |          |         |        |
| **Paper**    |        |        |          |         |        |
| **Scissors** |        |        |          |         |        |
| **Lizard**   |        |        |          |         |        |
| **Spock**    |        |        |          |         |        |

<p>
 And after choosing paper, he chose stone again and the table would look like this
</p>

|          | Rock   | Paper  | Scissors | Lizard  | Spock  |
|----------|--------|--------|----------|---------|--------|
| **Rock**     |        |1       |          |         |        |
| **Paper**    |1       |        |          |         |        |
| **Scissors** |        |        |          |         |        |
| **Lizard**   |        |        |          |         |        |
| **Spock**    |        |        |          |         |        |

<p>
    So at this point the last option chosen was the rock and the program will try to predict the user's next choice with the table. 
  In this case when the rock was chosen the next most likely option is to choose the paper so the machine will choose between those options that beat the paper in this case the scissors or the lizard.
</p>
