#include <cstdlib>
#include <iostream>
#include <Windows.h>
#pragma comment(lib, "Shell32.lib")

int main() {

    ShowWindow(GetConsoleWindow(), SW_SHOW);
    system("cd venv/Scripts/");
    system("start /venv/Scripts/activate.bat");
    system("python main.py" );

    return 0;
}