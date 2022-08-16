// Stack
// Time: O(n)
// Space: O(n)
class Solution {
public:
    bool isValid(string s) {
        stack<char> values;
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                values.push(s[i]);
            }
            else {
                if (values.size() == 0)
                    return false;
                if (s[i] == ')' && values.top() != '(')
                    return false;
                if (s[i] == '}' && values.top() != '{')
                    return false;
                if (s[i] == ']' && values.top() != '[')
                    return false;
                values.pop();
            }
        }
        
        return values.empty();
    }
};