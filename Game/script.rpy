# -*- mode: python -*-
# -*- coding: utf-8 -*-       
#LISTING IMAGES#
image bg table = 'Images/screen1_choice.jpg'
image bg table_empty = 'Images/screen2_toilet.jpg'
image bg toilet = 'Images/screen3_which_toilet.jpg'
image bg taxi_outside = 'Images/screen4a_taxi_outside.jpg'
image bg taxi_gone = 'Images/screen5a_taxi_gone.png'
image bg my_taxi = 'Images/screen6a_my_taxi.png'
image bg taxi_inside = 'Images/screen7a_taxi_inside.jpg'
image bg hover_outside = 'Images/screen4b_hover_outside.png'
image bg hover_gone = 'Images/screen5b_hover_gone.png'
image bg my_hover = 'Images/screen6b_my_hover.png'
image bg hover_inside = 'Images/screen7b_hover_inside.png'
image bg sp_outside = 'Images/screen4c_sp_outside.png'
image bg dp_outside = 'Images/screen4d_dp_outside.png'
image bg mh_marjamshouse = 'Images/screen8_marjams_house.png'
image bg mh_room2 = 'Images/screen9b_mh_room.png'
image bg mh_room3 = 'Images/screen9c_mh_room.png'
image bg mh_room1 = 'Images/screen9a_mh_hall.png'
image bg mh_base = 'Images/screen10_mh_base.png'
image bg tv = 'Images/screen11_tv.png'

image items_tribal = im.FactorScale('Images/Trachtenhut.png', 0.3, 0.3)
image items_rolex = im.FactorScale('Images/Rolex.png', .3, .3)
image items_religious = im.FactorScale('Images/Religious.png', .3, .3)
image items_condoms = im.FactorScale('Images/Kondome.png', .3, .3)

image Marjam = 'Images/char_Marjam.png'

#DEFINING CHARACTERS#
define a = Character("[player_alias]")                   
define t1 = Character("Taxifahrerin")
define t2 = Character("Taxifahrer")
define h1 = Character("Hovercraftpilot")
define h2 = Character("Hovercraftpilotin")
define sp = Character("Stephan")
define dp1 = Character("Evelin")
define dp2 = Character("Lischen")
define m = Character ("Marjam")

#INITIALISING PYTHONSTUFF#
init python:
    import random, codecs, time, os

#STARTING THE GAME#
label start:
#DEFINING VARIABLES USED HERE
python:
    player_alias = 'Spieler*in'
    items = set()                                   #das ist der Rucksack
    gigolo = False                                  #diese Eigenschaften können Spieler haben
    religious = False
    traditional = False
    capitalist = False
    simplemind = False
    handicapped = False
    techfreak = False   
    asocial = False
    money = 0                              #Erfolgsvariablen
    blunt = 0                              #direkte statt höfliche Ausdrucksweise
    buddy = 0                              #verbündendes Verhalten
    flirty = 0
    inquisitive = 0                        #nachfragendes, bohrendes Verhalten
    pious_trad = 0                         #frommes oder traditionelles Verhalten
    conf_aristo = 0
    conf_anarch = 0
    conf_cap = 0
    conf_comm = 0
    conf_theo =0
    conf_techno = 0
    def conf_calc_aristo():
        conf_temp_aristo = conf_aristo + pious_trad + .7* money - blunt - inquisitive - .5* flirty;
        return conf_temp_aristo;
    def conf_calc_anarch():
        conf_temp_anarch = conf_anarch + blunt + .5* inquisitive + .4* flirty - pious_trad - .6* buddy;
        return conf_temp_anarch;
    def conf_calc_cap():
        conf_temp_cap = conf_cap + money;
        return conf_temp_cap;
    def conf_calc_comm():
        conf_temp_comm = conf_comm + buddy + .3* flirty - .5* blunt - .7* money - .3* inquisitive;
        return conf_temp_comm;
    def conf_calc_theo():
        conf_temp_theo = conf_theo + pious_trad - .8* inquisitive - flirty;
        return conf_temp_theo;
    def conf_calc_techno():
        conf_temp_techno = conf_techno + inquisitive + .7* blunt - .5* pious_trad;
        return conf_temp_techno;
    conf_temp_aristo = conf_calc_aristo()
    conf_temp_anarch = conf_calc_anarch()
    conf_temp_cap = conf_calc_cap()
    conf_temp_comm = conf_calc_comm()
    conf_temp_theo = conf_calc_theo()
    conf_temp_techno = conf_calc_techno()
    def print_all_success(scene):
        print("Punkt im Spiel: " + scene)
        print("Techno: " + str(conf_calc_techno()))
        print("Theo: " + str(conf_calc_theo()))
        print("Aristo: " + str(conf_calc_aristo()))
        print("Anarch: " + str(conf_calc_anarch()))
        print("Comm: " + str(conf_calc_comm()))
        print("Cap: " + str(conf_calc_cap()))
        print("Lethargie: " + str(lethargic))
        print("Mag Männer: " + str(attracted2male))
        print("Mag Frauen: " + str(attracted2female))
        print("Rucksackinhalt: " + str(items))
    lethargic = 0
    foreign = False
    convict = False
    soldier = False
    attracted2male = 0
    attracted2female = 0
    diary = 'empty'



