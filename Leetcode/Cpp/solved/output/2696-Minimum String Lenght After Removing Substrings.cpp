class Solution {
public:
    int minLength(std::string s) {
        while (s.find("AB") != std::string::npos || s.find("CD") != std::string::npos) {
            size_t pos = s.find("AB");
            if (pos != std::string::npos) {
                s.erase(pos, 2);
            }
            pos = s.find("CD");
            if (pos != std::string::npos) {
                s.erase(pos, 2);
            }
        }
        return s.length();
    }
};