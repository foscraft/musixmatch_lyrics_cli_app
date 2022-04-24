from pyfiglet import Figlet

def figs_cli():
    '''
    Pyfiglet is a python module for converting strings into ASCII Text with arts fonts.
    '''
    msg = Figlet(font='slant')
    print(msg.renderText('Lyrics Finder'))
