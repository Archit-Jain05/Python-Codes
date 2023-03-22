def week(n):
    switcher={
        0:"Monday",
        1:"tueseday"

    }
    return switcher.get(n,"Invalid NUm")

print(week(0))