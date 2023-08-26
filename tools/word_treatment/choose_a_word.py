import random
with open("tools/myfile.txt","r") as file:
	word_list = file.readlines()
	word_list = [word[:-1] for word in word_list]

word_index = random.randint(0,len(word_list)-1)

word_to_guesse = word_list[word_index]

if __name__ == "__main__":
	print(word_list)
	print(word_to_guesse)