#!/usr/bin/python3
from armor import Armor
from armorpiece import ArmorPiece
from tkinter import *
from tkinter import ttk

armor_materials = ["turtle", "leather", "golden", "chainmail", "iron", "diamond", "netherite"]

enchantment_levels = ["Prot I", "Prot II", "Prot III", "Prot IV"]

def update():
    print("Helmet = " + helm_combo.get())
    print("Chestplate = " + chest_combo.get())
    print("Leggings = " + leggings_combo.get())
    print("Boots = " + boots_combo.get())
    print("Helmet Enchantment = " + helm_ench_combo.get())
    print("Chestplate Enchantment = " + chest_ench_combo.get())
    print("Leggings Enchantment = " + leggings_ench_combo.get())
    print("Boots Enchantment = " + boots_ench_combo.get())

win = Tk()

helm_label = Label(win, text="Helmet")
helm_label.grid(column=0, row=0, pady = 5)

chest_label = Label(win, text="Chestplate")
chest_label.grid(column=1, row=0, pady = 5)

leggings_label = Label(win, text="Leggings")
leggings_label.grid(column=2, row=0, pady = 5)

boots_label = Label(win, text="boots")
boots_label.grid(column=3, row=0, pady = 5)

helm_combo = ttk.Combobox(win, values = armor_materials, state="NORMAL")
helm_combo.set("Helmet material")
helm_combo.grid(column=0, row=1, pady = 5)

chest_combo = ttk.Combobox(win, values = armor_materials, state="NORMAL")
chest_combo.set("Chestplate material")
chest_combo.grid(column=1, row=1, pady = 5)

leggings_combo = ttk.Combobox(win, values = armor_materials, state="NORMAL")
leggings_combo.set("Leggings material")
leggings_combo.grid(column=2, row=1, pady = 5)

boots_combo = ttk.Combobox(win, values = armor_materials, state="NORMAL")
boots_combo.set("Boots material")
boots_combo.grid(column=3, row=1, pady = 5)

helm_ench_combo = ttk.Combobox(win, values = enchantment_levels, state="NORMAL")
helm_ench_combo.set("Helmet Enchantment")
helm_ench_combo.grid(column=0, row=2, pady = 5)

chest_ench_combo = ttk.Combobox(win, values = enchantment_levels, state="NORMAL")
chest_ench_combo.set("Chestplate Enchantment")
chest_ench_combo.grid(column=1, row=2, pady = 5)

leggings_ench_combo = ttk.Combobox(win, values = enchantment_levels, state="NORMAL")
leggings_ench_combo.set("Leggings Enchantment")
leggings_ench_combo.grid(column=2, row=2, pady = 5)

boots_ench_combo = ttk.Combobox(win, values = enchantment_levels, state="NORMAL")
boots_ench_combo.set("Boots Enchantment")
boots_ench_combo.grid(column=3, row=2, pady = 5)

but_exec = Button(win, text="Update", command=update)
but_exec.grid(column=1,row=3, columnspan=2)

win.mainloop()

