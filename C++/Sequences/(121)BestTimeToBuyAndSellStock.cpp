// Brute Force
// Time: O(n^2)
// Space: O(1)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int answer = 0;
        
        for (int i = 0; i < prices.size(); i++) {
            for (int j = i + 1; j < prices.size(); j++) {
                answer = max(answer, prices[j] - prices[i]);
            }
        }

        return answer;
    }
};

// One-pass
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 1)
            return 0;
        
        int mininum = prices[0];
        int answer = 0;
        
        for (int i = 1; i < prices.size(); i++) {
            if (mininum < prices[i])
                answer = max(answer, prices[i] - mininum);
            else
                mininum = prices[i];
        }

        return answer;
    }
};