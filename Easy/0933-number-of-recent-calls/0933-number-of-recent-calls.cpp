class RecentCounter {
private:
    std::vector<int> requests;
public:
    RecentCounter() {
        
    }
    
    int ping(int t) {
        requests.push_back(t);
        while(!requests.empty() && requests.front() < t - 3000){
            requests.erase(requests.begin());
        }
        return requests.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */