import anagrams
import test_list

from common.test.test_class import TestClass

test = TestClass(anagrams.anagrams, test_list.test)
test.assert_test()