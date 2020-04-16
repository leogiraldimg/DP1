#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
#define sc(number) scanf("%d", &number)
#define sf scanf
#define pf printf
#define N 100005
typedef long long ll;
int arr_f[N];

int main() {
    string s;
    int n, k;
    while (scanf("%d%d", &n, &k) == 2) {
        cin >> s;

        memset(arr_f, 0, sizeof(arr_f));
        for (int i = 0; i < n; i++) {
            arr_f[s[i]-'A'] += 1;
        }

        sort(arr_f, arr_f + 26);
        reverse(arr_f, arr_f + 26);
        ll result = 0;

        for (int i = 0; i < 26; i++) {
            if (arr_f[i] == 0) {
                break;
            }

            if (k == 0) {
                break;
            }

            if (arr_f[i] >= k) {
                ll temp = k;
                result += (temp * temp);
                break;
            }
            else {
                ll temp = arr_f[i];
                result += (temp * temp);
                k -= arr_f[i];
            }
        }
        cout << result << endl;
    }
    return 0;
}