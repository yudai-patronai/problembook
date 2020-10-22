from lib.testgen import TestSet

tests = TestSet()

# statement tests
tests.add('<tag1></tag1>', 'YES')
tests.add('<tag1>content and <tag2>another content</tag2></tag1>', 'YES')
tests.add('<tag1>content</tag2>', 'NO')
tests.add('<tag1><tag2></tag1></tag2>', 'NO')

# exactly one root element
tests.add('<tag1></tag1><tag2></tag2>', 'NO')
tests.add('content', 'NO')
tests.add('<tag1></tag1>content', 'NO')
tests.add('asd<wer></wer>', 'NO')

# empty string
tests.add('', 'NO')

# improperly formed tags
tests.add('<meow', 'NO')
tests.add('<meow</meow>', 'NO')
tests.add('<meow>meow>', 'NO')
tests.add('<meow></meow', 'NO')
tests.add('<meow><meow>', 'NO')
tests.add('</meow></meow>', 'NO')
tests.add('</meow><meow>', 'NO')
tests.add('<meow><meow/>', 'NO')
tests.add('<tag1><meow></tag1>', 'NO')
tests.add('<tag1></meow></tag1>', 'NO')

# unbalanced tags
tests.add('<tag1></tag1></tag1>', 'NO')
tests.add('<tag1><tag1></tag1>', 'NO')

# content like tag
tests.add('<tag1>tag1</tag1>', 'YES')
tests.add('<tag1>/tag1 tag2</tag2>', 'NO')

# tag and content mess
tests.add('<tag1>asd<tag2>fgf</tag2>dsa</tag1>', 'YES')
tests.add('<tag1>asd<tag2>fgf</tag2>dsa<tag2>wer</tag2>0.05<tag3></tag3></tag1>', 'YES')

# nested tags
tests.add('<tag1><tag2><tag2></tag2><tag3><tag2></tag2></tag3></tag2><tag2></tag2><tag3><tag2></tag2></tag3></tag1>', 'YES')
tests.add('<tag1><tag2><tag2></tag2><tag3><tag2></tag2></tag2></tag2><tag2></tag2><tag3><tag2></tag2></tag3></tag1>', 'NO')
tests.add('<tag1><tag2><tag2></tag2><tag3><tag2></tag2></tag3></tag2><tag2></tag2><tag2><tag2></tag2></tag3></tag1>', 'NO')
