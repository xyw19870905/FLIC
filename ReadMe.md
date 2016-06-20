# FLIC Project

## Radiation

### build_radiation.py

> __Input__: Fluent radiation distribution of the grate
>
> __Output__: FLIC radiation distribution of the grate

**Warning:** 使用过程中需要修改炉排的长度；在指定gap的时候尽量选小一点，否则容易超过FLIC上限14段。

## Data Analysis

### prof2csv.py

> __Input__: FLIC output (or Fluent input) prof file
>
> __Output__: CSV file with all variables

### csv2prof.py

> __Input__: CSV file with all variables
>
>__Output__: FILC output (or Fluent input) prof file
