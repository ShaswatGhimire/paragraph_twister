import requests,sys
import json
def main():
    try:
        while True:
            print("----------------------------------")
            print("Enter: (Ctrl + D to exit) ")
            x = str(input("RE for Rewriter \nSE for sentiment analysis \nAR for article extraction\n\n"))
            print("----------------------------------")

            if valid(x):
                match x.upper():
                    case "RE":
                        print("Rewrited Sentence:",rewriter(), end='\n\n')
                    case "SE":
                        print("The user is feeling:",sentiment(), end='\n\n')
                    case "AR":
                        print(article(), end='\n\n')
            else:
                print("Try again, error in input")
    except EOFError:
        sys.exit("terminated sucessfully")

def valid(x):
    return x.upper() in ["RE","SE","AR"]


def rewriter():
    sentence = str(input("Enter sentence: "))
    payload = f'text={sentence}&mode=fluent&lang=es&unique=true'
    return request_data("rewriter", payload)

def sentiment():
    sentence = str(input("Enter sentence: "))
    payload = f'text={sentence}'
    return request_data("sentiment", payload)

def article():
    url = str(input("Enter url: "))
    return request_data("article_extractor", f'url={url}')

def request_data(mode, sentence):
    option = {"article_extractor": 'text', "sentiment": 'sentiment', "rewriter" : 'rewrited'}
    url = f'https://app.plaraphy.com/api/{mode}'
    payload = sentence
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'authorization': 'Bearer 4384|fWTxx3UWJaMvKHNafY0VU3rT5hMYu1AiplM6YdZk',
        'cache-control': 'no-cache'
        }
    response = requests.request('POST', url, data=payload, headers=headers)
    value =  response.json()
    if value['success']:
        return value[option[mode]]
    else:
        return errormessage()


def errormessage():
    return "ERROR. TRY AGAIN"



if __name__ == "__main__":
    main()