var_string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
patches = [[4, 14, "Conquistador"], [25, 31, "King"], [42, 49, "Palace"]]

result = ""
start_index = 0

for patch in patches:
    start, end, replacement = patch
    result += var_string[start_index:start] + replacement
    start_index = end

result += var_string[start_index:]

print(result)

