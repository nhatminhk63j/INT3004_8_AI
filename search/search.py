# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    "*** YOUR CODE HERE ***"
    # init start node.
    start_node = problem.getStartState()

    # define stack will save node and actions result that will be return.
    stack = util.Stack()

    # define variable visited to store node that agent visited.
    visited = {}

    # stack will save (node,actions)
    stack.push((start_node, []))

    while not stack.isEmpty():
        current_node, actions = stack.pop()

        if current_node not in visited:
            visited[current_node] = True

            if problem.isGoalState(current_node):
                return actions
            
            for next_node, action, cost in problem.getSuccessors(current_node):
                new_actions = actions + [action]
                stack.push((next_node, new_actions))
    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # init start node.
    start_node = problem.getStartState()

    # road_state will store (node, action). road_state as linkedlist store way's agent.
    # road_state has structure { node : (next_node, action), ...}
    road_state = {}

    # init road_state with start node.
    road_state[start_node] = (None, None)

    # queue will be store nodes that agent can be moved.
    queue = util.Queue()

    # init queue with start node.
    queue.push(start_node)

    # define goal state.
    goal_node = None

    while not queue.isEmpty():
        # get top node from queue.
        top_node = queue.pop()

        # if top node is goal state, exit loop queue.
        if (problem.isGoalState(top_node)):
            goal_node = top_node
            break

        # try in any case can go.
        for next_node, action, cost in problem.getSuccessors(top_node):
            # if next node in road_state (visited), do not store to road_state.
            if next_node in road_state:
                continue
            road_state[next_node] = (top_node, action)
            queue.push(next_node)
    
    # if has not goal state return None.
    if goal_node is None:
        return None

    current_node = goal_node
    actions = []

    # loop road_state from goal state to get actions.
    while True:
        previous_node, action = road_state[current_node]
        if previous_node is None:
            break
        actions = actions + [action]
        current_node = previous_node

    # because we get way from goal state to start state, we will return array reverse of actions.
    actions.reverse()

    return actions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # uniform cost search is A* search with heuristic = 0.
    # using priority queue.
    
    return aStarSearch(problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # init start node.
    start_node = problem.getStartState()
    # road_state will store (node, action). road_state as linkedlist store way's agent.
    # road_state has structure { node : (next_node, action), ...}
    road_state = {}
    # cost_from_start store (node, cost)
    cost_from_start = {}
    # init road_state by start_node.
    road_state[start_node] = (None, None)
    # define priority_queue will be store (node, cost), sort by heuristic_cost
    priority_queue = util.PriorityQueue()

    cost_from_start[start_node] = 0

    priority_queue.push((start_node, 0), 0)

    goal_node = None

    while not priority_queue.isEmpty():
        top_node, current_cost = priority_queue.pop()

        if (cost_from_start[top_node] != current_cost):
            continue

        if (problem.isGoalState(top_node)):
            goal_node = top_node
            break
        for next_node, action, cost in problem.getSuccessors(top_node):
            new_cost = current_cost + cost
            if next_node in road_state:
                if (cost_from_start[next_node] <= new_cost):
                    continue
            
            road_state[next_node] = (top_node, action)
            cost_from_start[next_node] = new_cost
            heuristic_cost = new_cost + heuristic(next_node, problem)
            priority_queue.push((next_node, new_cost), heuristic_cost)
    
    if goal_node is None:
        return None
    
    current_node = goal_node
    actions = []

    # loop road_state from goal state to get actions.
    while True:
        previous_node, action = road_state[current_node]
        if previous_node is None:
            break
        actions = actions + [action]
        current_node = previous_node
    
    actions.reverse()
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
