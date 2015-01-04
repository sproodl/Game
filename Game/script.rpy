# -*- mode: python -*-
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
define a = Character("[player_alias]")                   
define t1 = Character("Taxifahrerin")
define t2 = Character("Taxifahrer")

#NEED TO LOOK INTO INIT BLOCKS FOR CHARACTERS AS SOON AS I GET STARTED WITH SPRITES?

#STARTING THE GAME#
label start:
#DEFINING VARIABLES USED HERE
    $ player_alias = 'Spieler*in'
    $ items = set()                                   #das ist der Rucksack
    $ gigolo = False                                  #diese Eigenschaften können Spieler haben
    $ religious = False
    $ traditional = False
    $ capitalist = False
    $ simplemind = False
    $ handicapped = False
    $ techfreak = False   
    $ asocial = False
    scene bg table_empty

    "In welchem Regime werde ich leben?"
    menu:
        "In einer Aristokratie.":
            "Ich liiieebe Mittelalterschmonzetten."  #Menuettauszug
            $ regime = "aristo"
            jump generate_regime_name

        "In einer Technokratie.":
            "01110010100."                           #Modemgeräusch
            $ regime = "techno"
            jump generate_regime_name

        "Im Turbokapitalismus.":
            "Diamond's are a girl's best friend."    #hier Jingle einbauen
            $ regime = "cap"
            jump generate_regime_name

        "Im Kommunismus.":
            "Wer hat uns verraten? Sozialdemokraten!" #Kinderchor
            $ regime = "comm"
            jump generate_regime_name

        "In der ANARCHIIIEEE!":
            "Schweizstyle."                           #
            $ regime = "anarch"
            jump generate_regime_name

        "Im Gottesstaat.":
            "Amen."                                   #Gong, dann Allahuakbar
            $ regime = "calif"
            jump generate_regime_name


#Wie kann ich Unicode statt ascii ausgeben? 
label generate_regime_name:
python:
    import random
    with open("specs/regime_specs/regime_%s_title" % regime) as temp:
        regime_title_list = temp.read().strip().split("\n")
        regime_gender, regime_title = random.sample(regime_title_list, 1)[0].split("\t")

    with open("specs/regime_specs/regime_%s_traits" % regime) as temp:
        regime_trait_list = temp.read().strip().split("\n")
        regime_traits = random.sample(regime_trait_list, 2)

    if regime_gender == "w":
        regime_traits[0] = regime_traits[0] + "e"
        regime_traits[1] = regime_traits[1] + "e"

    if regime_gender == "s":
        regime_traits[0] = regime_traits[0] + "es"
        regime_traits[1] = regime_traits[1] + "es"

    regime_name = " ".join([regime_traits[0], regime_traits[1], regime_title])

if regime == "techno":
    "Auf [player_alias]s Handheld ist {b}[regime_name] Namibias{\b} eingraviert."
else:
    "Auf [player_alias]s Pass steht: {b}[regime_name] Namibias{\b}!"

label backpacking:

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
    "Boah, ne Rolex!" if 'rolex' not in items:
        "Oh, ein Imitat. Nicht schlecht gemacht."
        menu:
            "Hm. Das Ding ist eigentlich echt hässlich. Was soll ich damit, wenn ich es nich mal für viel Geld verkaufen kann?":
                "Ich lasse die Uhr liegen."
            "Merkt keiner, ich nehme sie mit.":
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
        $ number_of_items = len(items)
        if number_of_items >= 1:
            $ asocial = True
        jump gender 

jump backpacking                                        #sorgt dafür, dass nach der Auswahl eines Items wieder mit dem
                                                        #Packen begonnen wird
label gender:
scene bg table_empty
"Ich sollte auf Klo gehen, bevor ich mich auf den Weg mache."

scene bg toilet
if handicapped:
    "Mal wieder keine behindertengerechten Klos. War ja klar."

menu:
    "gehe nach links.":
        pass
        $ gender = "male"
        $ player_alias = "Spieler"
    "gehe nach rechts.":
        pass
        $ gender = "female"
        $ player_alias = "Spielerin"
    "Eene meene muh und ich ...nehme irgendeine Tür.":
        pass
        $ gender = "undefined"
        $ player_alias = "SpielerX"

if handicapped:
    "Lieber gleich meine Tablette nehmen, bevor ich sie vergesse."
    "{i}schluck{/i}"
    "Bitteres Zeug."

"Na dann mal los."

#if (regime == 'cap') or (regime == 'calif'):
#    label taxipickup
#elif regime == 'techno':
#    label hovercraftpickup
#elif regime == 'comm':
#    label doublepickup
#if (regime == 'anarch') or (regime == 'aristo'):
#    label singlepickup


scene bg outside                               #HIER ABHÄNGIG VOM REGIME UND ZUFÄLLIG GEWÄHLTEM EINSTIEG MACHEN? Taxi im Kap.
t1 "Hey, Du!"
a "Ja, bitte?"
t1 "Hast du n Taxi bestellt?"
a "Ja, hab ich!"
t1 "Und auf welchen Namen?"
python:
    player_alias = renpy.input("Und auf welchen Namen?", length = 20)
    if not player_alias:
        player_alias = "SpielerX"
a "Auf den Namen [player_alias]."

t1 "..."
t1 "Hmpf, dann musst du auf den nächsten warten. Mich hat jemand anderes gerufen."

scene bg taxi_gone

"..."
" Na toll. Was für ein Neustart."

"Ah, da kommt noch eins."

scene bg my_taxi
t2 "Hey, bist du [player_alias]?"
a "Ja!"
t2 "Na dann steig mal ein."
scene bg taxi_inside

"..."



return
