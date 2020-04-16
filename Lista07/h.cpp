#include<bits/stdc++.h>
using namespace std;

#define ll unsigned long long

ll n;
ll arr_a[105], arr_dp[105][105], direct[105];

ll cabecaDeGelo(ll lol, ll contador){
    if(arr_dp[lol][contador] != -1)
        return arr_dp[lol][contador];

    if(contador == n)
        return 1;

    ll maxi = 0;

    for(ll i = 0; i < n; i++){
        if((arr_a[i]*3==arr_a[lol]) || (arr_a[lol]*2==arr_a[i]) ) {

            int tmp= cabecaDeGelo(i,contador+1);

            if(tmp>maxi){
                maxi=tmp;
                direct[lol]= i;
            }
        }
    }



    return arr_dp[lol][contador] = maxi;


}

void resolvePo(ll inicio){
    if (direct[inicio] == -1) {
        return;
    }

    cout<<" "<<arr_a[direct[inicio]];
    resolvePo(direct[inicio]);

}

main(){
    ll feladap, inicio;
    cin>>n;
    memset(arr_dp, -1, sizeof arr_dp);
    memset(direct, -1, sizeof direct);
    for(ll i = 0; i < n; i++)
        cin>>arr_a[i];

    for(ll i = 0; i < n; i++){
        feladap=cabecaDeGelo(i, 1);
        if(feladap == 1){
            inicio = i;
            break;
        }
    }

    cout<<arr_a[inicio];
    resolvePo(inicio);

    puts("");
}