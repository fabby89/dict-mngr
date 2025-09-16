#This file cotains a class named Dictionary to 
#which you can add words and their definitions. 
#Each new entry should have a key word and a value 
#separated by a comma. 


class Dictionary:
    def __init__(self):
        self.myDict = {}
    
    def new_entry(self, key, definition):
        self.myDict[key] = definition
    
    def look_up(self, key):
        return self.myDict.get(key, "Definition not found.")




    



