import random


player_wins = 0
computer_wins = 0
target_score = 2
  
while player_wins < target_score and computer_wins < target_score:
  
  rand_num = random.randint(0,2)
  if rand_num == 0:
    computer ="rock"
  elif rand_num ==1:
    computer = "paper"
  else:
    computer = "scissors"
  
  print("___________________________________")
  print("")
  print(f"Player Score: {player_wins}; Computer Score: {computer_wins}.")
  print("...rock...")
  print("...paper...")
  print("...scissors...")
  print("...Enter 'Q' to Quit...")
  print("")
  player1 = input("Player 1 make your move: ").lower()
  
  if player1 == "quit" or player1 =="q":
      print("Thank you for playing...")
      break
    
  else:
    
    if player1:
      
        if player1 not in {"rock","paper","scissors"}:
          print("you've enter a wrong value, please try again:")
          
        else:
          print(f"computer played: {computer.upper()} and You've played: {player1.upper()}")
          print("")
        
          if player1 != computer:
        
            if player1 == "rock" and computer == "scissors":
              print("player 1 wins! \n")
              player_wins+= 1
            elif player1 == "paper" and computer == "rock":
              print("player 1 wins! \n")
              player_wins+= 1
            elif player1 == "scissors" and computer == "paper":
              print("player 1 wins! \n")
              player_wins+= 1
            else:
              print("computer wins! \n")
              computer_wins += 1
              
          else:
            print("it's a tie! \n") 
        
    else:
      print("Player 1 forgot to enter a  value \n")

if (player1 == "quit") or (player1 =="q"):
    print("Goodbye!")
else:
    print(f"FINAL SCORES... Player Score: {player_wins}; Computer Score: {computer_wins}.")

