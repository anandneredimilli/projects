# list and dictionary comprehension

#list comprehension
nums=[1,2,4,3,7,766,55,44,6,5]
even_nums=[]
for n in nums:
    if n%2==0:
        even_nums.append(n)
#print(even_nums)

#other way to do the above process
even_nums=[n for n in nums if n%2==0] #list comprehension
print(even_nums)


#dict comprehension
student_scores={
    'anand':12,
    'ahex':13,
    'yamaha':23,
    'korg':14
}
items=student_scores.items() 
#items() converts dict into list [(key1:value1),(key2:value2),....]
# passed_students={}
# for student,score in items:
#     if score>13:
#         passed_students[student]=score
#print(passed_students)

#other way to do above process
passed_students={student:score for student,score in items if score>13}
#dict comprehension
print(passed_students)


#exercise
sentence="what is the airspeed velocity of an unladen swallow"
# to convert string to list spilt() is used

list=sentence.split()
word_length={ word:len(word) for word in list   }
print(word_length)

#exercise
weather_celcius={"monday":12,
                 "teusday":14,
                 "wednesday":15,
                 "thursday":14,
                 "friday":21,
                 "saturday":22,
                 "sunday":24}

weather_farenheit={day:(temp*9/5)+32 for day,temp in weather_celcius.items()}
print(weather_farenheit)

#iterating a pandas data frame



car_prices_dict={
    'company':['volvo','benz','bugatti','lamborghini','kia'],
    'price':[2500000,5000000,30000000,15000000,1300000]
    
}
import pandas
car_prices_dataframe=pandas.DataFrame(car_prices_dict)
# for i,j in car_prices_dataframe.items():
#     print(j) #this looping is not particularly useful

#so pandas have a dataframe looping technique
for key,value in car_prices_dataframe.iterrows():
    # print(value) #value is series type
    print(value.company)
    print(value.price)
    if value.company=='benz':
        print("best luxury car manufacturer")

