import sys
sys.setrecursionlimit(60)

def first(string):
    first_ = set()                                  # Initialising Empty set to store first set

    if string in non_terminals:                     # If the given string is a non-terminal symbol
        alternatives = productions_dict[string]

        for alternative in alternatives:            
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}                           # Set the First set to a set containing only the given terminal symbol

    elif string=='' or string=='@':
        first_ = {'@'}                              # Set the First set to a set containing only the epsilon symbol

    else:                                           # S -> AB
        first_2 = first(string[0])                  # A - > a | b | @
        if '@' in first_2:
            i = 1
            while '@' in first_2:

                first_ = first_ | (first_2 - {'@'})  
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2

    return  first_

def follow(nT):

    follow_ = set()                             # Initialising Empty set to store follow set

    prods = productions_dict.items()

    if nT==starting_symbol:
        follow_ = follow_ | {'$'}

    for nt,rhs in prods:                        # Following Follow Set Rules one-by-one
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2

    return follow_


terminals = []
non_terminals = []
productions = []
productions_dict = {}

# Taking Terminals

no_of_terminals=int(input("Enter number of terminals: "))
print("Enter", no_of_terminals ,"terminals: ")
for _ in range(no_of_terminals):
    terminals.append(input())

print("\n-----------------------------------------------------\n")

# Taking Non Terminals

no_of_non_terminals=int(input("Enter number of non-terminals: "))
print("Enter",no_of_non_terminals, "non terminals :")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

print("\n-----------------------------------------------------\n")

# Taking Starting Symbol

starting_symbol = input("Enter the starting symbol: ")
print("\n-----------------------------------------------------\n")

# Taking Productions

no_of_productions = int(input("Enter no. of productions: "))
print("Enter", no_of_productions ,"productions:")
for _ in range(no_of_productions):
    productions.append(input())

print("\n-----------------------------------------------------\n")

for nT in non_terminals:
    productions_dict[nT] = []

for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

FOLLOW = {}

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()


FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)

print("{: ^20}{: ^20}".format('Non Terminals','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}".format(non_terminal,str(FOLLOW[non_terminal])))