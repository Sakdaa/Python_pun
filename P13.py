def simple_poet(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # Strip newline characters from each line
    lines = [line.rstrip('\n') for line in lines]
    return lines

# Example usage
if __name__ == '__main__':
    res = simple_poet('poem.txt')
    print(res)
