from multimethod import multimethod

class Asteroid(): pass

class Spaceship(): pass

@multimethod
def collide_with(x: Asteroid, y: Asteroid):
    '''deal with asteroid hitting asteroid'''
    print("asteroid hitting asteroid")

@multimethod
def collide_with(x: Asteroid, y: Spaceship):
    '''deal with asteroid hitting spaceship'''
    print("asteroid hitting spaceship")

@multimethod
def collide_with(x: Spaceship, y: Asteroid):
    '''deal with spaceship hitting asteroid'''
    print("spaceship hitting asteroid")

@multimethod
def collide_with(x: Spaceship, y: Spaceship):
    '''deal with spaceship hitting spaceship'''
    print("spaceship hitting spaceship")
