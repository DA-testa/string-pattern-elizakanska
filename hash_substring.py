# python3
# Elīza Kanska 221RDB095

def readInput(sourceFile=None):
    # this funciotn reads the input data from the file or keyboard input
    if sourceFile is not None:
        try:
            with open(f"./tests/{sourceFile}") as f:
                data = f.readlines()
        except FileNotFoundError:
            raise ValueError("Data file not found")
        except:
            raise ValueError("Reading error")

        pttrn = data[0].strip()
        txt = data[1].strip()
    else:
        pttrn = input().rstrip()
        txt = input().rstrip()

    return pttrn, txt

def printOccurrences(output):
    # this function controls output, it doesn't need or have any return
    print(' '.join(map(str, output)))

def getOccurrences(pttrn, txt):
    # this function finds the occurrences using Rabin Karp algorithm
    pNumber = 101
    base = 256
    occur = []
    pttrnH = 0
    txtH = 0
    
    for i in range(len(pttrn)):
        pttrnH = (pttrnH * base + ord(pttrn[i])) % pNumber
        txtH = (txtH * base + ord(txt[i])) % pNumber

    for i in range(len(txt) - len(pttrn) + 1):
        if pttrnH == txtH:
            if pttrn == txt[i:i+len(pttrn)]:
                occur.append(i)

        if i < len(txt) - len(pttrn):
            txtH = ((txtH - ord(txt[i]) * (base**(len(pttrn)-1))) * base + ord(txt[i+len(pttrn)])) % pNumber

    return occur

# this part launches the functions
if __name__ == '__main__':
    inSource = input().rstrip()

    if inSource == 'I':
        pttrn, txt = readInput()
    elif inSource == 'F':
        sourceFile = "06"
        if str(sourceFile[-1]) == "a":
            raise ValueError("Invalid filename")
        pttrn, txt = readInput(sourceFile)
    else:
        raise ValueError("Invalid input source")

    printOccurrences(getOccurrences(pttrn, txt))
