import shutil

class center_block:
    def __init__(self, text):
        self.text = text
        self.centered_block = self._center_block()

    def _center_block(self):
        terminal_width = shutil.get_terminal_size().columns
        lines = self.text.split("\n")
        max_length = max(len(line) for line in lines)
        padding = (terminal_width - max_length) // 2

        centered_lines = [(" " * padding) + line for line in lines]
        return "\n".join(centered_lines)

    def __str__(self):
        return self.centered_block