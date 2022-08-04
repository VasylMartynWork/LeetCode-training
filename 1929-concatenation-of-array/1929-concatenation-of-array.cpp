#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::cin;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> res;
        int j = 0;
        while (j < 2) {
            for (int i = 0; i < size(nums); i++) {
                res.push_back(nums[i]);
            }
            j++;
        }
        return res;
    }
};