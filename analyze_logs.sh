#!/bin/bash

report="report.txt"
> $report

echo "Отчет о логе веб-сервера" >> $report
echo "==========" >> $report

# Считаем количество запросов
total_requests=$(wc -l < access.log)
echo "Общее количество запросов:" >> $report
echo "$total_requests" >> $report
echo "" >> $report

# Получаем уникальные IP
echo "Количество уникальных IP-адресов:" >> $report
awk '{ip[$1]++} END {print length(ip)}' access.log >> $report
echo "" >> $report

# Получаем методы запросов
echo "Количество запросов по методам:" >> $report

awk -F'"' '
{
    split($2, req, " ")
    method[req[1]]++
}
END {
    for (m in method)
        print method[m], m
}
' access.log | sort -rn >> $report

# Самый популярный URL
echo "Самый популярный URL:" >> $report
awk -F'"' '
{
    split($2, parts, " ");
    url = parts[2];
    urls[url]++
}
END {
    max = 0;
    for (u in urls) {
        if (urls[u] > max) {
            max = urls[u];
            max_url = u
        }
    }
    print "  " max " " max_url ""
}
' access.log >> $report

# Выводим результат
cat $report