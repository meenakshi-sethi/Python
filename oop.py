"""
COMPLETE LIBRARY MANAGEMENT SYSTEM - ALL OOP CONCEPTS INTEGRATED

This demonstrate how all OOP concepts work togther in a real - world system:
- Classes and Objects: foundational structure
- Encapsulation: Data protection and controlled access
- Polymorphism: Same interface, different behaviours
- Abstraction: Simple interface hiding complexity

This complete system shows how these concepts complements and enhance each other.
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from enum import Enum
import hashlib
import json
import uuid
from typing import List, Dict, Optional, Union

# CLASSES AND OBJECTS - Foundations

class LibraryConfig:
    """Configuration class - demonstrate basic class structure"""
    def __init__(self, name: str, max_books_per_member: int = 5):
        self.name = name
        self.max_books_per_member = max_books_per_member
        self.late_fee_per_day = 1.0
        self.max_renewal_count = 2
        self.borrowing_period_days = 14
        self.created_date = datetime.now()

    def __str__(self):
        return f"Library Config: {self.name}"
    
class Transaction:
    """Transaction class - demostrates objects with behavior"""
    transaction_counter = 0 # Class attribute

    def __init__(self, member_id:str, book_isbn: str, transaction_type: str):
        Transaction.transaction_counter += 1
        self.transaction_id = f"TXN-{Transaction.transaction_counter:06d}"
        self.member_id = member_id
        self.book_isbn = book_isbn
        self.transaction_type = transaction_type # Borrow, Return, Renew
        self.timestamp = datetime.now()
        self.processed_by = "SYSTEM"
        self.notes = ""

    def add_note(self, note: str):
        """Intance method to add notes"""
        self.notes += f"[{datetime.now().strftime("%Y-%m-%d %H:%M")}] {note}\n"
    
    def get_transaction_info(self):
        """Get formatted transaction information"""
        return {
            "id": self.transaction_id,
            "type": self.transaction_type,
            "member": self.member_id,
            "book": self.book_isbn,
            "date": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "processed_by": self.processed_by
        }

