import math

def solveQuadratic(a, b, c):
    """Solves a quadratic expression for the given constants
    
    :Parameters:
        - 'a, b, c': The constants in the expression ax^2 + bx + c = 0
    
    :Returns:
        A list of 2 solutions
        ["NONE", solution] if a is 0 (linear equation)
        ["NONE", "NONE"] if no real solutions exist (will never find complex solutions)
    
    :Examples:
    >>> from pygraph.utility.MoreMath import solveQuadratic
    >>> solveQuadratic(1, -2, 1) # [1.0, 1.0]
    >>> solveQuadratic(0, 2, -4) # ["NONE", 2.0]
    """
    assert(b != 0 or a != 0, "Expression received of the type 0x^2 + 0x + c = 0")

    if (a == 0.0): return ["NONE", -c/float(b)]

    desc = b*b - 4 * a * c
    if (desc < 0.0): return ["NONE", "NONE"]

    sqrt_desc = math.sqrt(desc)
    return [(-b + sqrt_desc)/(2.0 * a), (-b - sqrt_desc)/(2.0 * a)]
