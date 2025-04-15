st="print only the word that starts with s in this sentence"
for i in st.split():
    if(len(i)%2==0):
        print(i)

print(len(st))

#list method append
my_list=[1,2,3,4,7,8,9,"hello","name"]
my_list.append(99)
print(my_list)

#list method extend
another_list=["apple","ball","hii"]
my_list.extend(another_list)
print(my_list)