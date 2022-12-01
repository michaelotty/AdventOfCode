/**
 * @file 15.cpp
 * @author Michael Otty (michael.otty@gmail.com)
 * @brief Advent of Code 2021 day 15
 * @version 1.0.0
 * @date 2021-12-15
 *
 * @copyright Copyright (c) 2021
 *
 */

#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <vector>

#include "Days.h"
#include "Utilities.h"

/*
================================================================================
                                Classes
================================================================================
*/

/*
================================================================================
                            Function Definitions
================================================================================
*/
/**
 * @brief Solve the maze
 *
 * @param grid Grid maze to solve
 * @return int Path cost
 */
static int Solve(const std::vector<std::vector<int>>& grid)
{
    using priorityAndCoord = std::pair<int, std::pair<int, int>>;

    const auto start = std::make_pair(0, 0);
    const auto end = std::make_pair(static_cast<int>(grid[0].size()) - 1,
                                    static_cast<int>(grid.size()) - 1);
    std::map<std::pair<int, int>, std::pair<int, int>> cameFrom;
    std::map<std::pair<int, int>, int> costSoFar;
    cameFrom[start] = start;
    costSoFar[start] = 0;

    auto comparePriority
        = [](const priorityAndCoord& a, const priorityAndCoord& b)
    { return a.first > b.first; };

    std::priority_queue<priorityAndCoord, std::vector<priorityAndCoord>,
                        decltype(comparePriority)>
        frontier(comparePriority);

    frontier.emplace(grid[0][0], start);

    const std::array<std::pair<int, int>, 4> offsets{
        {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}};

    while (!frontier.empty())
    {
        const auto [currentPriority, currentPos] = frontier.top();
        frontier.pop();

        if (currentPos == end)
            break;

        for (const auto& [rowOffset, colOffset] : offsets)
        {
            auto nextPos = std::make_pair(currentPos.first + rowOffset,
                                          currentPos.second + colOffset);

            if ((nextPos.first >= 0) && (nextPos.first <= end.first)
                && (nextPos.second >= 0) && (nextPos.second <= end.second)
                && (!cameFrom.count(nextPos)))
            {
                int cost = costSoFar[currentPos]
                           + grid[nextPos.first][nextPos.second];
                costSoFar[nextPos] = cost;
                frontier.push(std::make_pair(cost, nextPos));
                cameFrom[nextPos] = currentPos;
            }
        }
    }

    // Trace back path
    auto currentPos = end;
    int ans = 0;
    do
    {
        ans += grid[currentPos.first][currentPos.second];
        currentPos = cameFrom[currentPos];
    } while (currentPos != start);
    return ans;
}

/**
 * @brief Expand the grid for part 2
 *
 * @param grid Original grid
 * @param expansionSize Scaling factor
 * @return std::vector<std::vector<int>> Expanded grid
 */
std::vector<std::vector<int>> ExpandGrid(std::vector<std::vector<int>> grid,
                                         size_t expansionSize)
{
    std::vector<std::vector<int>> newGrid;
    newGrid.reserve(grid.size() * expansionSize);
    for (size_t i = 0; i < grid.size() * expansionSize; i++)
        newGrid.push_back(std::vector<int>(grid[0].size() * expansionSize, 0));

    for (size_t i = 0; i < newGrid.size(); i++)
        for (size_t j = 0; j < newGrid.size(); j++)
            newGrid[i][j] = (grid[i % grid.size()][j % grid.size()]
                             + (i / grid.size()) + (j / grid.size()) - 1)
                                % 9
                            + 1;

    return newGrid;
}

/**
 * @brief Day 15 of Advent of Code
 *
 * @param fileName to read as puzzle input
 */
void Day15(const char* fileName)
{
    const std::string text = ReadTextFile(fileName);
    auto grid = ParseTextToNumberGrid(text);

    std::cout << "Part 1: " << Solve(grid) << "\n";
    grid = ExpandGrid(grid, 5);
    std::cout << "Part 2: " << Solve(grid) << "\n";
}
