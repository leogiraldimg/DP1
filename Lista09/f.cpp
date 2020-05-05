#include<string>
typedef long long int ll;
using namespace std;

int main() {
    ll i;
    ll entrada,entrada2,t;
    ll num1,num2;

    scanf("%I64d%I64d%I64d",&entrada,&num1,&num2);

    t = entrada / num1;
    t += 1;
    for (i = 0; i <= t; i++) {
        entrada2 = i * num1;
        if((entrada - entrada2) % num2 == 0 && entrada - entrada2 >= 0) {
            printf("YES\n%I64d %I64d", i, (entrada-entrada2) / num2);
            return 0;
        }
    }

    printf("NO");

    return 0;
}