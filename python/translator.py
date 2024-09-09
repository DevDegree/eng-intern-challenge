braile_to_english_dict = {
    ""
}

def is_braile(str):
    if (str.length() % 6 == 0):
        return True
    return False

is_braile("helo")