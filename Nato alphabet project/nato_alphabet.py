import pandas

#read csv file
nato_data=pandas.read_csv("Python/csv/Nato alphabet project/nato_phonetic_alphabet.csv")

nato_data_dict={i.letter:i.code for k,i in nato_data.iterrows()}
user_input=input("enter your name:").upper()
l1=[]
l2=[]
for i in user_input:
    l1.append(i)
l2=[j for k in l1 for i,j in nato_data_dict.items() if i==k]        
print(l2)

# print(.letter)