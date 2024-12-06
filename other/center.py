import shutil

class center:
    def __init__(self, text):
        self.text = text
        self.centered_text = self._center_text()

    def _center_text(self):
        terminal_width = shutil.get_terminal_size().columns
        padding = (terminal_width - len(self.text)) // 2
        return ' ' * padding + self.text

    def __str__(self):
        return self.centered_text