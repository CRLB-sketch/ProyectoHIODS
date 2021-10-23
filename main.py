import pandas as pd

def main():
    
    df_estudiantes = pd.read_csv("students.csv", encoding="latin1")

    print(df_estudiantes)

    print("Hello HIODS")
    print("Hola")

if __name__ == '__main__':
    main()
	