#include <iostream>
#include <tuple>
#include <algorithm>
using namespace std;

int n, m;
tuple<int, int, int> edges[100005];
int parent[1005];

int find_parent(int x) {
	if (parent[x] != x) parent[x] = find_parent(parent[x]);
	return parent[x];
}

void union_parent(int a, int b) {
	a = find_parent(a);
	b = find_parent(b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 1;i < n + 1;i++) {
		parent[i] = i;
	}
	for (int i = 0;i < m;i++) {
		int a, b, cost;
		cin >> a >> b >> cost;
		edges[i] = { cost,a,b };
	}
	sort(edges, edges + m);
	int cnt = 0;
	int result = 0; // 정수의 범위 생각

	for (int i = 0;i < m;i++) {
		int a, b, cost;
		tie(cost, a, b) = edges[i];
		if (find_parent(a) != find_parent(b)) {
			result += cost;
			union_parent(a, b);
			cnt++;
			if (cnt == n - 1) break;
		}
	}
	cout << result;
}