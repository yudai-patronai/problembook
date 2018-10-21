from lib.random import choice
from lib.testgen import TestSet

def getstr(a,b,c):
	return a + "\n" + b + "\n" + c;

tests = TestSet()


tests.add(getstr(
	"%s", 
	"input_string_data",
	"%s"  ),
	"input_string_data");

tests.add(getstr(
	"%d", 
	"543",
	"%04d"),
	"0543");

tests.add(getstr(
	"%lf",	
	"5.378",
	"%.2f"),
	"5.38");

tests.add(getstr(
	"%[absd]",
	"absddsbaasdbsdbaabds",
	"%s"),
	"absddsbaasdbsdbaabds");

tests.add(getstr(
	"%3d %d",	
	"12345",
	"%05d"),
	"00045");

tests.add(getstr(
	"%le",	
	"123.3",
	"%7.1e"),
	"1.2e+02");

tests.add(getstr(
	"%lx",	
	"400a037da037da03",
	"%4.2f"),
	"3.25");

tests.add(getstr(
	"%s",	
	"0123",
	"%x"),
	"33323130");

tests.add(getstr(
	"%s",	
	"!!!!!!!!",
	"%9.2e"),
	"4.19e-149");

tests.add(getstr(
	"nulltext",	
	"",
	""),
	"\n");