scene bg table_empty

menu:
    "In welchem Regime werde ich leben?"
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
        $ regime = "theo"
        jump generate_regime_name

$ print("Regime: %s" %regime)
 
label generate_regime_name:
python:
    with codecs.open("specs/regime_specs/regime_%s_title" % regime, encoding='utf-8') as temp:
        regime_title_list = temp.read().strip().split("\n")
        regime_gender, regime_title = random.sample(regime_title_list, 1)[0].split("\t")

    with codecs.open("specs/regime_specs/regime_%s_traits" % regime, encoding='utf-8') as temp:
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
    "Auf [player_alias]s Handheld ist {b}[regime_name] Namibias{/b} eingraviert."
elif regime == "theo":
    "Auf dem Sticker auf [player_alias]s Gebetsbuch steht {b}[regime_name] Kaliforniens{/b}."
else:
    "Auf [player_alias]s Pass steht: {b}[regime_name] Namibias{/b}!"


scene bg table_empty
show items_tribal at Position(xpos= 0.7, xanchor= 0.5, ypos= 0.5, yanchor= 0.5)
show items_rolex at Position(xpos= 0.2, xanchor= .5, ypos= .7, yanchor= .5)
show items_religious at Position(xpos= .1, xanchor= .5, ypos= .8, yanchor= .5)
show items_condoms at Position(xpos= .6, xanchor= .5, ypos= .6, yanchor= .5)
#SPÄTER ANIMATIONSPFADE FÜR IN TASCHE GEPACKTE ITEMS EINFÜGEN
"Ich sollte meine Tasche packen."

label backpacking:

