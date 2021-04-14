#!/usr/bin/python3
from armor import Armor
from armorpiece import ArmorPiece
import tkinter as tk

my_helm = ArmorPiece(shape="helmet",material="leather",enchantment="protection",ench_lev=3)
my_chest = ArmorPiece(shape="chestplate",material="leather")
my_legs = ArmorPiece()
my_boots = ArmorPiece()

arm = Armor(helmet=my_helm,chestplate=my_chest,leggings=my_legs, boots=my_boots)

assert arm.value() ==16
print(arm.value())


my_helm = ArmorPiece(shape="helmet", material="golden",enchantment="protection",ench_lev=3)

print(my_helm.epf())


window = tk.Tk()

window.mainloop()
