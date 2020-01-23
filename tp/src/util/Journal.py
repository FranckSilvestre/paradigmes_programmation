class Journal:

    def __init__(self):
        self.messages = []

    def ecrit(self, message: str):
        self.messages.append(message)


# Initialise un journal par défaut attaché à la classe directement.
# La classe journal peut maintenant mettre à disposition cete instance de journal
# à tout les objets qui en font la demande
# On dit que "journalParDefaut" est un attribut static de la classe "Journal"
Journal.journalParDefaut = Journal()


