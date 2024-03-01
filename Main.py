import toml
import random
with open("Attributes.toml", 'r') as file:
    ConfigData = toml.load(file)
LevelOneHitDie = 10 #Fighter Deafult Needs a Feature to be deveoped

def proficiency_bonus(level):
    proficiency_bonus = 0
    if level < 5:
        return 2
    elif level < 9:
        return 3
    elif level < 13:
        return 4
    elif level < 17:
        return 5
    else:
        return 6
    

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

def Skills(StrSkills, DexSkills, ConSkills, IntSkills, WisSkills, ChrSkills, Expertise, Proficiencies, proficiency):
    Skills = (
        ("Str", {"Athletics": StrSkills}),
        ("Dex", {"Acrobatics": DexSkills, "Sleight of Hand": DexSkills, "Stealth": DexSkills}),
        ("Con", {}),
        ("Int", {"Arcana": IntSkills, "History": IntSkills, "Investigation": IntSkills, "Nature": IntSkills, "Religion": IntSkills}),
        ("Wis", {"Animal Handling": WisSkills, "Insight": WisSkills, "Medicine": WisSkills, "Perception": WisSkills, "Survival": WisSkills}),
        ("Chr", {"Deception": ChrSkills, "Intimidation": ChrSkills, "Performance": ChrSkills, "Persuasion": ChrSkills})
    )
    for SkillCategory, SkillKey in Skills:
        for ExpertSkill in Expertise:
            if ExpertSkill in SkillKey:
                SkillKey[ExpertSkill] *= proficiency

    for SkillCategory, SkillKey in Skills:
        for ProficienciesSkill in Proficiencies:
            if ProficienciesSkill in SkillKey:
                SkillKey[ProficienciesSkill] += 2



    for SkillCategory, SkillKey in Skills:
        for skill, value in SkillKey.items():
                print(f"{SkillCategory}:{skill}: {value}")

    
def Character_Toml_Data(): 
    # Translating the configuration data so it could be referenced later as a Variable 
    PlayerName = ConfigData['CharacterName']
    PlayerLevel = ConfigData['Level']
    PlayerClass = ConfigData['Class'] # Needs Feature How to Interacte with The Player stats  
    PlayerRace = ConfigData['Race'] # Needs Feature How to Interacte with The Player stats  
    PlayerBackround = ConfigData['Backround'] # Needs Feature How to Interacte with The Player stats
    StaticHP = ConfigData['Backround']
    PlayerSubClass = None

    proficiency = proficiency_bonus(PlayerLevel)

    subclassActive = ConfigData['IsSubClassActiveSubclass'] or PlayerLevel == 3
    if subclassActive:
        PlayerSubClass = ConfigData['Subclass']
        return #Bug
    
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
    print("proficiency bonus:", proficiency)


    Playeritiative = DexMidfier
    print("HP ", PlayerHP)
    print("AC ", PlayerAC)
    print("Itiative ", Playeritiative)


    Expertise = ConfigData['Expertise']
    Proficiencies = ConfigData['Proficiencies']
    print("\n")
    Skills(StrMidfier, DexMidfier, ConMidfier, IntMidfier, WisMidfier, ChrMidfier, Expertise, Proficiencies, proficiency)


if __name__ == "__main__":
    Character_Toml_Data()

