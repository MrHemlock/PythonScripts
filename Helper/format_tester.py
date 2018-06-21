times = {}

for num_vars in (1, 2, 5, 10, 50, 250):
    f_str = "f'{" + '}{'.join([f'x{i}' for i in range(num_vars)]) + "}'"
    # "f'{x0}{x1}"
    concat = '+'.join([f'x{i}' for i in range(num_vars)])
    # 'x0+x1'
    pct_s = '"' + '%s'*num_vars + '" % (' + ','.join([f'x{i}' for i in range(num_vars)]) + ')'
    # '"%s%s" % (x0,x1)'
    dot_format = '"' + '{}'*num_vars + '".format(' + ','.join([f'x{i}' for i in range(num_vars)]) + ')'
    # '"{}{}".format(x0,x1)'
    dot_format2 = '"{' + '}{'.join([f'{i}' for i in range(num_vars)]) + '}".format(' + ','.join([f'x{i}' for i in range(num_vars)]) + ')'
    # '"{0}{1}".format(x0,x1)'

    vars = ','.join([f'x{i}' for i in range(num_vars)])
    vals_str = tuple(map(str, range(num_vars)))
    setup_str = f'{vars} = {vals_str}'
    # "x0,x1 = ('0', '1')"
    vals_int = tuple(range(num_vars))
    setup_int = f'{vars} = {vals_int}'
    # 'x0,x1 = (0, 1)'

    times[num_vars] = {
        'f_str_str': timeit(f_str, setup_str),
        'f_str_int': timeit(f_str, setup_int),
        'concat_str': timeit(concat, setup_str),
        # 'concat_int': timeit(concat, setup_int), # this will be summation, not concat
        'pct_s_str': timeit(pct_s, setup_str),
        'pct_s_int': timeit(pct_s, setup_int),
        'dot_format_str': timeit(dot_format, setup_str),
        'dot_format_int': timeit(dot_format, setup_int),
        'dot_format2_str': timeit(dot_format2, setup_str),
        'dot_format2_int': timeit(dot_format2, setup_int),
    }

table = BeautifulTable()
table.column_headers = ['Type \ num_vars'] + list(map(str, times.keys()))
# Order is preserved, so I didn't worry much
for key in ('f_str_str', 'f_str_int', 'concat_str', 'pct_s_str', 'pct_s_int', 'dot_format_str', 'dot_format_int', 'dot_format2_str', 'dot_format2_int'):
    table.append_row([key] + [times[num_vars][key] for num_vars in (1, 2, 5, 10, 50, 250)])
print(table)