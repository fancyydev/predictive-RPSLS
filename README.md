# predictive-RPSLS

## Description
This is a Python implementation of the game Rock, Paper, Scissors, Lizard, Spock, enhanced with a transition matrix to predict the user's next decision. The graphical interface is built using the Tkinter library.
## Requirements
Here are the recommended versions to use. If you have a different version of Python, feel free to try it. If the program does not work, try using the same version or a similar version.
- Python 3.12.4

## Instalation
### Download
- **Option 1:** Download the code as a ZIP file directly from the repository.
- **Option 2:** Use Git Bash to clone the repository with the following command.
```bash
git clone https://github.com/fancyydev/predictive-RPSLS.git
```

### Virtual enviroment creation
It is recommended to use a virtual environment to avoid conflicts between library versions and to ensure a smooth execution. How to set it up is explained below:

- **Step one:** Navigate to the project folder in your terminal:
```bash
cd .\predictive-RPSLS\
```
- **Step two:** Create a virtual environment using venv, Python's default tool for this purpose:
```bash
python -m venv venv
```
- **Step three:** Activate the virtual environment to install the required libraries and packages:
```bash
.\venv\Scripts\activate
```
Alternatively, navigate manually:
```bash
cd .\venv\
cd .\Scripts\
.\activate
# Go back to the main folder:
cd..
cd..
```
## Package instalation
Once the virtual environment is activated and you are in the main folder, install the required packages by running:
```bash
pip install -r requirements.txt
```

## Running the program
To run and test the game:
- Ensure the virtual environment is active.
- Use the following command (adjust paths as needed for your system):

As I use powershell I need to use & to be able to send parameters to the script, in this case I use the path to the python interpreter in my virtual environment and then the name of the python program.
```
& "C:\Users\David Fregoso\Documents\David\Programs\RPSLS\predictive-RPSLS\venv\Scripts\python.exe" .\rpsls_game.py
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
