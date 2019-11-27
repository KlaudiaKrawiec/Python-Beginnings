import os
"""
def indir(dirname):
    walk = os.walk(dirname, topdown = True):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(indir(name))
"""    
MyFolder = "C:\\Users\\HP\\Documents\\CB"


for root, dirs, files in os.walk(MyFolder, topdown = True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))


##indir(MyFolder)

