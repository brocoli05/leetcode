class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int altitude = 0;
        int highest = 0;
        
        for(int netGain : gain){
            // netGain: difference between the current(i) and the next point(i+1)
            altitude += netGain;
            highest = std::max(highest, altitude);
        }
        
    return highest;
    }
};