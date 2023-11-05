class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        int size = flowerbed.size();
        
        for(int i = 0; i < size; i++){
            //check if the current position is empty
            if(flowerbed[i] == 0){ 
                // 0 if at the beginning
                int prev = (i == 0) ? 0 : flowerbed[i-1];
                
                // 0 if at the end
                int next = (i == size - 1) ? 0 : flowerbed[i+1];
                
                if(prev == 0 && next == 0){
                    //place a flower
                    flowerbed[i] = 1;
                    count++;
                }
            }
        }
        //Check if the count of placed flowers is greater than or equal to the desired number (n)
        return (n <= count);
    }
};