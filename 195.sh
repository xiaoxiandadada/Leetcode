## 第十行
# awk 'NR == 10' file.txt

row_number=$(cat file.txt | wc -l)

if [ $row_number -le 10 ]; then
    echo "The number of row is less than 10"
else
    sed -n '10p' file.txt
    echo
fi

## file.txt
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10