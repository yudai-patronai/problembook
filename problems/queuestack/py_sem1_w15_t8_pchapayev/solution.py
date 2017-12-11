def play(cardset):
	stack=[]
	res=0
	for token in cardset.split():
		if stack and token[0]==stack[-1][0] and abs(int(token[1])-int(stack[-1][1]))<=2:
			res+=2
			stack.pop()
			if len(stack)>=2 and stack[-1][0]==stack[0][0]:
				res+=2
				stack.pop()
				stack.pop(0)
				stack.append(token)
		else:
			stack.append(token)
	return res

if __name__=="__main__":
	print(play(input()))