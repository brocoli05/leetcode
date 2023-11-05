class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        //find the maximum number of candies in the vector
        int maxCandies = *max_element(candies.begin(), candies.end());
        
        //initialize a vector result to store boolean values
        vector<bool> result;

        for (int i = 0; i < candies.size(); i++) {
            //If the child's candies + the extra candies are greater than or equal to the maximum candies, push true to the result vector
            result.push_back(candies[i] + extraCandies >= maxCandies);
        }

        return result;
        }
};