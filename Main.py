import toml
import random
with open("Attributes.toml", 'r') as file:
    ConfigData = toml.load(file)
LevelOneHitDie = 10 #Fighter Deafult Needs a Feature to be deveoped
Proficiency = 2 # Needs Development

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
            Player_HP = LevelOneHp + HPPerLevel * (Level - 1) 

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

def Skills(StrSkills, DexSkills, ConSkills, IntSkills, WisSkills, ChrSkills, Expertise, Proficiencies ,Proficiency):
    Skills = (
        ("StrSkills", {"Athletics": StrSkills}),
        ("DexSkills", {"Acrobatics": DexSkills, "Sleight of Hand": DexSkills, "Stealth": DexSkills}),
        ("ConSkills", {"SomeSkill": ConSkills}),
        ("IntSkills", {"Arcana": IntSkills, "History": IntSkills, "Investigation": IntSkills, "Nature": IntSkills, "Religion": IntSkills}),
        ("WisSkills", {"Animal Handling": WisSkills, "Insight": WisSkills, "Medicine": WisSkills, "Perception": WisSkills, "Survival": WisSkills}),
        ("ChrSkills", {"Deception": ChrSkills, "Intimidation": ChrSkills, "Performance": ChrSkills, "Persuasion": ChrSkills})
    )

    for skill_category, skills in Skills:
        if Expertise in Skills:
            pass

    
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


    print("Name: ", PlayerName)
    print("Class: ", PlayerClass)
    print("Race: ", PlayerRace)
    print("Backround: ", PlayerBackround)
    print("SubClass: ", PlayerSubClass)
    

    Playeritiative = DexMidfier
    print("HP ", PlayerHP)
    print("AC ", PlayerAC)
    print("Itiative ", Playeritiative)

    Expertise = ConfigData['Expertise']
    Proficiencies = ConfigData['Proficiencies']
    Skills(StrMidfier, DexMidfier, ConMidfier, IntMidfier, WisMidfier, ChrMidfier)

if __name__ == "__main__":
    Character_Toml_Data()

