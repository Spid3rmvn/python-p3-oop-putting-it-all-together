#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, page_count):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The total number of pages in the book
        """
        self.title = title
        self.author = author
        self.page_count = page_count
        self.current_page = 1
        self.bookmark = None
    
    def turn_page(self):
        """
        Turn to the next page of the book.
        Increments current_page by 1 if not at the end of the book.
        """
        if self.current_page < self.page_count:
            self.current_page += 1
        return self.current_page
    
    def turn_back(self):
        """
        Turn back to the previous page of the book.
        Decrements current_page by 1 if not at the beginning of the book.
        """
        if self.current_page > 1:
            self.current_page -= 1
        return self.current_page
    
    def place_bookmark(self):
        """
        Place a bookmark at the current page.
        """
        self.bookmark = self.current_page
        return self.bookmark
    
    def remove_bookmark(self):
        """
        Remove the current bookmark.
        """
        self.bookmark = None
    
    def go_to_bookmark(self):
        """
        Go to the bookmarked page if one exists.
        """
        if self.bookmark:
            self.current_page = self.bookmark
        return self.current_page
    
    def go_to_page(self, page):
        """
        Go directly to the specified page if it's within the valid range.
        
        Args:
            page (int): The page to go to
        """
        if 1 <= page <= self.page_count:
            self.current_page = page
        return self.current_page
    
    def get_current_page(self):
        """
        Get the current page number.
        
        Returns:
            int: The current page number
        """
        return self.current_page
    
    def get_bookmark_page(self):
        """
        Get the bookmarked page number.
        
        Returns:
            int or None: The bookmarked page number or None if no bookmark is set
        """
        return self.bookmark
