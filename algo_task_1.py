from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")
        
        def dfs(node, current_word):
            count = 0
            if node.is_end_of_word and current_word.endswith(pattern):
                count += 1
            for char, child in node.children.items():
                count += dfs(child, current_word + char)
            return count
        
        return dfs(self.root, "")
    
    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

# Вивід
print(trie.count_words_with_suffix("e"))    # Очікується 1
print(trie.count_words_with_suffix("ion"))  # Очікується 1
print(trie.count_words_with_suffix("a"))    # Очікується 1
print(trie.count_words_with_suffix("at"))   # Очікується 1

print(trie.has_prefix("app"))  # Очікується True
print(trie.has_prefix("bat"))  # Очікується False
print(trie.has_prefix("ban"))  # Очікується True
print(trie.has_prefix("ca"))   # Очікується True