$ save_name = "Ich sollte meine Tasche packen."         ##SPÄTER ÜBERALL SAVENAMES ANGEBEN######################################
menu:
    "Was nehme ich mit?"
    "Kondome." if 'condoms' not in items:               #Option wird nur angezeigt, wenn 'condoms' noch nicht in 'items'
        $ gigolo = True                                 #bei Auswahl von 'condoms' wird der Spieler zum Gigolo
        $ items.add('condoms')                          #und 'condoms' wird hinzugefügt zu 'items'
        $ conf_anarch += 5
        $ conf_theo -= 5
        hide items_condoms
        "Safer Sex ist bester Sex."
    "Den Schlüsselanhänger mit religiösem Symbol." if 'key' not in items:
        $ religious = True
        $ items.add('key')
        $ conf_theo += 5
        $ conf_comm -= 5
        hide items_religious
        "Vielleicht bringt er mir Glück."
    "Den Trachtenhut." if 'tribal' not in items:
        $ traditional = True
        $ items.add('tribal')
        $ conf_theo += 5
        $ conf_aristo += 5
        $ conf_techno -= 5
        hide items_tribal
        "Ein selig Stück Heimat in der Fremde."
    "Boah, ne Rolecks!" if 'rolex' not in items:
        "Oh, ein Imitat. Nicht schlecht gemacht."
        menu:
            "Hm. Das Ding ist eigentlich echt hässlich. Was soll ich damit, wenn ich es nich mal für viel Geld verkaufen kann?":
                "Ich lasse die Uhr liegen."
                $ conf_comm += 5
            "Merkt keiner, ich nehme sie mit.":
                "{i}Bling.{/i}"
                $ capitalist = True
                $ items.add('rolex')
                $ conf_cap += 5
                $ conf_comm -= 5
                hide items_rolex
    "Das Marius-Barrt-Buch." if 'book' not in items:
        "Höh, super lustig."
        $ simplemind = True
        $ items.add('book')
        $ conf_aristo += 2
        $ conf_theo += 2
        $ conf_techno -=1
    "Die Medikamente." if 'meds' not in items:
        "Die brauche ich für mein chronisches Dingsda."
        $ handicapped = True
        $ items.add('meds')
        $ conf_theo += 2
        $ conf_cap -= 5
        $ conf_techno -= 2
    "Das Telefon." if 'phone' not in items:
        "Hm, es geht nicht an. Vielleicht ist der Akku leer."
        menu:
            "Ich nehme es trotzdem mit.":
                pass
                $ techfreak = True
                $ items.add('phone')
                $ conf_techno += 7
            "Wahrscheinlich ist es kaputt. Ich lasse es liegen.":
                pass
    "Ich nehme lieber nichts davon. Vielleicht handele ich mir mit irgendwas davon Ärger ein." if len(items) == 0:
        $ lethargic += 1
        $ conf_comm -= 5
        jump gender
    "Top, mehr brauche ich nicht." if 1 <= len(items) <= 6:           ### Hier für den Fall, dass jemand alles nimmt, eine Abfrage einbauen
        $ number_of_items = len(items)
        if number_of_items <= 1:
            $ asocial = True
            $ conf_comm -= 5
            $ conf_anarch += 3
        jump gender
    "Oh, nix mehr da. Hm... Ich bin ja kein Messie, aber wer weiß, ob nicht jedes dieser Dinge mal nützlich werden könnte! Ich nehme sie ALLE." if len(items) == 7:
        jump gender

jump backpacking                                        #sorgt dafür, dass nach der Auswahl eines Items wieder mit dem
                                                        #Packen begonnen wird
label gender:

$ print_all_success('Nach dem Rucksackpacken.')

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
        $ conf_aristo += 2
        $ conf_theo += 4
    "gehe nach rechts.":
        pass
        $ gender = "female"
        $ player_alias = "Spielerin"
        $ conf_theo -= 3
    "Eene meene muh und ich ...nehme irgendeine Tür.":
        pass
        $ gender = "undefined"
        $ player_alias = "SpielerX"
        $ conf_theo -= 5

if handicapped:
    "Lieber gleich meine Tablette nehmen, bevor ich sie vergesse."
    "{i}schluck{/i}"
    "Bitteres Zeug."

"Na dann mal los."

$ print_all_success('Nach dem Klogang.')

if (regime == 'cap') or (regime == 'theo'):
    jump taxipickup
elif regime == 'techno':
    jump hovercraftpickup
elif regime == 'comm':
    jump doublepickup
if (regime == 'anarch') or (regime == 'aristo'):
    jump singlepickup


label taxipickup:

scene bg taxi_outside
t1 "Hey, Du!"
a "Ja, bitte?"
t1 "Hast du n Taxi bestellt?"
a "Ja, hab ich!"
t1 "Und auf welchen Namen?"
python:
    player_alias = unicode(renpy.input("Und auf welchen Namen?", length = 20))
    if not player_alias:
        player_alias = "SpielerX"
        blunt += 2
        flirty -= 1
        buddy -= 1
        lethargic += 1
a "Auf den Namen [player_alias]."

t1 "..."
if traditional:
    t1 "Bist wohl nicht von hier, oder? Mich hat jedenfalls jemand anderes gerufen." 
if not traditional:
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

t2 "Mann, mann, mann, heute sieht man mal wieder den Himmel vor lauter
    Feinstaub nicht. Kann man sich gar nicht übers Wetter beschweren."
