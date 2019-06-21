def matchingStrings(strings, queries):
    for q in queries:
        print(strings.count(q))

matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
