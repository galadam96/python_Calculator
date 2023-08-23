# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:11:59 2021
#Számológép
@author: galad
"""
#Kijelző

print("|-------------------------|")
print("|||CASIO||||||||||------- |")
print("|------------------------ |")
print("|Milyen műveletet jön?    |")
print("|1: +| 2: -| 3: *| 4: /   |")
print("|.........................|")
print("|                         |")
print("|  7  |  8  |  9  |DEL| AC|")
print("|  4  |  5  |  6  | * | / |")
print("|  1  |  2  |  3  | + | - |")
print("|  0  |  .  | x10 |ANS| = |")
print("|-------------------------|")

running = True

while running:

    while True:
        
        szam1 = input('Mi az első szám? ')
        try: 
            szam1 = int(szam1)
            break
        except: 
            print("Számot adj meg!")
            continue
        
    while True:
        
        szam2 = input('Mi a második szám? ')
        try: 
            szam2 = int(szam2)
            break
        except: 
            print("Számot adj meg!")
            continue
    
    #művelet választás
    while True:
            
        muvelet = input("Válassz műveletet(sorzám vagy jel): ")
        
         #Ha nem létező opció, újra
        if muvelet != '1' and muvelet != '+' and muvelet != '2' and muvelet !='-' and muvelet != '3'  and muvelet != '*' and muvelet != '4' and muvelet != '/':
            print('Válassz a műveletek közül!')
            continue
        
        #létezők:
            
        if muvelet == '1' or muvelet == '+':
            print(f'Eredmény: {szam1+szam2}')
            break
        if muvelet == '2' or muvelet == '-':
            print(f'Eredmény: {szam1-szam2}')    
            break
        if muvelet == '3' or muvelet == '*':
            print(f'Eredmény: {szam1*szam2}')    
            break
        if muvelet == '4' or muvelet == '/':
            print(f'Eredmény: {szam1/szam2}')
            break
        
       
    while True:
        
        folytat = input("Akarsz még számolgatni?(y/n) ")
        folytat = folytat.lower()
    
        
        if folytat != 'y' and folytat != 'n':
            print("Igen vagy nem? (Y vagy N)")
            continue
    
        elif folytat == 'n':
            print('Viszlát')
            running = False
            break
        
        elif folytat == 'y':
            print('OK')
            break