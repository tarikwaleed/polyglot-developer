def _private(n):
    """
    this function is not going to be imported in another module if you did `import *`
    but it's going to be imported if you imported it by its name
    """
    return n * 10


def public(n):
    return n * 10
