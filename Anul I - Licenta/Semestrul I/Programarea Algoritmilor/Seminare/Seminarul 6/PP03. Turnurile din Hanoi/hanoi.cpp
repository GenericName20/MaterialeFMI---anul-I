// https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1?itm_source=geeksforgeeks

class Solution {
  public:
    int towerOfHanoi(int n, int from, int to, int aux) {
        if (n == 0)
            return 0;
        else
        {
            return 1 + towerOfHanoi(n - 1, to, aux, from)
                     + towerOfHanoi(n - 1, aux, to, from);
        }
    }
};