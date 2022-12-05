lines = open('day2/input.txt', 'r').readlines()

data = [[line[0], line[2]] for line  in lines]


def score_for_choice(my_choice):
	if my_choice == 'A':
		return 1
	if my_choice == 'B':
		return 2
	if my_choice == 'C':
		return 3


def i_win(their_choice, my_choice): 
	if their_choice == 'A':
		return my_choice == 'B'
	if their_choice == 'B':
		return my_choice == 'C'
	if their_choice == 'C':
		return my_choice == 'A'


def we_draw(their_choice, my_choice):
	return their_choice == my_choice


def round_score(their_choice, my_choice):
	total = score_for_choice(my_choice)
	if i_win(their_choice, my_choice):
		total += 6
	elif we_draw(their_choice, my_choice):
		total += 3
	return total


strategy = {'X': 'A', 'Y': 'B', 'Z': 'C'}

result = 0
for their_choice, my_choice in data:
	result += round_score(their_choice, strategy[my_choice])

print('solution part 1:')
print(result)


i_should_win = lambda letter: letter == 'Z'
i_should_draw = lambda letter:letter == 'Y'
i_should_lose = lambda letter: letter == 'X'


def get_my_choice(their_choice, coded_desired_result):
	if i_should_win(coded_desired_result):
		if their_choice == 'A':
			return 'B'
		if their_choice == 'B':
			return 'C'
		if their_choice == 'C':
			return 'A'
	if i_should_lose(coded_desired_result):
		if their_choice == 'A':
			return 'C'
		if their_choice == 'B':
			return 'A'
		if their_choice == 'C':
			return 'B'
	if i_should_draw:
		return their_choice


result = 0
for their_choice, coded_desired_result in data:
	my_choice = get_my_choice(their_choice, coded_desired_result)
	result += round_score(their_choice, my_choice)

print('solution for part 2:')
print(result)
