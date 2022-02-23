import pickle
pkl_file = open('/home/ayush/assignment3/dic.pkl','rb')
my_dic = pickle.load(pkl_file)
pkl_file.close()
print(my_dic)
