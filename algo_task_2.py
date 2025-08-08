from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if strings is None:
            raise ValueError("strings must not be None")
        if len(strings) == 0:
            return ""
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All items in strings must be str")

        for i, word in enumerate(strings):
            if word == "":
                return ""
            self.put(word, i)

        node = self.root
        lcp_chars = []
        while not node.is_end_of_word and len(node.children) == 1:
            (char, child), = node.children.items()
            lcp_chars.append(char)
            node = child

        return "".join(lcp_chars)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    print("LCP 1:", repr(trie.find_longest_common_word(strings)))

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    print("LCP 2:", repr(trie.find_longest_common_word(strings)))

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    print("LCP 3:", repr(trie.find_longest_common_word(strings)))