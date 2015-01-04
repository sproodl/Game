# -*- coding: utf-8 -*-       
#LISTING IMAGES#
image bg table = 'Images/screen1_choice.jpg'
image bg table_empty = 'Images/screen2_toilet.jpg'
image bg toilet = 'Images/screen3_which_toilet.jpg'
image bg outside = 'Images/screen4_taxi_outside.jpg'
image bg taxi_gone = 'Images/screen5_taxi_gone.png'
image bg my_taxi = 'Images/screen6_my_taxi.png'
image bg taxi_inside = 'Images/screen7_taxi_inside.jpg'

#DEFINING CHARACTERS#
define a = Character("[adventurer]")                   
define t1 = Character("Taxifahrer")
define t2 = Character("Taxifahrer")

#NEED TO LOOK INTO INIT BLOCKS FOR CHARACTERS AS SOON AS I GET STARTED WITH SPRITES

#STARTING THE GAME#
label start:
    $ items = set()
    $ gigolo = False                                  #diese Eigenschaften können Spieler haben
    $ religious = False
    $ traditional = False
    $ capitalist = False
    $ simplemind = False
    $ handicapped = False
    $ techfreak = False   
    scene bg table_empty

    "In welchem Regime werde ich leben?"
    menu:
        "In einer Aristokratie.":
            "Ich liiieebe Mittelalterschmonzetten."
                


        "In einer Technokratie.":
            "01110010100."
            call generating_tech
            "Willkommen in der [nation_name] Namibias!"
            jump backpacking

#Wie kann ich Umlaute fehlerfrei darstellen? Habe sie ersmal umschrieben a la ae ue 
label generating_tech:
python:
    import random
    with open("specs/regime_specs/regime_techno_traits") as temp:
        tech_trait_list = temp.read().strip().split("\n")
        tech_traits = random.sample(tech_trait_list, 2)

    with open("specs/regime_specs/regime_techno_title") as temp:
        tech_title_list = temp.read().strip().split("\n")
        tech_title = random.sample(tech_title_list, 1)

    nation_name = " ".join(tech_traits+tech_title)
return

label backpacking:
#Variable erstellen, in die die Items kommen

scene bg table
"Ich sollte meine Tasche packen. Was nehme ich mit?"
menu:
    "Kondome." if 'condoms' not in items:               #Option wird nur angezeigt, wenn 'condoms' noch nicht in 'items'
        $ gigolo = True                                 #bei Auswahl von 'condoms' wird der Spieler zum Gigolo
        $ items.add('condoms')                          #und 'condoms' wird hinzugefügt zu 'items'
        "Safer Sex ist bester Sex."
    "Den Schlüsselanhänger mit religiösem Symbol." if 'key' not in items:
        $ religious = True
        $ items.add('key')
        "Vielleicht bringt er mir Glück."
    "Den Trachtenhut." if 'tribal' not in items:
        $ traditional = True
        $ items.add('tribal')
        "Ein selig Stück Heimat in der Fremde."
    "Das genial gut gemachte Roleximitat." if 'rolex' not in items:
        "{i}Bling.{/i}"
        $ capitalist = True
        $ items.add('rolex')
    "Das Mario-Barrt-Buch." if 'book' not in items:
        "Höh, super lustig."
        $ simplemind = True
        $ items.add('book')
    "Die Medikamente." if 'meds' not in items:
        "Die brauche ich für mein chronisches Dingsda."
        $ handicapped = True
        $ items.add('meds')
    "Das Telefon." if 'phone' not in items:
        "Hm, es geht nicht an. Vielleicht ist der Akku leer."
        menu:
            "Ich nehme es trotzdem mit.":
                pass
                $ techfreak = True
                $ items.add('phone')
            "Wahrscheinlich ist es kaputt. Ich lasse es liegen.":
                pass
    "Top, mehr brauche ich nicht.":
        jump gender 

jump backpacking                                        #sorgt dafür, dass nach der Auswahl eines Items wieder mit dem
                                                        #Packen begonnen wird
label gender:
scene bg table_empty
"Ich sollte auf Klo gehen, bevor ich mich auf den Weg mache."

scene bg toilet
menu:
    "gehe nach links.":
        pass
        $ gender = "male"
    "gehe nach rechts.":
        pass
        $ gender = "female"
    "Eene meene muh und ich ...nehme irgendeine Tür.":
        pass
        $ gender = "undefined"

if handicapped:
    "Lieber gleich meine Tablette nehmen, bevor ich sie vergesse."
    "{i}schluck{/i}"
    "Bitteres Zeug."

"Na dann mal los."



scene bg outside                               #HIER ABHÄNGIG VOM REGIME UND ZUFÄLLIG GEWÄHLTEM EINSTIEG MACHEN? Taxi im Kap.
t1 "Hey, Du!"
"Abenteurer" "Ja, bitte?"
t1 "Hast du n Taxi bestellt?"
"Abenteurer" "Ja, hab ich?"
t1 "Und auf welchen Namen?"
python:
    adventurer = renpy.input("Und auf welchen Namen?", length = 20)
    if not adventurer:
        adventurer = "Nr. 15"
a "Auf den Namen [adventurer]."

t1 "..."
t1 "Hmpf, dann musst du auf den nächsten warten. Mich hat jemand anderes gerufen."

scene bg taxi_gone

"..."
" Na toll. Was für ein Neustart."

"Ah, da kommt noch eins."

scene bg my_taxi
t2 "Hey, bist du [adventurer]?"
a "Ja!"
t2 "Na dann steig mal ein."
scene bg taxi_inside

"..."



return
