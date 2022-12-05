lines = open('day1/input.txt', 'r').readlines()
cleaned_lines = [i.strip() for i in lines]

elves = []

current_elf = 0
for calorie in cleaned_lines:
	if calorie == '':
		elves.append(current_elf)
		current_elf = 0
	else:
		current_elf += int(calorie)

elves.sort(reverse=True)

print('solution to part 1:')
print(elves[0])

print('solution to part 2:')
print(sum(elves[0:3]))
