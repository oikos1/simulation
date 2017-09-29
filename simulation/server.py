from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from model import HavvenModel


def make_server(n_agents=200, px_width=500, px_height=500):
    charts = [ChartModule([{"Label": "Gini", "Color": "red"},
                           {"Label": "Wealth SD", "Color": "blue"}]),

              ChartModule([{"Label": "Max Wealth", "Color": "purple"},
                           {"Label": "Min Wealth", "Color": "orange"}]),

              ChartModule([{"Label": "Profit %", "Color": "red"}]),
    
              ChartModule([{"Label": "Nomins", "Color": "blue"},
                           {"Label": "Escrowed Curits", "Color": "red"}]),

              ChartModule([{"Label": "Curit Demand", "Color": "red"},
                           {"Label": "Curit Supply", "Color": "orange"}]),

              ChartModule([{"Label": "Nomin Demand", "Color": "blue"},
                           {"Label": "Nomin Supply", "Color": "purple"}]),

              ChartModule([{"Label": "Fiat Demand", "Color": "green"},
                           {"Label": "Fiat Supply", "Color": "cyan"}]),
    
              ChartModule([{"Label": "Fee Pool", "Color": "blue"}]),

              ChartModule([{"Label": "Fees Distributed", "Color": "blue"}])]

    n_slider = UserSettableParameter('slider', "Number of Agents", n_agents, 2, 2000, 1)

    server = ModularServer(HavvenModel, charts, "Havven Model",
                        {"N": n_slider})
    return server