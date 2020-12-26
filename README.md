# TheDonald v 0.01

This project is used to access Donald Trump's Twitter Archive v2, search for particular tweets, and screenshot them.

Technologies used: PyCharm Comm Edition, Python, Selenium WebDriver

The project structure is very simple. All the tests are run from test_class.py, all test data contains in test_data.py

# How it works:

Initiates chrome driver in def __init__ function.
Navigate to URL and verifies if the navigation is successful in def test_navigation function.
Takes the keyword that is passed when class and method is called, and performs a search, stores search results in special variable, and starts parsing
all the tweets. While paring it verifies if each tweet contains the special keyword, and, if so, clicks "Show" button for the tweet and takes the screenshot of it.
All done in def test_enemy function


# How to run:

- Donwload the project.
- Adjust webdriver path in test_data.py file.
- Call TestClass directly from tes_class.py and specify all required functions.
- Run it

# Additional information:

During the automation process I've faced some issues with opening an additional window and going back and forth to the original Twitter website. And, as far as current archive implementation allows to open original tweet text right there, decided to use this functionality for completing the task.




Thanks,
Staincrazy, 
Jr Self-Taught Test Automation Engineer 




