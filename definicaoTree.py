class Tree:
    values = list()
    
    def insert(self, number: int) -> bool:
        if len(Tree.values) == 0:
            self.values.append([number])
            return True
        self.values.append(number)
        
    def select(self, number: int) -> bool:
        for x in range(len(self.values)):
            if self.values[x] is list:
                for n in self.values[x]:
                    if number in n:
                        return True
            else:
                if number == self.values[x]:
                    return True
        return False
