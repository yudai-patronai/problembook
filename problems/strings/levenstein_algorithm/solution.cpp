#include <iostream>
#include <string>
#include <algorithm>


int levenstein_dist(const std::string& str1, const std::string& str2)
{
	int** matrix = new int*[str1.length() + 1];
	for (int i = 0; i <= str1.length(); i++) {
		matrix[i] = new int[str2.length() + 1];
		matrix[i][0] = i;
	}

	for (int i = 0; i <= str2.length(); i++)
		matrix[0][i] = i;


	for (int i = 1; i <= str1.length(); i++) {
		for (int j = 1; j <= str2.length(); j++) {
			matrix[i][j] = std::min(
				std::min(
					matrix[i][j - 1] + 1,
					matrix[i - 1][j] + 1
				),
				matrix[i - 1][j - 1] + ((str1[i - 1] == str2[j - 1]) ? 0 : 1)
			);
		}
	}

	int res = matrix[str1.length()][str2.length()];

	for (int i = 0; i <= str1.length(); i++)
		delete[] matrix[i];

	delete[] matrix;

	return res;
}

int main() {
	std::string str1;
	std::string str2;
	std::cin >> str1 >> str2;

	std::cout << levenstein_dist(str1, str2);

	return 0;
}
