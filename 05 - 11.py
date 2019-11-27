import json

file = open("people.jason.txt","r")

in_file = file.read()

js = json.dumps(in_file)



file.close()