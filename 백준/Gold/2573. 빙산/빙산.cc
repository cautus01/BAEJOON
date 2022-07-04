#include <iostream>
#include <queue>
#include <algorithm>
#define X first
#define Y second
using namespace std;

int n, m;
int ice[305][305];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int year=0;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> ice[i][j];
		}
	}
	while (true) {
		year++;
		bool vis[300][300];
		int ice_count = 0;
		for (int i = 0; i < n; i++) {
			fill(vis[i],vis[i] + m, 0);
		}
		int next_ice[300][300];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (ice[i][j] == 0) {
					next_ice[i][j] = 0;
					continue;
				}
				else {
					int count = 0;
					for (int k = 0; k < 4; k++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						if (nx < 0 || ny < 0 || nx >= n || ny >= m)
							continue;
						if (ice[nx][ny] == 0)
							count++;
					}
					next_ice[i][j]= (ice[i][j]-count > 0) ? ice[i][j] - count : 0;
				}
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (next_ice[i][j] != 0 && vis[i][j] == 0) {
					//
					queue<pair<int, int>> Q;
					Q.push({ i,j });
					vis[i][j] = 1;
					while (!Q.empty()) {
						pair<int, int> cur = Q.front(); Q.pop();
						for (int d = 0; d < 4; d++) {
							int nx = cur.X + dx[d];
							int ny = cur.Y + dy[d];
							if (nx < 0 || ny < 0 || nx >= n || ny >= m)
								continue;
							if (next_ice[nx][ny] == 0 || vis[nx][ny] == 1)
								continue;
							if (vis[nx][ny] == 0 && next_ice[nx][ny] != 0) {
								Q.push({ nx,ny });
								vis[nx][ny] = 1;
							}
						}
					}
					//
					ice_count++;
				}
			}
		}
		if (ice_count >= 2) {
			cout << year << '\n';
			break;
		}
		if (ice_count ==0) {
			cout << 0 << '\n';
			break;
		}

		for (int i = 0; i < n; i++) { // next_ice를 ice로 옮기기
			for (int j=0; j < m; j++) {
				ice[i][j] = next_ice[i][j];
			}
		}
	}
}