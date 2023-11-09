class Solution {
public:
    string reverseWords(string s) {
        vector<string> tokens;
        stringstream line(s);
        string newline{};
        
        // tokenize the string by space and store each word in tokens
        while(line >> newline){ // getline(line, newline, ' ')
            tokens.push_back(newline);
        }
        
        string reversed{};
        // reverse the order of words
        for(int i = tokens.size() - 1; i >= 0; i--){
            reversed += tokens[i]; 
            // add space between words
            if(i > 0){
                reversed += ' ';
            }
        }
        return reversed;
    }
};