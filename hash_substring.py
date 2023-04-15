# python3

def read_input():
    # this function acquires input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    inType = input().rstrip()
    
    if inType == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif inType == 'F':
        # might need adjustments, will see when testing
        filename = input().rstrip()
        with open(filename) as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    
    # return both lines in one return
    return (pattern, text)

def print_occurrences(output):
    # this function controls output, it doesn't need or have any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function finds the occurrences using Rabin Karp algorithm
    
    occurrences = []
    
    if len(pattern) > len(text):
        return occurrences
    
    hash_pttrn = hash(pattern)
    hash_txt = hash(text[:len(pattern)])
    
    if hash_pttrn == hash_txt and pattern == text[:len(pattern)]:
        occurrences.append(0)
    
    prime = 2**31 - 1
    h = pow(2, 8*(len(pattern)-1), prime) # 256^(m-1)
    
    for i in range(1, len(text)-len(pattern)+1):
        hash_txt = ((hash_txt - ord(text[i-1])*h)*256 + ord(text[i+len(pattern)-1])) % prime
        
        if hash_txt == hash_pttrn and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
    
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
