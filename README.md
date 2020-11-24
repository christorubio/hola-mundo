# hola-mundo
Lab 12 and 14
Lab 12.7
def get_age():
    age = int(input())
    if age < 18:
        raise ValueError('Invalid age.')
    if age > 75:
        raise ValueError("Invalid age.")
    return age

def fat_burning_heart_rate(age):
  return .70*(220 - age)
   
if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as ve:
        print(ve)
        print("Could not calculate heart rate info.\n")
