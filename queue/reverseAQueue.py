def rev(q):

    #add code here

    lis=[]

    for i in range(q.qsize()):

        lis.append(q.get())

    lis.reverse()

    q.empty()

    for i in lis:

        q.put(i)

    return q
