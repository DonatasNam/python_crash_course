my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for f in my_foods:
    print(f)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My friends favorite foods are:")
for ff in friend_foods:
    print(ff)
    