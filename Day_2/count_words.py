def brand_counter (car_brand_list):

    car_brand_dictionary = {}
    brand_counter = 0
    most_seen_brand = car_brand_list[0]

    for brand in car_brand_list:
        if brand in car_brand_dictionary:
            car_brand_dictionary[brand] += 1
        else:
            car_brand_dictionary[brand] = 1
        
        if car_brand_dictionary[brand] > brand_counter:
            brand_counter = car_brand_dictionary[brand]
            most_seen_brand = brand
    
    return car_brand_dictionary, most_seen_brand

car_brand_list = ["audi", "bmw", "ford", "audi", "dacia", "bmw"]

result = brand_counter(car_brand_list)
print(result)

