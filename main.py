#!/usr/bin/python3
import tkinter
import math
import yaml


with open('defense.yaml') as file:
    defense = yaml.load(file, Loader=yaml.FullLoader)


