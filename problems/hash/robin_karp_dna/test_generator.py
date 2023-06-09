from lib.testgen import TestSet

tests = TestSet()

tests.add('\n','\n')
tests.add('AAA\n', '\n')
tests.add('CAAAAAAAAAC','\n')
tests.add('AAAAAAAAAAAA\n','AAAAAAAAAA\n')
tests.add('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT\n' ,'AAAAACCCCC CCCCCAAAAA\n')
tests.add('AAAAAAAAAAAACCCCCCCCCCCAAAACCCCCCCCCCCCCCCCCCTT\n', 'AAAAAAAAAA AAAACCCCCC AAACCCCCCC AACCCCCCCC ACCCCCCCCC CCCCCCCCCC\n')
tests.add('AAAAAGGGTTTAAAGGGTTT\n','\n')
tests.add('AAAAAGGGTTTAAAGGGTTTA','AAAGGGTTTA\n')
tests.add('ATCATCATCATCATCATC', 'ATCATCATCA CATCATCATC TCATCATCAT')
tests.add('ATCATCATCATCAT','ATCATCATCA TCATCATCAT\n')
tests.add('ATCATCATCATCA\n','ATCATCATCA\n')


