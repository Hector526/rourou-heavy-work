def country_goodWater(row):
    romanNum = row['前五项水质类别']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[romanNum] <= 3:
            return 1
        else:
            return 0
    except KeyError as e:
        pass


def country_expectedWater(row):
    source = row['前五项水质类别']
    expected = row['国考目标']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[source] <= romanSwitch[expected]:
            return 1
        else:
            return 0
    except KeyError as e:
        pass


def country_goodWater_yearOnyear(row):
    romanNum = row['同比（自动）']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[romanNum] <= 3:
            return 1
        else:
            return 0
    except KeyError as e:
        pass


def country_expectedWater_yearOnyear(row):
    source = row['同比（自动）']
    expected = row['国考目标']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[source] <= romanSwitch[expected]:
            return 1
        else:
            return 0
    except KeyError as e:
        pass


def country_goodWater_monthOnmonth(row):
    romanNum = row['环比（自动）']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[romanNum] <= 3:
            return 1
        else:
            return 0
    except KeyError as e:
        pass


def country_expectedWater_monthOnmonth(row):
    source = row['环比（自动）']
    expected = row['国考目标']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[source] <= romanSwitch[expected]:
            return 1
        else:
            return 0
    except KeyError as e:
        pass


def province_goodWater(row):
    romanNum = row['水质类别']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[romanNum] <= 3:
            return 1
        else:
            return 0
    except KeyError as e:
        pass


def province_expectedWater(row):
    source = row['水质类别']
    expected = row['水质目标']
    romanSwitch = {
        "I": 1,
        "Ⅱ": 2,
        "Ⅲ": 3,
        "Ⅳ": 4,
        "Ⅴ": 5,
        "劣Ⅴ": 6
    }
    try:
        if romanSwitch[source] <= romanSwitch[expected]:
            return 1
        else:
            return 0
    except KeyError as e:
        pass
