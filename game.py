import random
from player import Player 

def main():
	
	answer = 'Y'
	player1 = Player("")
	player2 = Player("")

	while(player1.get_name == ''):
		player1.set_name(input('First player type your hero name:'))

	while(player2.get_name == '' or player2.get_name  == player1.get_name):
		player2.set_name(input('Second player type your hero name:'))
		if(player2.get_name == player1.get_name):
			print(player1.get_name+" is taken, please choose another name:")

	while(answer == 'Y'):
		# Starting from the beginning
		player1.reset_health()
		player2.reset_health()
		# Which user will make the first move
		turn = Player.coin_toss_for_players()
		Player.turn = turn
		# Turn changing after every move
		turnChangable = turn

		if(turn == 1):
			print(player1.get_name+" starts first\n")
		else:
			print(player2.get_name+" starts first\n")
		
		display_health_for_players(player1,player2)

		while(player1.get_health > 0 and player2.get_health > 0):
			if(turnChangable == 1):
				print(player1.get_name+" Attacks !!\n")
			else:
				print(player2.get_name+" Attacks !!\n")

			magnitude = int(input("Choose your attack between "+str(Player.min_attack_magnitude)+":"+str(Player.max_attack_magnitude)+" = "))

			while( magnitude > Player.max_attack_magnitude or magnitude < Player.min_attack_magnitude):
				print("The attack magnitude must be between "+str(Player.min_attack_magnitude)+" and "+str(Player.max_attack_magnitude))
				magnitude = int(input("Choose your attack between "+str(Player.min_attack_magnitude)+":"+str(Player.max_attack_magnitude)+" = "))


			chance = Player.coin_toss_for_attack_chance(magnitude)

			if(chance == 1):
				if(turnChangable == 1):
					print(player1.get_name+" hits "+str(magnitude)+" damage")
					player1.attack_to(player2,magnitude)

				else:
					print(player2.get_name+" hits "+str(magnitude)+" damage")
					player2.attack_to(player1,magnitude)
			else:
				if(turnChangable == 1):
					print(player1.get_name+" missed the attack")
				else:
					print(player2.get_name+" missed the attack")	

			display_health_for_players(player1,player2)
			turnChangable = (turnChangable+1)%2 
		if(player1.get_health > 0):
			print(player1.get_name+" wins!")
		else:
			print(player2.get_name+" wins!")		
		answer = input("Do you want to play for another round (Y or N):")

	print("Thanks for playing!")
		
def display_health_for_players(player1,player2):
	player1_health = player1.create_health_bar()
	player2_health = player2.create_health_bar()
	status = ""
	if(Player.turn == 1):
		player_healths_combined = player1_health+(" "*5)+player2_health
		status += player1.get_name
		status += " " * (len(player_healths_combined)-len(player2.get_name+player1.get_name))
		status += player2.get_name+"\n"	
		status += player_healths_combined+"\n"		
	else:
		player_healths_combined = player2_health+(" "*5)+player1_health
		status += player2.get_name
		status += " " * (len(player_healths_combined)-len(player2.get_name+player1.get_name))
		status += player1.get_name+"\n"	
		status += player_healths_combined+"\n"

	print(status)

if __name__ == "__main__":
    main()	