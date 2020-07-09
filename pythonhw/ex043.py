#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 請依註解提示完成程式

# 有一筆資料如下, 依序為內含姓名, 生日, 身高, 體重的字串
# 請用 str.split() 將它指定給學生清單 student, 然後列印出來
data = "小明 1984-07-22 180 60"
student=data.split(' ')
print(student)

# 請用 L.extend 或 += 方式將國語, 英語, 數學三科分數 95, 65, 90
# 加到清單 student 後面, 然後列印出來
student.extend([95,65,90])
print(student)

# 我們注意到身高體重還是字串型態, 請將它們從 student 清單中改成整數型態
# 一樣列印出來
student[2]=int(student[2])
student[3]=int(student[3])
print(student)

# 我們想把這筆資料分成 name=姓名, info=[生日,身高,體重]
# chi=國語, eng=英語, math=數學, 請用星號前綴 * 的分法分割
# 然後只要列印出 info 學生個資部份
name,*info,chi,eng,math=student
print(info)
# 請將小明的三科成績由小到大排序並列印出來
# 提示 : 請將成績切片出來, 並用 L.sort() 排序之
a=[chi,eng,math]
a.sort()
print(a)

# 假設成績大於或等於90分就可以得到一個A, 下面程式會列出小明得到幾個A
# 請將它改寫成 List Comprehension 一行語法, 並列印出幾個A
# grade = []
# for i in range(4,7):
#     if student[i] >= 90:
#         grade.append("A")
# print(grade)
print(["A" for i in range(0,3) if a[i] >= 90])

