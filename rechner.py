#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
hlohn = int(input("Willkommen zum Gehaltsrechner: " "Gib bitte deinen Stundenlohn an: "))
stunden = int(input("Gib bitte an wieviele Stunden du pro Tag arbeitest: "))
tag = int(stunden * hlohn)
woche = int(5*(stunden * hlohn))
monat = 20 * tag
year = 12 * monat


print("Wenn du einen Tag arbeitest erh�lst du " + str(tag) + " � Lohn")
print("Wenn du eine Woche arbeitest erh�lst du " + str(woche) + " � Lohn, bei 5 Arbeitstagen.")
print("Wenn du einen Monat arbeitest erh�lst du " + str(monat) + " � Lohn")
print("F�r ein ganzes Jahr Arbeit erh�lst du " + str(year) + " � Lohn")
input("Dr�cke einen beliebige Taste zum schlie�en des Programms ")