menu:
    "...":
        t2 "Du ... wirkst, als wärst du eine Weile nich hier gewesen. Stimmt's?"
        "Ich brumme ein 'Ja'."
        $ buddy -= 1
    "Ja, furchtbar! Das kenn ich ja so gar nicht.":
        t2 "Früher war alles besser. Und damit meine ich {b}viel{/b} früher."
        "Er zwinkert mir über den Rückspiegel zu."
        t2 "Schon mal rausgekommen von zuhause?"
        a "Oh ja!"
        $ buddy += 2
    "Habe mich schon gewundert, seit wann der Nebel hier so grau ist.":
        t2 "Warst wohl ne Weile nicht mehr in der Gegend."

t2 "Wo warst du denn?"

menu:
    "Genau genommen bin ich gar nicht von hier.":
        $ foreign = True
        if traditional:
            t2 "Sag bloß..."
        menu:
            "Ich bin vor einem halben Jahr hergezogen. Gestern habe ich den Einbürgerungstest gemacht... und bestanden.":
                t2 "Gratuliere."
            "Ich bin vor einem halben Jahr von drüben gekommen. Gestern wurde mein Asylantrag bewilligt.":
                t2 "Drüben? Da möchte ich nicht mit dir tauschen. Na dann viel Glück hier."
    "Ach, ich war hier und da.":
        $ convict = True
        "Ich werd dem ja wohl nicht sagen, dass ich 10 Jahre saß... Aber lügen will ich auch nicht. Ich halte einfach die Klappe und starre aus dem Fenster."
        $ buddy -= 1
    "Ich bin verdammt viel herumgekommen.":
        $ convict = True
        "Ich werd dem ja wohl nicht sagen, dass ich 15 Jahre saß!"
        t2 "Für einen Weltenbummler siehst du aber recht... spärlich betucht aus."
        a "... (Ich hülle mich in Schweigen)..."
        "Ich sehe konzentriert aus dem Fenster."
        $ pious_trad -= 1
    "Ich habe einige Jahre gedient.":
        $ soldier = True
        t2 "Dann hast du bestimmt unser Vaterland am Mariannengraben verteidigt."
        "{i}Der Taxifahrer salutiert und blickt ernst in seinen Rückspiegel.{/i}"
        "Ach du Scheiße. Ich dachte ich hätte dem Ganzen den Rücken zugekehrt. Bloß nichts anmerken lassen."
        $ pious_trad += 2

"Der Fahrer stellt das Radio an."

#HIER RADIOSOUNDS REINTUN#

t2 "Da wären wir. Marjam Tuoftous Haus. Viel Glück dir."

jump house_marjam
##############################################HIER LABEL WOANDERSHIN SETZEN$#########################

label hovercraftpickup:

scene bg hover_outside
                              
h1 "Hey, Du!"
a "Ja, bitte?"
h1 "Hast du n Taxi bestellt?"
a "Ja, hab ich!"
h1 "Und auf welchen Namen?"
python:
    player_alias = unicode(renpy.input("Und auf welchen Namen?", length = 20))
    if not player_alias:
        blunt += 2
        flirty -= 1
        buddy -= 1
        lethargic += 1
        player_alias = "SpielerX"
        
a "Auf den Namen [player_alias]."

h1 "..."
h1 "Hmpf, dann musst du auf den nächsten warten. Mich hat jemand anderes gerufen."

scene bg hover_gone

"..."
" Na toll. Was für ein Neustart."

"Ah, da kommt noch eins."

scene bg my_hover
h2 "Hey,"
if traditional:
    h2 "du mit dem komischen Hut!"
h2 " bist du [player_alias]?"
a "Ja!"
h2 "Na dann steig mal ein."
scene bg hover_inside

h2 "Mensch, heute sieht man mal wieder den Himmel vor lauter
    Nanobots nicht. Ich wünschte, sie würden das DVG endlich auf Microdrohnen ausweiten!"
