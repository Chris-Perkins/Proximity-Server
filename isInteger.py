def isInt(s):
    print("HEY")
    try:
        int(s)
        print("true")
        return True
    except ValueError:
        print("false")
        return False