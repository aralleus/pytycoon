import os
import shutil

def clear_screen() -> None:
    """
    Clears the terminal screen in a cross-platform manner.

    On Windows, uses 'cls'; on other systems, uses 'clear'.
    """
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        # Fallback in case the system call fails.
        print("\n" * 100)

class CenterBlock:
    """
    A simple class for centering a block of text in the current terminal.

    Each line in 'text' is padded to match the width of the longest line,
    and then aligned to the center of the terminal's width (when possible).
    """

    def __init__(self, text: str):
        """
        :param text: A multi-line string to be centered.
        """
        self.text = text
        self.centered_block = self._center_block()

    def _center_block(self) -> str:
        """
        Splits 'text' into lines, calculates the maximum line length, and
        pads each line so that it appears centered within the terminal width.

        If the longest line is as wide or wider than the terminal, 
        no centering is done (the text is returned as-is).
        """
        terminal_width = shutil.get_terminal_size().columns
        lines = self.text.split("\n")
        if not lines:
            return ""

        max_length = max(len(line) for line in lines)
        # If text is longer than terminal, do not attempt centering
        if max_length >= terminal_width:
            return self.text

        # Calculate padding for each line
        padding = (terminal_width - max_length) // 2
        centered_lines = [(" " * padding) + line for line in lines]
        return "\n".join(centered_lines)

    def __str__(self) -> str:
        """
        Returns the centered block of text as a string.
        """
        return self.centered_block
      if __name__ == "__main__":
    # Clear the screen first
    clear_screen()

    # Create a block of text with multiple lines
    sample_text = (
        "Hello, world!\n"
        "This text should be centered.\n"
        "Have a great day!"
    )

    # Center it in the terminal
    block = CenterBlock(sample_text)
    print(block)

