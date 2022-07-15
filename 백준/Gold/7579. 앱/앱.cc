#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int m[105];
int c[105];
int d[10005];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;
	for (int i = 1;i <= N;i++)
		cin >> m[i]; // i번째 앱의 메모리 크기
	for (int i = 1;i <= N;i++)
		cin >> c[i]; // i번째 앱의 비활성화 비용
	int sum_value = 0;

	for (int i = 1;i <= N;i++) {
		sum_value += c[i]; // 최대 비용
	}
	for (int i = 1;i <= N;i++) { 
		for (int j = sum_value; j >= c[i]; j--) { // 비용이 1 ~ sum_value
			if (c[i] > j) continue; // 갱신하지 않는다.
			else {
				d[j] = max(d[j], d[j - c[i]] + m[i]); // 갱신
			}
		}
	}
	for (int i = 1;i <= sum_value;i++) {
		if (d[i] >= M) {
			cout << i;
			break;
		}
	}
}