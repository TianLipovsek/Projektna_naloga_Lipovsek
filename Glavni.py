import Poberi_podatke
import Doloci_podatke
import csv

vsi_igralci = []
for l in range(11):
    igralci_l_tega_htmlja = Doloci_podatke.poberi_iz_html(f'stran{l+1}.html')
    for igralec_l_tega in igralci_l_tega_htmlja:
        dodaj = True
        for ze_dodan in vsi_igralci:
            if ze_dodan[0] == igralec_l_tega[0] and ze_dodan[1] == igralec_l_tega[1]:
                dodaj = False
        if dodaj:
            vsi_igralci.append(igralec_l_tega)



with open('podatki_igralci.csv', "w") as dat:
    pisatelj = csv.writer(dat)
    pisatelj.writerow(
        [
            "Ime",
            "Priimek",
            "Pozicija",
            "Stevilo_tekem",
            "Minute_na_tekmo",
            "Tocke",
            "Met",
            "Trojke",
            "Prosti_meti",
        ]
    )
    for igralec in vsi_igralci:
        pisatelj.writerow(
            [
                igralec[0],
                igralec[1],
                igralec[2],
                igralec[3],
                igralec[4],
                igralec[5],
                igralec[6],
                igralec[7],
                igralec[8],
            ]
        )