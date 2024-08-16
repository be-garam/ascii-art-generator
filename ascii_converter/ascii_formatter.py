from colorama import Fore, Back, Style, init

init(autoreset=True)

class ASCIIFormatter:
    @staticmethod
    def add_border(ascii_art, padding=1):
        lines = ascii_art.splitlines()
        width = max(len(line) for line in lines)
        box_width = width + padding * 2 + 2
        
        result = [f'+{"-" * (box_width - 2)}+']
        result.extend(f'|{" " * (box_width - 2)}|' for _ in range(padding))
        
        for line in lines:
            result.append(f'|{" " * padding}{line.ljust(width)}{" " * padding}|')
        
        result.extend(f'|{" " * (box_width - 2)}|' for _ in range(padding))
        result.append(f'+{"-" * (box_width - 2)}+')
        
        return '\n'.join(result)
    
    @staticmethod
    def colorize(text, fore_color=Fore.GREEN, back_color=Back.BLACK):
        return f"{fore_color}{back_color}{text}{Style.RESET_ALL}"
