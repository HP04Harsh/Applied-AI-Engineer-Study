temp = int(input("Enter the temperature: "))
device_status = input("Enter the Device Status Active/Disabled: ")

if temp>35 and device_status=="Active":
  print("🚨 Warning! HIGH Temperature ahead")
elif temp>35 and device_status=="Disabled":
  print("Device is Disabled")
else:
  print("Normal Day")