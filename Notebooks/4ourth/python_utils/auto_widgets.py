import ipywidgets as widgets

def initialize():
    f_name = widgets.Text(
        value='start_values.tsv',
        description="Ім'я файлу:",
        disabled=False
    )
    number = widgets.IntSlider(
        value=100,
        min=1,
        max=1000,
        step=1,
        description='Кількість:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        layout=widgets.Layout(width='65%')
    )
    bottom = widgets.IntSlider(
        value=-400,
        min=-1000,
        max=-1,
        step=10,
        description='Від:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        layout=widgets.Layout(width='65%')
    )
    top = widgets.IntSlider(
        value=1000,
        min=10,
        max=1000,
        step=10,
        description='До:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        layout=widgets.Layout(width='65%')
    )
    error = widgets.IntSlider(
        value=13,
        min=0,
        max=25,
        step=1,
        description='Шанс помилки:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        layout=widgets.Layout(width='65%')
    )
    return f_name, number, bottom, top, error