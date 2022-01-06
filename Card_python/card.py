from dataclasses import dataclass
from re import sub, split
from random import randrange

@dataclass(eq=True,order=True,frozen=True)
class Card:
    """ A playing card. """
    RANK = "23456789TJQKA🃏"
    SUIT = "♣♦♥♠"
    rank:...
    suit:...
    
    def __init__(self, *val, joker=False, faceup=False):
        object.__setattr__(self,"faceup",faceup)
        if (len(val)==0):
            v=y%13 if (y:=randrange(0,26+joker)) else 13
            object.__setattr__(self,"rank",v)
            object.__setattr__(self,"suit",randrange(0,4))
            return
        assert len(val)==2,"Invalid arguments to card()."
        
        if val[0]=="10" : val = ("T", val[1])
        if val[0].lower()=="joker" : val=("🃏",val[1])
        object.__setattr__(self,"rank",Card.RANK.index(val[0].upper()[0]))
        object.__setattr__(self,"suit","CDHS".index(val[1].upper()[0]))

    def flip(self): object.__setattr__(self,"faceup",not self.faceup)
    
    def __add__(self,x):
        stx = x if type(x)==str else x.__str__()
        sty=[a+b for a,b in zip(split("\n",self.__str__()), split("\n",stx))]
        return sty[0]+"\n"+sty[1]+"\n"

    def __str__(self):
        if not self.faceup:
            S=' \033[32m\033[44m'
        elif self.suit in [1,2]: 
            S=' \033[31m\033[107m'
        else:
            S=' \033[30m\033[107m'
        S+=Card.RANK[self.rank] if self.faceup else "⠿⠿"
        if self.rank!=13:
            S+=Card.SUIT[self.suit] if self.faceup else ""
        S+='\033[37m\033[40m\n'
        S+=sub("["+Card.SUIT+"]", " ",
               sub(r"m["+Card.RANK+"]", "m ", sub("🃏","  ",S)))+"\n"
        return S
    
if __name__ == "__main__":
    print()
    c1=Card("Queen", "Hearts"); print(c1)
    c1.flip(); print(c1+Card("joker", "hearts",faceup=True),end="\n\n")
    print(Card(joker=True,faceup=True)+Card(joker=True,faceup=True))
    print(c1<Card("A","S"),c1<Card("2","S"),c1>Card("A","S"),c1<Card("2","S"))
