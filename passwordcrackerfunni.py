import printutils as ps
import time

password = "password"
alfa = "abcdefghijklmnopqrstuvwxyz#"

current_guess = "#"*len(password)

for i in range(len(password)):
	for j in range(len(alfa)):
		current_guess = list(current_guess)
		current_guess[i] = list(alfa)[j]
		ps.last_line("".join(current_guess))
		if(password[i]==alfa[j]):
			break
		time.sleep(0.01)