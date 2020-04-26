import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def runner():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("Відкриття файлів")
    with open(os.path.join(BASE_DIR, 'Python.ipynb')) as f:
        py_notebook = nbformat.read(f, as_version=4)
    with open(os.path.join(BASE_DIR, 'C_Sharp.ipynb')) as f:
        cs_notebook = nbformat.read(f, as_version=4)
    with open(os.path.join(BASE_DIR, 'C_PlusPlus.ipynb')) as f:
        cpp_notebook = nbformat.read(f, as_version=4)

    print("Налаштування")
    py_ep = ExecutePreprocessor(kernel_name="python3")
    cs_ep = ExecutePreprocessor(kernel_name=".net-csharp")
    cpp_ep = ExecutePreprocessor(kernel_name="xcpp17")
    print("Виконується Python")
    py_ep.preprocess(py_notebook)
    print("Виконується C#")
    cs_ep.preprocess(cs_notebook)
    print("Виконується C++")
    cpp_ep.preprocess(cpp_notebook)
    
    print("Запис до файлів")
    with open(os.path.join(BASE_DIR, 'Python.ipynb'), 'w', encoding='utf-8') as f:
        nbformat.write(py_notebook,f)
    with open(os.path.join(BASE_DIR, 'C_Sharp.ipynb'), 'w', encoding='utf-8') as f:
        nbformat.write(cs_notebook,f)
    with open(os.path.join(BASE_DIR, 'C_PlusPlus.ipynb'), 'w', encoding='utf-8') as f:
        nbformat.write(cpp_notebook,f)
    print("Успішно завершено!")