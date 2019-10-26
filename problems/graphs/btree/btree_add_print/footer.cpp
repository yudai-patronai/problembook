#include <sstream>

int main()
{
	std::vector<int> data;
	data.reserve(10000);

	std::string input;
	std::getline(std::cin, input);
   	std::stringstream stream(input);
    while(1) 
    {
    	int num;
        stream >> num;
       	if(!stream)
        	break;

       data.push_back(num);
    }

    Tree myTree;
    for(auto &iter : data)
    	myTree.add(iter);

    myTree.print(NULL);
	
	return 0;
}
