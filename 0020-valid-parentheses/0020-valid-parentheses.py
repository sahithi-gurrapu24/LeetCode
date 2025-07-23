class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top = st.pop() if st else '#'
                if mapping[char] != top:
                    return False
            else:
                st.append(char)

        return not st
