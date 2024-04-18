# #pip install matplotlib
# import matplotlib.pyplot as pt

# def focus_graph():
#     file = open("focus.txt","r")
#     content = file.read()
#     file.close()
#     content = content.split(",")
#     x1 = []
#     y1 = []
#     for i in range(0,len(content)):
#         if content[i]: 
#             content[i] = float(content[i])
#             x1.append(i)
#             y1.append(content[i])
        
#     print(content)
#     y1 = content
#     pt.plot(x1, y1, color="red", marker="o")
#     pt.title("Your Focus Time ",fontsize = 14)
#     pt.xlabel("Times",fontsize = 14)
#     pt.ylabel("Focus Times",fontsize = 14)
#     pt.grid()
#     pt.show()

import matplotlib.pyplot as pt

def focus_graph():
    file = open("focus.txt", "r")
    content = file.read()
    file.close()
    content = content.split(",")
    x1 = []
    y1 = []
    for i in range(len(content)):
        if content[i]:  # Check if the string is not empty
            content[i] = float(content[i])
            x1.append(i)
            y1.append(content[i])
        
    print(content)
    pt.plot(x1, y1, color="red", marker="o")  # 'colors' should be 'color'
    pt.title("Your Focus Time", fontsize=14)
    pt.xlabel("Times", fontsize=14)
    pt.ylabel("Focus Times", fontsize=14)
    pt.grid()
    pt.show()

focus_graph()
