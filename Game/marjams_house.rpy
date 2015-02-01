# -*- mode: python -*-
# -*- coding: utf-8 -*-

label house_marjam:

scene bg mh_marjamshouse

"Wow. Schönes Haus. Wirkt sehr einladend und gemütlich durch diese Beleuchtung. Bin mal gespannt, was diese Marjam für eine ist."

"Einfach mal Klingeln gehen." #KLINGELGERÄUSCH EINFÜGEN

'Stimme' "[player_alias]?"

a "Ja, das bin ich! Hallo, sind Sie Marjam?"
m "Die bin ich."

if regime == "comm":
    m "Sie sollten sich angewöhnen, mich mit 'Genossin' anzusprechen."
    a "Verzeihung, Genossin!"
    m "Sie brauchen nicht gleich zu salutieren, verstimmtnochmal."

m "Kommen Sie rein. Immer den Gang entlang, ich empfange Sie im Restaurant."

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


"ENDE"

return
