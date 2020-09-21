# <<<<<<< HEAD
# -*- coding=utf-8 -*-
#@author:liuAmon
#@contact:utopfish@163.com
#@file:bytedance_01.py
#@time: 2020/9/20 20:34
s="aba"*1000000+'c'
import time

start=time.time()
def get_next(p):
    n=len(p)
    nex=[0]*(n)
    nex[0]=0
    i,j=0,0
    for i in range(1,n):
        while j and s[i]!=s[j]:
            j=nex[j-1]
        if s[i]==s[j]:
            j+=1
        nex[i]=j
    return nex
l=len(s)
next=get_next(s)
print(s[:l-next[l-1]])
print("耗时:{}".format(str(time.time()-start)))

sss=time.time()
i, start, end, length = 1, 0, 1, len(s)
while i < length:
    if s[i] != s[start]:
        i=end = i + 1
    else:
        tmp = i + end - start
        if tmp <= length:
            if s[start:end] == s[i:tmp]:
                i = tmp
                continue
            else:
                i = end = end + 1
        else:
            end = length
            break

if end - start < length:
    print(''.join(s[start:end]))
else:
    print(s)
print("耗时:{}".format(str(time.time()-sss)))


start=time.time()
flag=0
for i in range(1,len(s)):
    if s==(s+s)[i:len(s)+i]:
        flag=1
        print(s[:i])
        break
if flag==0:
    print(s)
print("耗时:{}".format(str(time.time()-start)))


# =======
# #@Time:2020/9/19 14:59
# #@Author:liuAmon
# #@e-mail:utopfish@163.com
# #@File:bytedance_01.py
# __author__ = "liuAmon"
#
# """
# 描述：
# 输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度 第3行为一个正整数q代表查
# 询的组数  第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的
# 个数。 数据范围n <= 300000,q<=300000 k是整型
#
# 输入:
# 5
# 1 2 3 3 5
# 3
# 1 2 1
# 2 4 5
# 3 5 3
# 输出：
# 1
# 0
# 2
# """
#
# n=int(input())
# nums=list(map(int,input().split()))
# q_times=int(input())
# q=[]
# for _ in range(q_times):
#     q.append(list(map(int, input().split())))
# r={}
# for index,i in enumerate(nums):
#     r[i]=r.get(i,[])+[index]
# for i in q:
#     temp=r[i[2]]
#     count =0
#     for t in temp:
#         if t in range(i[0]-1,i[1]):
#             count+=1
#     print(count)
# >>>>>>> 21d27cf3fababaf4b7976371bd426c3b0b179f43
