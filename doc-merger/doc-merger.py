# 读取文档一中的内容
doc1 = {}
with open('doc1.txt', 'r') as f:
    for line in f:
        episode, date, duration, title = line.strip().split(';')
        doc1[title.lower()] = (episode, date, duration, '', title)

# 读取文档二中的内容
doc2 = {}
with open('doc2.txt', 'r') as f:
    for line in f:
        date, duration, title, description = line.strip().split(';')
        doc2[title.lower()] = (date, duration, description, title)

# 使用文档二中的内容覆盖文档一中的部分内容
success_count = 0
for title in doc2:
    if title in doc1:
        episode, _, _, _, _ = doc1[title]
        date, duration, description, original_title = doc2[title]
        doc1[title] = (episode, date, duration, description, original_title)
        success_count += 1

# 将结果写入新文档
with open('result.txt', 'w') as f:
    for title in doc1:
        episode, date, duration, description, original_title = doc1[title]
        f.write(f'{episode};{date};{duration};{original_title};{description}\n')

# 输出只存在于文档二中的数据
doc2_only_count = 0
with open('doc2_only.txt', 'w') as f:
    for title in doc2:
        if title not in doc1:
            date, duration, description, original_title = doc2[title]
            f.write(f'{date};{duration};{original_title};{description}\n')
            doc2_only_count += 1

# 统计只存在于文档一中的数据条数
doc1_only_count = 0
for title in doc1:
    if title not in doc2:
        doc1_only_count += 1

# 打印统计信息
print(f'Merged: {success_count}')
print(f'Doc1 only: {doc1_only_count}')
print(f'Doc2 only: {doc2_only_count}')
