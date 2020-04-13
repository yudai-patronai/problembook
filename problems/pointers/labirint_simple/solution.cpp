Location_t *find_medical_center(Location_t *start_location) {
    struct Location_t *current_location = start_location;
    while (true) {
        if (!current_location) {
            return nullptr;
        }        if (current_location->is_medical_center && current_location->free_beds > 0) {
            return current_location;
        } else if (current_location->indicator == UP) {
            current_location = current_location->up;
        } else if (current_location->indicator == DOWN) {
            current_location = current_location->down;
        } else if (current_location->indicator == RIGHT) {
            current_location = current_location->right;
        } else if (current_location->indicator == LEFT) {
            current_location = current_location->left;
        } else {
            return nullptr;
        }
    }
}

