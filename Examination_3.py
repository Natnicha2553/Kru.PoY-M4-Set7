price = float(input("ราคาเต็ม: "))
is_member = int(input("/10: "))
if is_member % 1:
  print("เป็นสมาชิก")
elif is_member % 0:
  print("ไม่เป็นสมาชิก")
