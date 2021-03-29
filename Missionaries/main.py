import sys
import time

from Graph import Graph, genPossibleMoves

from State import State, Direction, TERMINAL_STATE

from Constants import CONST

CON_OUT = sys.stdout


def runBFS(g, INITIAL_STATE):
	sys.stdout = open("outBFS.txt", "w")
	print("\n\nBFS :: \n")
	start_time = time.time()
	p = g.BFS(INITIAL_STATE)
	end_time = time.time()
	if len(p):
		g.printPath(p, TERMINAL_STATE)
	else:
		print("No Solution")
	print("\n Elapsed time in BFS: %.2fms" % ((end_time - start_time)*1000))


def main():
	CNST = CONST(3, 3, 2)

	moves = genPossibleMoves(CNST.CAP_BOAT)
	print(str(moves.__len__())+" iterations per Node.")

	INITIAL_STATE = State(CNST.MAX_M, CNST.MAX_C, Direction.RIGHT, 0, 0, 0, moves)

	g = Graph()
	sys.stdout = CON_OUT
	print("\nRunning BFS>")
	runBFS(g, INITIAL_STATE)
	sys.stdout = CON_OUT
	print("Executed BFS>")



if __name__ == '__main__':
	main()
