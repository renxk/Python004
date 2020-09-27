# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pandas as pd

class MaoyanPipeline:
    def process_item(self, item, spider):
        name = item['name']
        type = item['type']
        time = item['time']
        dt = {
            '电影名称': [name],
            '电影类型': [type],
            '上映时间': [time]
        }

        movie_csv = pd.DataFrame(data=dt)
        movie_csv.to_csv('./maoyan_movies.csv', encoding='utf8', index=False, mode='a', header=False)
        return item
