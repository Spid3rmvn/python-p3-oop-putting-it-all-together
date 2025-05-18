#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color, price=0, material="leather"):
        """
        Initialize a new Shoe instance.
        
        Args:
            brand (str): The brand of the shoe
            size (float): The shoe size
            color (str): The color of the shoe
            price (float, optional): The price of the shoe. Defaults to 0.
            material (str, optional): The material of the shoe. Defaults to "leather".
        """
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.material = material
        self.condition = "new"
        self.times_worn = 0
    
    def wear(self):
        """
        Wear the shoe, incrementing the times_worn counter and updating condition.
        
        Returns:
            str: The current condition of the shoe
        """
        self.times_worn += 1
        
        if self.times_worn > 30:
            self.condition = "worn out"
        elif self.times_worn > 15:
            self.condition = "used"
        elif self.times_worn > 5:
            self.condition = "lightly worn"
            
        return self.condition
    
    def clean(self):
        """
        Clean the shoe, potentially improving its condition.
        
        Returns:
            str: The current condition of the shoe
        """
        if self.condition == "lightly worn":
            self.condition = "new"
        elif self.condition == "used":
            self.condition = "lightly worn"
            
        return self.condition
    
    def polish(self):
        """
        Polish the shoe, improving its appearance.
        
        Returns:
            str: The current condition of the shoe
        """
        if self.material == "leather" and self.condition != "worn out":
            if self.condition == "used":
                self.condition = "lightly worn"
            elif self.condition == "lightly worn":
                self.condition = "new"
                
        return self.condition
    
    def get_info(self):
        """
        Get a formatted string with shoe information.
        
        Returns:
            str: A string containing shoe details
        """
        return f"{self.color} {self.brand} {self.material} shoe, size {self.size}, condition: {self.condition}"
    
    def get_condition(self):
        """
        Get the current condition of the shoe.
        
        Returns:
            str: The current condition
        """
        return self.condition
    
    def set_price(self, new_price):
        """
        Set a new price for the shoe.
        
        Args:
            new_price (float): The new price
            
        Returns:
            float: The updated price
        """
        self.price = new_price
        return self.price
