#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n,m;
int a, b;
vector<int> adj[100005];
int parent[18][100005];
int depth[100005];

int LCA(int a, int b);

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1;i < n;i++) {
		cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	for (int i = 1;i <= n;i++) depth[i] = -1;
	queue<int> Q;
	Q.push(1);
	depth[1] = 0;
	while (!Q.empty()) {
		int cur = Q.front();Q.pop();
		for (int next : adj[cur]) {
			if (depth[next] == -1) {
				Q.push(next);
				depth[next] = depth[cur] + 1;
				parent[0][next] = cur;
			}
		}
	}
	for (int r = 1;r < 18;r++) {
		for (int c = 1;c <= n;c++) {
			parent[r][c] = parent[r - 1][parent[r - 1][c]];
		}
	}
	cin >> m;
	for (int i = 0;i < m; i++) {
		cin >> a >> b;
		cout << LCA(a, b) << "\n";
	}
	return 0;
}

int LCA(int a, int b) {
	if (depth[a] < depth[b]) {
		int tmp = a;
		a = b;
		b = tmp;
	}
	int diff = depth[a] - depth[b];
	for (int r = 0;diff > 0;r++) {
		if (diff & 1) {
			a = parent[r][a];
		}
		diff >>= 1;
	}
	while (a != b) {
		int r;
		for (r = 0;r < 18;r++) {
			if (parent[r][a] == parent[r][b]) break;
		}
		if (r > 0) --r;
		a = parent[r][a];
		b = parent[r][b];
	}
	return a;
}