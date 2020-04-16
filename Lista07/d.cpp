#include<bits/stdc++.h>
typedef long long int ll;
#define inf 1000000000000000
using namespace std;
struct no {
    ll em, custo;

    no(ll where, ll price) {
        em = where;
        custo = price;
    }
};


struct topo {
    ll temp1, temp2;
    topo (ll tempa, ll tempb) {
        temp2 = tempa;
        temp1 = tempb;
    }
};

bool operator<(no a, no b) {
    return a.custo > b.custo;
}

ll n,m;
ll range[100010];
vector<topo> adj[100010];
map<ll,ll> path;
priority_queue<no> pq;

void dijkstra (ll s) {
    for (int i = 0; i <= n; i++) {
        range[i] = inf;
    }

    range[s] = 0;
    pq.push(no(s,range[s]));

    while (!pq.empty()) {
        no u = pq.top();
        pq.pop();

        if (u.custo != range[u.em]) {
            continue;
        }

        for(topo e : adj[u.em]) {
            if (range[e.temp2] > u.custo+e.temp1) {
                range[e.temp2] = u.custo+e.temp1;
                path[e.temp2] = u.em;
                pq.push(no(e.temp2,range[e.temp2]));
            }
        }
    }

}

int main() {
    ll i;
    ll j;
    ll k;
    ll s;
    ll e;
    ll w;

    cin>>n>>m;

    for (i = 1; i <= m; i++) {
        cin>>s>>e>>w;

        adj[e].push_back(topo(s,w));
        adj[s].push_back(topo(e,w));
    }

    for (i = 1; i <= n; i++) {
        path[i] = -7;
    }

    dijkstra(1);

    ll koiAsi = n;
    vector<ll> rasta;
    map<ll,bool> vis;
    bool ff = true;

    for (i = 1; i <= n; i++) {
        vis[i] = false;
    }

    path[1]=1;
    while(true) {
        if (path[koiAsi] >= 1 && path[koiAsi] < n && vis[koiAsi] == false) {
            rasta.push_back(koiAsi);
            vis[koiAsi] = true;
            koiAsi = path[koiAsi];
        }
        else {
            break;
        }
    }

    if(range[n] == inf) {
        cout<<"-1 "<<endl;
        return 0;
    }

    ll x=rasta.size();
    for (i = x-1; i >= 0; i--) {
        cout<<rasta[i]<<" ";
    }

    return 0;
}