import requests
url = 'https://tomato.sarthakgoelart.repl.co/predict_disease'
my_img = {'image': open('test.jpg', 'rb')}
r = requests.post(url, files=my_img)
print(r.json())