from searchAgents import PositionSearchProblem

class FindFurthestDotProblem(PositionSearchProblem):
    def __init__(self, state, start, goals):
        PositionSearchProblem.__init__(self, state, start=start, warn=False, visualize=False)
        self.goals = {key: True for key in goals}
        self.count = len(goals)

    def isGoalState(self, state):
        if state in self.goals:
            if (self.goals[state]):
                self.goals[state] = False
                self.count -= 1
            return self.count == 0
        return False