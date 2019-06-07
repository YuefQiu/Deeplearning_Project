#include <iostream>
#include<windows.h>

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
	system("del testset\\*.*");
	system("del trainingset\\*.*");
	string paths[8] = { "#wmh\\0", "#wmh\\1", "#qyf\\0", "#qyf\\1", "#cyl\\0", "#cyl\\1", "#szy\\0", "#szy\\1" };
	int marks[8] = { 0, 1, 0, 1, 0, 1, 0 ,1 };
	FILE* tp, * trp;
	fopen_s(&tp, "testset\\#.txt", "w");
	fopen_s(&trp, "trainingset\\#.txt", "w");
	for (int k = 0; k < 8; k++) {
		string List[8192];
		string path;
		int len = 0, mark;
		char smark[2];
		path = paths[k];
		mark = marks[k];
		path += "\\";
		dir(path, List, &len);
		_itoa_s(mark, smark, 10);
		for (int i = 0; i < len; i++) {
			if (i % 50 == 0) {
				CopyFile((path + List[i]).c_str(), ("testset\\" + List[i]).c_str(), FALSE);
				fprintf(tp, (List[i] + " " + smark + "\n").c_str());
			}
			else {
				CopyFile((path + List[i]).c_str(), ("trainingset\\" + List[i]).c_str(), FALSE);
				fprintf(trp, (List[i] + " " + smark + "\n").c_str());
			}
		}
	}
	fclose(tp);
	fclose(trp);
	system("pause");
	return 0;
}