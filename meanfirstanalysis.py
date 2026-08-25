class MeanEndAnalysis:
    def __init__(self, operators):
        self.operators = operators

    def solve(self, current, goal):
        print(f"Current state: {current} | Goal state: {goal}")

        # Goal reached
        if self.goal_reached(current, goal):
            return []

        # Find the first difference
        diff = self.find_difference(current, goal)

        if diff is None:
            return []

        # Select an operator to resolve the difference
        op = self.select_operator(diff)

        if op is None:
            print(f"No operator found to resolve difference: {diff}")
            return None

        # Solve preconditions first
        preconditions_path = self.solve(current, op['precond'])

        if preconditions_path is None:
            return None

        # Apply operator
        new_state = current.copy()
        new_state.update(op['effect'])

        # Solve remaining goal
        remaining_path = self.solve(new_state, goal)

        if remaining_path is None:
            return None

        return preconditions_path + [op['name']] + remaining_path

    # Check whether goal is achieved
    def goal_reached(self, current, goal):
        for key, value in goal.items():
            if current.get(key) != value:
                return False
        return True

    # Find first difference between current state and goal
    def find_difference(self, current, goal):
        for key in goal:
            if current.get(key) != goal[key]:
                return (key, goal[key])
        return None

    # Select operator that achieves the required effect
    def select_operator(self, diff):
        key, value = diff

        for op in self.operators:
            if op['effect'].get(key) == value:
                return op

        return None


# ---------------- Example Usage ----------------

if __name__ == "__main__":

    operators = [
        {
            'name': 'Drive_Car',
            'precond': {
                'has_car': True,
                'at_home': True
            },
            'effect': {
                'at_work': True,
                'at_home': False
            }
        },

        {
            'name': 'Buy_Car',
            'precond': {
                'has_money': True,
                'has_car': False
            },
            'effect': {
                'has_car': True
            }
        }
    ]

    current_state = {
        'has_money': True,
        'has_car': False,
        'at_home': True,
        'at_work': False
    }

    goal_state = {
        'at_work': True
    }

    mea = MeanEndAnalysis(operators)

    plan = mea.solve(current_state, goal_state)

    print("\nExecution Plan:", plan)

    print("Samarth 24BECS140")