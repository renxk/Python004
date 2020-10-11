# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd

from proxy_project.dbtool import DB


class ProxyProjectPipeline:
    def process_item(self, item, spider):
        name = item['name']
        type = item['type']
        time = item['time']
        with DB() as db:
            sql = """
                INSERT INTO maoyan(name, type, date) VALUES ('%s' , '%s', '%s')
            """ % (name, type, time)
            db.execute(sql)

        return item



