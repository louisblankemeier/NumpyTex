# Numpy To Latex Table Script Generator

## Functionality

- Can compute and add both row and column averages
- Places a dash wherever a nan appears in the numpy table
- Can add green color to indicate positive value, red color to indicate negative value
- If values are percentages, can add percent signs

## Installation

### pip

To install using pip, use the command:

`pip install git+https://github.com/louisblankemeier/NumpyTex`

Then, you can import within python. For example:

`from NumpyTex.two_axis_table import gen_two_axis_table`

*Generated latex scripts have only been tested in Overleaf.*

## Usage

This repo enables generating an aesthetically appealing table in the form of a latex script using a numpy array. 

examples/two_axis_colored.py demostrates usage of the function src/two_axis_table.py. 

Below is an image of the rendered table using the generated latex script, which is written to latex_scripts/two_axis_example.tex.

![](https://github.com/louisblankemeier/NumpyTex/blob/main/figs/two_axis_table_example.png)




