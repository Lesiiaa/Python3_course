#dictionary in list
people2 = [
          {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
            {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
            {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
            
          ]
#append adds element at the end of the list

#dictionary in dictionary
people = {
              "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},                                  
              "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
              "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'}, 
              "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
              "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
              "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
          }
#when adding a new item, the order is not important

print(people["IcFDG2bO9AYDF651DoyH"])