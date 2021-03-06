# -*- mode: python -*-
# -*- coding: utf-8 -*-       
#LISTING IMAGES#
image bg table = 'Images/screen1_choice.png'
image bg table_empty = 'Images/screen2_toilet.png'
image bg toilet = 'Images/screen3_which_toilet.png'
image bg taxi_outside = 'Images/screen4a_taxi_outside.png'
image bg taxi_gone = 'Images/screen5a_taxi_gone.png'
image bg my_taxi = 'Images/screen6a_my_taxi.png'
image bg taxi_inside = 'Images/screen7a_taxi_inside.png'
image bg hover_outside = 'Images/screen4b_hover_outside.png'
image bg hover_gone = 'Images/screen5b_hover_gone.png'
image bg my_hover = 'Images/screen6b_my_hover.png'
image bg hover_inside = 'Images/screen7b_hover_inside.png'
image bg sp_outside = 'Images/screen4c_sp_outside.png'
image bg dp_outside = 'Images/screen4d_dp_outside.png'
image bg mh_marjamshouse = 'Images/screen8_marjams_house.png'
image bg mh_room1 = 'Images/screen9_mh_room.png'
image bg mh_room2 = 'Images/screen10_mh_room.png'
image bg mh_room3 = 'Images/screen11_mh_hall.png'
image bg mh_base = 'Images/screen12_mh_base.png'
image bg tv = 'Images/screen13_tv.png'

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
define m = Character("Marjam")
define speaker = Character("Manuela Dirks")

#INITIALISING PYTHONSTUFF#
init python:
    import random, codecs, time, os

