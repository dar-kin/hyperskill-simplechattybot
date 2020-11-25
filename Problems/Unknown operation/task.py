def solve():
    test = "This is test string"
    a = hidden_operation(test)
    operation = ""
    hidden = ""
    if a == test:
        operation = "or"
        hidden = hidden_operation(False)
    else:
        a = hidden_operation(False)
        if a:
            operation = "not"
        else:
            operation = "and"
            hidden = hidden_operation(True)
    print(operation)
    if operation != "not":
        print(hidden)
