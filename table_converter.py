import argparse
import pandas as pd

def main(excel_file, caption):
    """
    Load excel file and output LaTeX text giving the same table
    """
    df = pd.read_excel(excel_file,header=1,index_col=0)
    nr_of_columns = df.shape[1]
    columns = []
    for i in df:
        if 'Unnamed' in i:
            columns.append('multicolumn')
        else:
            columns.append(i)
        
    caption = str(caption)
    
    print("\\begin{table}")
    print('\centering')
    print('\\begin{tabular}{',end='')

    for i in range(nr_of_columns):
        if i == (nr_of_columns-1):
            print('c}')
        else:
            print('c',end='|')

    for i,column in enumerate(columns):
        if i == (nr_of_columns-1):
            print(column + ' \\\\')

        elif column == 'multicolumn':
            print(' & ')

        else:
            print(column, end=' & ')

    print('\hline')      

    for index, row in df.iterrows():
        for i in range(nr_of_columns):
            if i == (nr_of_columns-1):
                print(str(row[i]) + ' \\\\')
            else:
                print(row[i], end=' & ')

    print('\hline')
    print('\end{tabular}')
    print('\caption{'+caption+'}')
    print("\end{table}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", type=str, default="table.xlsx",
                        help="Excel file to use in LaTeX")
    parser.add_argument("-c", "--caption", type=str, default="A table",
                        help="Caption of the table")

    args = parser.parse_args()
    main(args.data, args.caption)
