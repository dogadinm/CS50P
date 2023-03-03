def main():
    i = input('What time is it ? ')
    time = convert(i)

    if time >= 7 and time <= 8:
        print('breakfast time')

    if time >= 12 and  time <= 13:
        print('lunch time')

    if time >= 18 and time <= 19:
        print('dinner time')



def convert(time):
    hours, minutes = time.split(':')
    nmin = float(minutes) / 60
    return float (hours) + nmin


if __name__ == "__main__":
    main()