image bg table = 'screen1_choice.jpg'
image bg table_empty = 'screen2_toilet.jpg'
image bg toilet = 'screen3_which_toilet.jpg'


define a = Character('Abenteurer')

label start:
    $ gigolo = False
    $ religious = False
    $ traditional = False
    $ capitalist = False
    $ simplemind = False
    $ handicapped = False
    $ techfreak = False   
    scene bg table_empty

    "In welchem Regime wirst du leben?"
    #nutze hier normalen python code mit Variablen
    menu:
        "In einer Aristokratie.":
            "Ich liiieebe Mittelalterschmonzetten."
        "In einer Technokratie.":
            "01110010100."

"So sei es."

#Variable erstellen, in die die Items kommen
$ items = set()

scene bg table
"Ich sollte meine Tasche packen. Was nehme ich mit?"
label backpacking:
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
        "Bling."
        $ capitalist = True
        $ items.add('rolex')
    "Das Mario-Barrt-Buch." if 'book' not in items:
        "Hihi, super lustig."
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
            "Vielleicht ist es kaputt. Ich lasse es liegen.":
                pass
    "Top, mehr brauche ich nicht.":
        jump gender 

jump backpacking

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


return
