# input for header
M, N, T = map(int, input().split(' '))

input() # to remove spaceing

# input for state space
state_space = []
for i in range(M):
    state_space.append(tuple(input()[1:-1].split(", ")))

print(state_space)
input() # to skip one line

# input for rules
rules = []
for i in range(N):
    rules.append(input())

input() # to skip one line

# input for transition table
transition_table = []
for i in range(M):
    temp=[]
    inputs=(input().split(' '))
    for j in inputs:
        temp.append(int(j))
    transition_table.append(temp)

input() # to skip one line

# input for cases
test_cases = []
for i in range(T):
    temp=input().split('\t')
   
    test_cases.append({
        'start': state_space.index(tuple(temp[0][1:-1].split(", "))), #getting the indexes from states
        'end': state_space.index(tuple(temp[1][1:-1].split(", ")))
        })


def print_result(states):
    actions = []

    for i in range(len(states)-1):
        for j in range(N):
            if transition_table[states[i]][j] == states[i+1]:
                actions.append(rules[j])
                break
    print("->".join(actions))

# MAIN PROCEDURE
for test_case in test_cases:
    visited = []
    frontier = []
    frontier.append((test_case['start'],))
    visited.append(test_case['start'])

    while (len(frontier) != 0):
        state = frontier.pop(0)  # acting like priority queue
        if (state[-1] == test_case['end']):
            print_result(state)
            break
        else:
            for next_state in transition_table[state[-1]]: #getting values index by index[N] from 2d array at M index
                if next_state not in visited:
                    frontier.append(state + (next_state,))
                    visited.append(next_state)