vowels = 'aeoui'


def count_vowels(line: str) -> int:
    count = 0
    for i in line.lower():
        if i in vowels:
            count += 1
    # count = ([x for x in line.lower() if x in vowels])

    return count


vowels_count = count_vowels('Hello, Python!')
print(vowels_count)
