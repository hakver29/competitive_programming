#include <iostream>

int main(){
	int a,b;
	
	std::cin >> a >> b;

	if (a > b){
		std::cout << "MAGA!" << std::endl;
	} else if (a == b){
		std::cout << "WORLD WAR 3!" << std::endl;
	} else {
		std::cout << "FAKE NEWS!" << std::endl;
	}
	return 0;
}
