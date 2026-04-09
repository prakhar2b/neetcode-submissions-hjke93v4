class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        window = set()
        l, cur_len, max_so_far = 0, 0, 0
        for r in range(len(s)):
            if s[r] in window:
                while s[r] in window:
                    window.remove(s[l])
                    l = l+1
                window.add(s[r])
                cur_len = r-l+1
                max_so_far = max(max_so_far, cur_len)
            else:
                window.add(s[r])
                cur_len = r-l+1
                max_so_far = max(max_so_far, cur_len)
            print(window)
            print(r, cur_len, max_so_far)

        return max_so_far
                