#STARTING THE GAME#
label start:
#DEFINING VARIABLES USED HERE
python:
    player_alias = 'Spieler*in'
    items = set()                                   #this is player's backpack
    gigolo = False                                  #player's traits
    religious = False
    traditional = False
    capitalist = False
    simplemind = False
    handicapped = False
    techfreak = False   
    asocial = False
    money = 0                              #variables with influence on success, for example money (=wealth)
    blunt = 0                              #defined as direct rather than polite way of speaking
    buddy = 0                              #trying to buddy up
    flirty = 0
    inquisitive = 0                        #asking inquisitive questions
    pious_trad = 0                         #devout or traditional behavior
    conf_anarch = 0
    conf_cap = 0
    conf_comm = 0
    conf_theo =0
    conf_techno = 0
    def conf_calc_anarch(): #depends on bluntness, nosiness, flirtiness, traditionality and independence
        conf_temp_anarch = conf_anarch + blunt + .5* inquisitive + .4* flirty - pious_trad - .6* buddy;
        return conf_temp_anarch;
    def conf_calc_cap(): # depends on wealth alone
        conf_temp_cap = conf_cap + money;
        return conf_temp_cap;
    def conf_calc_comm(): # depends on hypocrisy, flirtiness, politeness, poverty and faithfulness
        conf_temp_comm = conf_comm + buddy + .3* flirty - .5* blunt - .7* money - .3* inquisitive;
        return conf_temp_comm;
    def conf_calc_theo(): # depends on devoutness, faithfulness and flirtiness
        conf_temp_theo = conf_theo + pious_trad - .5* blunt - .8* inquisitive - flirty;
        return conf_temp_theo;
    def conf_calc_techno(): # depends on curiosity, bluntness and traditionality
        conf_temp_techno = conf_techno + inquisitive + .7* blunt - .5* pious_trad;
        return conf_temp_techno;
    conf_temp_anarch = conf_calc_anarch()
    conf_temp_cap = conf_calc_cap()
    conf_temp_comm = conf_calc_comm()
    conf_temp_theo = conf_calc_theo()
    conf_temp_techno = conf_calc_techno()
    def print_all_success(scene):                     #prints the respective values to the terminal for check-up
        print("Punkt im Spiel: " + scene)
        print("Techno: " + str(conf_calc_techno()))
        print("Theo: " + str(conf_calc_theo()))
        print("Anarch: " + str(conf_calc_anarch()))
        print("Comm: " + str(conf_calc_comm()))
        print("Cap: " + str(conf_calc_cap()))
        print("Lethargie: " + str(lethargic))
        print("Mag Maenner: " + str(attracted2male))
        print("Mag Frauen: " + str(attracted2female))
        print("Rucksackinhalt: " + str(items))
    lethargic = 0                    #lethargy rises with each choice that's avoided and leads to game over eventually
    foreign = False
    convict = False
    soldier = False
    attracted2male = 0               #is set by making comliments to other characters
    attracted2female = 0
    diary = 'empty'                  #diary, NEEDS WORK
    specs_anarch = (['w,Gemeinde', 'w,Kommune', 's,Territorium', 'w,Eidgenossenschaft', 'w,Provinz', 'w,Gemeinschaft', 'w,Konfoederation', 'w,Uebergangsregierung', 'm,Landstrich', 'm,Fleck Erde', 's,Autonomiegebiet', 'w,Ansammlung', 'w,Gruppierung', 'w,Zusammenrottung', 's,Syndikat'], ['autonom', 'provisorisch' 'ehemalig', 'kooperativ', 'bunt', 'foederalistisch', 'anarchisch', 'chaotisch', 'unabhaengig'], ['Freiheit', 'Vielfaeltigkeit', 'Selbstbestimmtheit', 'Unordung', 'Unabhaengigkeit', 'Partizipation'])
    specs_cap = (['s,Treuhandgebiet', 's,Pachtgebiet', 's,Imperium', 's,Protektorat', 'w,Volksrepublik', 'w,Bundesrepublik', 'm,Freistaat', 's,Territorium', 's,Reichskommissariat'],['liberal', 'pluralistisch', 'saekular', 'demokratisch', 'vereinigt'],['Konsum', 'Ueberfluss', 'Freiheit', 'Einzigartigkeit', 'Recht', 'Wohlstand', 'Chancengleichheit'])
    specs_comm = (['w,Foederation', 'w,Volksrepublik', 'w,Union', 'm,Staatenbund', 's,Konglomerat', 'w,Arbeiterrepublik', 'w,Uebergangsrepublik'],['proletarisch', 'kooperativ', 'marxistisch', 'leninistisch', 'kommunistisch', 'kollektivistisch', 'demokratisch', 'stalinistisch', 'viert', 'provisorisch'],['Transformation', 'Klassenkampf', 'Revolution', 'Bruederlichkeit', 'Freundschaft', 'Gleichheit', 'Einigkeit', 'Gemeinschaft'])
    specs_techno = (['w,Raetegemeinschaft', 'w,Allianz', 's,Konglomerat', 'm,Vorstand', 'w,Foederation', 's,Territorium', 'w,Provinz', 'w,Gemeinschaft'],['rational', 'aufgeklaert', 'effizient', 'optimiert', 'fortschrittlich', 'befreit', 'erst'],['Vernunft', 'Sicherheit', 'Gesundheit', 'Fortschritt', 'Wohlstand', 'Ordnung', 'Innovation', 'Chancengleichheit'])
    specs_theo = (['s,Erzbistum', 's,Bistum', 's,Kalifat', 'm,Gottesstaat', 's,Reich', 's,Grossreich'],['haschimitisch', 'makkabaeisch', 'souveraen', 'friedlich', 'zweit', 'heilig', 'erleuchtet', 'ewig', 'wiedergekehrt', 'gesegnet', 'auserkoren', 'bahaiisch'],['Dogma', 'Vorbestimmtheit', 'Froemmigkeit', 'Hingabe', 'Treue', 'Reinheit'])


scene bg table_empty

