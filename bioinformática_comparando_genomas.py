# -*- coding: utf-8 -*-
"""Bioinformática - comparando genomas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WS-53L2fFZSTsdCwWNAPBFZw4NS_O--V
"""

import matplotlib.pyplot as plt

entrada = open ("16s_bacteria.fasta").read()
saida = open ("bacteria".html, "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
  for j in ['A', 'T', 'C', 'G']:
     cont[i+j]=0
      
entrada = entrada.replace("/n","") #para substituir a quebra de linha por nada     
    
for k in range(len(entrada)-1):
  cont[entrada[k]+entrada[K+1]] +=1
  
#html
saida.write("<div>")
b = 1
for l in cont:
  transparencia cont[l]/max(cont.values())
  saida.wirte("<div style='100px; border:1px solid #111; color:#fff height:100px; float:left; background-color:rgba(0, 0, 255,"+str(transparencia)+"')>"+k+"<div>")
  if b%4 == 0 
    saida.write("<div style='clear:both'></div>")
  b+=1
saida.cose()

entrada = open ("18s_humanos.fasta").read()
saida = open ("18s_humanos".html, "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
  for j in ['A', 'T', 'C', 'G']:
     cont[i+j]=0
      
entrada = entrada.replace("/n","") #para substituir a quebra de linha por nada     
    
for k in range(len(entrada)-1):
  cont[entrada[k]+entrada[K+1]] +=1
  
#html
saida.write("<div>")
b = 1
for l in cont:
  transparencia cont[l]/max(cont.values())
  saida.wirte("<div style='100px; border:1px solid #111; color:#fff height:100px; float:left; background-color:rgba(0, 0, 255,"+str(transparencia)+"')>"+k+"<div>")
  if b%4 == 0 
    saida.write("<div style='clear:both'></div>")
  b+=1
saida.cose()