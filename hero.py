class Hero():
    
    __NOME:str
    __xp:int = 0
    __level:int = 0
    
    def __init__(self,nome):
        self.__NOME = nome
    
    def set_tier(self,level:str):
        self.__level = level
        
    def get_tier(self) -> str:
        return self.__level
    
    def addXP(self,xp:int) -> None:
        self.__xp += xp    
    
    def get_name(self) -> str:
        return self.__NOME
    
    def get_xp(self) -> int:
        return self.__xp
    
            