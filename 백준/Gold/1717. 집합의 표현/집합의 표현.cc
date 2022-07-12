#include <iostream>
using namespace std;

int n, m;
int a, b, c;
int parent[1000005];

int find_parent(int x) {
	if (parent[x] != x)
		parent[x] = find_parent(parent[x]);
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
	for (int i = 0;i <= n;i++) parent[i] = i;

	for (int i = 0;i < m;i++) {
		cin >> a >> b >> c;
		if (a == 0) union_parent(b, c);
		else {
			if (find_parent(b) == find_parent(c))
				cout << "YES" << "\n";
			else
				cout << "NO" << "\n";
		}
	}
	return 0;
}