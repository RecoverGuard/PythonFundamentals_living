
#how to create a dictionary

extension_list = {'Albert' : 'ext21', 'Beth' : 'ext42', 'Charles' : 'ext07'}
print(extension_list)

#how to index a dictionary

print(extension_list['Albert'])  #ext21
print(extension_list['Beth'])   #ext42
print(extension_list['Charles']) #ext07


#get the keys of a dictionary

print(extension_list.keys())

#get the values of a dictionary

print(extension_list.values())

x = [2, 4, 6]     #[2, 4, 6]
x.append(8)     #update [2, 4, 6, 8]

extension_list.update({'Terry' : 'ext67'})
print(extension_list)

extension_list.update({'Albert' : 'ext100'})
print(extension_list.get('Albert'))
extension_list['Beth'] = 'ext55'
print(extension_list)

#dictionary example

phone_book = { 'pizza': ['253-347-4456', '253-342-4421', '253-124-6570'],
               'auto' : ['253-342-5555', '253-343-3434', '253-667-2323'],
               'salon' : ['253-123-4321', '253-989-7878']}

print(phone_book['pizza'])
print(phone_book['pizza'][1])
