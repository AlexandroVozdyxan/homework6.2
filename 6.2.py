seconds = int(input("Ente a number: "))
max_time = 8640000
min_time = 0
if seconds > max_time:
     print("Error")
elif seconds <= min_time:
        print("Error")
else:
     days = seconds // (24 * 60 * 60)
     seconds = seconds % (24 * 60 * 60)
     hours = seconds // (60 * 60)
     seconds = seconds % (60 * 60)
     minutes = seconds // 60
     seconds = seconds % 60

     total_time = f"Days: {days}, Hours: {hours} Minutes: {minutes} Seconds: {seconds}"
     print(total_time)
