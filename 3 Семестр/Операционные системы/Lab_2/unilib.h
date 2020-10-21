#ifndef LAB_2_1_UNILIB_H
#define LAB_2_1_UNILIB_H


#include <string.h>
#include <vector>
#include <string>

std::vector<std::string> split(std::string s, std::string delimiter = "!");

std::string GetStdoutFromCommand(std::string cmd);

#endif //LAB_2_1_UNILIB_H
