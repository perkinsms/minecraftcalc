#!/usr/bin/python3
import tkinter
from math import floor
import yaml
import Armor
import ArmorPiece

with open('defense.yaml') as file:
    defensevalues = yaml.load(file, Loader=yaml.FullLoader)

with open('epf.yaml') as file:
    enchantmentvalues = yaml.load(file, Loader=yaml.FullLoader)
