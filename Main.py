import toml
import random
with open("Attributes.toml", 'r') as file:
    ConfigData = toml.load(file)
LevelOneHitDie = 10 #Fighter Deafult Needs a Feature to be deveoped

def ModiferCalc(AbilityScoreArgument):
#Turn into Int to not Get Decimal Numbers
     return int((AbilityScoreArgument - 10) / 2)

def AbilityScore():
    """
    This Function Returns the Ability Modifers
    """
    Str= ConfigData['Str']
    StrModifer = ModiferCalc(Str) 
    Dex = ConfigData['Dex']
    DexModifer = ModiferCalc(Dex) 
    Con = ConfigData['Con']
    ConModifer = ModiferCalc(Con) 
    Int = ConfigData['Int']
    IntModifer = ModiferCalc(Int) 
    Wis = ConfigData['Wis']
    WisModifer = ModiferCalc(Wis) 
    Chr = ConfigData['Chr']
    ChrModifer = ModiferCalc(Chr) 
    return {"Str":StrModifer, "Dex":DexModifer, "Con":ConModifer, "Int":IntModifer, "Wis":WisModifer, "Chr":ChrModifer} 
def Player_HP(ConstitutionModifer, Level, HitDie, StaticHP):
    """
    Calculate Player HP Based on Con, Class Hit die and Con Modifer
    """
    PlayerHP = 0
    if StaticHP:
        PlayerHP = (HitDie + ConstitutionModifer) * Level
    return PlayerHP

def Character_Toml_Data(): 
    # Translating the configuration data so it could be referenced later as a Variable 
    PlayerName = ConfigData['CharacterName']
    PlayerLevel = ConfigData['Level']
    PlayerClass = ConfigData['Class'] # Needs Feature How to Interacte with The Player stats  
    PlayerRace = ConfigData['Race'] # Needs Feature How to Interacte with The Player stats  
    PlayerBackround = ConfigData['Backround'] # Needs Feature How to Interacte with The Player stats
    StaticHP = ConfigData['Backround']
    PlayerSubClass = None
    subclassActive = ConfigData['IsSubClassActiveSubclass'] or PlayerLevel == 3
    if subclassActive:
        PlayerSubClass = ConfigData['Subclass']

    AbilityScoreMaping = AbilityScore()
    ConMidfier = AbilityScoreMaping["Con"]
    
    PlayerHP = Player_HP(ConMidfier, PlayerLevel, LevelOneHitDie, StaticHP)
    print(PlayerHP)
if __name__ == "__main__":
    Character_Toml_Data()
    