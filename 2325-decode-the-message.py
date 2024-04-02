class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        list_key = list(key.replace(" ", ""))
        list_uniq = list(dict.fromkeys(list_key))
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        result = ""
        for i, j in enumerate(message):
            if j == " ":
                result += " "
                continue
            old_index = list_uniq.index(j)
            new_letter = alphabet[old_index]
            old_letter = list_uniq[old_index]
            result += new_letter

        return result
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    decodeMessage(0, key, message)