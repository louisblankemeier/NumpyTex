import numpy as np
import os

def gen_two_axis_table(table_name, col_labels, row_labels, col_axis_label, row_axis_label, vals, row_average = True, col_average = True, color_vals = None , uncertainties = None, percent = True, decimals = 2):
    assert len(col_labels) == vals.shape[1], "length of column labels doesn't match vals axis 1 shape"
    assert len(row_labels) == vals.shape[0], "length of column labels doesn't match vals axis 0 shape"
    
    row_averages = []
    for i in range(len(row_labels)):
        row_averages.append(np.mean(vals[i, :][~np.isnan(vals[i, :])]))

    col_averages = []
    for i in range(len(col_labels)):
        col_averages.append(np.mean(vals[:, i][~np.isnan(vals[:, i])]))

    to_write = f"\\documentclass[11pt]{{article}}\n\\usepackage[table]{{xcolor}}\n\\usepackage{{amsmath}}\n\\usepackage{{booktabs}}\n\\newcommand\headercell[1]{{\n\t\\smash[b]{{\\begin{{tabular}}[t]{{@{{}}c@{{}}}} #1 \\end{{tabular}}}}}}\n\\begin{{document}}\n\\noindent\n"
    
    # Edit this to distribute row axis label on two lines differently
    first_part = row_axis_label.split(" ")[0]
    second_part = row_axis_label.split(" ")[1]

    if row_average:
        num_col_labels = len(col_labels) + 1
    else:
        num_col_labels = len(col_labels)
    
    if row_average:
        to_write += f"\\begin{{tabular}}{{@{{}} *{{{num_col_labels}}}{{c}} | c @{{}}}}\n\\headercell{{{first_part} \\\\ {second_part}}} & \multicolumn{{{num_col_labels}}}{{c@{{}}}}{{{col_axis_label}}}\\\\\n\\cmidrule(l){{2-{num_col_labels + 1}}}\n"
    else:
        to_write += f"\\begin{{tabular}}{{@{{}} *{{{num_col_labels + 1}}}{{c}} @{{}}}}\n\\headercell{{{first_part} \\\\ {second_part}}} & \multicolumn{{{num_col_labels}}}{{c@{{}}}}{{{col_axis_label}}}\\\\\n\\cmidrule(l){{2-{num_col_labels + 1}}}\n"
    
    #if not os.path.isdir('./latex_scripts'):
    #    os.mkdir('./latex_scripts')
    #latex_script = open(f"./latex_scripts/{table_name}.tex","w")
    
    # Column labels
    for col_label in col_labels:
        to_write += f" & {col_label}"
    if row_average:
        to_write += f" & average"
    to_write += f" \\\\ \n \\midrule \\midrule" 

    # Generate each row of the table
    for i, row_label in enumerate(row_labels):
        to_write += f"\n\t{row_label}"

        for j in range(len(col_labels)):
            if np.isnan(vals[i, j]):
                to_write += f" & -"
            else:
                if color_vals is not None:
                    if color_vals[i, j] < 0:
                        if percent:
                            to_write += f"& \\cellcolor{{red!{np.abs(color_vals[i, j])}}} {vals[i, j]:.{decimals}f}\%"
                        else:
                            to_write += f"& \\cellcolor{{red!{np.abs(color_vals[i, j])}}} {vals[i, j]:.{decimals}f}"
                    else:
                        if percent:
                            to_write += f"& \\cellcolor{{green!{np.abs(color_vals[i, j])}}} {vals[i, j]:.{decimals}f}\%"
                        else:
                            to_write += f"& \\cellcolor{{green!{np.abs(color_vals[i, j])}}} {vals[i, j]:.{decimals}f}"
                else:
                    if percent:
                        to_write += f" & {vals[i, j]:.{decimals}f}\%"
                    else:
                        to_write += f" & {vals[i, j]:.{decimals}f}"
                if uncertainties is not None:
                    to_write += f" ± {uncertainties[i, j]:.{decimals}f}"

        if row_average:
            if color_vals is not None:
                if row_averages[i] < 0:
                    if percent:
                        to_write += f"& \\cellcolor{{red!{np.abs(row_averages[i])}}} {row_averages[i]:.{decimals}f}\%"
                    else:
                        to_write += f"& \\cellcolor{{red!{np.abs(row_averages[i] * 100)}}} {row_averages[i]:.{decimals}f}"
                else:
                    if percent:
                        to_write += f"& \\cellcolor{{green!{np.abs(row_averages[i])}}} {row_averages[i]:.{decimals}f}\%"
                    else:
                        to_write += f"& \\cellcolor{{green!{np.abs(row_averages[i] * 100)}}} {row_averages[i]:.{decimals}f}"
            else:
                if percent:
                    to_write += f" & {row_averages[i]:.{decimals}f}\%"
                else:
                    to_write += f" & {row_averages[i]:.{decimals}f}"

        to_write += f"\\\\"

    if col_average:
        to_write += f"\n\t \\hline \n\t average"
        for i in range(len(col_labels)):
            if color_vals is not None:
                if col_averages[i] < 0:
                    if percent:
                        to_write += f"& \\cellcolor{{red!{np.abs(col_averages[i])}}} {col_averages[i]:.{decimals}f}\%"
                    else:
                        to_write += f"& \\cellcolor{{red!{np.abs(col_averages[i] * 100)}}} {col_averages[i]:.{decimals}f}"
                else:
                    if percent:
                        to_write += f"& \\cellcolor{{green!{np.abs(col_averages[i])}}} {col_averages[i]:.{decimals}f}\%"
                    else:
                        to_write += f"& \\cellcolor{{green!{np.abs(col_averages[i] * 100)}}} {col_averages[i]:.{decimals}f}"
            else:
                if percent:
                    to_write += f"& {col_averages[i]:.{decimals}f}\%"
                else:
                    to_write += f"& {col_averages[i]:.{decimals}f}"

        if row_average:
            to_write += f" & -"

    # Latex end statements
    to_write += f"\n\\end{{tabular}}\n\\end{{document}}"
    #latex_script.write(to_write)

    print(to_write)
    #latex_script.close()