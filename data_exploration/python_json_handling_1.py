import json


class JSONHandling:
    def __init__(self, json: object):
        self.json =  json




def func(strng):
    a =json.loads(strng)
    print(type(a))


if __name__== "__main__":
    #json.loads('../data/create_repo.json')
    json_string = '{"name":"Rupert", "age": 25, "desig":"developer"}'
    print(type (json_string))
    func(json_string)

    # read file
    with open('../data/create_repo.json', 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)# show values
    print("usd: " + str(obj['repo_name']))


