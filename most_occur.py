text=input().split()
st=set(text)
most=''
mc=0
for each in st:
    if(text.count(each)>mc):
        mc=text.count(each)
        most=each
print(f"{most} occured {mc} times")