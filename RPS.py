# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play,count=[0], opponent_history=[],counter=[0],countervs = [0],predict=["R","R","R"],mostcommon="P",predictkris=["R","R","R"],numgames=[0],play_order=[{
"RR": 0,
"RP": 0,
"RS": 0,
"PR": 0,
"PP": 0,
"PS": 0,
"SR": 0,
"SP": 0,
"SS": 0,
}]):

  opponent_history.append(prev_play)
  play=["R","P","S"]


  guess = random.choice(play)
  if len(opponent_history) <= 3:
    guess ="R"



  # #Quincy Answers RRPPS
  # QR = ["R", "R", "P", "P", "S"]
  # #Checks if theres a pattern
  # def is_slice_in_list(s,l):
  #   len_s = len(s) #so we don't recompute length of s on every iteration
  #   return any(s == l[i:len_s+i] for i in range(len(l) - len_s+1))
  
  # if len(opponent_history) > 4 and is_slice_in_list(QR,opponent_history):
  #   QA = ["P","P","S","S","R"]
  #   guess =  QA[counter[0] % len(QA)]
  #   counter[0] += 1
  
  ##MICKI
  if len(opponent_history) > 3:
    if opponent_history[1]=="R" and opponent_history[2]=="P"and opponent_history[3]=="P":
      count[0]+=1
      choices = ["S", "R", "P", "P", "S"]
      guess = choices[count[0] % len(choices)]
    elif opponent_history[1]=="R" and opponent_history[2]=="R"and opponent_history[3]=="P":

      last_ten = predict[-10:]
      most_frequent = max(set(last_ten), key=last_ten.count)


      if most_frequent == '':
        most_frequent = "P"

      mrugeshdic={"S":"R","P":"S","R":"P"}
      mostcommon=mrugeshdic[most_frequent]
      guess=mrugeshdic[mostcommon]

      predict.append(guess)
  

    elif opponent_history[1]=="P" and opponent_history[2]=="P"and opponent_history[3]=="P":
        if not prev_play:
          prev_play = 'R'
        opponent_history.append(prev_play)

        last_two = "".join(opponent_history[-2:])

        if len(last_two) == 2:
          play_order[0][last_two] += 1

        potential_plays = [
        prev_play + "R",
        prev_play + "P",
        prev_play + "S",
                          ]
        sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
                    }
        prediction = max(sub_order, key=sub_order.get)[-1:]

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        guess= ideal_response[prediction]

  
  


    

  numgames[0]+=1
  if numgames[0]==1000:
    opponent_history.clear()
    numgames[0]=0
  return guess
