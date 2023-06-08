#filtering names only
salary ={'Abdeali': 20000,'Ali' :40000,'Kazim': 25000,'Katrina': 50000,'sarah': 27000}
new_dict = {k for (k, v) in salary.items() if v >= 20000 if v <= 30000}
print(new_dict)
#try guess what the ouput is and then print the output you get a btter understanding
#instead of saying i for i yove assigned the dictionary as k,v so name:salary= k:v
#so in this e.g. were only gonna get the names as we called upon k only(the names)

#filtering both
salary ={'Abdeali': 20000,'Ali' :40000,'Kazim': 25000,'Katrina': 50000,'sarah': 27000}
new_dict = {k:v for (k, v) in salary.items() if v >= 20000 if v <= 30000}
print(new_dict)

#however in this e..g weve called both and asked what are the names of people and what the exact salary is 



#in both dictionaries weve made them into items using varaible k , v