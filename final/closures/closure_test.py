def outerFunction():
    val = 10

    def innerFunction():
        # text += " Ravinuthala"
        inner_val = 20
        return val + 10

    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction

ifn = outerFunction()
print(ifn())
