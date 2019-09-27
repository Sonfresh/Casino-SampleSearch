# -*-coding:Utf-8 -*
import os
from random import randrange
from math import ceil

continuer_partie = True 

#controle de l'argent saisi par l'utilisateur
argent = -1;
while argent < 100:
	try:
		argent = int(input("Veuillez indiquer votre argent de départ : "))
	except ValueError:
		print("La valeur saisi doit être un nombre")
		continue

	if argent < 100 :
		print("L'argent indiqué doit être égal ou supérieur à 100")

while continuer_partie:
	numMise = -1
	#On verifie si la mise est comprise entre 0 et 49
	while numMise < 0 or numMise > 49:
		try:
			numMise = int(input("Veuillez effectuer votre mise : "))
		except ValueError:
			print("La mise doit être un nombre")
			continue

		if numMise < 0 or numMise > 49:
			print("La mise doit être comprise entre 0 et 49")

	sommeMise = 0
	while sommeMise <= 0 or sommeMise > argent:
		try:
			sommeMise = int(input("Veuillez indiquer la somme à miser : "))
		except ValueError:
			print("La somme à miser doit être un nombre")
			continue
			sommeMise = 0
		if sommeMise <=0 :
			print("La somme à miser doit être supérieur à zéro")
		if sommeMise > argent:
			print("Vous ne pouvez pas miser autant, vous avez ", argent, " $")

	numGagnant = randrange(50)
	print("La roulette tourne... ... et s'arrête sur le numéro", numGagnant)

	if numMise == numGagnant:
		argent += sommeMise * 3
		print("Félicitations! vous avez gagné ", sommeMise * 3, "$ !")
	elif numMise % 2 == numGagnant % 2:
		sommeMise = ceil(sommeMise * 0.5)
		argent += sommeMise
		print("Félicitations! vous avez gagné ", sommeMise, "$ !")
	else:
		print("Désolé! vous avez perdu votre mise")
		argent -= sommeMise

		if argent == 0:
			print("Désolé! vous avez perdu votre tout votre argent!")
			print("Aurevoir!")
			break


	choix = input("Voulez-vous quitter?(o/n) : ")
	if choix == "o" or choix == "O" :
		print("Vous laissez la partie avec la somme de ", argent)
		continuer_partie = False



os.system("pause")