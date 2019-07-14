def get_element():
    """Tuples are accessed with brackets []. Using parentheses is always a function call and is thus incorrect."""
    t = ("Some", 4, True)
    print(t[1]) # 4

if __name__ == "__main__":
    get_element()