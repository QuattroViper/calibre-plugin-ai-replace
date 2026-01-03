from calibre.gui2.actions import InterfaceAction
from PyQt5.QtWidgets import QAction, QMessageBox


class AIReplaceAction(InterfaceAction):
    """A minimal InterfaceAction that adds one menu item under 'Tools'."""

    name = 'AI Replace'

    def genesis(self):
        """Called by calibre to set up the action and menus."""
        # Create a QAction and attach it to the Tools menu.
        action = QAction('AI Replace', self.gui)
        action.triggered.connect(self.run)

        # Add to the Tools menu if available, otherwise add to menubar.
        try:
            self.gui.menu_tools.addAction(action)
        except Exception:
            # Fallback: add to the main menubar
            try:
                self.gui.menuBar().addAction(action)
            except Exception:
                # As a last resort, add it to the main window (still visible)
                self.gui.addAction(action)

        self.action = action

    def run(self):
        """Action callback: show a simple message box."""
        QMessageBox.information(self.gui, 'AI Replace', 'Hello from the AI Replace plugin!')
