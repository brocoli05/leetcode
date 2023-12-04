class Solution {
public:
    int compress(vector<char>& chars) {
        int cnt = 0;
        std::vector<char> temp;
        
        for (char c : chars) {
            // start a new character count
            if (temp.empty() || temp.back() != c) {
                // add the number of charcacter only when count is greater than 1
                if (cnt > 1) {
                    // convert the count to a string 
                    for (char digit : std::to_string(cnt)) {
                        temp.push_back(digit);
                    }
                }
                temp.push_back(c); // update the character into the temp
                cnt = 1; // reset the count
            } 
            else {
                cnt++; // count the number of the character
            }
        }
        
        // check if there is a count remaining
        if (cnt > 1) {
            // convert the count to a string 
            for (char digit : std::to_string(cnt)) {
                temp.push_back(digit);
            }
        }
        
        // update the original chars vector
        chars = temp;
        
        return temp.size();
    }
};