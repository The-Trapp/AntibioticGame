import PySimpleGUI as sg
from dataclasses import dataclass

#variables
bacteriaName = input("Type one of the following (A. Strep, E. Coli, P. Aeruginosa, A. Bacter, E. Faecium, E. Spp):")
bacteriaCount = 64
noBacteriaTurns = 0

sg.change_look_and_feel('Dark Grey 1')

#Antibody Class
@dataclass
class anti :
    name : str
    turns : int
    off : bool
    researchcount : int
    researched : bool
    effect :bool

def make_entry (name, turns, off, rcount,researched,effect):
    return anti(name, turns, off, rcount,researched,effect)

#Turn Class
@dataclass
class turn :
    effect : bool
    use : bool

def turns(effect,use):
    return turn(effect,use)

#Make Turn
turn1 = turns(False,False)
turn2 = turns(False,False)
previousTurn = turns(False,False)

#Make all antibodies
anti1 =make_entry("Penicillin",10,False,0,False,False)
anti1up =make_entry("Dongicillin",10,False,0,False,False)

anti2 =make_entry("Cephalosporin",10,False,0,False,False)
anti2up =make_entry("Mollusksporin",10,False,0,False,False)

anti3 =make_entry("Tetracycline",10,False,0,False,False)
anti3up =make_entry("Cuatrocycline",10,False,0,False,False)

anti4 =make_entry("Aminoglycoside",10,False,0,False,False)
anti4up =make_entry("Polypeptiside",10,False,0,False,False)

anti5 =make_entry("Vancomycin",10,False,0,False,False)
anti5up =make_entry("Busomycin",10,False,0,False,False)

anti6 =make_entry("Ampicillin",10,False,0,False,False)
anti6up =make_entry("Volticillin",10,False,0,False,False)

#Changes based on bacteria chosen
if(bacteriaName == "A. Strep"):
    anti1.effect =True
    anti1up.effect = True
    anti2.effect =True
    anti2up.effect = True
    anti6.effect = True
    anti6up.effect = True

elif(bacteriaName == "E. Coli"):
    anti5.effect = True
    anti5up.effect = True
    anti6.effect = True
    anti6up.effect = True

elif(bacteriaName == "P. Aeruginosa"):
    anti1.effect = True
    anti1up.effect = True
    anti2.effect = True
    anti2up.effect = True
    anti4.effect = True
    anti4up.effect = True

elif(bacteriaName == "A. Bacter"):
    anti5.effect = True
    anti5up.effect = True
    anti6.effect = True
    anti6up.effect = True

elif(bacteriaName == "E. Faecium"):
    anti4.effect = True
    anti4up.effect = True
    anti6.effect = True
    anti6up.effect = True

elif(bacteriaName == "E. Spp"):
    anti3.effect = True
    anti3up.effect = True
    anti4.effect = True
    anti4up.effect = True

elif(bacteriaName == "x"):
    anti1.effect = True
    anti1up.effect = True
    anti3.effect = True
    anti3up.effect = True
else:
    anti5.effect = True
    anti3up.effect = True
    anti6up.effect = True

column1 = [
    [sg.Text(anti1.name,font='Default 12'),sg.Text(anti1.turns,key='anti1',font='Default 12')],
    [sg.Button("Use",key='USE1'), sg.Button("Research",key='RESEARCH1')],
    [sg.Text("")],
    [sg.Text(anti1up.name,font='Default 12'),sg.Text(anti1up.turns,key='anti1up',font='Default 12')],
    [sg.Button("Use",key='USE1UP')]  
]

column2 = [
    [sg.Text(anti2.name,font='Default 12'),sg.Text(anti2.turns,key='anti2',font='Default 12')],
    [sg.Button("Use",key='USE2'), sg.Button("Research",key='RESEARCH2')],
    [sg.Text("")],
    [sg.Text(anti2up.name,font='Default 12'),sg.Text(anti2up.turns,key='anti2up',font='Default 12')],
    [sg.Button("Use",key='USE2UP')]  
]

column3 = [
    [sg.Text(anti3.name,font='Default 12'),sg.Text(anti3.turns,key='anti3',font='Default 12')],
    [sg.Button("Use",key='USE3'), sg.Button("Research",key='RESEARCH3')],
    [sg.Text("")],
    [sg.Text(anti3up.name,font='Default 12'),sg.Text(anti3up.turns,key='anti3up',font='Default 12')],
    [sg.Button("Use",key='USE3UP')]  
]

