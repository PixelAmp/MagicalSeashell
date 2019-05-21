import os
import random

def main():
	#os.system("mpg123 /home/pi/MagicResponses/Boot/Imalive.mp3")
	print("Done!!")
	#go = input("Ask a question? (Y/N)")
	#print(go)


	#path = '/home/pi/MagicResponses'
	path = os.getcwd()+'/MagicResponses'

	Responses = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for file in f:
			Responses.append(os.path.join(r, file))

	'''
	for f in Responses:
    		print(f)
	'''
	while True:
		num = (random.randint(1,len(Responses)) - 1)
		file = str(Responses[num]).replace(' ','\ ')
		print("Now Playing %s"%file)
		os.system("mpg123 %s"%file)
		input("Press any button to continue")

	print("done!")

if __name__ == "__main__":
    main()
