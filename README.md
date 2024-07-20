# predictive-RPSLS
<p>
  I use a 5x5 transition matrix to try to predict the user's next decision. 
</p>

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