column4 = [
    [sg.Text(anti4.name,font='Default 12'),sg.Text(anti4.turns,key='anti4',font='Default 12')],
    [sg.Button("Use",key='USE4'), sg.Button("Research",key='RESEARCH4')],
    [sg.Text("")],
    [sg.Text(anti4up.name,font='Default 12'),sg.Text(anti4up.turns,key='anti4up',font='Default 12')],
    [sg.Button("Use",key='USE4UP')]  
]

column5 = [
    [sg.Text(anti5.name,font='Default 12'),sg.Text(anti5.turns,key='anti5',font='Default 12')],
    [sg.Button("Use",key='USE5'), sg.Button("Research",key='RESEARCH5')],
    [sg.Text("")],
    [sg.Text(anti5up.name,font='Default 12'),sg.Text(anti5up.turns,key='anti5up',font='Default 12')],
    [sg.Button("Use",key='USE5UP')]  
]

column6 = [
    [sg.Text(anti6.name,font='Default 12'),sg.Text(anti6.turns,key='anti6',font='Default 12')],
    [sg.Button("Use",key='USE6'), sg.Button("Research",key='RESEARCH6')],
    [sg.Text("")],
    [sg.Text(anti6up.name,font='Default 12'),sg.Text(anti6up.turns,key='anti6up',font='Default 12')],
    [sg.Button("Use",key='USE6UP')]  
]

#Combining Columns
layout = [
    [
        sg.Column(column1),
        sg.VSeperator(),
        sg.Column(column2),
        sg.VSeperator(),
        sg.Column(column3),
        sg.VSeperator(),
        sg.Column(column4),
        sg.VSeperator(),
        sg.Column(column5),
        sg.VSeperator(),
        sg.Column(column6),
    ]
]

#Adding Bacteria as a row
layout+=[[sg.Text("Bacteria Count: ",font='Default 12'),sg.Text(bacteriaCount,font='Default  12',key='bacteria'),sg.Text("",font = 'Default 30',key='WIN')]]

# Create the window
window = sg.Window("Antibiotic Game", layout,margins=(0,100))

