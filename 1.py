t=open("1.txt","r").readlines()
o=len(t)

for i,p in zip(open("1.txt"),range(0,o)):
    #print(i[:-1])
    l=i[:-1]
    g=l.split(":")
    #print("============")
    #print(g[0])
    if(g[1] == "0"):
        print(">> "+g[0])
    else:
        print("s")
