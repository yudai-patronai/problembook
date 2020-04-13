void fixlocptr(Level_t* old, Level_t* dup) {
    std::ptrdiff_t diff = &(dup->locations[0]) - &(old->locations[0]);
    for (auto& one: dup->locations) {
        if (one.up != nullptr)     one.up += diff;
        if (one.left != nullptr)   one.left += diff;
        if (one.right != nullptr)  one.right += diff;
        if (one.down != nullptr)   one.down += diff;
    }
}

int main() {
    Level_t original;
    original.load_level();
    // bad students can modify level, so we will give them the copy
    Level_t duplicate(original);

    fixlocptr(&original, &duplicate);

    Location_t *start_point = duplicate.get_location_pointer(duplicate.start_point_index);
    // Student's code is called here:
    Location_t *end_point = find_medical_center(start_point);

    if (!end_point) {
        std::cout << "NO\n";
        std::cerr << "nullptr is reached. Bad for you!\n";
        return 1;
    }
    int index = duplicate.get_location_index(end_point);

    if (index == -1) {
        std::cout << "NO\n";
        std::cerr << "Unknown location address reached. Bad for you!\n";
        return 2;
    }
    if (index == original.end_point_index) {
        std::cout << "YES";
        return 0;
    }
    std::cerr << "Unknown error!\n";
    return 3;
}

