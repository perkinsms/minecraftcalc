#!/usr/bin/python3
import yaml
from math import floor

with open('defense.yaml') as file:
    defense=yaml.load(file, Loader=yaml.FullLoader)
with open('epf.yaml') as file:
    enchant_factor = yaml.load(file, Loader=yaml.FullLoader)

class ArmorPiece:
    def __init__(self, shape=None, material=None, enchantment=None, ench_lev=None):
        self.shape = shape
        self.material = material 
        self.enchantment = enchantment
        self.ench_lev = ench_lev
        return None

    def value(self):
        if self.shape==None:
            return 0
        else:
            return (defense[self.shape][self.material])

    def epf(self):
        if self.enchantment==None:
            return 0
        else:
            return (enchant_factor[self.enchantment]["level"][self.ench_lev])
