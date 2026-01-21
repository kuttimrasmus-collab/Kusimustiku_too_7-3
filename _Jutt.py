# ÜLDINE ÜLEVAADE PROGRAMMIST
# See programm on käsureal töötav küsimustiku automaatprogramm.
# Selle eesmärk on viia läbi lihtne test või küsitlus mitme inimese vahel.
# Programm küsib vastajatelt küsimusi, kontrollib nende vastuseid,
# hindab tulemusi ning salvestab andmed erinevatesse failidesse.
# Lisaks annab programm vastajale tagasisidet simuleeritud e-kirja kujul.
#
# Programm töötab CLI ehk käsurea rakendusena,
# mis tähendab, et kogu suhtlus kasutajaga toimub terminalis tekstipõhiselt.

# PROGRAMMI KIRJELDAV KOMMENTAAR
# Programmi alguses on dokumentatsioonikommentaar,
# mis ütleb, et tegemist on küsimustiku automaatprogrammiga.
# See kommentaar ei mõjuta programmi tööd,
# vaid on mõeldud inimesele lugemiseks ja koodi paremaks mõistmiseks.

# MOODULITE IMPORTIMINE
# Programmis imporditakse kolm moodulit.
# Moodul os on vajalik failidega töötamiseks,
# näiteks selleks, et kontrollida, kas mingi fail on juba olemas.
# Moodulit random kasutatakse küsimuste juhuslikuks valimiseks,
# et test ei oleks iga kord samas järjekorras.
# Moodul unicodedata on vajalik täpitähtede eemaldamiseks,
# sest e-posti aadressides ei tohi olla täpitähti.

# KONSTANDID JA SEADISTUSED
# Programmis on määratud konstandid M ja N.
# Muutuja M näitab, mitu inimest võib ühe programmi käivitamise jooksul vastata.
# Muutuja N määrab, mitu küsimust saab üks vastaja.
# Need väärtused on eraldi välja toodud,
# et neid oleks lihtne muuta ilma ülejäänud koodi muutmata.

# FAILIDE NIMED
# Programmis on määratud failide nimed, kuhu andmed salvestatakse.
# Ühes failis hoitakse küsimusi ja vastuseid.
# Teistes failides hoitakse vastajate tulemusi.
# Andmed jäävad alles ka pärast programmi sulgemist.

# E-KIRJA SEADISTUS
# Programmis on muutuja, mis määrab,
# kas e-kirju saadetakse päriselt või ainult simuleeritakse.
# Praegu on e-kirjade saatmine välja lülitatud.
# E-kiri kuvatakse ainult ekraanil.

# FUNKTSIOON normalize_email
# See funktsioon loob vastaja nimest e-posti aadressi.
# Nimi muudetakse väikesteks tähtedeks ja jagatakse osadeks.
# Täpitähed eemaldatakse.
# E-posti aadress pannakse kokku kujul eesnimi.perenimi@example.com.
# Kui nime ei sisestata, kasutatakse vaikimisi e-posti aadressi.

# FUNKTSIOON load_questions
# Selle funktsiooni ülesanne on lugeda küsimused failist.
# Kontrollitakse, kas küsimuste fail eksisteerib.
# Kui faili ei ole, tagastatakse tühi sõnastik.
# Kui fail on olemas, loetakse see rida-realt.
# Küsimused ja vastused salvestatakse sõnastikku.

# FUNKTSIOON add_question
# See funktsioon võimaldab kasutajal lisada uusi küsimusi.
# Kasutajalt küsitakse küsimus ja õige vastus.
# Need salvestatakse faili kujul küsimus:vastus.
# Kui mõni väli on tühi, siis küsimust ei lisata.

# FUNKTSIOON already_tested
# Selle funktsiooni eesmärk on kontrollida,
# kas inimene on juba varem vastanud.
# Programm loeb faili koik.txt.
# Sealt võetakse vastajate nimed.
# Nimed salvestatakse hulka (set).
# See väldib korduvat vastamist.

# FUNKTSIOON send_email
# See funktsioon simuleerib e-kirja saatmist.
# Kuna päris e-kirja saatmine on välja lülitatud,
# prindib programm e-kirja sisu ekraanile.
# Näidatakse saajat, teemat ja kirja sisu.

# FUNKTSIOON run_quiz
# See on programmi kõige olulisem funktsioon.
# Siin toimub kogu küsimustik.
# Laetakse küsimused failist.
# Kontrollitakse varem vastanuid.
# Küsitakse vastaja nimi.
# Valitakse juhuslikud küsimused.
# Võrreldakse vastuseid õigete vastustega.
# Loendatakse õiged vastused.
# Määratakse staatus SOBIS või EI SOBINUD.
# Salvestatakse tulemused failidesse.
# Simuleeritakse e-kiri vastajale.
# Kui nime ei sisestata, katkestatakse sessioon.

# FUNKTSIOON write_results
# See funktsioon salvestab sessiooni tulemused.
# Vastajad jagatakse sobivateks ja mittesobivateks.
# Sobivad vastajad sorteeritakse punktide järgi.
# Mittesobivad vastajad sorteeritakse nime järgi.
# Andmed kirjutatakse vastavatesse failidesse.

# FUNKTSIOON menu
# See funktsioon loob programmi menüü.
# Menüü töötab lõpmatus tsüklis.
# Kasutaja saab alustada küsimustikku.
# Kasutaja saab lisada uusi küsimusi.
# Kasutaja saab programmist väljuda.

# PROGRAMMI KÄIVITAMINE
# Programm käivitub ainult siis,
# kui see fail käivitatakse otse.
# Sel juhul avatakse menüü.

# LÕPPKOKKUVÕTE
# See programm on hea näide:
# funktsioonide kasutamisest,
# failidega töötamisest,
# tsüklitest ja tingimustest,
# kasutaja sisendi kontrollimisest,
# andmete salvestamisest.
