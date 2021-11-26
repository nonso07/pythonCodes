from random import shuffle


firstDic= {"one":["orange","Appel","Paw Paw", "Mango"], "two":["Lagos","Abuja", "Abdijian","kenya"]}
print(firstDic["one"][0].capitalize())
print(firstDic["one"][0].upper())
changeToArr= list(firstDic)
shuffle(changeToArr)
print(changeToArr)
if str(firstDic["one"][0])=="Orange" or firstDic["one"][0]=="orange":
    print("equal")
else:
    print("Not Equal")
for item in firstDic:
    print(firstDic[item])
    
    