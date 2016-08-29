class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_offset, max_pat, last_dup = {}, 0, -1
        # word_offset: dictionary for word and its last position
        # max_pat: max pattern
        # last_dup: last position for duplicate word
        for idx, ch in enumerate(s):
            if ch in word_offset and word_offset[ch] > last_dup:
                last_dup = word_offset[ch]
            pat = idx - last_dup
            if pat > max_pat:
                max_pat = pat
            word_offset[ch] = idx

        return max_pat
