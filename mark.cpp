#include <iostream>
#include <string>
#include <io.h>
#include<stdio.h>
using namespace std;
void dir(string path, string* List, int* len)
{
	long hFile = 0;
	struct _finddata_t fileInfo;
	string pathName, exdName;
	if ((hFile = _findfirst(pathName.assign(path).append("\\*.jpg").c_str(), &fileInfo)) == -1) {
		return;
	}
	do
	{
		List[(*len)++] = (string)fileInfo.name;
	} while (_findnext(hFile, &fileInfo) == 0);
	_findclose(hFile);
	return;
}
int main()
{
	string path, List[15360], str_, str0;
	int len = 0, mark, len0, index;
	char str[8], smark[2], txtname[32];
	FILE* fp;
	cout << "path:" << endl;
	cin >> path;
	cout << "mark:" << endl;
	cin >> mark;
	_itoa_s(mark, smark, 10);
	cout << "txtname:" << endl;
	cin >> txtname;
	cout << "start:" << endl;
	cin >> index;
	index *= 10000;
	strcat_s(txtname, 16, ".txt");
	path += "\\";
	fopen_s(&fp, (path + txtname).c_str(),"w");
	dir(path, List, &len);
	for (int i = 0; i < len; i++) {
		str0 = "";
		_itoa_s(index + i, str, 10);
		str_ = str;
		len0 = 5 - str_.size();
		for (int j = 0; j < len0; j++) str0 += "0";
		str_ = str0 + str_;
		rename((char*)(path + List[i]).c_str(), (path + str_ + "_" + smark + ".jpg").c_str());
		cout << List[i]+" -> "+ str_ + "_" + smark + ".jpg" << endl;
		fprintf(fp, (str_ + "_" + smark + ".jpg " + smark + "\n").c_str());
	}
	fclose(fp);
	system("pause");
	return 0;
}