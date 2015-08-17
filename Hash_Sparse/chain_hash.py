def chainHash(InputList):
    res={}
    for line in InputList:
        if line.split()[0] not in res:
            temp=[]
            temp.append(line.split()[1])
            res["%s"%line.split()[0]]=temp
        else:
            res["%s"%line.split()[0]].append(line.split()[1])
    return res


input=["k1 v1", "k2 v1", "k3 v1", "k1 v2", "k2 v2", "k1 v3"]

print chainHash(input)
