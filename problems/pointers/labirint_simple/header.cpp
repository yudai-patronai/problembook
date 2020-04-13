#include <iostream>
#include <vector>

const size_t neighbours_count = 4;enum Direction {
    UP = 0,
    DOWN = 1,
    RIGHT = 2,
    LEFT = 3
};

struct Location_t {
    bool is_medical_center;
    int free_beds;
    int indicator;
    struct Location_t *up;
    struct Location_t *down;
    struct Location_t *right;
    struct Location_t *left;
};

struct Level_t {
    int width;
    int height;
    int start_point_index;
    int end_point_index;
    std::vector<struct Location_t> locations;

    /**
    * initializes all the fields of Level_t with ASCII image of the level got from std::cin
    */
    void load_level() {
        std::cin >> width >> height >> std::ws;
        for (int i = 0; i < height; ++i) {
            int format = 5;
            std::string line;
            std::getline(std::cin, line);
            for (int k = 0; k < width; ++k) {
                struct Location_t point;
                point.up = point.down = point.left = point.right = nullptr;
                point.is_medical_center = (bool) (line[k * format + 0] - 48);
                point.free_beds = (int) (line[k * format + 1] - 48);
                if ((char) line[k * format + 3] == '$') {
                    start_point_index = i * width + k;
                }
                if ((char) line[k * format + 3] == '#') {
                    end_point_index = i * width + k;
                }
                int direction = line[k * format + 2] - '0';
                if (direction == UP)
                    point.indicator = UP;
                else if (direction == DOWN)
                    point.indicator = DOWN;
                else if (direction == LEFT)
                    point.indicator = LEFT;
                else if (direction == RIGHT)
                    point.indicator = RIGHT;
                locations.push_back(point);
            }
        }
        // don't forget to init pointers UP, DOWN, LEFT, RIGHT
        for (int i = 0; i < height; ++i) {
            for (int k = 0; k < width; ++k) {
                if (locations[i * width + k].indicator == UP)
                    locations[i * width + k].up = &locations[(i - 1) * width + k];
                if (locations[i * width + k].indicator == DOWN)
                    locations[i * width + k].down = &locations[(i + 1) * width + k];
                if (locations[i * width + k].indicator == RIGHT)
                    locations[i * width + k].right = &locations[i * width + k + 1];
                if (locations[i * width + k].indicator == LEFT)
                    locations[i * width + k].left = &locations[i * width + k - 1];
            }
        }
    }
    struct Location_t *get_location_pointer(int index)
    {
        return &locations[index];
    }
    int get_location_index(Location_t *location)
    {
        for (int index = 0; index < width * height; ++index) {
            if (location == &locations[index])
                return index;
        }
        return -1;
    }
};

