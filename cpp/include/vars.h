#include <string>
#if _WIN64	
std::string GetImgFolder(char* argv[])
{
	std::string argv_str(argv[0]);
	std::string base = argv_str.substr(0, argv_str.find_last_of("cpp") - 3);
	return base + "\\images";
}	
#endif
