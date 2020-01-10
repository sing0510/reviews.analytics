data = []
count = 0

with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))


print('檔案讀取完成,總共有',len(data),'個檔案')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	if sum_len % 10000 == 0:
		print(sum_len)
	
print('留言的平均長度' , sum_len/len(data))





