
def openfile():
	data = []
	with open('reviews.txt','r') as f:
		for line in f:
			data.append(line)
	return data


	print('檔案讀取完成,總共有',len(data),'個檔案')

def cw(data): #check word in reviews
	wc = {} #word_count
	for d in data:
		words = d.split(' ')
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1 #新增新的key進wc字典
	for word in wc:
		if wc[word] > 10000:
			print(word, wc[word])

	while True:
		word = input('請問想查什麼字?')
		if word == 'q':
			break
		elif word not in wc:
			print('沒有此字')
		else:
			print(word, '出現過的次數為',wc[word])

	print('感謝便用')

def alir(): # average word len in reviews 
	sum_len = 0
	for d in data:
		sum_len = sum_len + len(d)
		if sum_len % 10000 == 0:
			print(sum_len)
		
	print('留言的平均長度' , sum_len/len(data))

	new = []
	for d in data:
		if len(d) < 100:
			new.append(d)
	print('一共有', len(new), '筆留言長度小於100')
	print(new[0])
	print(new[1])

def cwir(): #check word in reviews
	good = []
	for d in data:
			if 'good' in d:
				good.append(d)

	print('一共有', len(good), '筆留言包含good字')

	good = [d for d in data if 'good' in d ]

	print (len(good))

data = openfile()
cw(data)
alir()
cwir()