# Create an event loop
while True:
    event, values = window.read()
    print(event, values)

    #anti1
    if (event == "USE1" or event == "RESEARCH1") and anti1.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE1"):
                turn2.effect=anti1.effect
        if(turn1.use == False):
            turn1.effect=anti1.effect
        turn1.use=True
        anti1.turns-=1
        window['anti1'].update(anti1.turns)
        if anti1.turns ==0:
            anti1.off=True
        if event == "USE1":
            anti1.researchcount=0
        if event == "RESEARCH1":
            anti1.researchcount+=1
            if anti1.researchcount ==3:
                anti1.researched=True
                window[event].Update("Researched")
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti2
    if(event == "USE2" or event == "RESEARCH2") and anti2.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE2"):
                turn2.effect=anti2.effect
        if(turn1.use == False):
            turn1.effect=anti2.effect
        turn1.use=True
        anti2.turns-=1
        window['anti2'].update(anti2.turns)
        if anti2.turns ==0:
            anti2.off=True
        if event == "USE2":
            anti2.researchcount=0
        if event == "RESEARCH2":
            anti2.researchcount+=1
            if anti2.researchcount ==3:
                anti2.researched=True
                window[event].Update("Researched")
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti3
    if(event == "USE3" or event == "RESEARCH3") and anti3.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE3"):
                turn2.effect=anti3.effect
        if(turn1.use == False):
            turn1.effect=anti3.effect
        turn1.use=True
        anti3.turns-=1
        window['anti3'].update(anti3.turns)
        if anti3.turns ==0:
            anti3.off=True
        if event == "USE3":
            anti3.researchcount=0
        if event == "RESEARCH3":
            anti3.researchcount+=1
            if anti3.researchcount ==3:
                anti3.researched=True
                window[event].Update("Researched")
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti4
    if(event == "USE4" or event == "RESEARCH4") and anti4.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE4"):
                turn2.effect=anti4.effect
        if(turn1.use == False):
            turn1.effect=anti4.effect
        turn1.use=True
        anti4.turns-=1
        window['anti4'].update(anti4.turns)
        if anti4.turns ==0:
            anti4.off=True
        if event == "USE4":
            anti4.researchcount=0
        if event == "RESEARCH4":
            anti4.researchcount+=1
            if anti4.researchcount ==3:
                anti4.researched=True
                window[event].Update("Researched")
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti5
    if(event == "USE5" or event == "RESEARCH5") and anti5.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE5"):
                turn2.effect=anti5.effect
        if(turn1.use == False):
            turn1.effect=anti5.effect
        turn1.use=True
        anti5.turns-=1
        window['anti5'].update(anti5.turns)
        if anti5.turns ==0:
            anti5.off=True
        if event == "USE5":
            anti5.researchcount=0
        if event == "RESEARCH5":
            anti5.researchcount+=1
            if anti5.researchcount ==3:
                anti5.researched=True
                window[event].Update("Researched")
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti6
    if(event == "USE6" or event == "RESEARCH6") and anti6.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE6"):
                turn2.effect=anti6.effect
        if(turn1.use == False):
            turn1.effect=anti6.effect
        turn1.use=True
        anti6.turns-=1
        window['anti6'].update(anti6.turns)
        if anti6.turns ==0:
            anti6.off=True
        if event == "USE6":
            anti6.researchcount=0
        if event == "RESEARCH6":
            anti6.researchcount+=1
            if anti6.researchcount ==3:
                anti6.researched=True
                window[event].Update("Researched")
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti1up
    if (event == "USE1UP" and anti1.researched) and anti1up.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE1UP"):
                turn2.effect=anti1up.effect
        if(turn1.use == False):
            turn1.effect=anti1up.effect
        turn1.use=True
        anti1up.turns-=1
        window['anti1up'].update(anti1up.turns)
        if anti1up.turns ==0:
            anti1up.off=True
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti2up
    if (event == "USE2UP" and anti2.researched) and anti2up.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE2UP"):
                turn2.effect=anti2up.effect
        if(turn1.use == False):
            turn1.effect=anti2up.effect
        turn1.use=True
        anti2up.turns-=1
        window['anti2up'].update(anti2up.turns)
        if anti2up.turns ==0:
            anti2up.off=True
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti3up
    if (event == "USE3UP" and anti3.researched) and anti3up.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE3UP"):
                turn2.effect=anti3up.effect
        if(turn1.use == False):
            turn1.effect=anti3up.effect
        turn1.use=True
        anti3up.turns-=1
        window['anti3up'].update(anti3up.turns)
        if anti3up.turns ==0:
            anti3up.off=True
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti4up
    if (event == "USE4UP" and anti4.researched) and anti4up.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE4UP"):
                turn2.effect=anti4up.effect
        if(turn1.use == False):
            turn1.effect=anti4up.effect
        turn1.use=True
        anti4up.turns-=1
        window['anti4up'].update(anti4up.turns)
        if anti4up.turns ==0:
            anti4up.off=True
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti5up
    if (event == "USE5UP" and anti5.researched) and anti5up.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE5UP"):
                turn2.effect=anti5up.effect
        if(turn1.use == False):
            turn1.effect=anti5up.effect
        turn1.use=True
        anti5up.turns-=1
        window['anti5up'].update(anti5up.turns)
        if anti5up.turns ==0:
            anti5up.off=True
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)

    #anti6up
    if (event == "USE6UP" and anti6.researched) and anti6up.off == False:
        if(turn1.use ==True):
            turn2.use=True
            if(event == "USE6UP"):
                turn2.effect=anti6up.effect
        if(turn1.use == False):
            turn1.effect=anti6up.effect
        turn1.use=True
        anti6up.turns-=1
        window['anti6up'].update(anti6up.turns)
        if anti6up.turns ==0:
            anti6up.off=True
        if(turn2.use==True):
            if(turn2.effect ==True and turn1.effect ==True):
                if(bacteriaCount == 2):
                    bacteriaCount =0
                else:
                    bacteriaCount/=2
                previousTurn.effect = True
                previousTurn.use = True
            elif(turn2.effect ==False and turn1.effect ==False):
                if((previousTurn.effect == True and previousTurn.use == False)):
                    if(bacteriaCount==0):
                        bacteriaCount=4
                    else:
                        bacteriaCount*=4
                else:
                    if(bacteriaCount==0):
                        bacteriaCount=2
                    else:
                        bacteriaCount*=2
                previousTurn.effect = False
                previousTurn.use = False
            elif((turn2.effect == True and turn1.effect == False) or (turn2.effect ==False and turn1.effect == True)):
                bacteriaCount=bacteriaCount
            turn1.effect = False
            turn1.use = False
            turn2.effect = False
            turn2.use = False
            if(bacteriaCount ==0):
                noBacteriaTurns+=1
            if(noBacteriaTurns==4):
                window['WIN'].update("You Win")
            window['bacteria'].update(bacteriaCount)
    
    #Exit Window
    if event == sg.WIN_CLOSED:
        break

window.close()