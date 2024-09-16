from .getinput import getinput

def getyesno(prompt: str = "Enter [Y]es to continue. Press [Enter] or enter [N]o to cancel.", skip_on_empty = True, empty_default_val = True):
    userinput = getinput(prompt, strip=True, lower=True, allow_empty=True)

    if not userinput:
        if skip_on_empty:
            return False
        else:
            return empty_default_val

    return userinput == "y" or userinput == "yes"