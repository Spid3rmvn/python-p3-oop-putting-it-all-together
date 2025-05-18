#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        """
        Initialize a new Shoe instance.

        Args:
            brand (str): The brand of the shoe
            size (int): The shoe size
        """
        self.brand = brand
        self._size = None  # Initialize with None
        self.size = size  # Use the setter

        # Initialize condition
        self.condition = "Old"
    
    @property
    def size(self):
        """Getter for size"""
        return self._size
    
    @size.setter
    def size(self, value):
        """
        Setter for size that validates the value is an integer.
        
        Args:
            value: The value to set size to
        """
        if not isinstance(value, int):
            print("size must be an integer")
        self._size = value

    def cobble(self):
        """
        Repair the shoe, setting its condition to 'New'.
        """
        print("Your shoe is as good as new!")
        self.condition = "New"
