#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

#define X first
#define Y second
int v, e;
int k;

vector<pair<int, int>> adj[20005];
const int INF = 1e9;
int d[20005];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> v >> e;
	cin >> k; // 시작 정점
	fill(d, d + v + 1, INF);
	int a, b, c;
	for (int i = 0 ;i < e;i++) {
		cin >> a >> b >> c;
		adj[a].push_back({ c, b });
	}
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> PQ;
	d[k] = 0;
	PQ.push({ d[k],k });
	while (!PQ.empty()) {
		auto cur = PQ.top();PQ.pop(); // auto 조심
		if (d[cur.Y] < cur.X) continue;
		for (auto next : adj[cur.Y]) {
			int cost = d[cur.Y] + next.X;
			if (cost < d[next.Y]) {
				d[next.Y] = cost;
				PQ.push({ cost, next.Y });
			}
		}
	}
	for (int i = 1; i < v + 1;i++) {
		if (d[i] == INF) {
			cout << "INF" << "\n";
			continue;
		}
		cout << d[i] << "\n";
	}
}