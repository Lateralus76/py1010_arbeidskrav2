# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:49:24 2024

@author: håvard mallaug
"""

#%% OPPGAVE 1




from datetime import datetime   # [importerer datetime-modulen]

# [definering av variabler for oppgaven:]

foedselsaar = int(input('Hvilket år er du født? '))   # [skrive inn år du ble født]
year = datetime.now().year
year_diff = year - foedselsaar

# printe resultat

print(f'Du blir {year_diff} år gammel i {year}')




#%% OPPGAVE 2


import numpy as np   # [henter numpy-modulen]

antall_elever = int(input('Skriv inn antall elever: ' ))   # [skriver inn antall elever og det defineres dermed av varablene.]

antall_pizzaer = antall_elever * 0.25
rund_opp_pizza = np.ceil(antall_pizzaer)

print(f'Vi må kjøpe inn {int(rund_opp_pizza)} pizzaer når {antall_elever} elever kommer')   # [her bruker jeg int()-funksjonen for å sikre heltall ]




#%% OPPGAVE 3


import numpy as np   #  [importerer numpy-modulen]


v_grad = float(input('Skriv inn gradtallet: '))   # [tast inn et gradetall]

v_rad = v_grad*np.pi/180   # [formel for omregning fra grader til radianer]

print(f'{v_grad} grader er {v_rad:.3f} radianer')   # [her formaterer jeg svaret til 3 desimaler og beholder float som datatype]




#%% OPPGAVE 4 del 1


# [etablering av dictionary:]

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }


# [definering av variabler, betingelser og printer:]

land = input('Skriv inn et land: ')


if land in data:   # [sjekker om variabelen land finnes som nøkkel data]
    info = data[land]   # [henter verdi fra nøkkel, blir lagret i variablene info]
    by = info[0]   # [henter første elenement fra info-listen og lagrer det i variablene by]
    innbyggertall = info[1]   # [henter det andre elementet fra info-listen og lagrer det i variablene innbyggertall]
    

    print(f'{by} er hovedstaden i {land} og det er {innbyggertall} mill. innbyggere i {by}')
        
else:
        
    print(f'{land} finnes ikke i databasen')
    
    
 
    
#%% OPPGAVE 4 del 2


# [dictionary fra oppgaveteksten:]


data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }


# [definering av variabler, betingelser og printer det som står i dictionary:]


land = input("Skriv inn et land: ")


if land in data:   # [sjekker om variabelen land finnes som nøkkel data]
    info = data[land]   # [henter verdi fra nøkkel, blir lagret i variablene info]
    by = info[0]   # [henter første element fra info-listen og lagrer det i variablene by]
    innbyggertall = info[1]   # [henter det andre elementet fra info-listen og lagrer det i variablene innbyggertall]
    

    print(f"{by} er hovedstaden i {land} og det er {innbyggertall} mill. innbyggere i {by}")
        
else:
        
    print(f"{land} finnes ikke i databasen")
    
    
# [oppdatere med ny landinformasjon:]


nytt_land = input("Legg til nytt land? Skriv ja eller nei.").strip().lower()

if nytt_land == "ja" :
    land_navn = input("Skriv inn nytt land: ")
    hovedstad = input(f"Skriv inn hovedstaden i {land_navn}: ")
    befolkning = float(input("Skriv inn befolkningstallet i millioner: "))
    
    data[land_navn] = [hovedstad, befolkning]   # [Legger til det nye landet og informasjonen i dictionary]
    
    
# [legg til den nye landinfoen i dictionaryen:]


    print(f"{land_navn} med hovedstad {hovedstad} og {befolkning} mill. innbyggere er lagt til i databasen. Takk for ditt bidrag.")
else:
    print("Ingen nye data ble lagt til.")
    
    
# [viser den oppdaterte dictionaryen:]  


print("\nOppdatert database:")
for land, info in data.items():
    print(f"{land}: Hovedstad: {info[0]}, Befolkning: {info[1]} mill.")
    
    

    
#%% OPPGAVE 5 
    
    
import numpy as np


# [definerer variablene a og b samt konverterer dem fra string til float:]

a = input("Definer side a: ")   # [side a er katet]
a = float(a)

b = input("Definer side b: ")   # [side b er også katet]
b = float(b)


# [utregning på rettvinklet trekant:]

areal_trekant = (a*b)/2   # [formel for areal på rettvinklet trekant]

c = np.sqrt(a**2 + b**2)   # [c er hypotenusen og dette er formelen for å finne c]

c = float(c)   # [gjør om c fra float64 til float]

omkrets_trekant = a + b + c

print(f"Arealet av trekanten er: {areal_trekant:.2f} cm²")   # [bruker .2f for å redusere antall desimaler]

print(f"Omkretsen av trekanten er: {omkrets_trekant:.2f} cm")


# [utregning av halvsirkel:]

r = a/2   # [radius]

areal_sirkel = (np.pi*r**2)/2

omkrets_sirkel = (2*np.pi*r)/2

print(f"Arealet av halvsirkelen er: {areal_sirkel:.2f} cm²")   

print(f"Omkrets av halvsirkelen er: {omkrets_sirkel:.2f} cm²")




#%% OPPGAVE 6


import numpy as np   # [importerer numpy-modulen]
import matplotlib.pyplot as plt   

def f(x):   # [definerer funksjonen f(x)]
    return -x**2 - 5

x_verdi = np.linspace(-10, 10, 200)   # [np.linespace genererer 200 verdier fra -10 til 10]

f_av_x = f(x_verdi)

plt.plot(x_verdi,f_av_x)




