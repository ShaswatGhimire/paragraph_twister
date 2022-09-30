from project import request_data, errormessage,valid
import requests

def test_errormessage():
    assert errormessage() == "ERROR. TRY AGAIN"

def test_valid():
    assert valid("RE") == True
    assert valid("Se") == True
    assert valid("aR") == True

    assert valid(" ")== False
    assert valid("cat") == False

def test_request_data():
    sentence = "I am happy but not as happy to jump from cliff"
    assert request_data("sentiment", f'text={sentence}') == "positive"

    sentence = "I am sad and i want to die"
    assert request_data("sentiment", f'text={sentence}') == "negative"





