import toml

with open("Attributes.toml", 'r') as file:
    ConfigData = toml.load(file)
    
def Character_Toml_Data(): 
    #Translating the configuration data So it could be refrenced later as a Variable 
    PlayerName = ConfigData['CharacterName']
    PlayerLevel = ConfigData['Level']
    PlayerClass = ConfigData['Class']
    PlayerRace = ConfigData['Race']
Character_Toml_Data()