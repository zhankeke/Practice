class cocacola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self,how_much):      #HERE

        if how_much == 'a sip':
            print('cool~')
        elif how_much == 'whole bottle':
            print('headache!')

coke = cocacola()
coke.drink('a sip')

