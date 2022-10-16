from webbrowser import open

class SocialLinks():
    def __init__(self, link) -> None:
        self.link = link

    def openLink(self):
        if self.link == 'instagram':
            url = 'https://instagram.com/biellviana'
        elif self.link == 'twitter':
            url = 'https://twitter.com/_katiorro'
        elif self.link == 'github':
            url = 'https://github.com/pySiriusDev?tab=repositories'
        elif self.link == 'paypal':
            url = 'https://www.paypal.com/donate/?hosted_button_id=X74DV8VCZH84A'

        open(url)