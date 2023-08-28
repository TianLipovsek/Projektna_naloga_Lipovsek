import Poberi_podatke
import Doloci_podatke
import csv

vsi_igralci = []
for l in range(11):
    igralci_l_tega_htmlja = Doloci_podatke.poberi_iz_html(f'stran{l+1}.html')
    vsi_igralci += igralci_l_tega_htmlja

with open('podatki_igralci.csv', "w") as dat:
    pisatelj = csv.writer(dat)
    pisatelj.writerow(
        [
            "ime",
            "priimek",
            "pozicija",
            "tekme",
            "minute",
            "tocke",
            "met",
            "trojke",
            "prosti_met",
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