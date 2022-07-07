#include <iostream>
using namespace std;

int a1, b1;
int a2, b2;
int A, B;

int gcd(int a, int b) {
	int n;

	while (b != 0) {
		n = a % b;
		a = b;
		b = n;
	}

	return a;
}
int lcm(int a, int b) {
	return a * b / gcd(a, b);
}
int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> a1 >> b1;
	cin >> a2 >> b2;

	A = a1 * b2 + a2 * b1;
	B = b1 * b2;

	cout << A / gcd(A, B) << " " << B / gcd(A, B);
	return 0;
}