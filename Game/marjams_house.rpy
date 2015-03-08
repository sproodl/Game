# -*- mode: python -*-
# -*- coding: utf-8 -*-

label house_marjam:

scene bg mh_marjamshouse

$ print_all_success('Nach dem Pickup.')

"Wow. Schönes Haus. Wirkt sehr einladend und gemütlich durch diese Beleuchtung. Bin mal gespannt, was diese Marjam für eine ist."

"Einfach mal Klingeln gehen." #KLINGELGERÄUSCH EINFÜGEN

"Stimme" "[player_alias]?"

a "Ja! Hallo, bist du Marjam?"
m "Die bin ich."

if regime == "comm":
    m "Du solltest es dir angewöhnen, mich mit ''Genossin'' anzusprechen."
    a "Verzeihung, Genossin!"

m "Komm rein. Immer den Gang entlang, ich empfange dich im Restaurant."

# GERÄUSCH VON SCHRITTEN

scene bg mh_room1

"..."

scene bg mh_room2 

"Hoppla. Bett und Badewanne im gleichen Raum? Was ist das für eine merkwürdige Pension?"

scene bg mh_room3

"Das muss wohl das Restaurant sein. Keiner hier, und das zur Mittagszeit. Vielleicht läuft der Laden nicht gut?"
"Vielleicht nehmen sie deshalb Leute wie mich auf?"

show Marjam

a "..."

m "Willkommen in Marjams Pension, einem der traditionsreichsten Bordelle des Landes."
m "Aufgrund der derzeitigen politischen Lage sind wir... nicht ganz ausgebucht. Deshalb haben wir entschieden, Leute wie dich zu beherbergen."
m "Du kannst hier schlafen und essen, bis du eine permanente Bleibe gefunden hast. Im Gegenzug erwarte ich, für die Unterbringungskosten entschädigt zu werden, sobald du einen Job hast. Und dass du dich unsichtbar machst, wenn Kunden im Haus sind. Das wäre dann alles. Fragen?"

menu:
    "Was meinst du mit der ''derzeitigen politischen Lage''?":
        m "..."
        "Aha, scheint ein schwieriges Thema zu sein."
        $ inquisitive += 3
    "Wo ist mein Zimmer?":
        m "Du scheinst mir von der besonders gesprächigen Sorte zu sein, hm?"
        $ blunt += 2
        $ lethargic += 1
    "Wie hoch ist die Miete? In welchen Raten und bei welchem Zins soll ich sie abstottern?":
        m "Steht im Vertrag. Der liegt in deinem Zimmer."
        $ inquisitive += 1
        $ conf_cap += 2
    "Wie großzügig! Darf ich dir zum Dank einen traditionellen Tanz vorführen?" if 'tribal' in items:
        "Mirjam guckt irritiert."
        m "Später vielleicht."
        $ buddy += 3
        $ pious_trad += 5

m "Ich bringe dich jetzt zu deinem Zimmer."

scene bg mh_room1

"..."
"ganz schön verwinkelt hier."

scene bg mh_base

m "Da sind wir. Um 18:30 Uhr kannst du dir dein Abendessen holen. Bitte benutze die Botengänge, nicht die für den Publikumsverkehr."
menu:
    "Das versteht sich von selbst. Diesem unmoralischen Freiervolk will ich nicht begegnen.":
        $ pious_trad += 3
        jump gone
    "Wird gemacht." if soldier == True:
        m "Bitte, nicht ständig salutieren."
        a "Verzeihung. Alte Gewohnheiten lassen sich schwer ausrotten."
        jump gone
    "Auch nicht, wenn ich mich unauffällig verhalte? Würde mich schwer interessieren, wie dieses Freiervolk aussieht und was es so erzählt...":
        $ inquisitive += 3
        if (regime == "aristo") and (conf_calc_aristo() <=0):
            m "Nagut. Aber bitte wirklich unauffällig."
        elif (regime == "anarch") and (conf_calc_anarch() >=1):
            m "Nagut. Aber nerv niemanden."
        elif (regime == "cap") and (conf_calc_cap() <=0):    
            m "Nagut. Aber bitte wirklich unauffällig."
        elif (regime == "comm") or (regime == "techno"):
            m "Nagut. Aber bitte wirklich unauffällig."
        elif (regime == "theo") and (conf_calc_theo() <=0):
            m "Nagut. Aber bitte wirklich unauffällig."
        else:
            m "Definitiv nicht."
        jump gone
    "Auch nicht, wenn ich zahlender Kunde bin?":
        $ capitalist = True
        $ conf_cap += 4
        $ flirty += 1
        m "Pah, wovon willst du Habenichts meine Angestellten bezahlen?"
        if 'rolex' in items:
            a "Ich kann die hier anbieten..."
            "Marjam betrachtet die Uhr aufmerksam, bewegt sie im durch das kleine Fenster hereinfallenden Licht hin und her."
            m "Für dieses Imitat kannst du mit dem Rezeptionisten 10 Minuten ''Vier gewinnt'' spielen, mehr nicht."
            "Mist. Die Frau hat Geschäftssinn."
            jump gone
        if 'rolex' not in items:
            a "Noch habe ich nichts. Aber ich werde mir einen Job suchen."
            m "Wenn es soweit ist, können wir gerne wieder darüber sprechen. Bis dahin bleiben dir nur die Botengänge."
            jump gone
    "Auch nicht als Angestellter?" if gender == "male":
        jump whore
    "Auch nicht als Angestellte?" if gender == "female":
        jump whore
    "Auch nicht als AngestelltX?" if gender == "undefined":
        jump whore

