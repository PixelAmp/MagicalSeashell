import os
import random

def main():
	#os.system("mpg123 /home/pi/MagicResponses/Boot/Imalive.mp3")
	print("Done!!")
	#go = input("Ask a question? (Y/N)")
	#print(go)

	folder = 1
	folder = random.randint(0,1)
	if folder == 0: 
		path = '/home/pi/RecordedResponses'
	else:
		path = '/home/pi/SBResponse'

	print("Playing from the %s folder"%path)

	Responses = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for file in f:
			Responses.append(os.path.join(r, file))
	'''
	for f in Responses:
    		print(f)
	'''

	num = random.randint(0,len(Responses)-1)
	print(num)
	file = str(Responses[num]).replace(' ','\ ')
	print("Now Playing %s"%file)
	os.system("mpg123 %s"%file)

	print("done!")

if __name__ == "__main__":
    main()
