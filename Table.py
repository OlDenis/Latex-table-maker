"""Module to produce Latex tables with python."""

class Table():
    """Generates a Latex tabular environment from
       a nested python list."""

    begin     = 3*"\t"+"\\begin{tabular}{|c|| place | }"
    hline     = "\hline"
    first_row_block = "& {} "
    row_block       = "& {:4.3f} "
    endline   = "\\\\"
    end       = "\end{tabular}"

    def __init__(self, rows, col_names, row_names=None, indent=3, title=None, diff_last_row=0):
        self.rows       = rows
        self.row_names  = row_names
        self.col_names  = col_names
        self.n_rows     = len(row_names)
        self.n_cols     = len(col_names)
        self.indent     = indent
        self.title      = title
        self.diff_last_row   = diff_last_row
        if len(rows) != len(row_names):
            print("Error : number of rows doesn't match number of row names.")
            exit()

    def make(self, last_block = "& {:4.3f} "):
        table = [self.begin.replace("place", self.n_cols*'c'), "\t" + self.hline]
        if self.title:
            title_width = self.n_cols+int(not self.row_names is None)
            title_row = "\multicolumn{n_cols}{|c|}{title} \\\\".replace("n_cols", str(title_width)).replace("title", self.title)
            table.append(title_row)
            table.append("\t" + self.hline)
        first_row = self.n_cols*self.first_row_block + self.endline
        table.append("\t" + first_row.format(*self.col_names))
        c=0
        for name, row in zip(self.row_names, self.rows):
            table.append("\t" + self.hline)
            is_last_row = c == len(self.rows) - self.diff_last_row
            if self.diff_last_row and is_last_row:
                table.append("\t" + self.hline)
            line = "{} " + (self.n_cols-1)*self.row_block + last_block + self.endline
            if len(row) != len(self.col_names):
                print("Error : number of values doesn't match number of column names.")
                print("Number of values:", len(row))
                print("Number of names :", len(self.col_names))
                exit()
            table.append("\t" + line.format(name, *row))
            c+=1
        table += ["\t" + self.hline, self.end]
        return ("\n"+self.indent*"\t").join(table)
