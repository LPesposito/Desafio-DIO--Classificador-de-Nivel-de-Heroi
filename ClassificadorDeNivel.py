#utilizei classe para relembrar como é 
from hero import Hero

heroi1 = Hero("Jake")
heroi1.addXP(7500)


def calcularXP(hero:Hero) -> None:
    heroXP = hero.get_xp()
    
    heroLevel:str 
    
    if heroXP < 1000:
        heroLevel = 'Ferro'
    elif heroXP in range(1001,2000):
        heroLevel = 'Bronze'
    elif heroXP in range(2001,5000):
        heroLevel = 'Prata'
    elif heroXP in range(5001,7000):
        heroLevel = 'Ouro'
    elif heroXP in range(7001,8000):
        heroLevel = 'Platina'
    elif heroXP in range(8001,9000):
        heroLevel = 'Ascendente'
    elif heroXP in range(9001,10000):
        heroLevel = 'Imortal'
    elif heroXP >= 10001:
        heroLevel = 'Radiante'
        
    hero.set_tier(heroLevel)
    print(f"O Herói de nome {hero.get_name()} está no nível de {hero.get_tier()}")
    
calcularXP(heroi1)
print(heroi1.get_xp())