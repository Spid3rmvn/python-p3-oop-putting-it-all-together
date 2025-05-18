#!/usr/bin/env python3


class Book:
    def __init__(self, title, page_count):
        """
        Initialize a new Book instance.

        Args:
            title (str): The title of the book
            page_count (int): The total number of pages in the book
        """
        self.title = title
        self._page_count = None  # Initialize with None
        self.page_count = page_count  # Use the setter
    
    @property
    def page_count(self):
        """Getter for page_count"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """
        Setter for page_count that validates the value is an integer.
        
        Args:
            value: The value to set page_count to
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        """
        Turn to the next page of the book.
        Outputs a message about flipping the page.
        """
        print("Flipping the page...wow, you read fast!")
