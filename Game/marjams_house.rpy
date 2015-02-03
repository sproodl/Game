# -*- mode: python -*-
# -*- coding: utf-8 -*-

label house_marjam:

scene bg mh_marjamshouse

"Allmacht" "Dein Punktestand beträgt [conf_comm] (Kommunismus)"
"Allmacht" "... [conf_cap] (Kapitalismus)"
"Allmacht" "... [conf_anarch] (Anarchie)"
"Allmacht" "... [conf_aristo] (Aristokratie)"
"Allmacht" "... [conf_techno] (Technokratie)"
"Allmacht" "... [conf_theo] (Theokratie)"

"Wow. Schönes Haus. Wirkt sehr einladend und gemütlich durch diese Beleuchtung. Bin mal gespannt, was diese Marjam für eine ist."

"Einfach mal Klingeln gehen." #KLINGELGERÄUSCH EINFÜGEN

"Stimme" "[player_alias]?"

a "Ja, das bin ich! Hallo, bist du Marjam?"
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
        pass
        $ inquisitive += 3
    "Wo ist mein Zimmer?":
        pass
        $ blunt += 2
    "Wie hoch ist die Miete? In welchen Raten und bei welchem Zins soll ich sie abstottern?":
        pass
        $ inquisitive += 1
    "Wie großzügig! Darf ich dir zum Dank einen traditionellen Tanz vorführen?" if 'tribal' in items:
        pass
        $ buddy += 3
        $ pious_trad += 5

m "Ich bringe dich jetzt zu deinem Zimmer"
    
"Allmacht" "Dein Punktestand beträgt [conf_comm] (Kommunismus)"
"Allmacht" "... [conf_cap] (Kapitalismus)"
"Allmacht" "... [conf_anarch] (Anarchie)"
"Allmacht" "... [conf_aristo] (Aristokratie)"
"Allmacht" "... [conf_techno] (Technokratie)"
"Allmacht" "... [conf_theo] (Theokratie)"

"ENDE"

return
