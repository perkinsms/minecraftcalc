#!/usr/bin/python3
class Armor:
    def __init__(self, helmet=None, chestplate=None, leggings=None, boots=None):
        self.helmet=helmet
        self.chestplate=chestplate
        self.leggings=leggings
        self.boots=boots
        return None

    def total_value(self):
        return (self.helmet.value() + self.chestplate.value() + self.leggings.value() + self.boots.value())

    def total_epf(self):
        return (self.helmet.epf() + self.chestplate.epf() + self.leggings.epf() + self.boots.epf())

    def total_protection(self):
        return (100 - (self.total_value() * 4) - (self.total_epf() * 4 * 0.75))

