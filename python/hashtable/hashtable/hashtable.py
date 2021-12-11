from hashtable.linked_list import LinkedList
class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size




    def hash(self,key):

        ascii_sum=0
        for char in key:
            ascii_sum+=ord(char)
        return ascii_sum*11 % self.size


    def add(self, key, value):


        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = [key,value]
            return [key,value]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].append([key,value])
                return [key,value]

            else:
                chain = LinkedList()
                existing_pair= self.map[hashed_key]
                new_pair =[key,value]
                self.map[hashed_key]=chain
                chain.append((existing_pair))
                chain.append(new_pair)
            return [key,value]



    def get(self, key):


        hashed_key=self.hash(key)

        if  self.map[hashed_key]==None:
              print("Not Found")

        else:

            if type(  self.map[hashed_key])== list:
                return self.map[hashed_key][1]

            else:

                current =  self.map[hashed_key].head

            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (current.value[1])
                        return (current.value[1])
                    current = current.next


    def contains(self, key):


        hashed_key=self.hash(key)

        if  self.map[hashed_key]==None:
            return False

        else:

            if type(  self.map[hashed_key])== list:
                print (True)
                return True

            else:
                current =  self.map[hashed_key].head

            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (True)
                        return (True)
                    current = current.next
                print ("false")
                return False


if __name__ == '__main__':


    hashtable = HashTable()
    hashtable.add('rihan', 30)
    hashtable.add('ibrahim', 29)
    hashtable.add('Twix', 25)
    hashtable.add('Burger', 45)
    for hashed_key, item in enumerate(hashtable.map):
        if item:
            print(hashed_key, item)
