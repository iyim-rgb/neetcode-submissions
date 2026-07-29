class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"]
        encoded_string = "" 
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
            # "5#Hello5#World"

        return encoded_string # "5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        decoded_strs = [] # "10#0123456789|10#0123456789"
        i = 0
        j = i
    
        while j < len(s):
            while s[j] != "#":
                j += 1
            else:
                length = 0 if s[i:j] == "" else int(s[i:j])
                start = j + 1
                end = start + length

                decoded_strs.append(s[start:end])
                i = end
                j = i
 
        return decoded_strs