menu:
    "In welchem Regime werde ich leben?"
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
    if regime == "anarch":
        regime_name = "".join(random.sample(specs_anarch[0], 1))
        regime_traits = random.sample(specs_anarch[1], 2)
    elif regime == "cap":
        regime_name = "".join(random.sample(specs_cap[0], 1))
        regime_traits = random.sample(specs_cap[1], 2)
    elif regime == "comm":
        regime_name = "".join(random.sample(specs_comm[0], 1))
        regime_traits = random.sample(specs_comm[1], 2)
    elif regime == "techno":
        regime_name = "".join(random.sample(specs_techno[0], 1))
        regime_traits = random.sample(specs_techno[1], 2)
    elif regime == "theo":
        regime_name = "".join(random.sample(specs_theo[0], 1))
        regime_traits = random.sample(specs_theo[1], 2)

    regime_gender, regime_title = regime_name.split(",")


    if regime_gender == "w":
        regime_traits[0] = regime_traits[0] + "e"
        regime_traits[1] = regime_traits[1] + "e"

    if regime_gender == "s":
        regime_traits[0] = regime_traits[0] + "es"
        regime_traits[1] = regime_traits[1] + "es"

    if regime_gender == "m":
        regime_traits[0] = regime_traits[0] + "er"
        regime_traits[1] = regime_traits[1] + "er"

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
if (regime == 'anarch'):
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
    t1 "Was für ein komischer Name. Bist wohl nicht von hier, oder? Mich hat jedenfalls jemand anderes gerufen." 
if not traditional:
    t1 "Hmpf, dann musst du auf den nächsten warten. Mich hat jemand anderes gerufen." 

scene bg taxi_gone

"..."
" Na toll. Was für ein Neustart."

if 'gigolo' == True:
    "Dabei sah sie ganz süß aus."

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
            "Findest du mich exotisch? Manche finden sowas ja sehr interessant...;)":
                $ attracted2male += 1
                $ flirty += 2
                t2 "Oh, also, so genau habe ich jetzt gar nicht geguckt..."
    "Ach, ich war hier und da.":
        $ convict = True
        $ conf_anarch += 1
        "Ich werd dem ja wohl nicht sagen, dass ich 10 Jahre saß... Aber lügen will ich auch nicht. Ich halte einfach die Klappe und starre aus dem Fenster."
        $ buddy -= 1
    "Ich bin verdammt viel herumgekommen.":
        $ convict = True
        $ conf_anarch += 1
        "Ich werd dem ja wohl nicht sagen, dass ich 15 Jahre saß!"
        t2 "Für einen Weltenbummler hast du aber ganz schön wenig Kram dabei..."
        a "... (Ich hülle mich in Schweigen)..."
        "Ich sehe konzentriert aus dem Fenster."
        $ pious_trad -= 1
    "Ich habe einige Jahre gedient.":
        $ soldier = True
        t2 "Dann hast du bestimmt unser Vaterland am Mariannengraben verteidigt."
        "{i}Der Taxifahrer salutiert und blickt ernst in seinen Rückspiegel.{/i}"
        "Ach du Scheiße. Ich dachte ich hätte dem ganzen strammen Gehabe den Rücken gekehrt. Bloß nichts anmerken lassen."
        $ pious_trad += 2

