month=input("enter the month:")
day=int(input("enter the date:"))
if(month=="Mar" and day>19)or(month=="Apr")or(month=="May")or(month=="Jun" and day<21):
    season='Summer'
elif(month=="Jun" and day>20)or(month=="Jul")or(month=="Aug")or(month=="Sep" and day<22):
    season=='Spring'
elif(month=="Sep"and day>21)or(month=="Oct")or(month=="Nov")or(month=="Dec" and day<21):
    season=='Fall'
else:
    season='Winter'
print("the current season is:",season)
