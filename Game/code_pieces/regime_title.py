# regime name nur mit Daten innerhalb des Skripts erzeugen
import random

regime = "techno"

specs_anarch = (['w,Gemeinde', 'w,Kommune', 's,Territorium', 'w,Eidgenossenschaft', 'w,Provinz', 'w,Gemeinschaft', 'w,Konfoederation', 'w,Uebergangsregierung', 'm,Landstrich', 'm,Fleck Erde', 's,Autonomiegebiet', 'w,Ansammlung', 'w,Gruppierung', 'w,Zusammenrottung', 's,Syndikat'], ['autonom', 'provisorisch' 'ehemalig', 'kooperativ', 'bunt', 'foederalistisch', 'anarchisch', 'chaotisch', 'unabhaengig'], ['Freiheit', 'Vielfaeltigkeit', 'Selbstbestimmtheit', 'Unordung', 'Unabhaengigkeit', 'Partizipation'])

specs_cap = (['s,Treuhandgebiet', 's,Pachtgebiet', 's,Imperium', 's,Protektorat', 'w,Volksrepublik', 'w,Bundesrepublik', 'm,Freistaat', 's,Territorium', 's,Reichskommissariat'],['liberal', 'pluralistisch', 'saekular', 'demokratisch', 'vereinigt'],['Konsum', 'Ueberfluss', 'Freiheit', 'Einzigartigkeit', 'Recht', 'Wohlstand', 'Chancengleichheit'])

specs_comm = (['w,Foederation', 'w,Volksrepublik', 'w,Union', 'm,Staatenbund', 's,Konglomerat', 'w,Arbeiterrepublik', 'w,Uebergangsrepublik'],['proletarisch', 'kooperativ', 'marxistisch', 'leninistisch', 'kommunistisch', 'kollektivistisch', 'demokratisch', 'stalinistisch', 'viert', 'provisorisch'],['Transformation', 'Klassenkampf', 'Revolution', 'Bruederlichkeit', 'Freundschaft', 'Gleichheit', 'Einigkeit', 'Gemeinschaft'])

specs_techno = (['w,Raetegemeinschaft', 'w,Allianz', 's,Konglomerat', 'm,Vorstand', 'w,Foederation', 's,Territorium', 'w,Provinz', 'w,Gemeinschaft'],['rational', 'aufgeklaert', 'effizient', 'optimiert', 'fortschrittlich', 'befreit', 'erst'],['Vernunft', 'Sicherheit', 'Gesundheit', 'Fortschritt', 'Wohlstand', 'Ordnung', 'Innovation', 'Chancengleichheit'])

specs_theo = (['s,Erzbistum', 's,Bistum', 's,Kalifat', 'm,Gottesstaat', 's,Reich', 's,Grossreich'],['haschimitisch', 'makkabaeisch', 'souveraen', 'friedlich', 'zweit', 'heilig', 'erleuchtet', 'ewig', 'wiedergekehrt', 'gesegnet', 'auserkoren', 'bahaiisch'],['Dogma', 'Vorbestimmtheit', 'Froemmigkeit', 'Hingabe', 'Treue', 'Reinheit'])

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

print regime_name
