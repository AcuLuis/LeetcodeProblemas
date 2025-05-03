#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> posiciones;
        for(int i = 0; i < nums.size(); i++) {
            for(int j = 0; j < nums.size(); j++) {
                if(i != j && nums[i] + nums[j] == target) {
                    auto it1 = find(posiciones.begin(), posiciones.end(), i);
                    auto it2 = find(posiciones.begin(), posiciones.end(), j);
                    if(it1 != posiciones.end()) break;
                    if(it2 != posiciones.end()) break;
                    posiciones.push_back(i);
                    posiciones.push_back(j);
                }
            }
        }
        return posiciones;
    }
};

int main() {
    Solution sol;
    vector<int> numeros = {2, 7, 11, 15};
    int objetivo = 9;
    vector<int> resultado = sol.twoSum(numeros, objetivo);
    cout << "Índices encontrados: ";
    for(int i : resultado) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

