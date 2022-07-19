#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		string path1, path2;
		bool output = true;
		cin >> path1 >> path2;
		for (int j = 0; j < n; j++) {
			if (path1[j] == path2[j] && path1[j] == '1') {
				output = 0;
				break;
			}
		}
		if (!output)
			cout << "NO\n";
		else
			cout << "YES\n";

	}

		return 0;
	}