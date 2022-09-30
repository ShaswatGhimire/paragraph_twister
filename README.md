# Paragraph Twister

## Video Demo:  https://youtu.be/iyrne0Ffd0s
&nbsp;

## Description
    A python program to perform:
    1. Rewriting of given sentences
    2. Sentiment extraction
    3. Article extraction from given url

    The project is done through api of: https://plaraphy.com/

### Files
    1. project.py
        In this file, the implementation of the project is done.
    2. test_project.py
        The test cases of functions of project.py file is written here.
    3. requirements.txt
        It contains packages to install for running this project.


### Components
#### 1. Rewriter
    It rewrites our given input sentences in a shorter keeping the meaning
    as it is. It is implemented through api request to url :
    url = https://app.plaraphy.com/api/rewriter

    And the json response then is extracted, error checked and displayed to the user.

#### 2. Sentiment Analysis
    It finds the emotional state of the sentence inputted by user.
    It performs sentiment analysis and outputs whether the result is positive, negative or other.
    API request url  = https://app.plaraphy.com/api/sentiment

#### 3. Article Extraction
    It extracts the article from a the webpage of given url.
    A url is given to the api request as input and it returns the articles of the webpage in text format.
    API request url = https://app.plaraphy.com/api/article_extractor

#### 4. Testing
    Testing of functions in the project i.e. project.py file is done.
    Various functions like errormessage(), valid(), request_data() is imported to test_project.py file
    and then testing is done under different functions namely starting from test_(function name).
    The testing of sentiment analysis is only done out of rewriter, sentiment analysis and article extraction
    as sentiment analysis is the only one which returns definitive output whereas other two returns somewhat
    dynamic output of pretty large output for testing using pytest.

Commands to Run in terminal:
```
python project.py
pytest test_project.py
```

