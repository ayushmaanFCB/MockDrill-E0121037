def organize(itenary):
    stops = [stop for stop in itenary]

    stack = []
    stack.append("JFK")

    for stop in stops:
        if stop[0] not in stack:
            print(stack[0])
            stack.append(stop[0])
        if stop[1] not in stack:
            stack.append(stop[1])

    print(stack)


test_cases = [
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
    [["JFK", "SFO"], ["SFO", "JFK"], ["JFK", "SFO"], ["SFO", "JFK"]],
    [["JFK", "SFO"]]
]


for case in test_cases:
    organize(case)
