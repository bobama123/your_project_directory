from lib.gratitudes import *

def test__for_all_gratitude_given():
    gratitudes = Gratitudes()
    gratitudes.add("Food")
    gratitudes.add("Money")
    gratitudes.add("Water")
    result = gratitudes.format()
    assert result == "Be grateful for: Food, Money, Water"


def test__for_all_gratitude_given():
    gratitudes = Gratitudes()
    gratitudes.add("")
    result = gratitudes.format()
    assert result == "Be grateful for: "