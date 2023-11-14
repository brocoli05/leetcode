class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX;
        int second = INT_MAX;
        bool res = false;
        
        for(int num : nums){
            if(num <= first){
                first = num; // update the smallest
            }
            else if(num <= second){
                second = num; // update the smallest
            }
            else{
                res = true;
            }
        }
        
        return res;
    }
};