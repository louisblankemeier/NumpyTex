import numpy as np

def gen_two_axis_table(table_name, col_labels, row_labels, col_axis_label, row_axis_label, vals, color = True):
    assert len(col_labels) == vals.shape[1], "length of column labels doesn't match vals axis 1 shape"
    assert len(row_labels) == vals.shape[0], "length of column labels doesn't match vals axis 0 shape"
    to_write = f"\\documentclass[11pt]{{article}}\n\\usepackage[table]{{xcolor}}\n\\usepackage{{amsmath}}\n\\usepackage{{booktabs}}\n\\newcommand\headercell[1]{{\n\t\\smash[b]{{\\begin{{tabular}}[t]{{@{{}}c@{{}}}} #1 \\end{{tabular}}}}}}\n\\begin{{document}}\n\\noindent\n"
    first_part = row_axis_label.split(" ")[0]
    second_part = row_axis_label.split(" ")[1]
    to_write += f"\\begin{{tabular}}{{@{{}} *{{{len(col_labels) + 1}}}{{c}} @{{}}}}\n\\headercell{{{first_part} \\\\ {second_part}}} & \multicolumn{{{len(col_labels)}}}{{c@{{}}}}{{{col_axis_label}}}\\\\\n\\cmidrule(l){{2-{len(col_labels) + 1}}}\n"
    latex_script = open(f"../latex_scripts/{table_name}.tex","w")
    for col_label in col_labels:
        to_write += f" & {col_label}"
    to_write += f" \\\\ \n \midrule" 
    for i, row_label in enumerate(row_labels):
        to_write += f"\n\t{row_label}"
        for j in range(len(col_labels)):
            if color:
                if vals[i, j] < 0:
                    to_write += f"& \\cellcolor{{red!{np.abs(vals[i, j] * 100)}}} {vals[i, j]}"
                else:
                    to_write += f"& \\cellcolor{{green!{np.abs(vals[i, j] * 100)}}} {vals[i, j]}"
            else:
                to_write += f" & {vals[i, j]}"
        to_write += f"\\\\"
    to_write += f"\n\\end{{tabular}}\n\\end{{document}}"
    latex_script.write(to_write)
    latex_script.close()