// Hash Table
// Time: O(n)
// Space: O(n)
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> firstWord;
        map<char, int> secondWord;
        
        for (int i = 0; i < s.length(); i++) {
            if (firstWord[s[i]] != -1)
                firstWord[s[i]] = firstWord[s[i]] + 1;
            else
                firstWord[s[i]] = 1;
        }
        
        for (int i = 0; i < t.length(); i++) {
            if (secondWord[t[i]] != -1)
                secondWord[t[i]] = secondWord[t[i]] + 1;
            else
                secondWord[t[i]] = 1;
        }
        
        return firstWord == secondWord;
    }
};

// Sorting
// Time: O(nlogn)
// Space: O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        return s == t;
    }
};