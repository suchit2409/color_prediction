from threading import _DummyThread
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

first_number = open("firstnumber.txt", "r+")
Weather = first_number.read().strip().split()
print(Weather)
second_number = open("secondnumber.txt", "r+")
Temp = second_number.read().strip().split()
print(Temp)
third_number = open("thirdnumber.txt","r+")
line3 = third_number.read().strip().split()
print(line3)
fourth_number = open("fourthnumber.txt","r+")
line4 = fourth_number.read().strip().split()
print(line4)
ans = open("ans.txt","r+")
Play = ans.read().strip().split()
print(Play)
while(1):
    weather_encoded = le.fit_transform(Weather)
    # print("weather:",weather_encoded)
    temp_encoded = le.fit_transform(Temp)
    # print("temp:",temp_encoded)
    line3_encoded = le.fit_transform(line3)
    # print("line3 :",line3_encoded)
    line4_encoded = le.fit_transform(line4)
    # print("line4 :",line4_encoded)
    label = le.fit_transform(Play)
    # print("label:", label)
    features = list(zip(weather_encoded,temp_encoded,line3_encoded, line4_encoded))

    from sklearn.naive_bayes import GaussianNB
    sf = input("Press Enter to Start")
    a = input("first number")
    # first_number.write(f"{a}\n")
    
    b = input("second number")
    # second_number.write(f"{b}\n")
    
    c = input("third number")
    # third_number.write(f"{c}\n")
    
    d = input("fourth number")
    # fourth_number.write(f"{d}\n")
    

    model = GaussianNB()
    model.fit(features, label)
    predict = model.predict([[a,b,c,d]])
    print ("predicted values are:", predict)
    if predict < 5:
        print("blue")
    else :
        print("yellow")
    e = int(input("actual output :"))
    
    # ans.write(f"{e}\n")
    
    