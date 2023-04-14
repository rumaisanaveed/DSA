def printMatrix(weightedMat):
    for r in range(len(weightedMat)):
        for c in range(len(weightedMat)):
            print(weightedMat[r][c],end = "\t")
        print()

def FloydAlgorithm(weightedMat):
    for k in range(len(weightedMat)):
        for i in range(len(weightedMat)):
            for j in range(len(weightedMat)):
                weightedMat[i][j] = min(weightedMat[i][j],weightedMat[i][k] + weightedMat[k][j])
    return printMatrix(weightedMat)

FloydAlgorithm([[0,3,float('inf'),7],
                [8,0,2,float('inf')],
                [5,float('inf'),0,1],
                [2,float('inf'),float('inf'),0]])
