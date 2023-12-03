class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_toiminto = None

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def paivita_toiminto(self, toiminto):
        self._edellinen_toiminto = toiminto

    def edellinen_toiminto(self):
        return self._edellinen_toiminto

class Summa:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._arvo = self._sovellus.arvo()

    def suorita(self):
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass

        self._sovellus.plus(arvo)

    def kumoa(self):
        self._sovellus.aseta_arvo(self._arvo)

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._arvo = self._sovellus.arvo()

    def suorita(self):
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass

        self._sovellus.miinus(arvo)

    def kumoa(self):
        self._sovellus.aseta_arvo(self._arvo)

class Nollaus:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._arvo = self._sovellus.arvo()

    def suorita(self):
        self._sovellus.nollaa()

    def kumoa(self):
        self._sovellus.aseta_arvo(self._arvo)

class Kumoa:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        toiminto = self._sovellus.edellinen_toiminto()
        if toiminto:
            toiminto.kumoa()

    def kumoa(self):
        pass