$ print_all_success('Nach dem Taxipickup.')
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
    "Also genau genommen bin ich gar nicht von hier.":
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
        $ conf_anarch += 1
        "Ich werd der ja wohl nicht sagen, dass ich 10 Jahre saß... Aber lügen will ich auch nicht. Ich halte einfach die Klappe und starre aus dem Fenster."
        $ buddy -= 1
    "Ich bin verdammt viel herumgekommen.":
        $ convict = True
        $ conf_anarch += 1
        "Ich werd der ja wohl nicht sagen, dass ich 15 Jahre saß!"
        h2 "Für einen Weltenbummler hast du aber ganz schön wenig Kram dabei..."
        a "... (Ich hülle mich in Schweigen)..."
        "Ich sehe konzentriert aus dem Fenster."
        $ pious_trad -= 1
    "Ich habe einige Jahre gedient.":
        $ soldier = True
        h2 "Dann hast du bestimmt unser Vaterland am Mariannengraben verteidigt."
        "{i}Die Pilotin salutiert und blickt ernst in ihren Rückspiegel.{/i}"
        "Ach du Scheiße. Ich dachte ich hätte dem ganzen strammen Gehabe den Rücken gekehrt. Bloß nichts anmerken lassen."
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
sp "Sehr gut. Miriam hat mich gebeten, dich abzuholen."
menu:
    "Das ist aber freundlich.":
        $ buddy += 2
        $ inquisitive -= 1
        sp "Ist doch klar. Eine Hand wäscht die andere. Mit nem guten Start in unsere Gemeinschaft findest du bald deinen Platz. Da helf ich gern."
    "Von wem wurdest du beauftragt?":
        $ inquisitive += 3
        sp "Marjam Touftou ist ihr voller Name. Aber den benutzen wir selten. Weiß auch so jeder hier, wer gemeint ist."
    "Für diese Aufgabe werden wohl die charismatischten Leute ausgesucht;)?":
        $ attracted2male += 1
        $ flirty += 1
        $ inquisitive -= 1
        sp "Haha, du...!."
        "Er guckt etwas verunsichert."
    "Wo bringst du mich hin?":
        $ inquisitive += 1
        $ buddy -= 1
        sp "Zu Marjams Haus. Es liegt am östlichen Rand des Orts. Sie wird dir dann helfen, dich zu orientieren."
        sp "Ich kann das leider nicht übernehmen, weil ich gleich zurück in den Laden muss."
sp "..."
sp "Erzähl mal, was kannst du eigentlich? Wir brauchen dringend einen Meirer und einen Schuster."
"Oh, ist ja wie ein Bewerbungsgespräch hier."
menu:
    "Ach, ich kann von allem ein bisschen, weißt du...":
        sp "..."
        sp "Verstehe."
        "Er betrachtet mich nachdenklich. Vielleicht auch eine Spur abschätzig? Dann schaut er weg."
        $ buddy -= 4
        $ lethargic += 1
    "Ich habe weder von Käse noch von Schuhen Ahnung, aber ich habe im Knast weben und stricken gelernt. Vielleicht bringt das ja was.":
        $ convict = True
        $ conf_anarch += 1
        sp "In der Weberei können sie tatsächlich immer Leute gebrauchen."
    "Mit Produktion kenne ich mich nicht aus. Eher mit Kochen. Ich weiß aber nicht, ob ihr die Gewürze habt, mit denen ich sonst koche.":
        $ foreign = True
        sp "Kommst du nicht von hier?"
        "Nein, das Schicksal hat mich vor einigen Wochen von drüben hierher verschlagen."
        sp "Von so weit her kommst du? Interessant! Ich fürchte nur, dass unser Bezirk keine Handlungsbeziehungen mit drüben pflegt."
        sp "Sieht gewürzetechnisch also düster aus."
    "5 Jahre dritte Kompanie der Infanterie in den südlichen Kolonien haben mir kaum Zeit gelassen, etwas Lebensnahes zu lernen.":
        $ soldier = True
        sp "Ah, ein Berufsmörder. Was Lebensbejahenderes würde mir in dem Fall schon reichen..."
        $ conf_anarch -= 4
        sp "Nagut, wir haben schon härtere Fälle als dich sozialisiert."
        "Der scheint genauso ein Militärfan wie ich zu sein... Hat schon gute Gründe, warum ich den Verein verlassen hab."


"Hündchen" "Wuff."
if traditional:
    "Warum guckt der Hund so komisch auf meinen Hut? Hoffentlich will er ihn nicht fressen..."

