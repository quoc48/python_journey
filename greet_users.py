def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each designs, until none are left.
    Move each deign to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_model(completed_models):
    """ Show all the models that were printed. """
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprintted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprintted_design,completed_models)
show_completed_model(completed_models)