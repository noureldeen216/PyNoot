def ادخل_عنصر(list_object, place, item):
    list_object.insert(place, item)




# Code Explain BY Nour_eldeen Ahmed
    
    #def ادخل_عنصر(list_object, place, item):
    # here it works as a space like for example "place" python understand this is the place where we want to write in and for item is second spot that python
    # understands as a real built in item but in the end they r u custom 
     # (list_object, place, item)

    #list_object.insert(place, item)








# Function DOC 
def ادخل_عنصر(القائمة, الموقع, العنصر):
    """
    📥 **ادخل_عنصر (Insert)**

    **شغلانتها**: بتحط عنصر جديد في مكان محدد أنت بتختاره جوه القائمة، وبتحرك باقي العناصر عشان تفضي له مكان.
    
    ---

    ### 📝 المكونات:
    * **القائمة**: القائمة اللي عايز تضيف فيها.
    * **الموقع**: رقم المكان (الـ Index) اللي عايز العنصر ينزل فيه (بيبدأ من 0).
    * **العنصر**: الحاجة اللي عايز تحطها (نص، رقم، إلخ).
    
    ---

    ### ✨ مثال:
    # قائمة فيها شوية طلبات
الطلبات = ["رز", "سكر"]

# عايزين نحط "زيت" في النص (الموقع رقم 1)
ادخل_عنصر(الطلبات, 1, "زيت")

# اطبع عشان تشوف النتيجة
اطبع(الطلبات) 
# النتيجة: ['رز', 'زيت', 'سكر']
    """
    القائمة.insert(الموقع, العنصر)