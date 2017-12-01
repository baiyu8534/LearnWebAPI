import pygal

from pygal.style import LightColorizedStyle as LCS

chart = pygal.Bar(x_label_rotation=45, show_legend=False)

chart.title = 'python_Projects'
chart.x_labels = ['https', 'django', 'flask']

# 'label': 'Description of httpie.' 自定义提示信息
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
