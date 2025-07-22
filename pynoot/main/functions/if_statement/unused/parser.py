
# coding if statment by using Parser 
# الكود ده بيقرأ كل سطر مكتوب بالعربي (زي لو، لو_تاني، وإلا)
# وبيحوّله لسطر بايثون حقيقي
# يعني مثلاً لو كتبت: لو(name == "نور")  
# هيحوّلها لـ: if name == "نور":

# نفس الفكرة لـ لو_تاني (اللي هي elif) و وإلا (اللي هي else)

# كل ده بيحصل جوه دالة اسمها parse_line
# اللي بتاخد السطر العربي وتحوله لكود بايثون يتنفذ 


def parse_line(line):
    line = line.strip()

    # لو (if)
    if line.startswith("لو("):
        condition_action = line[3:-1]  # شيل "لو(" من البداية و")" من الآخر
        parts = condition_action.split(",", 1)
        condition = parts[0].strip()
        action = parts[1].strip()
        return f'لو({condition}, {action})'

    # أي حاجة تانية:
    return line

# اقرأ الملف العربي
with open("Test_pynoot1", "r", encoding="utf-8") as f:
    lines = f.readlines()

# اكتب الملف الناتج
with open("output.py", "w", encoding="utf-8") as f:
    for line in lines:
        converted = parse_line(line)
        if converted:
            f.write(converted + "\n")

