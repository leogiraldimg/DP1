#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <vector>
using namespace std;

set<int>Set;

int main(){
	int n,count,maximum = 0;
	cin >> n;
    int k = 0;
    while (k < n) {
        cin >> count;

		while (Set.count(count)){
            Set.erase(count);
            count++;
        }

        Set.insert(count);
		maximum = max(maximum,count);

        k++;
    }
    int setSize = Set.size();
	cout << maximum - setSize + 1 << endl;
    return 0;
}