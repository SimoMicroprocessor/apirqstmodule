import requests
import json

'''result = requests.get("https://jsonplaceholder.typicode.com/todos")
result.text  #المعلومة التي ستأتي ستكون جيسون يعني سترينج و من أجل الوصول إلى أي قسم من المعلومة يجب أن نحولها إلى متغير من نوع المعجم 
print(result)
result= json.loads(result.text)
print(result[0]["title"])
for i in result:
    if(i["userId"]) == 1:
        print(i["title"])
print(type(result))'''



''' github api '''
class Github :
    def __init__(self):
        self.api_url ='https://api.github.com'
    def getuser(self,username):
        response = requests.get('https://api.github.com'+'/users/'+username)
        return response.json()

github = Github()

while(1):
    secim = input('choose please')
    if secim == '1':
        username = input('username')
        result=github.getuser(username)
        
        print(f"name : {result['name']}  public respos : {result['public_repos']}  follower : {result['followers']}")




