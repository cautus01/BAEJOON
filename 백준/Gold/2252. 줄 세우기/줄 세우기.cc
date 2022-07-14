#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
vector<int> adj[32005];
int d[32005];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	int a, b;
	for (int i = 0;i < m;i++) {
		cin >> a >> b;
		adj[a].push_back(b);
		d[b]++;
	}
	queue<int> Q;

	for (int i = 1;i <= n;i++) {
		if (d[i] == 0)
			Q.push(i);
	}
	while (!Q.empty()) {
		int x = Q.front();Q.pop();
		cout << x << " ";
		for (int next : adj[x]) {
			d[next]--;
			if (d[next] == 0) Q.push(next);
		}
	}
}