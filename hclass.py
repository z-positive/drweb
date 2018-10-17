class Handle:

    #act = ('SET', 'GET', 'UNSET', 'COUNTS', 'FIND', 'END')

    objects = {}
    transactions = []

    def __init__(self, query):
        self.elements = query.split(' ')
        self.router(self.elements[0])
        print(self.objects)


    def router(self, action):
        if action == 'SET':
            self.objects[self.elements[1]] = self.elements[2]
            #self.trnsctns(self.objects[self.elements[1]],self.elements[2])
        elif action == 'GET':
            print(self.objects[self.elements[1]])
        elif action == 'UNSET':
            print('Удаляем значение ', self.elements[1])
            del self.objects[self.elements[1]]
        elif action == 'COUNTS':
            self.counts(self.elements[1])
        elif action == 'FIND':
            self.find(self.elements[1])
        elif action == 'END':
            exit()
        #elif action == 'BEGIN':
        #    if self.begin == 0:
        #        self.begin == 1
        #    else:
        #        print('Транзакция')


    #def trnsctns(self,item,data):
    #    try:
    #        self.transactions.append({item:data})
    #    except:
    #        print('лог изменений не создан')



    def counts(self, data):
        i=0
        count = 0

        for item in self.objects:
            if self.objects[item] == data:
                count+=1

        print('Количество переменных со значением {0} составляет {1}'.format(data, count))

    def find(self,data):
        i=0
        count = 0
        lst = []

        for item in self.objects:
            if self.objects[item] == data:
                lst.append(item)

        print('Переменная {0} встречается в переменных {1}'.format(data, lst))


















