import screen
screen.clear()

def print_models(unprinted_designs, completed_models):
    # Simulate printing each design, until none are left.
    print("\nUnprinted Designs:")
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #Simulate creating 3D print from the design
        print("\tPrinting model: " + current_design.title())
        completed_models.append(current_design)

def show_completed_Models(completed_models):
    # Show all the models that are printed.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print("\t" + completed_model.title())
    
# Start some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_Models(completed_models)

