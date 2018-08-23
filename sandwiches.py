import screen
screen.clear()

def sandwich_maker(*sandwiches):
    print("\nHere are the sandwiches you ordered:")
    for sandwich in sandwiches:
        print(f'\t- {sandwich.title()} - sandwiche')

sandwich_maker('chicken')
sandwich_maker('egg', 'chicken', 'ham', 'cheese')
sandwich_maker('bacon', 'egg', 'ham&cheese', 'shawarma', 'vagetable')
