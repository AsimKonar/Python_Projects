d = [
    {
        'id':1,
        'name':"test1",
        'email':'abc1@xyz.com'
    },
    {
        'id':2,
        'name': "test2",
        'email':'abc2@xyz.com'
    },
    {
        'id':3,
        'name': "test3",
        'email':'abc3@xyz.com'
    }
]
print("unchanged: ", d)
for i in d:
    print("i= ", i)
    if i['name'] == 'test2':
        i['email'] = 'xyz@abc.com'

print("changed: ", d)