# doc-merger
使用 doc-merger 可以对两个文档中的内容进行比较和分析，然后在文档一的基础上，将文档二中的数据覆盖到文档一中对应的部分，输出合并结果并筛选出只存在于文档二中的数据。
<br>
<br>
## 功能演示
假设您有两个文本文件，`doc1.txt`和`doc2.txt`，这两个文件中都包含一些电视剧集的信息，但是信息都不完整，您希望使用`doc2.txt`补充和覆盖`doc1.txt`中的部分内容，并提取出只存在于`doc2.txt`中的数据。

`doc1.txt`的内容如下：
```
1;2023-01-01;45;The first episode
2;2023-01-08;45;The second episode
3;2023-01-15;45;The third episode
```
`doc2.txt`的内容如下：
```
2023-01-01;45;The first episode;This is the first episode of the show.
2023-01-08;45;The second episode;This is the second episode of the show.
2023-01-22;45;The fourth episode;This is the fourth episode of the show.
```
运行`doc-merger.py`脚本后，将生成一个名为`result.txt`的新文件，其中包含合并后的数据：
```
1;2023-01-01;45;The first episode;This is the first episode of the show.
2;2023-01-08;45;The second episode;This is the second episode of the show.
3;2023-01-15;45;The third episode;
```
此外，脚本还会生成一个名为`doc2_only.txt`的文件，其中包含只存在于`doc2.txt`中的数据：
```
2023-01-22;45;The fourth episode;This is the fourth episode of the show.
```
脚本还会打印一些统计信息：
```
Merged: 2
Doc1 only: 1
Doc2 only: 1
```
<br>

## 运行条件
请确保您的系统上安装了 Python 3.6 或更高版本。
<br>
<br>
## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改`start.command (Mac)`或`start.bat (Win)`中的路径，以指向您存放`doc-merger.py`脚本的目录。
3. 将要处理的文本分别保存为`doc1.txt`和`doc2.txt`文件，并放在与脚本相同的目录中。
4. 双击运行`start.command`或`start.bat`脚本以执行`doc-merger.py`脚本。
5. 结果将写入到同一目录下名为`result.txt`和`doc2_only.txt`的文件中。
<br>


# line-indexer
With doc-merger, you can compare and analyze the contents of two documents, then overlay the data from document two onto the corresponding part of document one based on document one, output the merged results and filter out data that only exists in document two.
<br>
<br>
## Demo
Suppose you have two text files,`doc1.txt`and`doc2.txt`, both of which contain some information about TV episodes, but the information is incomplete. You want to use`doc2.txt`to supplement and overwrite some of the content in`doc1.txt`, and extract data that only exists in`doc2.txt`.

The content of`doc1.txt`is as follows:
```
1;2023-01-01;45;The first episode
2;2023-01-08;45;The second episode
3;2023-01-15;45;The third episode
```
The content of`doc2.txt`is as follows:
```
2023-01-01;45;The first episode;This is the first episode of the show.
2023-01-08;45;The second episode;This is the second episode of the show.
2023-01-22;45;The fourth episode;This is the fourth episode of the show.
```
After running the`doc-merger.py`script, a new file named`result.txt`will be generated, which contains the merged data:
```
1;2023-01-01;45;The first episode;This is the first episode of the show.
2;2023-01-08;45;The second episode;This is the second episode of the show.
3;2023-01-15;45;The third episode;
```
In addition, the script will also generate a file named`doc2_only.txt`, which contains data that only exists in`doc2.txt`:
```
2023-01-22;45;The fourth episode;This is the fourth episode of the show.
```
The script will also print some statistical information:
```
Merged: 2
Doc1 only: 1
Doc2 only: 1
```
<br>

## Requirements
Make sure you have Python 3.6 or higher installed on your system.
<br>
<br>
## Usage
1. Clone or download the repository to a directory on your computer.
2. Modify the path in`start.command (Mac)`or`start.bat (Win)`to point to the directory where you store the`doc-merger.py`script.
3. Save the text to be processed as`doc1.txt`and`doc2.txt`files respectively and place them in the same directory as the script.
4. Double-click`start.command`or`start.bat`to execute the`doc-merger.py`script.
5. The result will be written to files named`result.txt`and`doc2_only.txt`in the same directory.
