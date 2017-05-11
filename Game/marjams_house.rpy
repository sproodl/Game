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
"Oh, ein Bordell. Das erklärt die Badewannen-Bett-Situation."
m "Aufgrund der derzeitigen politischen Lage sind wir... nicht ganz ausgebucht. Deshalb haben wir entschieden, Leute wie dich zu beherbergen."
m "Du kannst hier schlafen und essen, bis du eine permanente Bleibe gefunden hast. Im Gegenzug erwarte ich, für die Unterbringungskosten entschädigt zu werden, sobald du einen Job hast. Und dass du dich unsichtbar machst, wenn Kunden im Haus sind. Das wäre dann alles. Fragen?"

menu:
    "Was meinst du mit der ''derzeitigen politischen Lage''?":
        m "Ich kann weder dementieren, noch bestätigen, dass die Lage schwierig ist."
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
        if (regime == "anarch") and (conf_calc_anarch() >=1):
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

if regime == 'anarch':
    jump tv_anarch
elif regime == 'comm':
    jump tv_comm
elif regime == 'cap':
    jump tv_cap
elif regime == 'theo':
    jump tv_theo
else:
    jump tv_techno

#label tv_aristo:
#scene bg tv_studio_aristo
#"Nachrichtensprecherin" "Mein Name ist Manuela Dirks und Sie sehen (Fernsehsender) mit den 18:00Uhr Nachrichten."
#speaker "Die 14 Arbitri läuteten die Festwoche der Patrimonio mit einer Parade in der Hauptstadt ein."# Arbitra = entscheidende Macht
#speaker "2,5 Millionen Schaulustige sahen dem Festumzug zu. Wie jedes Jahr durfte jeder Stand einen Wagen stellen. Neu dabei sind in diesem Jahr die Wagen der "#Praktikanten, Subunternehmer, Aufstocker, dann Bild des Wagens
#speaker "Höhepunkt der Feierlichkeiten war die traditionelle Ansprache zum Lob des Patrimonio, die nach dem Rotationsprinzip Arbitrus de Gonen, Regent der Eidsgrafschaft Karas hielt."
#"de Gonen" "So möchte ich Euch daran erinnern, wie wir all diese Bedrohungen des 21. Jahrhunderts überwinden konnten: Indem wir jedem seinen angestammtem Platz zurückgaben, indem wir jedem zu seinem angeborenen Rechte verhalfen und jedem jene Pflichten abverlangten, die ihm in die Wiege gelegt worden sind. Wir haben die Herrschaft der natürlichen Ordnung wiederhergestellt, unser Erbe, unser Patrimonio."
#speaker "Die Rede schloss mit einer Wiedergabe unserer Hymne durch das eidgenössische Großorchester."

#scene bg tv_conflict_aristo

#scene bg tv_sport_aristo

#scene bg tv_weather

jump diary_first_entry

label tv_anarch:
scene bg tv_studio_anarch

scene bg tv_holiday_anarch

scene bg tv_conflict_anarch

scene bg tv_sport_anarch

scene bg tv_weather

jump diary_first_entry

label tv_cap:
scene bg tv_studio_cap

scene bg tv_holiday_cap

scene bg tv_conflict_cap

scene bg tv_sport_cap

scene bg tv_weather


jump diary_first_entry

label tv_comm:
scene bg tv_studio_comm

scene bg tv_holiday_comm

scene bg tv_conflict_comm

scene bg tv_sport_comm

scene bg tv_weather

jump diary_first_entry

label tv_techno:
#scene bg tv_studio_techno
"Nachrichtensprecherin" "Mein Name ist Manuela Dirks und Sie sehen (Fernsehsender) mit den 18:00Uhr Nachrichten."
speaker "In allen Ländern der Freihandelszone® zelebrierten die Menschen heute den Beginn des Fashionweekends."
"Fashionista" "Ich liebe diesen Feiertag, und ich liebe diese wundervollen Sachen! Sie strahlen soviel aus, soviel Mut, Seele, soviel Eigenheit!"
speaker "Höhepunkt war der von EdHardy - pure fashion, pure soul - gesponserte Rave. "

#scene bg tv_holiday_techno

#scene bg tv_conflict_techno

#scene bg tv_sport_techno

#scene bg tv_weather


jump diary_first_entry

label tv_theo:
scene bg tv_studio_theo

scene bg tv_holiday_theo

scene bg tv_conflict_theo

scene bg tv_sport_theo

scene bg tv_weather


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
