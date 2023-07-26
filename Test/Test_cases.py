from moneycontrol import moneycontrol_api as mci
import json

test = mci.get_news()

if __name__ == "__main__":
    assert isinstance(json.loads(test), dict) != type(str), "Test Failed it should be json output in dict format"
    print("Test passed")
