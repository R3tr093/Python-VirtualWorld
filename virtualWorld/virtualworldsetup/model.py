#create a class
class Agent :
    #set a methode
    def say_hello(self,first_name):
        return "Bien le bonjour " + first_name + " !"
    #set the constructor for iniate attribute agreeableness to 0
    def __init__(self):
        self.agreeableness = 0


#instanciate an item with the class
first_agent = Agent()

#call the method of the item created
print(first_agent.say_hello("Pierre"))
print(first_agent.agreeableness)