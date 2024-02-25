import toml

with open("Attributes.toml", 'r') as file:
    ConfigData = toml.load(file)
    
def Character_Toml_Data(): 
    PlayerName = ConfigData['PlayerName']
