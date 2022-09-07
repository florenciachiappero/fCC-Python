def add_time(start, duration, day=None):

    weekDays = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
    }


    # Getting data from start string
    startHour, midday = start.split()
    hour, minutes = startHour.split(":")
    hour = int(hour)
    minutes = int(minutes) 

    # 24 hour format 
    if midday == "PM":
        hour += 12


    # Getting data from duration string
    durationHour, durationMinutes = duration.split(":")
    durationHour = int(durationHour)
    durationMinutes = int(durationMinutes)


    # Calculate total minutes
    totalMinutes = minutes + durationMinutes
    newMinutes = int(totalMinutes % 60)
    if newMinutes < 10:
        newMinutes = '0' + str(newMinutes)
    else: 
        newMinutes = str(newMinutes)

    # Calculate hours
    plusHours = totalMinutes / 60
    totalHours = hour + durationHour + plusHours
    newHours = int((totalHours % 24) % 12)
    if newHours == 0:
        newHours = 12
    newHours = str(newHours)


    # Calculate days
    totalDays = int(totalHours / 24)

    
    # Get wether AM or PM
    newMidday = ""
    if (totalHours % 24) < 12:
        newMidday = "AM"
    else: 
        newMidday = "PM"
        
    
    # Return newTime
    newTime = newHours + ":" + newMinutes + " " + newMidday
    if day == None:
        if totalDays == 0: 
            return newTime
        if totalDays == 1: 
            return newTime + " (next day)"
        else:
            return newTime + " (" + str(totalDays) + " days later)"
    
    else:
      newDay = (weekDays[day.lower().capitalize()] + totalDays) % 7
      for i, j in weekDays.items():
          if j == newDay:
              newDay = i
              break

      if totalDays == 0:
          return newTime + ', ' + newDay
      if totalDays == 1:
          return newTime + ', ' + newDay + ' (next day)'
      return newTime + ', ' + newDay + ' (' + str(totalDays) + ' days later)'
    




    return new_time