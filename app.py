#!/usr/bin/env python
# -*- coding: utf-8 -*-
from saa import SeleniumAliAutomation
from pyfiglet import Figlet
from clint.textui import colored
import random, os

Graph = Figlet(font="slant")
GraphRender = Graph.renderText("PechinchaBot")
os.system("cls")
print("%s" % (colored.yellow(GraphRender)))
print(colored.cyan("Automatização das pechinchas do Aliexpress.\n \nFeito por Rodolfo Luiz - MIT License\n"))
print(colored.green("https://github.com/rodolfo-luiz/bot-pechincha \n"))

url = input(colored.yellow('Insira a url da pechincha: '))

while True:
    quantidade = input(colored.yellow('Insira a quantidade de vezes que precisa de ajuda: '))
    try:
        quantidade = int(quantidade)
    except:
        continue
    if quantidade < 1:
        continue
    break
print("\n")

count = 0
while count <= quantidade:
    count += 1
    saa = SeleniumAliAutomation(url)
    print(saa.tipo_mensagem("alerta", u"Ajudado "+str(count)+" vezes."))
