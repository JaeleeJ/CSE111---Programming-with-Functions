# Jaelee Hutchinson
# Final Project
# Random Date Generator test functions
from attr import s
from RandomDateGenerator import dateIdeas, userInput
import pytest 

def test_dateIdeas():
    dates = dateIdeas()
    assert isinstance(dates, list), \
        "dateIdeas function must return a list:" \
        f" expected a list but found a {type(dates)}"

    assert dateIdeas()



def test_userInput():
    count = userInput()
    assert isinstance(count, int), \
        "userInput function must return an int:" \
        f" expected a list but found a {type(count)}"

    assert userInput()

    


pytest.main(["-v", "--tb=line", "-rN", __file__])