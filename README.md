# ExcelToLaTeXtable
Converting an excel table to LaTeX text. Especially helpful for big tables.

## Usage

``` bash
python table_converter.py -d "EXCEL FILE" -c "TABLE CAPTION"
```

Text output can be copied directly into LaTeX.

## Example

Using the given example excel table:

```
python table_converter.py -d table_small.xlsx -c "A table"
```

Output:
``` latex
\begin{table}
\centering
\begin{tabular}{c|c|c}
Language & Hours & Users \\
\hline
Python & 12 & 2 \\
MATLAB & 15 & 100 \\
Java & 20 & 20 \\
C++ & 4 & 37 \\
\hline
\end{tabular}
\caption{A table}
\end{table}
```