sp "Da wären wir. Marjam Tuoftous Haus. Viel Glück dir."

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
    menu:
        "Das ist aber freundlich.":
            $ buddy += 2
            $ inquisitive -= 1
            dp1 "Ist doch klar. Mit nem guten Start in unsere Gemeinschaft findest du bald deinen sinnvollen Platz. Da helf ich gern."
            dp2 "... Genosse! Es heißt Genosse, Mama."
            dp1 "Ja, gut aufgepasst, sehr höflich von dir... Genösschen."
            "Man muss also jeden mit Genosse ansprechen? Irgendwie albern. Aber anscheinend scheint die Dame den Humor nicht darüber verloren zu haben."
        "Von wem wurdest du beauftragt?":
            $ inquisitive += 3
            dp1 "Marjam Touftou ist der Name der Geschäftsführerin des VEB FH."
            dp2 "Mama, wofür steht eigentlich fau-eh-beh-eff-ha?"
            dp1 "Für volkseigener Betrieb Fr... ach, das lernst du schon noch in der Jugendgruppe."
            "Hm, jetzt bin ich neugierig. Wofür steht das FH? Fahrradhandel?"
        "Für diese Aufgabe werden wohl die charismatischsten Leute ausgesucht;)?":
            $ attracted2female += 1
            $ flirty += 1
            $ inquisitive -= 1
            dp2 "Was ist Sakrisma?"
            dp1 "Haha, du...!."
            "Sie bekommt leicht rosige Wangen. Bevor ich ein weiteres Kompliment anbringen kann, nimmt sie den Faden wieder auf."
        "Wo ist denn diese Marjam?":
            $ inquisitive += 1
            $ buddy -= 1
            dp1 "In ihrem VEB FH am östlichen Rand des Orts. Mirjam wird dir ein Obdach geben und von dort aus helfen, dich zu orientieren."
    dp1 "..."
    dp1 "Erzähl mal, was kannst du eigentlich? Wir brauchen dringend Lehrer und Landwirte."
    "Oh, ist ja wie ein Bewerbungsgespräch hier."
    menu:
        "Ach, ich kann von allem ein bisschen, weißt du...":
            dp1 "Aha."
            "Sie betrachtet mich, die linke Augenbraue leicht angehoben. War wohl die falsche Antwort."
            $ buddy -= 4
            $ lethargic += 1
            dp2 "Da kann ja sogar ich mehr! Ich kann nämlich aaalle meine Fibellieder!"
        "Ich habe weder von Kindern noch von Kartoffeln Ahnung, aber ich habe im Knast weben und stricken gelernt. Vielleicht bringt das ja was.":
            a "Hier, eine Arbeitsprobe!"
            "Ich mache meinen Reißverschluss auf und präsentiere stolz meinen Pullover."
            dp2 "Darf ich...?"
            "Sie deutet auf meine Brust und kommt näher."
            menu:
                "Klar, ist ne top Qualität!":
                    pass
                "Komm ruhig näher ;)":
                    $ flirty += 2
                    $ attracted2female += 1
                    pass
            "Sie befühlt meinen handgestrickten Pulli."
            dp1 "Der ist echt schön."
            $ convict = True
            $ conf_anarch += 1
            dp1 "In der Weberei können sie tatsächlich immer Leute gebrauchen."
        "Damit kenne ich mich leider nicht so aus. Ich war vorher Wandererzähler, da reist man herum und wird für seine Geschichten bewirtet. Man macht eigentlich nie was... Handfestes.":
            $ foreign = True
            dp1 "Klingt, als kämst du nicht von hier."
            "Nein, das Schicksal hat mich vor einigen Wochen von drüben hierher verschlagen."
            dp1 "Spannend."
            dp2 "Papa sagt, in der Schule erzählen sie auch Märchen, da kannst d-"
            dp1 "Sowas würde Papa nie sagen, du hast ihn falsch verstanden!"
            "Ah, klassischer Fall von ''Kindermund tut selten gut''. Treffendes Sprichwort."
            if simplemind == False:
                "Neee, warte mal, das hieß irgendwie anders."
        "5 Jahre dritte Kompanie der Infanterie in den westlichen Kolonien haben mir kaum Zeit gelassen, etwas so Lebensnahes zu lernen.":
            $ soldier = True
            dp1 "Ah, ein Pionier der Revolution! Für Leute wie dich finden wir immer was zu tun."
            $ conf_anarch -= 4
            "Hoffentlich hat die Tätigkeit nix mit meiner bisherigen zu tun..."

jump house_marjam
##############################################HIER LABEL WOANDERSHIN SETZEN$#########################


