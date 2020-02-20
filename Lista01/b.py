num_cars = int(input())
persons = input()

persons_splitted = persons.split(" ")

total_person = 0

for num_person in persons_splitted:
    total_person += int(num_person)

total_cars = 0

for car in range(num_cars):
    if total_person <= 0:
        break
    
    total_person = total_person - 5
    total_cars += 1

print(total_cars)