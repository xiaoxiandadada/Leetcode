## 转置文件

awk '
{ 
for (i =1; i<=NF;i++)
col[i]=(NR==1?$i:col[i]" "$i)
}
END {
for (i=1;i<=NF;i++) {
print col[i]
}
}' file.txt

# cond ? x : y 如果 cond 为真 → 返回 x，否则返回 y