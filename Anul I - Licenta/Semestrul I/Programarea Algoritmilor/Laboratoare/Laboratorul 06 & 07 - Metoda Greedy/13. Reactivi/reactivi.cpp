#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int, int> TemperatureRange;

bool sortCond(const TemperatureRange& a, const TemperatureRange& b)
{
    return (a.second < b.second) || (a.second == b.second && a.first < b.first);
}

int main()
{
    const string inputFileName = "reactivi.in";
    const string outputFileName = "reactivi.out";
    ifstream inputFile(inputFileName);

    int refrigeratorsNumber;
    inputFile >> refrigeratorsNumber;

    vector<TemperatureRange> temperatures;

    for (int i = 0; i < refrigeratorsNumber; ++i)
    {
        int x, y;
        inputFile >> x >> y;
        temperatures.emplace_back(x, y);
    }

    inputFile.close();

    sort(temperatures.begin(), temperatures.end(), sortCond);

    int neededRefrigerators = 1;
    int last = 0;

    for (int index = 1; index < refrigeratorsNumber; ++index)
    {
        if (temperatures[index].first > temperatures[last].second)
        {
            last = index;
            ++neededRefrigerators;
        }
        else
        {
            temperatures[last] = make_pair(
                max(temperatures[index].first, temperatures[last].first),
                min(temperatures[index].second, temperatures[last].second)
            );
        }
    }

    ofstream outputFile(outputFileName);
    outputFile << neededRefrigerators << endl;
    outputFile.close();

    return 0;
}