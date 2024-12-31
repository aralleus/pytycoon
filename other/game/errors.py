import ctypes
def throw_error(title, message): ctypes.windll.user32.MessageBoxW(0, message, title, 0x10)  # 0x10 - error ico, 0x30 - warning ico, 0x40 - info