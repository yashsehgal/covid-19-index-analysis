# importing modules
import io
import pandas as pandas
import matplotlib.pyplot as plotter

def generateGraphs():
    pass
    # retreving data from the CSV file
    COVID_DATA = pandas.read_csv("covid_19_india.csv")
    # retreving data for different states
    MADHYA_PRADESH_DATA = COVID_DATA[COVID_DATA.states == "Madhya Pradesh"]
    DELHI_DATA = COVID_DATA[COVID_DATA.states == "Delhi"]
    MAHARASHTRA_DATA = COVID_DATA[COVID_DATA.states == "Maharashtra"]
    
    plotter.plot(MADHYA_PRADESH_DATA.Cured, MADHYA_PRADESH_DATA.Deaths)
    plotter.plot(DELHI_DATA.Cured, DELHI_DATA.Deaths)
    plotter.plot(MAHARASHTRA_DATA.Cured, MAHARASHTRA_DATA.Deaths)
    plotter.title("COVID-19 Index")
    plotter.xlabel("Confirmed Deaths Cases")
    plotter.ylabel("Confirmed Cured Cases")
    plotter.legend(["Madhya Pradesh", "Delhi", "Maharashtra"])
    plotter.show()
    
generateGraphs()
