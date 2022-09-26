# 1) Skip 'a' character

def skipChar(word, char, newWord=''):
    if not word:
        return newWord
    if word[0] != char:
        return skipChar(word[1:], char, newWord + word[0])
    return skipChar(word[1:], char, newWord)


print(skipChar('aramanyana', 'a'))

# SHORTCUT :: word.replace(char)

# 2) Skip a String

def skipString(word, char, newWord=''):
    if not word:
        return newWord
    if word.startswith(char):
        return skipString(word[(len(char)):], char, newWord)
    return skipString(word[1:], char, newWord + word[0])


print(skipString('aramanyanaaram', 'ram'))
# SHORTCUT :: word.replace(char)

# 3) Print all subsets

def subsets(un, p=''):
    if not un:
        print(p)
        return
    ch = un[0]
    subsets(un[1:], p+ch)
    subsets(un[1:], p)

subsets('abc')


# 4) Array of all subsets

def subsetsArr(un, p=''):
    if not un:
        return [p]
    ch = un[0]
    return subsetsArr(un[1:], p + ch) + subsetsArr(un[1:], p)


print(subsetsArr('abc'))


# 5) Count no of subsets

def subsetsArrCount(un, p=''):
    if not un:
        return [p]
    ch = un[0]
    return subsetsArrCount(un[1:], p + ch) + subsetsArrCount(un[1:], p)


print(len(subsetsArrCount('abc')))


# 6) print all subset with their ASCII

def subsets1(un, p=''):
    if not un:
        print(p)
        return
    ch = un[0]
    subsets1(un[1:], p+ch)
    subsets1(un[1:], p+str(ord(ch)))
    subsets1(un[1:], p)

subsets1('abc')


# 7) all sequence of arrangement

def permutations(un, p=""):
    if not un:
        print(p)
        return
    for i in range(len(p)+1):
        f= p[0:i]
        s = p[i:len(p)]
        permutations(un[1:], f+un[0]+s)

permutations('abc')
