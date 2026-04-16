class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        
        Format: [length_of_string] + "#" + [string]
        """
        encoded_str = ""
        for s in strs:
            # Append the length, the delimiter, and then the string
            encoded_str += str(len(s)) + "#" + s
        
        # Example: ["neet", "code"] -> "4#neet4#code"
        return encoded_str
            

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded_list = []
        i = 0 # Our main pointer for the start of a new chunk

        while i < len(s):
            # 1. Find the delimiter '#' to get the length
            j = i # A second pointer to find the '#'
            while j < len(s) and s[j] != '#':
                j += 1
            
            # At this point, j is at the '#'.
            # The length is the string from i to j.
            length = int(s[i:j])
            
            # 2. Find the string itself
            # The string starts right after the '#' (at j + 1)
            # and lasts for 'length' characters
            start_of_string = j + 1
            end_of_string = start_of_string + length
            
            decoded_list.append(s[start_of_string : end_of_string])
            
            # 3. Update our main pointer 'i' to the start of the next chunk
            i = end_of_string
            
        return decoded_list