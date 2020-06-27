#＃ 練習檔案讀取
data = []
count = 0
with open("reviews.txt","r") as f :    ##其中r 是讀取w是寫
	for na in f :
		data.append(na.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))

		##with 結束 讀取檔案就結束了
# 這種形式 只會顯示橫的 如果要直的必須用for



print("檔案已讀取完","共有",len(data),"筆資料")
n = 3
while n < 5:
	print(data[n])
	print("------------------------")
	n += 1
##計算平均留言字數
sum_len = 0
for d in data :
	sum_len += len(d)
print("平均留言字數為: ",sum_len/len(data))

newdata = []
for d in data :
	if len(d) < 100:
		newdata.append(d)

dd = 0
while dd <5 :
	print(newdata[dd])
	print("------------------------")
	dd += 1

good = []
for ddd in data: # 一定得提取 不然無法收集所需要的資料 進行整理
	if "good" in ddd:
		good.append(ddd)
print("總共有",len(good),"留言包含good")
print(good[2])
