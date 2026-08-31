from dataclasses import dataclass
@dataclass(unsafe_hash=True)
class Book:
    name: str
    
    
