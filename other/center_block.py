import shutil

class CenterBlock:
    """
    A class for centering a block of text in the current terminal.
    Each line is independently padded based on the maximum line length.
    """

    def __init__(self, text: str):
        """
        :param text: A multi-line string to center.
        """
        self.text = text
        self.centered_block = self._center_block()

    def _center_block(self) -> str:
        """
        Splits the text into lines, calculates the max line length,
        and pads each line to be centered within the terminal width.
        
        If the longest line is wider than the terminal, no padding is added.
        """
        terminal_width = shutil.get_terminal_size().columns
        lines = self.text.split("\n")

        if not lines:
            return ""

        max_length = max(len(line) for line in lines)
        if max_length >= terminal_width:
            return self.text  # No centering applied if text is too wide

        padding = (terminal_width - max_length) // 2
        centered_lines = [(" " * padding) + line for line in lines]
        return "\n".join(centered_lines)

    def __str__(self) -> str:
        """
        Returns the centered block of text as a string.
        """
        return self.centered_block
