class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int maxArea = 0;
        
        // find the minimum and maximum elements in the height vector
        int left = 0;
        int right = height.size() - 1;

        while (left < right) {
            int h = std::min(height[left], height[right]);
            int w = right - left;
            
            // update maxArea if the calculated area is greater than the current maxArea
            maxArea = std::max(maxArea, h * w);
            
            // find the taller one
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
};