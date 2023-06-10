import pandas

#read csv file
nato_data=pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data_dict={i.letter:i.code for k,i in nato_data.iterrows()}

'''1st way'''
# user_input=input("enter your name:").upper()

# l1=[]
# l2=[]
# for i in user_input:
#     l1.append(i)
# l2=[j for k in l1 for i,j in nato_data_dict.items() if i==k]        
# print(l2)

'''2nd way'''
words=[]
# n=True
# while n:
#     try:
#         user_input=input("enter your name:").upper()
#         words = [nato_data_dict[i] for i in user_input]
#         print(words)
#         n=False
#     except KeyError:
#         print("please enter characters only.")

'''3rd way'''
def generate_phenotic():
    try:
        user_input=input("enter your name:").upper()
        if user_input=='':
            raise Exception
        words = [nato_data_dict[i] for i in user_input]
        
        
    except KeyError:
        print("please enter characters only.")
        generate_phenotic()
    except Exception:
        print("enter characters, dont leave it blank")
        generate_phenotic()
    else:
        print(words)
generate_phenotic()

# print(.letter)