from tekoaly_parannettu import TekoalyParannettu
from kivipaperisakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)

        print(f"Tietokone valitsi: {siirto}")

        return siirto
