import json

listdata = []

def student():

    for s in range(2):
        print("student", s+1)

        dictdata = {
            "name": input("pls enter your name: "),
            "id": input("pls enter your id: "),
            "address": input("pls enter your address: ")
        }

        listdata.append(dictdata)


def file():

    with open("testing.json", "w") as f:
        json.dump(listdata, f, indent=4)

    print("Data stored in JSON file")

    jsonstring=json.dumps(listdata,indent=4)
    print(jsonstring)


student()
file()
