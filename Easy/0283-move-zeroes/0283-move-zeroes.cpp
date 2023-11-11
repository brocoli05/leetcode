class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        vector<int> temp;
        int count = 0;
        
        for(auto& num : nums){
            if(num != 0){
                temp.push_back(num);
            }
            else{
                count++;
            }            
        }
        
        for(int i = 0; i < count; i++){
            temp.push_back(0);
        }
        nums = temp;
    }
};