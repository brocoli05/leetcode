class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sIndex = 0;
        
        // Iterate through each character in string t
        for(char tChar : t){
            // If the current character in t matches the character in s at the current index
            if(tChar == s[sIndex]){
                sIndex++;
            }
        }
        
        return sIndex == s.size();
    }
};