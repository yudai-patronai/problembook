#include <iostream>
#include <vector>
#include <map>
#include <sstream>

using std::string;
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::map;
using std::ostream;
using std::atoi;


/////////////////////////
// Utility functions
/////////////////////////
void add_player(Party* p, const vector<string>& cmd) {
    string name = cmd[1];
    unsigned strength = atoi(cmd[2].c_str());

    p->add(Player(name, strength));
}

void give(Party* p, const vector<string>& cmd) {
    string player_name = cmd[1];
    string item_name = cmd[2];
    unsigned weight = atoi(cmd[3].c_str());
    unsigned price = atoi(cmd[4].c_str());
    Item i(item_name, weight, price);

    p->give(player_name, i);
}

int main() {
    // cmds
    //  add: Name inventory_size
    //  give: Name Item weight price

    Party p;

    string cmd_line;
    while (getline(cin, cmd_line)) {
        std::stringstream ss(cmd_line);
        vector<string> cmd;

        string s;
        while (getline(ss, s, ' ')) {
            cmd.push_back(s);
        }
        cout << endl;
        if (!cmd.empty()) {
            if (cmd[0] == "give")
                give(&p, cmd);
            else if (cmd[0] == "add")
                add_player(&p, cmd);

            p.print(cout);
        }
    }

    return 0;
}
