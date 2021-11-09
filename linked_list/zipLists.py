from linked_list.linked_list import Linkedlist

def zipLists(list1, list2):
    current1=list1.head
    current2=list2.head

    if  current1 == None and current2 == None  :
        return None
    elif current1 == None  :
        return list2.__str__()
    elif  current2 == None  :
            return list1.__str__()

    temp=''
    while current1 and current2:

        if current2:

            temp = current1.next
            current1.next = current2
            current1 = temp

        if current1:

            temp = current2.next
            current2.next = current1
            current2 = temp

    return list1.__str__()

#########################################################################

# old solve 2 :

# def zipLists(list1, list2):
#     temp='head -> '
#     current1=list1.head
#     current2=list2.head
#     values=[]
#     while current1:
#         values+=[current1.value]
#         current1 = current1.next
#         if current2:
#             values+=[current2.value]
#             current2 = current2.next

#     if current1==None and current2 != None:
#         while current2:
#             values+=[current2.value]
#             current2 = current2.next

#     for  i in range(len(values)):
#         temp+='{'+f'{values[i]}'+'} '+'-> '
#     temp+='NULL'
#     return temp

#########################################################################

# old solve :

# def zipLists(list1, list2):
#         current1=list1.head
#         current2=list2.head
#         new_List =Linkedlist()
#         while current1:
#             new_List.append(current1.value)
#             current1 = current1.next
#             if current2:
#                 new_List.append(current2.value)
#                 current2 = current2.next

#         if current1==None and current2 != None:
#             while current2:
#                 new_List.append(current2.value)
#                 current2 = current2.next

#         return f'head-> {new_List.__str__()}'

if __name__ == "__main__":

        # List1 =Linkedlist()
        # List1.append(11)
        # List1.append(12)
        # List1.append(13)
        # # List1.append(14)
        # # List1.append(15)
        # print(List1)

        # List2 =Linkedlist()
        # List2.append(21)
        # List2.append(22)
        # List2.append(23)
        # List2.append(24)
        # List2.append(25)
        # print(List2)

        # print(zipLists(List1 , List2 ) )

    lnk_lst1=Linkedlist()
    lnk_lst1.insert("L1 ,V1")
    lnk_lst1.append("L1 ,V2")
    lnk_lst1.append("L1 ,V3")

    lnk_lst2=Linkedlist()
    lnk_lst2.insert("L2 ,V1")
    lnk_lst2.append("L2 ,V2")
    lnk_lst2.append("L2 ,V3")
    lnk_lst2.append("L2 ,V4")


    actual=zipLists(lnk_lst1,lnk_lst2)
    print(actual)
