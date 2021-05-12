#include <bits/stdc++.h>

using namespace std;

void stringTransform(string& s, char a_, char b_, char c_) {
	for (char& c : s) {
		if (c == 'A')
			c = a_;
		if (c == 'B')
			c = b_;
		if (c == 'C')
			c = c_;
	}
}

int main()
{
	int t;
	cin >> t;
	while (t--) {
		string a;
		cin >> a;

		string s[8];
		for (string& stri : s)
			stri = a;

		stringTransform(s[0], '(', '(', ')');
		stringTransform(s[1], '(', ')', ')');
		stringTransform(s[2], '(', ')', '(');
		stringTransform(s[3], '(', '(', '(');
		stringTransform(s[4], ')', '(', ')');
		stringTransform(s[5], ')', ')', ')');
		stringTransform(s[6], ')', ')', '(');
		stringTransform(s[7], ')', '(', '(');

		bool out = false;
		for (string i : s) {
			int count1(0);
			int count2(0);
			out = false;
			for (char x : i) {
				if (x == '(')
					count1++;
				else
					count2++;
				if (count2 > count1)
					break;

			}
			if (count1 == count2)
				out = true;
			if (out) {
				cout << "YES"<< endl;
				break;
			}
		}
		if (!out)
			cout << "NO"<< endl;
	}
}