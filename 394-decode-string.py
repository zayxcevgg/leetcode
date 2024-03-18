class Solution:
    def decodeString(self, s: str) -> str:
        multiplier = 0
        decodedStack = []
        string = ''
        for character in s:
            if character.isdigit():
                multiplier = multiplier*10 + int(character)
            elif character == "[":
                decodedStack.append(string)
                decodedStack.append(multiplier)
                string = ''
                multiplier = 0
            elif character.isalpha():
                string += character    
            elif character == "]":
                pre_num = decodedStack.pop()
                pre_string = decodedStack.pop()
                string = pre_string + pre_num * string
        return string

    
    s = "3[a]2[bc]"
    decodeString(0, s)
                

                