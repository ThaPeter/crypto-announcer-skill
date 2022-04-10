from mycroft import MycroftSkill, intent_file_handler


class CryptoAnnouncer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('announcer.crypto.intent')
    def handle_announcer_crypto(self, message):
        currency = message.data.get('currency')

        self.speak_dialog('announcer.crypto', data={
            'currency': currency
        })


def create_skill():
    return CryptoAnnouncer()

