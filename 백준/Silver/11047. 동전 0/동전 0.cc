#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <string.h>
using namespace std;

// main
int main(){
    int N, K;
    int coin = 0;
    scanf("%d %d", &N, &K);
    vector<int> coin_vec(N, 0);
    for ( int n_idx = 0 ; n_idx < N; n_idx++)
        scanf("%d", &(coin_vec.at(n_idx)));

    sort(coin_vec.begin(), coin_vec.end(), greater<int>());

    auto coin_iter = coin_vec.begin();
    while(K){
        int now_coin_num = K/(*coin_iter);
        if(now_coin_num) coin += now_coin_num;
        K = K - now_coin_num*(*coin_iter);
        coin_iter++;
    }

    cout << coin;

    return 0;
}