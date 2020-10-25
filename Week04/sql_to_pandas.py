# _*_ encoding:utf-8 _*_
# Author: renxk

import pandas as pd
import  numpy as np

#创建数据
size = 200
df = pd.DataFrame({
    'id' : np.random.randint(0, 2000, size),
    'age' : np.random.randint(1, 100, size)
})


table1 = pd.DataFrame({
    'id' : np.random.randint(0, 2000, size),
    'order_id' : np.random.randint(1, 20000, size)
})

# 1.SELECT * FROM data;
print('=' * 20 + '1.SELECT * FROM data;' + '=' * 20)
print(df)
print('=' * 50)
print()

# 2. SELECT * FROM data LIMIT 10;
print('=' * 20 + 'SELECT * FROM data LIMIT 10;' + '=' * 20)
print(df.head(10))
print('=' * 50)
print(df[:10])
print('=' * 50)
print()

# 3. SELECT id FROM data;
print('=' * 20 + '3. SELECT id FROM data;' + '=' * 20)
print(df['id'])
print('=' * 50)
print()


# 4. SELECT COUNT(id) FROM data;
print('=' * 20 + '4. SELECT COUNT(id) FROM data;' + '=' * 20)
print(df['id'].count())
print('=' * 50)
print()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print('=' * 20 + '5. SELECT * FROM data WHERE id<1000 AND age>30;' + '=' * 20)
print(df[(df['id'] < 1000) & (df['age'] > 30)])
print('=' * 50)
print()

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print('=' * 20 + '6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;' + '=' * 20)
print(table1.groupby('id').agg({'order_id': pd.Series.nunique}))
print('=' * 50)
print()

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print('=' * 20 + '7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;' + '=' * 20)
print(pd.merge(df, table1, on="id"))
print('=' * 50)
print()

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print('=' * 20 + '8. SELECT * FROM table1 UNION SELECT * FROM table2;' + '=' * 20)
print(pd.concat([df, table1]).drop_duplicates())
print('=' * 50)
print()

# 9. DELETE FROM table1 WHERE id=10;
print('=' * 20 + '9. DELETE FROM table1 WHERE id=10;' + '=' * 20)
print(df.drop(df[df['id'] == 10].index))
print('=' * 50)
print()

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print('=' * 20 + '10. ALTER TABLE table1 DROP COLUMN column_name;' + '=' * 20)
print(df.drop('id', axis=1))
print('=' * 50)
print()