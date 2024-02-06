def label_encode(data):
    unique_values = list(set(data))
    encoding_dict = {val: i for i, val in enumerate(unique_values)}
    encoded_data = [encoding_dict[val] for val in data]
    
    return encoded_data, encoding_dict


user_input = input("Enter categorical values separated by spaces: ")


data = user_input.split()


encoded_data, encoding_dict = label_encode(data)

print("Original Data:", data)
print("Encoded Data:", encoded_data)

print("\nEncoding Dictionary:") 
for key, value in encoding_dict.items():
    print(f"{key}: {value}")

