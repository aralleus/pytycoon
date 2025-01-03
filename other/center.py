import shutil

class CenterText:
    """
    A simple class to center a given string in the current terminal window width.
    """

    def __init__(self, text: str):
        """
        :param text: The string to be centered.
        """
        self.text = text
        self.centered_text = self._center_text()

    def _center_text(self) -> str:
        """
        Centers the text using the current terminal width. If the text length is 
        greater than or equal to the terminal width, it returns the text as-is.
        """
        terminal_width = shutil.get_terminal_size().columns
        if len(self.text) >= terminal_width:
            return self.text
        padding = (terminal_width - len(self.text)) // 2
        return ' ' * padding + self.text

    def __str__(self) -> str:
        """
        Returns the centered string representation.
        """
        return self.centered_text
