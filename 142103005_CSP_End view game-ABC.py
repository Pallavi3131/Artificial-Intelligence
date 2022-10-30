#14213005
#Pallavi Gaikwad

# End View-ABC Game-
# Each letter must appear exactly once in each row and column. Not every cell is filled and Within a row,
# each letter must be in a different column.
# Some rows and columns' ends are specified. These mean that the filled cell closest to that
# end must have the given letter.

#Here, I have designed an example for 7x7 grid wherein 1 box can be blank.
#Similarly we can increase the grid size,alphabets,no. of blanks according to our choice.

from constraint import Problem, AllDifferentConstraint
from itertools import permutations

print("<<<<<<<   WELCOME TO End View-ABC GAME!  >>>>>>>")
print("              Here's the Result!!\n")
letters = "ABCDEF"

#letters at end of row, from top to bottom['.' signifies no letter exists]
left = ".F.CBE."
right = "FBE.CAB"
#letters at end of column, from left to right
top = "ECAD.A."
bottom = "AFCFE.B"

N = len(letters)
S = len(left)  # grid size.
B = S - N  # no. of blanks per row/column.

variables = [letter + str(row) for letter in letters for row in range(S)]
problem = Problem()
problem.addVariables(variables, list(range(S)))

for row in range(S):
	rowvars = [letter + str(row) for letter in letters]
	problem.addConstraint(AllDifferentConstraint(), rowvars)

for letter in letters:
	lettervars = [letter + str(row) for row in range(S)]
	problem.addConstraint(AllDifferentConstraint(), lettervars)

for row, letter in enumerate(left):
	if letter == ".": continue
	for other in letters:
		if other != letter:
			problem.addConstraint(lambda x, y: x < y, (letter + str(row), other + str(row)))

for row, letter in enumerate(right):
	if letter == ".": continue
	for other in letters:
		if other != letter:
			problem.addConstraint(lambda x, y: x > y, (letter + str(row), other + str(row)))

def tbconstraint(col):
	def ok(*values):
		for j, value in enumerate(values):
			if value == col:
				return j % N == 0
		return False
	return ok

def orderedvars(rows, letter):
	values = []
	for j, row in enumerate(rows):
		values.append(letter + str(row))
		# No need to check the incorrect letters on the last row in the list.
		# (This makes a huge difference in runtime!)
		if j < len(rows) - 1:
			values += [other + str(row) for other in letters if other != letter]
	return values

for col, letter in enumerate(top):
	if letter == ".": continue
	problem.addConstraint(tbconstraint(col), orderedvars(range(B+1), letter))

for col, letter in enumerate(bottom):
	if letter == ".": continue
	problem.addConstraint(tbconstraint(col), orderedvars(range(S-1, S-B-2, -1), letter))

for solution in problem.getSolutions():
	grid = [["." for col in range(S)] for row in range(S)]
	for value, col in solution.items():
		letter = value[0]
		row = int(value[1:])
		grid[row][col] = letter
	print("\n".join(" ".join(row) for row in grid))
