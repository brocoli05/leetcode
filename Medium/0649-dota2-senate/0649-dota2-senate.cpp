class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> radiant, dire;
        int n = senate.size();
        
        // populate queues for Radiant and Dire senators
        for(int i = 0; i < n; i++){
            if(senate[i] == 'R'){
                radiant.push(i);
            }
            else{
                dire.push(i);
            }        
        }
        
        while(!radiant.empty() && !dire.empty()){
            // retrieves the front indices of both queues
            int radiantIndex = radiant.front();
            int direIndex = dire.front();
            
            // removes them from the queues
            radiant.pop();
            dire.pop();
            
            if(radiantIndex < direIndex){
                radiant.push(radiantIndex + n);
            }
            else{
                dire.push(direIndex + n);
            }
        }        
        return radiant.empty() ? "Dire" : "Radiant";
    }
};