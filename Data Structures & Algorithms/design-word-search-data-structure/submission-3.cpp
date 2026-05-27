class WordDictionary {
    struct TrieNode {
        array<TrieNode*, 26> children;
        bool is_word;
        TrieNode() : is_word(false) { children.fill(nullptr); };
    };
    TrieNode* root;

    bool search(string word, TrieNode* node) {
        for (int i = 0; i < word.size(); ++i) {
            char c = word[i];

            if (c == '.') {
                for (const auto& ch : node->children) {
                    if (ch && search(word.substr(i + 1), ch)) return true;
                }
                return false;
            } else {
                if (!node->children[c - 'a']) return false;
                node = node->children[c - 'a'];
            }
        }
        return node->is_word;
    }

   public:
    WordDictionary() { root = new TrieNode(); }

    void addWord(string word) {
        TrieNode* node = root;

        for (char c : word) {
            int i = c - 'a';
            if (!node->children[i]) node->children[i] = new TrieNode();
            node = node->children[i];
        }
        node->is_word = true;
    }

    bool search(string word) { return search(word, root); }
};