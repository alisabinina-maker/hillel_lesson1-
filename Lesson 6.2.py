seconds = int(input(" Input seconds (0 - 8640000): "))

if 0 <= seconds < 8640000:

    days, remainder = divmod(seconds, 86400)

    hours, remainder = divmod(remainder, 3600)

    minutes, secs = divmod(remainder, 60)


    if days == 1:
        word = "day"
    elif 2 <= days <= 4:
        word = "days"
    else:
        word = "days"


    print(f"{days} {word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}")

else:
    print("Number supposed to be from 0 to 8640000!")
