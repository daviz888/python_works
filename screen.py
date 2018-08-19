# Clear screen Class
import os
from subprocess import  call

def clear():
    # check os type
    _ = call('clear' if os.name == 'posix' else 'cls')

if __name__ == '__main__':
    clear()
    