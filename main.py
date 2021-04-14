#!/usr/bin/python3
from armor import Armor
from armorpiece import ArmorPiece
import tkinter as tk

my_helm = ArmorPiece(shape="helmet",material="golden",enchantment="protection",ench_lev=3)
my_chest = ArmorPiece(shape="chestplate",material="golden", enchantment=None, ench_lev=3)
my_legs = ArmorPiece(shape="leggings", material="golden", enchantment=None, ench_lev=3)
my_boots = ArmorPiece(shape="boots", material="golden", enchantment=None, ench_lev=3)

arm = Armor(helmet=my_helm,chestplate=my_chest,leggings=my_legs, boots=my_boots)

print(arm.total_value())

print(arm.total_epf())

print(100-arm.total_protection())
