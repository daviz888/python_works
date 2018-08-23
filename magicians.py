import screen
screen.clear()

def show_magicians(magicians):
    print("Our top Magicians:")
    for magician in magicians:
        print(f'\t{magician.title()}')

def make_great(magicians):
    for magician in range(len(magicians)):
        magicians[magician] += ' Great'

magicians = ['alice', 'david', 'carolina']
make_great(magicians)
show_magicians(magicians)