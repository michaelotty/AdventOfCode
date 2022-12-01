/**
 * @file 25.cpp
 * @author Michael Otty (michael.otty@gmail.com)
 * @brief Advent of Code 2021 day 25
 * @version 1.0.0
 * @date 2021-12-25
 *
 * @copyright Copyright (c) 2021
 *
 */

#include <iostream>
#include <string>
#include <vector>

#include "Days.h"
#include "Utilities.h"

/*
================================================================================
                                Classes
================================================================================
*/
/// Sea cucumber state
enum class State
{
    none,
    down,
    right,
};

/**
 * @brief Print State to ostream
 *
 * @param os to print to
 * @param state to be printed
 * @return std::ostream& to print to
 */
std::ostream& operator<<(std::ostream& os, const State& state)
{
    switch (state)
    {
    case State::none:
        os << '.';
        break;

    case State::down:
        os << 'v';
        break;

    case State::right:
        os << '>';
        break;

    default:
        throw std::invalid_argument("State undefined");
        break;
    }

    return os;
}

/// Sea cucumbers class
class SeaCucumbers
{
private:
    std::vector<std::vector<State>> m_grid; ///< The grid of sea cucumbers
    std::size_t m_iterations;               ///< Number of iterations

    /**
     * @brief Extract data from line of text from input data
     *
     * @param inLine Line input
     * @return std::vector<State> Data parsed into vector of States
     */
    std::vector<State> ExtractLine(const std::string& inLine)
    {
        std::vector<State> outLine;
        for (const auto& ch : inLine)
        {
            switch (ch)
            {
            case '.':
                outLine.push_back(State::none);
                break;

            case 'v':
                outLine.push_back(State::down);
                break;

            case '>':
                outLine.push_back(State::right);
                break;

            default:
                throw std::invalid_argument("Character not recognised");
                return outLine;
            }
        }

        return outLine;
    }

public:
    /**
     * @brief Construct a new SeaCucumbers object
     *
     * @param text from the input file
     */
    SeaCucumbers(const std::string& text) : m_iterations(0)
    {
        std::size_t splitPoint = 0;
        std::size_t end;

        while ((end = text.find('\n', splitPoint + 1)) != std::string::npos)
        {
            std::string line = text.substr(splitPoint, end - splitPoint);
            m_grid.push_back(ExtractLine(line));
            splitPoint = end + 1;
        }
        m_grid.push_back(ExtractLine(text.substr(splitPoint)));
    }

    /**
     * @brief Print the iteration value and grid
     */
    void Print() const
    {
        std::cout << "Iteration: " << m_iterations << "\n";
        for (const auto& row : m_grid)
            PrintVector(row, "");
        std::cout << "\n";
    }

    /**
     * @brief Get the next iteration
     *
     * @return true if we aren't yet at the end
     * @return false if it's the last iteration
     */
    bool Next()
    {
        std::vector<std::vector<State>> gridCopy = m_grid;
        const std::vector<std::vector<State>> gridFixedCopy = m_grid;
        for (std::size_t i = 0; i < m_grid.size(); i++)
        {
            for (std::size_t j = 0; j < m_grid[0].size(); j++)
            {
                if (m_grid[i][j] == State::right)
                {
                    // If on edge, moves off edge
                    if (j == m_grid[0].size() - 1)
                    {
                        if (m_grid[i][0] == State::none)
                        {
                            gridCopy[i][j] = State::none;
                            gridCopy[i][0] = State::right;
                        }
                        continue;
                    }

                    // If right is empty, move along
                    if (m_grid[i][j + 1] == State::none)
                    {
                        gridCopy[i][j] = State::none;
                        gridCopy[i][j + 1] = State::right;
                    }
                    continue;
                }
            }
        }

        m_grid = gridCopy;

        for (std::size_t i = 0; i < m_grid.size(); i++)
        {
            for (std::size_t j = 0; j < m_grid[0].size(); j++)
            {
                if (m_grid[i][j] == State::down)
                {
                    // If on edge, moves off edge
                    if (i == m_grid.size() - 1)
                    {
                        if (m_grid[0][j] == State::none)
                        {
                            gridCopy[i][j] = State::none;
                            gridCopy[0][j] = State::down;
                        }
                        continue;
                    }

                    // If down is empty, move along
                    if (m_grid[i + 1][j] == State::none)
                    {
                        gridCopy[i][j] = State::none;
                        gridCopy[i + 1][j] = State::down;
                    }
                    continue;
                }
            }
        }

        bool hasChanged = m_grid != gridFixedCopy;
        m_iterations++;

        m_grid = std::move(gridCopy);
        return hasChanged;
    }

    /**
     * @brief Get the number of iterations
     *
     * @return std::size_t Amount of iterations
     */
    std::size_t GetIterations() const { return m_iterations; }
};

/*
================================================================================
                            Function Definitions
================================================================================
*/

/**
 * @brief Day 25 of Advent of Code
 *
 * @param fileName to read as puzzle input
 */
void Day25(const char* fileName)
{
    SeaCucumbers seaCucumbers(ReadTextFile(fileName));

    while (seaCucumbers.Next())
    {
    }

    std::cout << "Part 1: " << seaCucumbers.GetIterations() << "\n";
}
