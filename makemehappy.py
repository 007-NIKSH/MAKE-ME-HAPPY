from PIL import Image
import requests

def classify(text):
    key = "d0c46240-6d04-11eb-b315-f510e093cfba994f035b-748b-44b3-a40d-730b062b6c9f"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

input = input("ENTER A COMPLIMENT OR INSULT >>> ")

recognized = classify(input)

label = recognized["class_name"]

if label == "KIND_THING":
    print ("YOU ARE VERY KIND :)")
    img = Image.open("Happy_Face.jpg")
    img.show()

else:
    print ("YOU ARE VERY MEAN :(")
    img = Image.open("Sad_Face.jpg")
    img.show()