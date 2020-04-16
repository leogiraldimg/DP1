#include <cstdio>
#include <vector>

void calcula(const std::vector<std::vector<long> > &arr_g, long no, std::vector<bool> &visitado, long &ordenacao, long &tamanho) {
    if(visitado[no]) {
        return;
    }
    visitado[no] = true;
    ++ordenacao; tamanho += arr_g[no].size();
    for (long i = 0; i < arr_g[no].size(); i++){
        long ultramen = arr_g[no][i];
        if (visitado[ultramen]) {
            continue;
        }
        calcula(arr_g, ultramen, visitado, ordenacao, tamanho);
    }

    return;
}


int main() {
    long n, m; scanf("%ld %ld", &n, &m);
    std::vector<std::vector<long> > g(n + 1);
    for (long i = 0; i < m; i++) {
        long x, y; scanf("%ld %ld", &x, &y);
        g[x].push_back(y); g[y].push_back(x);
    }

    long contador(0);
    std::vector<bool> arr_bean(n + 1, 0);
    for (long i = 1; i <= n; i++) {
        if (arr_bean[i]) {
            continue;
        }
        long vvv = 0, eee = 0;
        calcula(g, i, arr_bean, vvv, eee);
        contador += (vvv > eee / 2);
    }

    printf("%ld\n", contador);

    return 0;
}