from util.Journal import Journal


class VueJournal:

    def __init__(self, journal: Journal):
        self.journal = journal

    def affiche(self):
        for message in self.journal.messages:
            print(message)
