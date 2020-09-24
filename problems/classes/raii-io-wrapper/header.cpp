#include <string>
#include <vector>
#include <unordered_set>
#include <stdexcept>
#include <iostream>
#include <type_traits>

typedef int32_t handle_t;
const handle_t kNullHandle = -1;

void raw_write(handle_t handle, const std::string& content);
void raw_close(handle_t handle); 
