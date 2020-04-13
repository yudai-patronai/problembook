nclude <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int age, height, weight;
    double temperature;
    int counter = 0;
    double temp_sum = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> age;
        cin >> height;
        cin >> weight;
        cin >> temperature;

        if ((age >= 60) || (abs(height - weight - 100) > 10))
        {
            counter++;
            temp_sum = temp_sum + temperature;
        }
    }
    if (counter == 0)
    {
        cout << 0;
    }
    else
    {
        cout << temp_sum/counter;
    }
    return 0;
}

