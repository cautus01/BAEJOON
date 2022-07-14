#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int d[105][105];
const int INF = 9900005;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;

	for (int i = 1;i <= n;i++) {
		for (int j = 1;j <= n;j++) {
			d[i][j] = INF;
		}
	}
	for (int i = 1;i <= n;i++) {
		d[i][i] = 0;
	}
	for (int i = 0;i < m;i++) {
		int a, b, c;
		cin >> a >> b >> c;
		d[a][b] = min(d[a][b],c);
	}

	for (int k = 1;k <= n;k++) 
		for (int i = 1;i <= n;i++) 
			for (int j = 1;j <= n;j++) 
				d[i][j] = min(d[i][j], d[i][k]+d[k][j]);

	for (int i = 1;i <= n;i++) {
		for (int j = 1;j <= n;j++) {
			if (d[i][j] == INF) cout << "0 ";
			else cout << d[i][j] << " ";
		}
		cout << "\n";
	}
}