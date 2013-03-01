class LSystem:
    """A class that instantiates an Lsystem, which can be used to generate graphics or simply grammars
    
    :Methods:
        - 'addRule': Adds a new production rule to the L-System, and computes it's probability
        - 'generate': Expands a starting symbol multiple iterations, returning the resulting symbol list
        - 'expand': Expands a symbol. generate will call this multiple times iteratively
        - 'setRasterFunction': Associates a function pointer with a symbol. Functions 'implement' each symbol
        - 'rasterize': Goes through the given symbol list and calls the function for each symbol
    
    :Examples:
    >>> from pygraph.generate.LSystem import LSystem
    >>> lsys = LSystem()
    >>> lsys.addRule('A', ['B', 'i']) # upper case is a Symbol that can expand, lowercase is a constant that cannot expand
    >>> lsys.addRule('A', ['i', 'B', 'i']) # A now 50% generates Bi, and 50% Generates iCi
    >>> lsys.addRule('A', ['i', 'B']) # A now has 33% chance of any
    >>> lsys.addRule('B', ['j', 'A'], 6) # This is like adding the rule 6 times regarding probability. It is 6 times more likely than other rules
    >>> lsys.addRule('B', ['i']) # This has a 1/7 chance, the first one has a 6/7 chance
    >>> lsys.setRasterFunction('i', drawLeaf) # Assign the draw leaf function to i
    >>> lsys.setRasterFunction('j', drawBranch) # Extends the branch of a tree
    >>> lsys.setRasterFunction('A', drawLeaf) # Any undeveloped A symbols will be leaves
    >>> lsys.setRasterFunction('B', drawLeaf) # Any undeveloped B symbols will be leaves
    >>> generated = lsys.generate(['j', 'j', 'B'], 7) # Generate a list of symbols. Note that we didn't add any symbols for rotation, so this is more of a theoretical example
    >>> lsys.rasterize(generated) # Calls the functions, which would presumably draw a tree if we had rotations and a stack implemented (use symbols to push and pop from a stack)
    """
    
    def __init__(self):
        self.rules = {}
        self.raster_functions = {}

    def addRule(self, symbol, product_list, factor=1):
        product_index = 0
        if (symbol in self.rules):
            product = filter(lambda x: x[1][1:] == product_list, enumerate(self.rules[symbol])) # returns tuple(index_in_list_of_lists_of_symbols, [symbols_of_product])
            if (product):
                self.rules[symbol][product[0][0]][0] += factor
            else:
                self.rules[symbol].append([factor] + product_list)
        else:
            self.rules[symbol] = [[factor] + product_list]

    def expand(self, symbol_list):
        pass

    def generate(self, symbol_list, depth):
        pass

    def setRasterFunction(self, symbol, raster_function):
        pass

    def rasterize(self, symbol_list):
        pass
