""" @title utils.py """

def safe_stoi(inp: str) -> (bool, int):
    """ @docstring
    @title
    converts string to integer, catching invalid strings

    @returns (is inp a valid int): bool, (int(inp)): int
    """
    try:
        # try to convert str to int
        outp = int(inp)
    except:
        # catches all exception

        # print("Wrong input format. Please try again.")
        return False, None
    
    return True, outp