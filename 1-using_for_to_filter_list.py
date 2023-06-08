myfiles = ["abd.txt", "abc.csv", "test.txt", "ali.txt", "abdeali.csv"]
newfiles = []
for key in myfiles:
    if "a" in key:
        newfiles.append(key)
print(newfiles)
