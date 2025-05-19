#!/usr/bin/env python3

from list_comprehension import return_evens, make_exclamation

class TestReturnEvens:
    '''function return_evens()'''

    def test_return_empty_list_if_odds(self):
        '''returns empty list when num_list has no evens'''
        num_list = range(1,10,2)
        

    def test_return_evens(self):
        '''returns evens from num_list'''
        num_list = range(10)
        

class TestMakeExclamation:
    '''function make_exclamation()'''

    def test_return_empty_list_if_empty_input(self):
        '''returns empty list when sentence_list is empty'''
        

    def test_return_exclamation_list(self):
        '''returns list of sentences with exclamation marks'''
        sentence_list = [
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]
    
            
        