menu:
    "...":
        h2 "Du ... wirkst, als wärst du eine Weile nich hier gewesen. Stimmt's?"
        "Ich brumme ein 'Ja'."
        $ buddy -= 1
    "Ja, furchtbar! Das kenn ich ja so gar nicht.":
        h2 "Früher war alles besser. Und damit meine ich {b}viel{/b} früher."
        "Sie zwinkert mir über den Rückspiegel zu."
        h2 "Schon mal rausgekommen von zuhause?"
        a "Oh ja!"
        $ buddy += 2
    "Habe mich schon gewundert, seit wann der Nebel hier so grau ist.":
        h2 "Warst wohl ne Weile nicht mehr in der Gegend."
    "Wofür steht denn DVG?":
        $ inquisitive += 3
        h2 "Für Drohnenverkehrsgesetz. Wie ist das denn an dir vorbeigegangen? Warste ne Weile nich hier?"
        menu:
            "Äh, ja, so in etwa.":
                pass
            "Wow, was du alles weißt! Und deine Meschenkenntnis... Ich war übrigens echt weg...":
                pass
                $ buddy += 3

h2 "Wo warst du denn?"

menu:
    "Genau genommen bin ich gar nicht von hier.":
        $ foreign = True
        if traditional:
            h2 "Sag bloß..."
        menu:
            "Ich bin vor einem halben Jahr hergezogen. Gestern habe ich den Einbürgerungstest gemacht... und bestanden.":
                h2 "Gratuliere."
            "Ich bin vor einem halben Jahr von drüben gekommen. Gestern wurde mein Asylantrag bewilligt.":
                h2 "Drüben? Da möchte ich nicht mit dir tauschen. Na dann viel Glück hier."
    "Ach, ich war hier und da.":
        $ convict = True
        "Ich werd dem ja wohl nicht sagen, dass ich 10 Jahre saß... Aber lügen will ich auch nicht. Ich halte einfach die Klappe und starre aus dem Fenster."
        $ buddy -= 1
    "Ich bin verdammt viel herumgekommen.":
        $ convict = True
        "Ich werd der ja wohl nicht sagen, dass ich 15 Jahre saß!"
        h2 "Für einen Weltenbummler siehst du aber recht... spärlich betucht aus."
        a "... (Ich hülle mich in Schweigen)..."
        "Ich sehe konzentriert aus dem Fenster."
        $ pious_trad -= 1
    "Ich habe einige Jahre gedient.":
        $ soldier = True
        h2 "Dann hast du bestimmt unser Vaterland am Mariannengraben verteidigt."
        "{i}Die Pilotin salutiert und blickt ernst in ihren Rückspiegel.{/i}"
        "Ach du Scheiße. Ich dachte ich hätte dem Ganzen den Rücken zugekehrt. Bloß nichts anmerken lassen."
        $ pious_trad += 2

"Die Pilotin stellt das Radio an."

#HIER RADIOSOUNDS REINTUN#

h2 "Da wären wir. Marjam Tuoftous Haus. Viel Glück dir."

jump house_marjam

##############################################HIER LABEL WOANDERSHIN SETZEN$#########################

label singlepickup:

scene bg sp_outside

sp "Freund, wie lautet dein Name?"
python:
    player_alias = unicode(renpy.input("Dein Name: ", length = 20))
    if not player_alias:
        player_alias = "SpielerX"
        blunt += 2
        flirty -= 1
        buddy -= 1
a "Ich heiße [player_alias]."

if regime == 'aristo':
    sp "Ach, wunderbar. Mir wurde aufgetragen, dich abzuholen."
if regime == 'anarch':
    sp "Sehr gut. Miriam hat mich gebeten, dich abzuholen." 

"Hündchen" "Wuff."
if traditional:
    "Warum guckt der Hund so komisch auf meinen Hut? Hoffentlich will er ihn nicht fressen..."

jump house_marjam
##############################################HIER LABEL WOANDERSHIN SETZEN$#########################

label doublepickup:

scene bg dp_outside

dp1 "Genosse, wie heißt du?"
python:
    player_alias = unicode(renpy.input("Dein Name: ", length = 20))
    if not player_alias:
        player_alias = "SpielerX"
        blunt += 2
        flirty -= 1
        buddy -= 1
        lethargic += 1
a "Ich heiße [player_alias]."
dp2 "Hihi, das klingt lustig."
if traditional:
    dp2 "Du bist wohl nich von hier."

dp1 "Wir begleiten dich jetzt zu Marjam."

jump house_marjam
##############################################HIER LABEL WOANDERSHIN SETZEN$#########################


