def problem1(asdf, k):
    visitedSet = set()
    for i in range(0, len(asdf)):
        if (asdf[i] in visitedSet):
            return True
        visitedSet.add(k - asdf[i])
    return False
