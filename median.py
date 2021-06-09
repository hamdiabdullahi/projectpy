# def mean(L):
#     total=0
#     for x in L:
#         total+= x #total = total +x
#     mean = total / len(L)
#     return mean

# def median(L):
#     L.sort()
#     if len(L)%2 !=0:
#         median = L [int(len(L)/2)]
#     else:
#         median= L[(int(len(L)/2))-1]+ L[int(len(L)/2)]
#     return median

# def mode():
#     counter = 0
#     num = L[8]
#     for i in L:
#         current_frequency =L.counter(i)
#         if(current_frequency>counter):
#             counter= current_frequency
#             num = 1
#         if len(set(L)) == len(L):
#             return 'there is no mode'
#     return num
# number_list=[]
# while(True):
#     ask = input('enter a number and say "stop" to end:')
#     if ask == 'stop':
#       break
# number_list.append(int(ask))
# mean= str(mean(number_list))
# median= str(median(number_list))
# mode= str(mode(number_list))
# print('mean: '+ mean + '\n' + 'median: ' + median + '\n' + 'mode: ' + mode)
