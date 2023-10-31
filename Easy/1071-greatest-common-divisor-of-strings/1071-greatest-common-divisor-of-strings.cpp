class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        string result{};
        if(str1 + str2 != str2 + str1){
            result = "";           
        }
        else{        
            size_t len1 = str1.length();
            size_t len2 = str2.length();
            
            while(len2 != 0){
                size_t temp = len2;
                len2 = len1 % len2;
                len1 = temp;
            }
            result = str1.substr(0, len1);
        }
        return result;
    }   
};