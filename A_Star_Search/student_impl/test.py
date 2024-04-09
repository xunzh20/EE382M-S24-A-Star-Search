from p2_routing_base import A_Star_Search_Base, GridAstarNode, PriorityQueue

class A_Star_Search(A_Star_Search_Base):
    def __init__(self) -> None:
        super().__init__()
    
    def print_block(self):
        for row in self.blockage_map:
            for col in row:
                if col == 0:
                    print("0", end=" ")
                else:
                    print("1", end=" ")
            print("\n")
    
    def print_blockage_pos_x(self):
        print(self.blockage_pos_x)
if __name__ == "__main__":
    solver = A_Star_Search()
    solver.read_benchmark("A_Star_Search/benchmarks/example_1.txt")
    solver.print_block()
    solver.print_blockage_pos_x()
    print(solver.pin_pos_x)