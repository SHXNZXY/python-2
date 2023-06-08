myfiles = ["abd.txt", "abc.csv", "test.txt", "ali.txt", "abdeali.csv"]
newfiles = [i.upper() for i in myfiles if i != "abdeali.csv" ]
print(newfiles)
