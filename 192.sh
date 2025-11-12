## 统计词频
tr -s ' ' '\n' < words.txt |sort |uniq -c |sort -r |awk '{print $2,$1}'

## uniq -c在行首显示该行重复出现的次数
## tr -s ' ' '\n' 将空格替换为换行符
## sort 对单词进行排序，使得相同的单词相邻