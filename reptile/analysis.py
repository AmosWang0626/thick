# 解析网页数据

# 模糊匹配   1.正则表达式
# 结构化解析 2.html.parser
# 结构化解析 3.Beautiful Soup
# 结构化解析 4.lxml

# 其中: 2 <--- 3 ---> 4

# 学习Beautiful Soup

import re

from bs4 import BeautifulSoup

html_doc = '<a href="https://alpha.wallhaven.cc/wallpaper/682481"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-682481.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/681363"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-681363.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/681052"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-681052.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/680441"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-680441.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/679282"><img class="s1" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-679282.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/678669"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-678669.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/678855"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-678855.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/678905"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-678905.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/676594"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-676594.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/675521"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-675521.jpg" alt=""></a>' \
           '<a href="https://alpha.wallhaven.cc/wallpaper/675395"><img class="s0" src="//wallpapers.wallhaven.cc/wallpapers/thumb/small/th-675395.jpg" alt=""></a>'

soup = BeautifulSoup(html_doc, 'html.parser')

img_info = soup.find_all('img', src=re.compile('//wallpapers.wallhaven.cc/wallpapers/thumb/small/'))

print(img_info)

for img in img_info:
    print(img.find_all('img', class_='s1'))
