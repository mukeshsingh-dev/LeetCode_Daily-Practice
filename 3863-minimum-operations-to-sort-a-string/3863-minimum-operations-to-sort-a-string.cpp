#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(string s) {
        int n = s.size();

        string target = s;
        sort(target.begin(), target.end());

        if (s == target) {
            return 0;
        }

        char minimumChar = target.front();
        char maximumChar = target.back();

        if (s.front() == minimumChar ||
            s.back() == maximumChar) {
            return 1;
        }

        bool minimumBeforeLast =
            s.find(minimumChar) < n - 1;

        bool maximumAfterFirst =
            s.rfind(maximumChar) > 0;

        if (minimumBeforeLast || maximumAfterFirst) {
            return 2;
        }

        if (n == 2) {
            return -1;
        }

        return 3;
    }
};