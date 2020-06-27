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
while n < 7:
	print(data[n])
	print("------------------------")
	n += 1
