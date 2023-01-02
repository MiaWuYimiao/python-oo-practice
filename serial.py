"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start) :
        "initial a start number"
        self.start = start
        self.cur_number = start
    
    def generate(self) :
        "generate the next number based on current number"
        self.cur_number += 1
        return self.cur_number - 1

    def reset(self) :
        "reset the current number to the start number"
        self.cur_number = self.start
    



