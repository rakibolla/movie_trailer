import webbrowser
class movie:
    def __init__(self,ra,raa,raas,hima):
        self.ra=ra
        self.raa=raa
        self.raas_url=raas
        self.hima_url=hima
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
