# import matplotlib.pyplot as plt
# subjects=["hindi", "mararthi", "english", "computer", "science"]
# marks=[67, 45, 75, 65, 76]
# plt.bar(subjects, marks)
# plt.title("Marks of subjects")
# plt.xlabel("subjects")
# plt.ylabel("marks")
# plt.show()



# import matplotlib.pyplot as plt
# monthly=["Jan", "Feb", "Mar", "Apr" , "May"]
# sales=[3000, 5000, 7000, 9000, 11000]
# plt.plot(monthly, sales)
# plt.title("Monthly sales of a company")
# plt.xlabel("monthly")
# plt.ylabel("sales")
# plt.show()



# import matplotlib.pyplot as plt
# market_shares=[6000, 7000, 9000, 11000, 13000]
# mobile_brands=["Vivo", "Xiaomi", "Galaxy", "Honor", "Oppo"]
# plt.pie(market_shares, labels=mobile_brands, autopct="%1.1f%%")
# plt.title("Market shares of different mobile brands")
# plt.show()



# import matplotlib.pyplot as plt
# Marks=[35, 40, 45, 50, 55, 60, 65, 70, 75, 62, 68, 72, 78, 80, 82, 85, 88, 90]
# plt.hist(Marks, bins=5)
# plt.title("Distribution of examination")
# plt.xlabel("Marks")
# plt.ylabel("Number of students")
# plt.show()



# import matplotlib.pyplot as plt
# hours=[1, 2, 3, 4, 5, 6, 7, 8] 
# scores=[40, 45, 50, 60, 65, 70, 80, 90]
# plt.scatter(hours, scores)
# plt.title("study hours vs examination scores")
# plt.xlabel("study hours")
# plt.ylabel("examination scores")
# plt.show()



import matplotlib.pyplot as plt
rainfall=[20, 30, 25, 40, 60]
months=["May", "Jun", "Jul", "Aug", "Sep"]
plt.fill_between(months, rainfall)
plt.title("Monthly rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall")
plt.show()