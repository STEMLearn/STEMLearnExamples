import random 

class TutorialModels:
    def __init__(self):
        pass

    @staticmethod
    def our_first_model(prank_type: str):
        """Predicts Pranker using only prank type"""
        
        # If prank is misinformation, we predict culprit is rob
        if prank_type == "misinformation":
            return "rob"
         
        # Otherwise, we guess randomly
        else:
            return ["bill", "martha"][random.randint(0,1)]

    @staticmethod
    def our_second_model(prank_type: str, damage: int):
        """Predicts Pranker using Prank Type and Damage"""
        
        # If prank is misinformation, we predict culprit is rob
        if prank_type == "misinformation":
            return "rob"
            
        # Otherwise, predict Bill if damage > 4, Martha if not
        else:
            if damage > 4:
                return "bill"
            else:
                return "martha"
    