def remove_dup(a):
    return list(set(a))
a=list(map(int,input("ENTER ELEMENTS OF A LIST TO REMOVE DUPLICATES: ").split()))
print(remove_dup(a))