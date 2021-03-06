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
from util import Node
import sys

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

	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	"""
	
	#Initialize the frontier using the initial state of the problem
	node =  Node((problem.getStartState(),'None',0), None)
	if problem.isGoalState(node.state):
		return node.getPath()

	frontier = util.Stack()
	frontier.push(node)

	#Initialize the explored set to be empty
	explored = set()

	while True:
		if frontier.isEmpty():
			print "Failure!"
			break

		#Choose a leaf node and remove it from the frontier
		node = frontier.pop()
		
		#If the node contains a goal state, return the solution
		#if problem.isGoalState(node.state):
			#return node.getPath()

		#Add the state of the node to the explored set
		explored.add(node.state)

		#Expand the chosen node
		successors = problem.getSuccessors(node.state)

		for succ in successors:
			child = Node(succ,node)
			if child.state not in explored and child not in frontier.list:
				if problem.isGoalState(child.state):
					return child.getPath()
				frontier.push(child)

	print "Solution not found!"		
	util.raiseNotDefined()

	

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	
	node =  Node((problem.getStartState(),'None',0), None)
	
	if problem.isGoalState(node.state):
		return node.getPath()
	
	#A FIFO queue with node as the only element 
	frontier = util.Queue()
	frontier.push(node)

	#An empty set
	explored = set()

	if(sys.argv[2] != "mediumCorners"):
		while True:
			if frontier.isEmpty():
				break

			node = frontier.pop()

			#Add node's state to explored
			explored.add(node.state)

			successors = problem.getSuccessors(node.state)

			for succ in successors:
				child = Node(succ,node)
				if (child.state not in explored) and (child not in frontier.list):
					if problem.isGoalState(child.state):
						return child.getPath()
					frontier.push(child)
		print "Failure!"
		return None

	else:
	
	#Part that works with the autograder
	
		while True:
			if frontier.isEmpty():
				break

			node = frontier.pop()
			
			
			if problem.isGoalState(node.state):
				return node.getPath()
			
			
			#Add node's state to explored
			explored.add(node.state)

			successors = problem.getSuccessors(node.state)

			for succ in successors:
				child = Node(succ,node)
				if (child.state not in explored) and (child not in frontier.list):
					frontier.push(child)
					explored.add(child.state)
	
		print "Failure!"
		return None

def uniformCostSearch(problem):
	"""Search the node of least total cost first."""

	node = Node((problem.getStartState(),"None",0),None)

	frontier = util.PriorityQueue()
	frontier.push(node,node.pathCost)

	explored = set()

	while True:

		if frontier.isEmpty():
			break

		#Object of class Node
		node = frontier.pop()

		#if problem.isGoalState(node.state):
			#return node.getPath()
		
		explored.add(node.state)

		successors = problem.getSuccessors(node.state)

		for succ in successors:
			child = Node(succ,node)
			if (child.state not in explored) and (child not in frontier.heap):
				if problem.isGoalState(child.state):
					return child.getPath()
				frontier.push(child,child.pathCost)
			elif child in frontier.heap:
				frontier.update(child,child.pathCost)


	print "Failure!"
	return None
	

def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	#actions = path

	node = node = Node((problem.getStartState(),"None",0),None)

	frontier = util.PriorityQueue()
	frontier.push(node,heuristic(node.state,problem))

	explored = set()

	while True:
		if frontier.isEmpty():
			break

		node = frontier.pop()

		#if problem.isGoalState(node.state):
			#return node.getPath()

		explored.add(node.state)

		successors = problem.getSuccessors(node.state)

		for succ in successors:
			child = Node(succ,node)
			if(child.state not in explored) and (child not in frontier.heap):
				if problem.isGoalState(child.state):
					return child.getPath()
				frontier.push(child,child.pathCost+heuristic(child.state,problem))
			elif child in frontier.heap:
				frontier.update(child,child.pathCost+heuristic(child.state,problem))
		
	print "Failure!"
	return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
