// Time: O(n)
// Space: O(1)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        
        answer.push_back(1);
        
        for (int i = 1; i < nums.size(); i++) {
            answer.push_back(nums[i-1] * answer[i-1]);
        }
        
        int right = 1;
        
        for (int i = nums.size() - 1; i >= 0; i--) {
            answer[i] = answer[i] * right;
            right *= nums[i];
        }
        
        return answer;
    }
};