
# import json
# listdata=[]

# for s in range(2):
#     print("s", s+1)
#     dict = {
#         "name": input("pls enter name: "),
#         "id":int(input("pls enter id:")),
#         "address":input("pls enter address:"),
#         "qualification":{
#             "qualification":input("pls enter qualification:"),
#             "passing year":int(input("pls enter passing year: "))
#     }
# }
#     dict["email"]=input("pls enter email:")
#     dict.pop("name")
#     listdata.append(dict)
    
#     data=json.dumps(listdata,indent=4)
#     print(data)
    
dict = {
        "name": input("pls enter name: "),
        "id":int(input("pls enter id:")),
        "address":input("pls enter address:")
    }
id = int(input("pls enter id: "))
if dict["id"] == id:
    print(dict)
else:
    print("not found")