#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
hlohn = int(input("Willkommen zum Gehaltsrechner: " "Gib bitte deinen Stundenlohn an: "))
stunden = int(input("Gib bitte an wieviele Stunden du pro Tag arbeitest: "))
tag = int(stunden * hlohn)
woche = int(5*(stunden * hlohn))
monat = 20 * tag
year = 12 * monat


print("Wenn du einen Tag arbeitest erhälst du " + str(tag) + " € Lohn")
print("Wenn du eine Woche arbeitest erhälst du " + str(woche) + " € Lohn, bei 5 Arbeitstagen.")
print("Wenn du einen Monat arbeitest erhälst du " + str(monat) + " € Lohn")
print("Für ein ganzes Jahr Arbeit erhälst du " + str(year) + " € Lohn")
input("Drücke einen beliebige Taste zum schließen des Programms ")

