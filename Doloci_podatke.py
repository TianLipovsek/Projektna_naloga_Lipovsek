import re

def poberi_iz_html(html):
    with open(html, encoding='utf-8') as dat:
        besedilo = dat.read()
        igralec = [[] for _ in range(9)]
        for najdba in re.finditer(
            r'<span class="CellPlayerName--long"><span class=""><a\s+href="/nba/players/\d+/[^>]*?">(?P<ime>.+?)\s',
            besedilo
        ):
            igralec[0].append(najdba['ime'])

        for najdba in re.finditer(
            r'<span class="CellPlayerName--long"><span class=""><a\s+href="/nba/players/\d+/[^>]*?">.+?\s(?P<priimek>.+?)</a>',
            besedilo
        ):
            priimek = najdba['priimek']
            igralec[1].append(priimek)


        for najdba in re.finditer(
            r'</a><span class="CellPlayerName-position">\s*(?P<pozicija>.+?)\s*</span><span class="CellPlayerName-team">\s*[A-Z]+\s*</span></span></span></td><td class="TableBase-bodyTd',
            besedilo
        ):
            pozicija = najdba['pozicija'].strip()
            igralec[2].append(pozicija)

        for najdba in re.finditer(
            r'</span></span></span></td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(?P<tekme>.+?)\s*</td>',
            besedilo
            ):


            igralec[3].append(najdba['tekme'])

        for najdba in re.finditer(
            r'</span></span></span></td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(?P<minute>.+?)\s*</td>',
            besedilo
            ):
            igralec[4].append(najdba['minute'])


        for najdba in re.finditer(
            r'</span></span></span></td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(?P<tocke>.+?)\s*</td>',
            besedilo
            ):
            igralec[5].append(najdba['tocke'])

        for najdba in re.finditer(
            r'</span></span></span></td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(?P<met>.+?)\s*</td>',
            besedilo
            ):
            igralec[6].append(najdba['met'])

        for najdba in re.finditer(
            r'</span></span></span></td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td>\s*<td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(?P<trojke>.+?)\s*</td>',
            besedilo
            ):
            igralec[7].append(najdba['trojke'])

        for najdba in re.finditer(
            r'</span></span></span></td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\.\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(\d+\.\d+)?(—)?\s*</td>\s*<td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(\d+\.\d+)?(—)?\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*\d+\s*</td><td class="TableBase-bodyTd\s*TableBase-bodyTd--number\s*">\s*(?P<prosti_met>.+?)\s*</td>',
            besedilo
            ):
            igralec[8].append(najdba['prosti_met'])


    igralci_seznami = []
    for j in range(len(igralec[0])):
        trenutni_igralec = []
        for k in range(9):      
            trenutni_igralec.append(igralec[k][j])
        dodaj = True
        for ze_dodan in igralci_seznami:
            if ze_dodan[0] == trenutni_igralec[0] and ze_dodan[1] == trenutni_igralec[1]:
                dodaj = False
        if dodaj:
            igralci_seznami.append(trenutni_igralec)
    return igralci_seznami



