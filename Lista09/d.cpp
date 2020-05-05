#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using vi = vector<ll>;

int main() {
    int n;
	cin >> n;
	vi arr_a(n);
	for (ll &value : arr_a) {
		cin >> value;
	}

	map<ll, ll> count[2];
	count[0][0]++;
	int i = 0;
	ll firstIndex = 0LL, result = 0LL;
	for (ll value : arr_a) {
		firstIndex ^= value;
		result += count[1-i][firstIndex];
		count[1-i][firstIndex]++;
		i = 1 - i;
	}
	cout << result << endl;
}