import pandas as pd

def warnings_list(warnings, conclusion, py_data, cs_data, cpp_data):
    start_data = pd.read_csv('start_values.tsv', sep='\t', names=['a','b','c','d'])
    for index in warnings:
        bool_s = pd.Series({
            0: '&#10004;' if conclusion.Py_Cs[index] else '&#10006;',
            1: '&#10004;' if conclusion.Py_Cpp[index] else '&#10006;',
            2: '&#10004;' if conclusion.Cs_Cpp[index] else '&#10006;'
        })
        data_s = pd.Series({
            "py" : dict(
                first=round(float(py_data.First[index]),4),
                second=round(float(py_data.Second[index]),4),
                third=round(float(py_data.Third[index]),4),
                fourth=round(float(py_data.Fourth[index]),4),
                fifth=round(float(py_data.Fifth[index]),4),
                sixth=round(float(py_data.Sixth[index]),4),
                seventh=round(float(py_data.Seventh[index]),4),
                result=round(float(py_data.Result[index]),4)
            ),
            "cs" : dict(
                first=round(float(cs_data.First[index]),4),
                second=round(float(cs_data.Second[index]),4),
                third=round(float(cs_data.Third[index]),4),
                fourth=round(float(cs_data.Fourth[index]),4),
                fifth=round(float(cs_data.Fifth[index]),4),
                sixth=round(float(cs_data.Sixth[index]),4),
                seventh=round(float(cs_data.Seventh[index]),4),
                result=round(float(cs_data.Result[index]),4)
            ),
            "cpp" : dict(
                first=round(float(cpp_data.First[index]),4),
                second=round(float(cpp_data.Second[index]),4),
                third=round(float(cpp_data.Third[index]),4),
                fourth=round(float(cpp_data.Fourth[index]),4),
                fifth=round(float(cpp_data.Fifth[index]),4),
                sixth=round(float(cpp_data.Sixth[index]),4),
                seventh=round(float(cpp_data.Seventh[index]),4),
                result=round(float(cpp_data.Result[index]),4)
            )
        })
        start_s = pd.Series({
            'a': start_data.a[index],
            'b': start_data.b[index],
            'c': start_data.c[index],
            'd': start_data.d[index],
        })
        table = f"""<table>
                        <tr>
                            <th>Index</th>
                            <th>Py vs C#</th>
                            <th>Py vs C++</th>
                            <th>C# vs C++</th>
                        </tr>
                        <tr>
                            <td>{index}</td>
                            <td>{bool_s[0]}</td>
                            <td>{bool_s[1]}</td>
                            <td>{bool_s[2]}</td>
                        </tr>
                    </table>"""
        py_formula = rf"""Python \\
        \frac{{ \lg(4*{start_s.b}-{start_s.c})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} =
        \frac{{ \lg({data_s.py['first']}-{start_s.c})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = \\
        \frac{{ \lg({data_s.py['second']})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = 
        \frac{{ \textbf{{{data_s.py['third']}*{start_s.a}}} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = \\
        \frac{{ \textbf{{ {data_s.py['fourth']} }} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = 
        \frac{{ {data_s.py['fourth']} }}{{{start_s.b}+({data_s.py['fifth']})-1}} = \\
        \frac{{ {data_s.py['fourth']} }}{{{data_s.py['sixth']}-1}} = 
        \frac{{ {data_s.py['fourth']} }}{{{data_s.py['seventh']}}} = {data_s.py['result']} \\
        """
        cs_formula = rf"""\\ C\# \\
        \frac{{ \lg(4*{start_s.b}-{start_s.c})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} =
        \frac{{ \lg({data_s.cs['first']}-{start_s.c})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = \\
        \frac{{ \lg({data_s.cs['second']})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = 
        \frac{{ \textbf{{{data_s.cs['third']}*{start_s.a}}} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = \\
        \frac{{ \textbf{{ {data_s.cs['fourth']} }} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = 
        \frac{{ {data_s.cs['fourth']} }}{{{start_s.b}+({data_s.cs['fifth']})-1}} = \\
        \frac{{ {data_s.cs['fourth']} }}{{{data_s.cs['sixth']}-1}} = 
        \frac{{ {data_s.cs['fourth']} }}{{{data_s.cs['seventh']}}} = {data_s.cs['result']} \\
        """
        cpp_formula = rf"""\\ C++ \\
        \frac{{ \lg(4*{start_s.b}-{start_s.c})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} =
        \frac{{ \lg({data_s.cpp['first']}-{start_s.c})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = \\
        \frac{{ \lg({data_s.cpp['second']})*{start_s.a} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = 
        \frac{{ \textbf{{{data_s.cpp['third']}*{start_s.a}}} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = \\
        \frac{{ \textbf{{ {data_s.cpp['fourth']} }} }}{{{start_s.b}+({start_s.c}/{start_s.d})-1}} = 
        \frac{{ {data_s.cpp['fourth']} }}{{{start_s.b}+({data_s.cpp['fifth']})-1}} = \\
        \frac{{ {data_s.cpp['fourth']} }}{{{data_s.cpp['sixth']}-1}} = 
        \frac{{ {data_s.cpp['fourth']} }}{{{data_s.cpp['seventh']}}} = {data_s.cpp['result']} \\
        """
        yield table, py_formula + cs_formula + cpp_formula