label whore:
"Ich habe sicher Potential ;)"
$ flirty += 4
$ attracted2female += 1
"Marjam nimmt mich in Augenschein, als sähe sie mich zum erstem Mal."
if traditional == False:
    m "Bei der derzeitigen Flaute wäre es leider verantwortungslos, dich einzustellen. Ich könnte dich nicht bezahlen."
if traditional == True:
    m "Definitiv nicht."
    if gender == 'undefined':
        m "Obwohl mir so ein Exot wie du gut ins Kozept passen würde..."
        "Marjam seufzt."

label gone:
"Die Dame des Hauses macht auf dem Absatz Kehrt."
"Ein leichter Hauch ihres Parfüms, Rosen und Zimt, bleibt zurückt."
$ renpy.pause(1.0)

"Ich bin ganz schön müde. Sollte mich hinlegen und Mittagsschlaf machen."  ######### HIER GÄHNSOUND EINFÜGEN#####

$ print_all_success('Nach dem ersten Gespräch mit Marjam.')

scene black
$ renpy.pause(3.0)

centered "gähhn."
centered "Oh, wie lange habe ich geschlafen?"

scene white
"Ah, perfekt, kurz vor sechs. Ich könnte ein bisschen fernsehen, bevor ich zum Abendessen gehe. In ein paar Minuten laufen Nachrichten."

scene bg tv ## Vielleicht erst ein Werbeclip, dann Nachrichten inklusive der Ankündigung von Feiern eines Staatstages

if regime == 'aristo':
    jump tv_aristo
elif regime == 'anarch':
    jump tv_anarch
elif regime == 'comm':
    jump tv_comm
elif regime == 'cap':
    jump tv_cap
elif regime == 'theo':
    jump tv_theo
else:
    jump tv_techno

label tv_aristo:

jump diary_first_entry

label tv_anarch:

jump diary_first_entry

label tv_cap:

jump diary_first_entry

label tv_comm:

jump diary_first_entry

label tv_techno:

jump diary_first_entry

label tv_theo:

jump diary_first_entry

"..." 
$ renpy.pause(1.0)

label diary_first_entry:
    "Krass."

if asocial == True:
    "Ich denke, es ist eine gute Idee, diese neuen Eindrücke in das Tagebuch zu schreiben, das ich Freddy abgezogen habe."
else:
    "Ich denke, es ist eine gute Idee, das Abschiedsgeschenk, das ich von meinen Freunden bekommen habe, jetzt zu benutzen."

$ items.add('diary')  ## Titel mit Tag, Datum, Uhrzeit, geschrieben in ein neues Dokument. Später Funktion, die neuen Text an hier geschaffenes
python:                ## Dokument anhängt und dieses öffnet, sodass man es auch lesen kann.
    ndir = os.getcwd() + '/' + player_alias
    os.mkdir(ndir, 0777)
    with codecs.open(os.path.join(os.getcwd(), player_alias, player_alias) + '_diary', 'a+', encoding='utf-8') as diary:
        diary.write(u"Tagebuch von %s" %player_alias)
        diary.write(time.strftime("%A, %x %X -- ") + renpy.input(u"Liebes Tagebuch, "))
    print(u"Das steht im Tagebuch: %s " %diary)

$ print_all_success('Nach dem ersten Tagebucheintrag.')

"Jut."

        
    


"ENDE"

return
