myfile = "main.txt"

with open(myfile, "r") as f:
  f2 = f.readlines()
  
for line in f2:
  print(line)

