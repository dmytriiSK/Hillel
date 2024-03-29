class colorizer:
    def __init__(self, color=None, color_code=None):
        self.color_code = color_code
        self.color = color.lower() if color else None
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            # 'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
        }

    def __enter__(self):
        if self.color in self.colors.keys():
            print(self.colors[self.color], end='')
        else:
            print(self.color_code, end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print('\033[0m', end='')


with colorizer(color_code='\033[94m'):
    print('printed in blue')

with colorizer('red'):
    print('printed in red')