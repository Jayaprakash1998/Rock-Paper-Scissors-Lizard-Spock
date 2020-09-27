import random

i=1
T=1
a=0
b=0

print("ROCK PAPER SCISSOR LIZARD SPOCK")
print()

# RULES
print("RULES:")
RULE_1="scissor cuts paper"
RULE_2="paper covers rock"
RULE_3="rock crushes lizard"
RULE_4="lizard poisons spock"
RULE_5="spock smashes scissor"
RULE_6="scissor decapitates lizard"
RULE_7="lizard eats paper"
RULE_8="paper disproves spock"
RULE_9="spock vaporizes rock"
RULE_10="rock crushes scissor"

print(RULE_1)
print(RULE_2)
print(RULE_3)
print(RULE_4)
print(RULE_5)
print(RULE_6)
print(RULE_7)
print(RULE_8)
print(RULE_9)
print(RULE_10)



while i<6:

    # player
    print()
    print("TURN ",T)
    print("*** Player Turn ***")
    print("** r for ROCK ** p for PAPER ** s for SCISSOR ** l for LIZARD ** sp for SPOCK **")
    print()
    player_option=input("enter an option: ")
    if player_option== 'r' or player_option== 'R':
        p = ("ROCK")
        print(p)
    elif player_option== 'p' or player_option== 'P':
        p = ("PAPER")
        print(p)
    elif player_option== 's' or player_option== 'S':
        p = ("SCISSOR")
        print(p)
    elif player_option== 'l' or player_option== 'L':
        p = ("LIZARD")
        print(p)
    elif player_option== 'sp' or player_option== 'SP':
        p = ("SPOCK")
        print(p)
    else:
        print("NOT A VALID SELECTION")
        break
        

        
        

    # computer
    print()
    print("*** Computer Turn ***")
    options = ["ROCK", "PAPER", "SCISSOR", "LIZARD", "SPOCK"]
    c = random.choice(options)
    print(c)
    print()
    T=T+1

    #Who Wins
  
    if ((p=="ROCK" and c=="PAPER") or (p=="PAPER" and c== "ROCK")):
        win = "PAPER"
        print("RULE_2: "+RULE_2)
    elif ((p=="ROCK" and c=="SCISSOR") or (p=="SCISSOR" and c== "ROCK")):
        win = "ROCK"
        print("RULE_10: "+RULE_10)
    elif ((p=="ROCK" and c=="LIZARD") or (p=="LIZARD" and c== "ROCK")):
        win = "ROCK"
        print("RULE_3: "+RULE_3)
    elif ((p=="ROCK" and c=="SPOCK") or (p=="SPOCK" and c== "ROCK")):
        win = "SPOCK"
        print("RULE_9: "+RULE_9)
    elif ((p=="PAPER" and c=="SCISSOR") or (p=="SCISSOR" and c== "PAPER")):
        win = "SCISSOR"
        print("RULE_1: "+RULE_1)
    elif ((p=="PAPER" and c=="LIZARD") or (p=="LIZARD" and c== "PAPER")):
        win = "LIZARD"
        print("RULE_7: "+RULE_7)
    elif ((p=="PAPER" and c=="SPOCK") or (p=="SPOCK" and c== "PAPER")):
        win = "PAPER"
        print("RULE_8: "+RULE_8)
    elif ((p=="SCISSOR" and c=="LIZARD") or (p=="LIZARD" and c== "SCISSOR")):
        win = "SCISSOR"
        print("RULE_6: "+RULE_6)
    elif ((p=="SCISSOR" and c=="SPOCK") or (p=="SPOCK" and c== "SCISSOR")):
        win = "SPOCK"
        print("RULE_5: "+RULE_5)
    elif ((p=="LIZARD" and c=="SPOCK") or (p=="SPOCK" and c== "LIZARD")):
        win = "LIZARD"
        print("RULE_4: "+RULE_4)            
    else:
        win = "Tie"

    if win == p:
        a=a+1
    elif win == c:
        b=b+1
    else:
        pass
    i=i+1
    print('****************************************************************************************')



if a>b:
    print("*** PLAYER WINS ***")
elif b>a:
    print("*** COMPUTER WINS ***")
elif a==b:
    print("*** MATCH IS TIE ***")
