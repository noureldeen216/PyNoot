# دي بترجعلك أي حاجة جوا الأوبجكت لو عايز تجيبها بالاسم بتاعها كسترينج

def لو(condition, action):
    if condition:
        action()

def لو_تاني(condition, action):
    if not getattr(لو_تاني, "already_matched", False) and condition:
        action()
        لو_تاني.already_matched = True

def وإلا(action):
    if not getattr(لو_تاني, "already_matched", False):
        action()
    لو_تاني.already_matched = False  # reset for next use