#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # index of the last row in the grid
    lst_max = len(grid[0]) - 1  # index of the last cell in a row

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # Check left and right neighbors
                if land_idx == 0:
                    # No left neighbor (first column)
                    counter += 1

                    # Check right neighbor
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # Check left neighbor
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # No right neighbor (last column)
                    counter += 1
                else:
                    # Check left neighbor
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # Check right neighbor
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # Check top and bottom neighbors
                if lst_idx == 0:
                    # No top neighbor (first row)
                    counter += 1

                    # Check bottom neighbor
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # Check top neighbor
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # No bottom neighbor (last row)
                    counter += 1
                else:
                    # Check top neighbor
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # Check bottom neighbor
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter
