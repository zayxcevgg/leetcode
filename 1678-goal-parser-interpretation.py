class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(", "").replace(")", "")
    
    command = "G()(al)"
    interpret(0, command)