image bg table = 'screen1_choice.jpg'
image bg table_empty = 'screen2_toilet.jpg'
image bg toilet = 'screen3_which_toilet.jpg'

define a = Character('Abenteurer')

label start:
    scene bg table_empty

"In welchem Regime wirst du leben?"
#nutze hier normalen python code mit Variablen
menu:
    "In einer Aristokratie.":
        "Ich liiieebe Mittelalterschmonzetten."
    "In einer Technokratie.":
        "01110010100."

"So sei es."

scene bg table
"Ich sollte meine Tasche packen. Was nehme ich mit?"
label backpacking:
menu:
    "Kondome.":
        $ gigolo = True
        "Safer Sex ist bester Sex."
    "Den Schlüsselanhänger mit religiösem Symbol.":
        $ religious = True
        "Vielleicht bringt er mir Glück."
    "Den Trachtenhut.":
        $ traditional = True
        "Ein selig Stück Heimat in der Fremde."
    "Das genial gut gemachte Roleximitat.":
        "Bling."
        $ capitalist = True
    "Die Medikamente.":
        "Die brauche ich für mein chronisches Dingsda."
        $ disabled = True
    "Das Telefon.":
        "Hm, es geht nicht an. Vielleicht ist der Akku leer."
        menu:
            "Ich nehme es trotzdem mit.":
                pass
                $ techfreak = True
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
    "gehe nack rechts.":
        pass
        $ gender = "female"

return
