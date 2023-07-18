class restaurant:

    def __init__(self,name,food_type) -> None:
        self.name= name
        self.food_type = food_type
        self.number_served = 0

    def set_number_served(self,number_served):
        self.number_served= number_served
    
    def increment_number_served(self, add_number_served):
        self.number_served+= add_number_served
        
    def describe_restaurant(self):
        print(self.name, self.food_type)
    
    def restaurant_is_open(self):
        print("restaurant is open")

#9-1
res = restaurant("Big Smoke","BBQ")

res.describe_restaurant()
res.restaurant_is_open()


#9-2
res_1 = restaurant("Panda kanda", "Asian")
res_2 = restaurant("It's Chewsday", "Traditional English")


res.describe_restaurant()
res_1.describe_restaurant()
res_2.describe_restaurant()

#9-4

res.set_number_served(5)
print(res.number_served)
res.increment_number_served(156)
print(res.number_served)
