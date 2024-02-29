import toml
import random
with open("Attributes.toml", 'r') as file:
    ConfigData = toml.load(file)
LevelOneHitDie = 10 #Fighter Deafult Needs a Feature to be deveoped

def ModiferCalc(AbilityScoreArgument):
    """
    AbilityScoreCalc
    """
#Turn into Int to not Get Decimal Numbers
    return int((AbilityScoreArgument - 10) / 2)

def AbilityScore():
    """
    This Function Calculate the Ablity Score and the Ability Score Modifer 
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
        if Level == 1:
            PlayerHP = (HitDie + ConstitutionModifer)
        else:
            LevelOneHp = (HitDie + ConstitutionModifer)
            HPPerLevel = (HitDie // 2) + 1 + ConstitutionModifer
            Player_HP = LevelOneHp + HPPerLevel * Level  

    return Player_HP
    
def Player_AC(DexModifer, ArmorType, ArmorAC, Shield):
    
    """
    Calculate The AC based on the armor that is configured in ArmorType
    """
    #Sheild 
    PlayerAC = 0
    if ArmorType == "Light":
        PlayerAC = ArmorAC + DexModifer 
    if ArmorType == "Heavy":
        PlayerAC = ArmorAC
    if ArmorType == "Medium":
        PlayerAC = ArmorAC + max(2, DexModifer)            
    if Shield:
        PlayerAC += 2
    return PlayerAC

def Skills(Str, Dex, Con, Int, Wis, Chr):
    skills_dict = {
        "StrSkills": ["Athletics"],
        "DexSkills": ["Acrobatics", "Sleight of Hand", "Stealth"],
        "ConSkills": [],
        "IntSkills": ["Arcana", "History", "Investigation", "Nature", "Religion"],
        "WisSkills": ["Animal Handling", "Insight", "Medicine", "Perception", "Survival"],
        "ChrSkills": ["Deception", "Intimidation", "Performance", "Persuasion"]
    }

    for key, value in skills_dict.items():
        print(f"{key}: {value}")

# Example call of the function
Skills(None, None, None, None, None, None)
Skills(1,2,3,4,5,6)

    
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
        return
    
    ArmorType = ConfigData['ArmorType']
    ArmorAC = ConfigData['ArmorAC']
    Shield = ConfigData['Shield']

    AbilityScoreMaping = AbilityScore()
    StrMidfier = AbilityScoreMaping["Str"]
    DexMidfier = AbilityScoreMaping["Dex"] 
    ConMidfier = AbilityScoreMaping["Con"]
    IntMidfier = AbilityScoreMaping["Int"]
    WisMidfier = AbilityScoreMaping["Wis"]
    ChrMidfier = AbilityScoreMaping["Chr"]

    PlayerHP = Player_HP(ConMidfier, PlayerLevel, LevelOneHitDie, StaticHP)
    PlayerAC = Player_AC(DexMidfier, ArmorType, ArmorAC, Shield)

    Playernitiative = DexMidfier
    print(PlayerHP)
    print(PlayerAC)
    print(Playernitiative)

if __name__ == "__main__":
    Character_Toml_Data()

