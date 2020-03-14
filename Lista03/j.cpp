#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

#define ll long long

int main(void) {
	vector<ll>arr_v;
	ll n, k;
	cin >> n >> k;

	for (int j = 1; j <= sqrt(n); j++) {
		if (n % j == 0) {
			ll temp = n / j;
			arr_v.push_back(j);
			if (temp != j) {
                arr_v.push_back(temp);
            }
		}
	}
	sort(arr_v.begin(), arr_v.end());

	if (k > arr_v.size()) {
        cout << -1;
    }
	else cout << arr_v[k-1];
	return 0;
}