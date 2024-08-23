class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        specialChars = "!@#$%^&*()-+"
        prevChar = ""
        lower = False
        upper = False
        digit = False
        special = False
        subsequent = False

        for character in password:
            if character.islower():
                lower = True
            elif character.isupper():
                upper = True
            elif character.isdigit():
                digit = True
            elif character in specialChars:
                special = True
            elif subsequent == character:
                subsequent = True
            
            subsequent = character
         
        if lower and upper and digit and special and not subsequent:
            print("F")
            return True
        else:
            return False

    password = "1aB!"
    strongPasswordCheckerII(0, password)