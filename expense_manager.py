import numpy as np 
import pandas as pd  
import datetime as dt
import matplotlib.pyplot as plt 

def add_amount(amount):
    amont=float(input("ادخل المبلغ"))
    category=input("ادخل الفئة")
    date=dt.datetime.now().strftime("%Y-%m-%d,%I:%M")
    amount.append({"التاريخ": date,"الفئة":category,"المصروفات":amont})

# دالة لحفظ البيانات في ملف csv 
def save_data(amount):
    data=pd.DataFrame(amount,columns=["الفئة","التاريخ","المصروفات"])
    data.to_csv("ملف_بيانات_ادارة_الحسابات.csv",index=False,encoding="utf-8-sig",mode="a",header=False)
    
# دالة لعرض البيانات
def vew_amount(amount):
    data_read=pd.read_csv(r"ملف_بيانات_ادارة_الحسابات.csv")
    data_read.drop_duplicates(inplace=True)
    print(data_read)

# دالة لحساب اجمالي المصروفات  
def total_amount():
    data_read=pd.read_csv(r"ملف_بيانات_ادارة_الحسابات.csv")
    return data_read["المصروفات"].sum()

# دالة لتوضيح رسم البيانات
def graphcal():
    data=pd.read_csv(r"ملف_بيانات_ادارة_الحسابات.csv")
    label=data["الفئة"]
    data.groupby("الفئة")["المصروفات"].sum().plot(kind="pie",autopct="%1.1f%%")
    plt.xlabel("المصروفات")
    plt.ylabel("المصروفات")
    plt.grid(True)
    plt.show()
    plt.bar(data["الفئة"],data["المصروفات"])
    plt.xlabel("الفئة")
    plt.ylabel("المصروفات")
    plt.grid(True)
    plt.show()

amount=[]
print("1:الرقم واحد للاضافة\n", "2:الرقم اثنين للحفظ\n", "3:الرقم ثلاثة لعرض البيانات\n", "4:الرقم اربعة لعرض اجمالي المصروفات\n", "5:الرقم خمسة لتوضيح رسم البيانات\n", "6:الرقم ستة للخروج من البرنامج")

while True:
    n=input("اختار نوع العملية")
    if n=="1":
        add_amount(amount)
    if n=="2":
        save_data(amount)
    if n=="3": 
        vew_amount(amount)
    if n=="4":
        print("اجمالي المصروفات", total_amount()) 
    if n=="5":
        graphcal()
    if n=="6":
        break
        