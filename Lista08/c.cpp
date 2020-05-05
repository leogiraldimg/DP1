#include "iostream";
#include "vector";
using namespace std;
const int MAX=2e5+10;
vector<int> arr_g[MAX];
bool sinalizador,arr_bool[MAX];

void calcula(int number) {
    arr_bool[number] = 1;

    if (arr_g[number].size() != 2) {
        sinalizador=0;
    }

    for (int i = 0; i< arr_g[number].size(); i++) {
        if (!arr_bool[arr_g[number][i]]) {
            calcula(arr_g[number][i]);
        }
    }
}

int main() {
    int n = 0;
    int m = 0;
    int u = 0;
    int v = 0;
    int result = 0;

    cin>>n>>m;
    
    for (int i = 0; i < MAX; i++) {
        arr_g[i].clear();
    }

    for (int i = 0; i < m; i++){
        cin>>u>>v;

        arr_g[u].push_back(v);
        arr_g[v].push_back(u);
    }

    for(int i = 1; i <= n;i++){
        sinalizador = 1;
        if (!arr_bool[i]){
            calcula(i);
            if(sinalizador) {
                result++;
            }
        }
    }
    cout<<result<<endl;
    return 0;
}