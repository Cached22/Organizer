from ortools.linear_solver import pywraplp
from SpaceOrganizer.backend.api.models import Item, Layout

def generate_layout(items, space_dimensions):
    """
    Generates an optimal layout for the given items within the provided space dimensions.
    
    :param items: List of Item objects with their dimensions and positions.
    :param space_dimensions: Tuple of (width, height) representing the space dimensions.
    :return: Layout object with positions for each item.
    """
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        raise Exception("Failed to create solver")

    width, height = space_dimensions
    item_vars = {}

    # Define variables for item positions
    for item in items:
        x = solver.NumVar(0, width - item.width, f'x_{item.id}')
        y = solver.NumVar(0, height - item.height, f'y_{item.id}')
        item_vars[item.id] = (x, y)

    # Define constraints to prevent items from overlapping
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            item_i = items[i]
            item_j = items[j]
            xi, yi = item_vars[item_i.id]
            xj, yj = item_vars[item_j.id]

            # Create overlap constraints
            solver.Add(xi + item_i.width <= xj | xj + item_j.width <= xi)
            solver.Add(yi + item_i.height <= yj | yj + item_j.height <= yi)

    # Define the objective function (optional)
    # For example, minimize the total distance from a certain point (e.g., entrance)
    entrance_x, entrance_y = 0, 0
    objective = solver.Objective()
    for item in items:
        x, y = item_vars[item.id]
        distance = solver.Sum([(x - entrance_x) ** 2, (y - entrance_y) ** 2])
        objective.SetCoefficient(distance, 1)
    objective.SetMinimization()

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        # If the solution is optimal, create a Layout object with the positions
        layout = Layout()
        for item in items:
            x, y = item_vars[item.id]
            layout.positions[item.id] = (x.solution_value(), y.solution_value())
        return layout
    else:
        raise Exception("The solver did not find an optimal solution.")

# Example usage:
# items = [Item(id=1, width=2, height=3), Item(id=2, width=3, height=2)]
# space_dimensions = (10, 10)
# layout = generate_layout(items, space_dimensions)
# print(layout.positions)