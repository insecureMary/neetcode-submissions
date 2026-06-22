class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        # Loop through the string and encode (ex: 5#Hello5#World)
        for i in strs: 
            encoded_str += str(len(i)) + "#" + i 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s): 
            # Find the delim
            delim = s.find("#", i)
            # Find the length of the string (number before the delimiter and convert it to int -- it's a str in encoder)
            length = int(s[i:delim])
            # Extract the string (word)
            str_ = s[delim+1:delim+1+length]
            # Append it to the list
            decoded_str.append(str_)
            # Move the pointer
            i = delim + 1 + length 
        return decoded_str 