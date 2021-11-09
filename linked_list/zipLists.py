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


if __name__ == "__main__":



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
