def duplicated_sensors (list_id_sensors):

    sensor_dictionary = {}

    for id in list_id_sensors:
        if id in sensor_dictionary:
            sensor_dictionary[id] += 1
        else:
            sensor_dictionary[id] = 1
    
    list_duplicated_sensors = []

    for id in sensor_dictionary:
        if sensor_dictionary[id] > 1:
            list_duplicated_sensors.append(id)
    
    return list_duplicated_sensors

id_sensors = [12, 15, 12, 8, 9, 15, 12, 20, 8]

result = duplicated_sensors(id_sensors)
print(f"The duplicated sensors are {result}")
