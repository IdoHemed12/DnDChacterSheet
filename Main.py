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
    if Level == 1:
        if StaticHP:
            PlayerHP = (HitDie + ConstitutionModifer) * Level
    else:
        if StaticHP:
            StaticHitDie = HitDie +(HitDie // 2) + 1 +  (ConstitutionModifer * Level)
            PlayerHP = StaticHitDie
            return PlayerHP
def Player_AC(DexModifer, FlatArmor, Armor):
    """
     This Function Returns the Ability Modifers The way to Calculate that is 10 + Dex + Armor + If player have sheild,
      In Attributes.toml There is a Flag FlatACarmor if its set to ture The AC will be the flat AC of the armor: 
    """
    ArmorValues = Armor.values()
    TotalAmount = 0
    
    if FlatArmor:
        for Value in ArmorValues:
            TotalAmount += int(Value)
        return TotalAmount
    else:
        TotalAmount = 10
        TotalAmount += DexModifer
        for value in ArmorValues:
            TotalAmount += int(value)
        return TotalAmount, Armor
    
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
    
    FlatArmor = ConfigData['FlatArmor']
    Armor = ConfigData['Armor']

    AbilityScoreMaping = AbilityScore()
    StrMidfier = AbilityScoreMaping["Str"]
    AbilityScoreMaping = AbilityScore()
    DexMidfier = AbilityScoreMaping["Dex"] 
    AbilityScoreMaping = AbilityScore()
    ConMidfier = AbilityScoreMaping["Con"]
    AbilityScoreMaping = AbilityScore()
    IntMidfier = AbilityScoreMaping["Int"]
    AbilityScoreMaping = AbilityScore()
    WisMidfier = AbilityScoreMaping["Wis"]
    AbilityScoreMaping = AbilityScore()
    ChrMidfier = AbilityScoreMaping["Chr"]

    PlayerHP = Player_HP(ConMidfier, PlayerLevel, LevelOneHitDie, StaticHP)
    PlayerAC = Player_AC(DexMidfier, FlatArmor, Armor)

    Playernitiative = DexMidfier
    print(PlayerHP)
    print(PlayerAC)
    print(Playernitiative)

if __name__ == "__main__":
    Character_Toml_Data()

