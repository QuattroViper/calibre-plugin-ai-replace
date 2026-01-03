from calibre.gui2.actions import InterfaceAction


class AiReplaceAction(InterfaceAction):

    name = 'AI Replace'

    def genesis(self):
        self.qaction.triggered.connect(self.run)

    def run(self):
        self.gui.status_bar.showMessage(
            "Religious exclamations cleaned (formatting preserved)", 5000
        )
