'''
Description:
Author: Jiaqi Gu (jqgu@utexas.edu)
Date: 2022-03-07 16:42:12
LastEditors: Jiaqi Gu (jqgu@utexas.edu)
LastEditTime: 2022-03-08 16:04:28
'''
#######################################################################
# Implementation of A Star Search
# You need to implement initialize() and route_one_net()
# All codes should be inside A Star Search class
# Name: Xun Zhou
# UT EID: xz7637
#######################################################################

from typing import List, Tuple

import numpy as np

from .p2_routing_base import A_Star_Search_Base, GridAstarNode, PriorityQueue, AdvancedPriorityQueue

__all__ = ["A_Star_Search"]

class A_Star_Search(A_Star_Search_Base):
    def __init__(self) -> None:
        super().__init__()

    def initialize(self):
        """Initialize necessary data structures before starting solving the problem
        """
        # TODO initialize any auxiliary data structure you need
        self.source = GridAstarNode((self.pin_pos_x[0], self.pin_pos_y[0]), cost_g = 0, cost_f = 0, bend_count=0)
        self.target = GridAstarNode((self.pin_pos_x[1], self.pin_pos_y[1]), cost_g = 0, cost_f = 0, bend_count=0)
        self.visited_location = []
        self.open_list = AdvancedPriorityQueue() # Initialize the the node queue
        # self.open_list = PriorityQueue()

        self.open_list.put(self.source) # Add the source node to the open list

    def _find_avaliabe_neighbors(self, node: GridAstarNode) -> List[GridAstarNode]:
        """Find all the neighbors of a node that are not blocked

        Args:
            node (GridAstarNode): the node to find neighbors

        Returns:
            List[GridAstarNode]: a list of neighbors
        """
        neighbors = []
        x,y = node.pos[0] - 1, node.pos[1]
        # if (x,y) == (3,6) : print("this is true left")
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1] and self.blockage_map[y][x] == 0:
            neighbors.append(GridAstarNode((x, y), cost_g = 0, cost_f = 0, bend_count=0))

        x,y = node.pos[0], node.pos[1] - 1
        # if (x,y) == (3,6) : print("this is true top")
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1] and self.blockage_map[y][x] == 0:
            neighbors.append(GridAstarNode((x, y), cost_g = 0, cost_f = 0, bend_count=0))

        x,y = node.pos[0] + 1, node.pos[1]
        # if (x,y) == (3,6) : print("this is true right")
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1] and self.blockage_map[y][x] == 0:  
            neighbors.append(GridAstarNode((x, y), cost_g = 0, cost_f = 0, bend_count=0))

        x,y = node.pos[0], node.pos[1] + 1
        # if (x,y) == (3,6) : print("this is true bnotom")
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1] and self.blockage_map[y][x] == 0:  
            neighbors.append(GridAstarNode((x, y), cost_g = 0, cost_f = 0, bend_count=0))
        

        # # check left
        # if x > 0 and self.blockage_map[x-1][y] == 0:
        #     neighbors.append(GridAstarNode((x-1, y), cost_g = 0, cost_f = 0, bend_count=0))
        # # check top
        # if y > 0 and self.blockage_map[x][y+1] == 0:
        #     neighbors.append(GridAstarNode((x, y+1), cost_g = 0, cost_f = 0, bend_count=0))
        # # check right
        # if x < self.grid_size[0]-1 and self.blockage_map[x+1][y] == 0:
        #     neighbors.append(GridAstarNode((x+1, y), cost_g = 0, cost_f = 0, bend_count=0))
        # # check bottom
        # if y < self.grid_size[1]-1 and self.blockage_map[x][y-1] == 0:  
        #     neighbors.append(GridAstarNode((x, y-1), cost_g = 0, cost_f = 0, bend_count=0))
            
        return neighbors
    def route_one_net(self) -> Tuple[List[Tuple[Tuple[int], Tuple[int]]], int, List[int], List[int]]:
        """route one multi-pin net using the A star search algorithm

        Return:
            path (List[Tuple[Tuple[int], Tuple[int]]]): the vector-wise routing path described by a list of (src, dst) position pairs
            wl (int): total wirelength of the routing path
            wl_list (List[int]): a list of wirelength of each routing path
            n_visited_list (List[int]): the number of visited nodes in the grid in each iteration
        """
        # TODO implement your A star search algorithm for one multi-pin net.
        # To make this method clean, you can extract subroutines as methods of this class
        # But do not override methods in the parent class
        # Please strictly follow the return type requirement.

        # self.source.visited = True
        # print("\n")
        # for row in self.blockage_map:
        #     for col in row:
        #         if col == 0:
        #             print("0", end=" ")
        #         else:
        #             print("1", end=" ")
        #     print("\n") 
        
        path = []
        wirelength = 0
        wirelength_list = []
        n_visited_list = []

        # number_of_node_visited = 0
        while not self.open_list.empty():
            current_node = self.open_list.get() # Get the node with the lowest cost_f
            # print(current_node.pos)
            if current_node.pos == self.target.pos:
                path = (self._backtrack(current_node))
                wirelength = current_node.cost_g
                # print(self._backtrack(current_node))
                # print(path)
                break
            if current_node.pos not in self.visited_location:
                self.visited_location.append(current_node.pos)
            # self.visited.add(current_node.pos)
                # number_of_node_visited += 1

            neighbors = self._find_avaliabe_neighbors(current_node)
            # for n in neighbors:
            #     print(n.pos)
            # m = 0
            for neighbor in neighbors:
                # print(m)
                # print(neighbor.visited)
                # print(self.open_list.exist(neighbor))
                # print(i for i in self.visited)
                if (self.open_list.exist(neighbor)):
                    
                    continue
                
                if neighbor.pos in self.visited_location:

                    # print("this is true")
                    continue
                
                # print("this is the neighbor")
                neighbor.parent = current_node
                neighbor.cost_g = current_node.cost_g + 1
                neighbor.cost_f = neighbor.cost_g + self._find_manhattan_dist_to_target(neighbor.pos, self.target.pos)
                
                # self.open_list.update()
                if self._has_bend(current_node, neighbor):
                    neighbor.bend_count = current_node.bend_count + 1
                
                self.open_list.put(neighbor)
            # print(self.open_list._heap)
            # print(" this is the open list")
        # print("\n",path)
        # wirelength = (len(path) - 1)
        # print(wirelength)
        wirelength_list.append(wirelength)
        # print(wirelength_list)
        n_visited_list.append(len(self.visited_location))
        # print(self._merge_path(path))
        # if self.blockage_map[6][3] == 1: print("YES\n")
        return self._merge_path(path), wirelength, wirelength_list, n_visited_list
#         raise NotImplementedError


