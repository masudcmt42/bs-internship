import jeson

j = json.loads(open('data.json', "r").read())
count =1
for x in j:
    print("data no", count)
    count+=1
    for key, val in x.items():
        print(key, "  ==> ", val)
