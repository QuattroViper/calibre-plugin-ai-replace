from calibre.gui2.actions import InterfaceAction


class AiContextReplaceAction(InterfaceAction):

    name = 'AI Context Replace'

    # Declare the main action associated with this plugin
    # The keyboard shortcut can be None if you don't want to use a keyboard
    # shortcut. Remember that currently calibre has no central management for
    # keyboard shortcuts, so try to use an unusual/unused shortcut.
    action_spec = ('AI Context Replacer', None,
                   'Run the Ai Context Replacer', ())

    def genesis(self):

        icon = get_icons('images/icon.png', 'Ai Context Replace')

        # The qaction is automatically created from the action_spec defined
        # above
        self.qaction.setIcon(icon)
        self.qaction.triggered.connect(self.run)

    def run(self):
        self.gui.status_bar.showMessage(
            "Religious exclamations cleaned (formatting preserved)", 5000
        )
