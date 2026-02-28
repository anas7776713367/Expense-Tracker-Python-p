import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# دالة اضافة
def add_amount(amount):
    amont=float(input("المبلغ ادخل(("))
    input=category
    date=dt.datetime.now().strftime("%Y-%m-%d,%I:%M")
    ["المصروفات","الفئة","التاريخ"]=d
    amount.append({"التاريخ": date,"الفئة":category,"المصروفات":amont,})
    data=pd.DataFrame(columns=d)
    data.to_csv("data.csv",index=False)

# csv دالة لحفظ البانات في ملف
def save_data(amount):
    data=pd.DataFrame(amount)
    file=data.to_csv("data.csv",index=False,encoding="utf-8-sig",mode="a",header=False)

# دالة لعرض البانات
def vew_amount(amount):
    # data_read=pd.read_csv(r"الحسابات_ادارة_بيانات_ملف.csv")
    data_read=pd.read_csv(r"data.csv")
    data_read.drop_duplicates(inplace=True)
    display(data_read)

# دالة لحساب اجملي المصروفات
def total_amount():
    data_read=pd.read_csv(r"data.csv")
    return data_read["المصروفات["].sum()

# دالة لتوضيح رسم البيانات
def graphcal():
    data=pd.read_csv(r"data.csv")
    label=data["الفئة["]
    data.groupby("الفئة")("المصروفات[".sum().plot(kind="pie",autopct="%1.1f%%")
    plt.legend()
    plt.xlabel("المصروفات(")
    plt.ylabel("الفئات(")
    plt.grid(True)
    plt.show()
    plt.bar(data["الفئة["],data["المصروفات["],width=0.1)
    plt.xlabel("الفئة(")
    plt.ylabel("المصروفات(")
    plt.grid(True)
    plt.show()

amount=[]
print("الرقم واحد لالضافة1:","n\الرقم اثنين للحفظ2:","n\الرقم ثالثة لعرض البيانات3:","n\الرقم اربعة لعرض اجمالي المصروفات4:")
print("الرقم خمسة لتوضيح رسم البيانات5:","n\الرقم ستة للخروج من البرنامج6:")

while True:
    n=input("ادخل نوع العملية")
    if n=="1":
        add_amount(amount)
    if n=="2":
        save_data(amount)
    if n=="3":
        vew_amount(amount)
    if n=="4":
        print("المصروفات اجمالي",total_amount())
    if n=="5":
        graphcal()
    if n=="6":
        break
    
