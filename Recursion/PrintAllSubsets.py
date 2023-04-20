'''print all the possible subsets of first n natural numbers'''

def findSubsets(n,subset):
    if n == 0:
        print(subset)
        return
    subset.append(n)
    findSubsets(n-1,subset)

    subset.pop()
    findSubsets(n-1,subset)
findSubsets(3,[])