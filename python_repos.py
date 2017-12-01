import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print('status code::', r.status_code)

response_dict = r.json()
print(response_dict.keys())

item_dict = response_dict['items']
names, plot_dicts = [], []

# 输出每个项目的一些信息
print('item keys::', item_dict[0].keys())
print("\nSelected information about first repository:")

for repo_dict in item_dict:
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at'])
    # print('Updated:', repo_dict['updated_at'])
    # print('Description:', repo_dict['description'])
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
# my_style = LS('#333366', base_style=LCS)

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_config.dots_size = 8

chart = pygal.Bar(my_config)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)

chart.render_to_file('python_repos.svg')
