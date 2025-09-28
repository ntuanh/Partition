from src.dijkstra import Dijkstra
from src.handle_data import Data

if __name__ == "__main__" :
    cost = Data().get_test_bed_cost()
    dijkstra_app = Dijkstra(cost)
    dijkstra_app.run()