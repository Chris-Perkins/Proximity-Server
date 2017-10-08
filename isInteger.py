def isInt(s):
    print("HEY")
    try:
        int(s)
        return True
    except ValueError:
        return False