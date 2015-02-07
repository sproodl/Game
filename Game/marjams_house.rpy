# -*- mode: python -*-
# -*- coding: utf-8 -*-

label house_marjam:

scene bg mh_marjamshouse

python:
    conf_temp_comm = conf_calc_comm()
    conf_temp_cap = conf_calc_cap()
    conf_temp_anarch = conf_calc_anarch()
    conf_temp_aristo = conf_calc_aristo()
    conf_temp_theo = conf_calc_theo()
    conf_temp_techno = conf_calc_techno()

"Allmacht" "Dein Punktestand beträgt [conf_temp_comm] (Kommunismus)"
"Allmacht" "... [conf_temp_cap] (Kapitalismus)"
"Allmacht" "... [conf_temp_anarch] (Anarchie)"
"Allmacht" "... [conf_temp_aristo] (Aristokratie)"
"Allmacht" "... [conf_temp_techno] (Technokratie)"
"Allmacht" "... [conf_temp_theo] (Theokratie)"
"Allmacht" "... [lethargic] (Lethargiepunkte)"

"Wow. Schönes Haus. Wirkt sehr einladend und gemütlich durch diese Beleuchtung. Bin mal gespannt, was diese Marjam für eine ist."

"Einfach mal Klingeln gehen." #KLINGELGERÄUSCH EINFÜGEN

"Stimme" "[player_alias]?"

a "Ja! Hallo, bist du Marjam?"
m "Die bin ich."

if regime == "comm":
    m "Du solltest es dir angewöhnen, mich mit ''Genossin'' anzusprechen."
    a "Verzeihung, Genossin!"
    m "Du brauchst nicht gleich zu salutieren, verstimmtnochmal."

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

m "Ich bringe dich jetzt zu deinem Zimmer"

python:
    conf_temp_comm = conf_calc_comm()
    conf_temp_cap = conf_calc_cap()
    conf_temp_anarch = conf_calc_anarch()
    conf_temp_aristo = conf_calc_aristo()
    conf_temp_theo = conf_calc_theo()
    conf_temp_techno = conf_calc_techno()

"Allmacht" "Dein Punktestand beträgt [conf_temp_comm] (Kommunismus)"
"Allmacht" "... [conf_temp_cap] (Kapitalismus)"
"Allmacht" "... [conf_temp_anarch] (Anarchie)"
"Allmacht" "... [conf_temp_aristo] (Aristokratie)"
"Allmacht" "... [conf_temp_techno] (Technokratie)"
"Allmacht" "... [conf_temp_theo] (Theokratie)"
"Allmacht" "... [lethargic] (Lethargiepunkte)"

scene bg mh_room1

"..."
"ganz schön verwinkelt hier."

scene bg mh_base

m "Da sind wir. Um 18:30 Uhr kannst du dir dein Abendessen holen. Bitt benutze die Botengänge, nicht die für den Publikumsverkehr."
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
        if conf_temp_aristo <=0:
            m "Nagut. Aber bitte wirklich unauffällig."
        if conf_temp_anarch >=1:
            m "Nagut. Aber nerv niemanden."
        if conf_temp_cap <=0:    
            m "Nagut. Aber bitte wirklich unauffällig."
        if regime == 'comm' OR regime == 'techno':
            m "Nagut. Aber bitte wirklich unauffällig."
        if conf_temp_theo <=0:
            m "Nagut. Aber bitte wirklich unauffällig."
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
            "Mist, enttarnt."
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
if traditional = False:
    m "Bei der derzeitigen Flaute wäre es leider verantwortungslos, dich einzustellen. Ich könnte dich nicht bezahlen."
if traditional = True:
    m "Definitiv nicht."
    if gender = 'undefined':
        m "Obwohl mir so ein Exot wie du gut ins Kozept passen würde..."
        "Marjam seufzt."

label gone:
"Die Dame des Hauses macht auf dem Absatz Kehrt."
"Ein leichter Hauch ihres Parfüms, Rosen und Zimt, bleibt zurückt."
$ renpy.pause(1.0)

"Ich bin ganz schön müde. Sollte mich hinlegen und Mittagsschlaf machen."  ######### HIER GÄHNSOUND EINFÜGEN#####

scene black
$ renpy.pause(3.0)

        
    


"ENDE"

return
