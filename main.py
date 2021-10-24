import pandas as pd
  
from controller import Controller

if __name__ == '__main__':
    # df_estudiantes = pd.read_csv("docs//students.csv", encoding="latin1")
    # print(df_estudiantes)

    system = Controller()
    system.main()
