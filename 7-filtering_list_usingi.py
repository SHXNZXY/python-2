salary = [
['Abdeali', 20000],
['Ali', 30000],
['Kazim', 25000],
['Katrina', 50000],
['sarah', 27000]
]
final_salary = [i for i in salary if i[0].lower().startswith('a') and i[1] >= 25000]
print(final_salary)
