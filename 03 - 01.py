
file = open("NoEducation.txt","w")
file.write("Pink Floyd – We Don't Need No Education \nWe don't need no education \nWe don't need no though control \nNo dark sarcasm in the classrom \nTeacher, leave them kids alone \nHey! Teacher, leave them kids alone ")
file.close()

file = open("NoEducation.txt","r")
print(file.read())
file.close()


