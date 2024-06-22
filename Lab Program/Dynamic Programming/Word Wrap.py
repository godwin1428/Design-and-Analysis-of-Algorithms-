import sys

def solve_word_wrap(words, max_length):
    n = len(words)
    
    # Step 1: Initialize extras array
    extras = [[0] * n for _ in range(n)]
    
    for i in range(n):
        extras[i][i] = max_length - len(words[i])
        for j in range(i + 1, n):
            extras[i][j] = extras[i][j - 1] - len(words[j]) - 1
    
    # Step 2: Initialize line cost array
    line_cost = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if extras[i][j] < 0:
                line_cost[i][j] = sys.maxsize
            elif j == n - 1:
                line_cost[i][j] = 0
            else:
                line_cost[i][j] = extras[i][j] ** 2
    
    # Step 3: Calculate total cost and positions
    total_cost = [0] * n
    p = [0] * n
    
    for j in range(n):
        total_cost[j] = sys.maxsize
        for i in range(j + 1):
            if total_cost[i - 1] + line_cost[i][j] < total_cost[j]:
                total_cost[j] = total_cost[i - 1] + line_cost[i][j]
                p[j] = i
    
    # Step 4: Reconstruct the solution
    lines = []
    i = n
    while i > 0:
        start = p[i - 1]
        lines.append(" ".join(words[start:i]))
        i = start
    
    lines.reverse()
    return lines, total_cost, p, extras, line_cost

# Input
text = "Saveetha School of Engineering"
words = text.split()
max_length = 11

wrapped_text, total_cost, p, extras, line_cost = solve_word_wrap(words, max_length)

# Output results
print("Wrapped Text:")
for line in wrapped_text:
    print(line)

print("\nTotal Cost Array:")
print(total_cost)

print("\nPosition Array:")
print(p)

print("\nExtras Array:")
for row in extras:
    print(row)

print("\nLine Cost Array:")
for row in line_cost:
    print(row)
