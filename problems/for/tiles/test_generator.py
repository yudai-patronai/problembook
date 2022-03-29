from lib.testgen import TestSet

tests = TestSet()

tests.add("""1""", """0""")

tests.add("""4""", """3""")

tests.add("""8""", """7""")

tests.add("""1000000000000000000""", """999999999999999976""")

tests.add("""2587587""", """2587573""")

tests.add("""658763""", """658754""")

tests.add("""13285753683""", """13285753666""")

