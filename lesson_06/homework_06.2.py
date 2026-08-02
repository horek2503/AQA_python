result = False
while not result:
    input_string = input("Please enter a word with letter 'h':")
    result = True if 'h' in input_string.lower() else False