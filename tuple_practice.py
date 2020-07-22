import time

tuple_record = ('eth0', '192.168.1.2', '3F:e5:D6:77')
print(tuple_record)
print(tuple_record * 2)




local_time = time.localtime(time.time())
print(local_time)
print(type(local_time))
print(local_time[0])   #year
print(local_time[1])   #month
print(f'The month is: {local_time[1]}')  #show month use f to call the function
print(f'The day is {local_time[2]}')    #show date use f to call the function
print('The hour is {}'.format(local_time[3]))  #show hour
print('The minute is {}'.format(local_time[4]))  #show minute
print('{}/{}/{}'.format(local_time[0], local_time[1], local_time[2]))  #show date year/month/date