import re
#
# userStr = "abcd abc efgh"
# match = re.search(r'\w{4}', userStr)
#
# print(match.group()) # abcd
# print(match.group(0)) # abcd
#
# userStr = "abcd abc 123 efgh 456"
# match = re.search(r'\d{3}', userStr)
# print(match.group()) # 123
#
# import re
# userStr = "My cell phone numbers: Vodafone +38(095)1234567; Cellcom +38(067)9875612";
# match1 = re.search(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)', userStr)
#
# print(match1.group()) # Vodafone +38(095)1234567; Cellcom +38(067)9875612
# print(match1.group(0)) # Vodafone +38(095)1234567; Cellcom +38(067)9875612
#
# print(match1.group(1)) # 1234567
# print(match1.group(2)) # 9875612
#
# print(match1.group(1,2)) # ('1234567', '9875612')
#
# my_string = 'aaaa bbb aaaa bbb'
#
# mo = re.search(r'(\w{3})', my_string)
#
# print(mo.group())


phone_num_regex = re.compile(r"(\d\d\d-)?(\d\d\d-\d\d\d\d)")

mo1 = phone_num_regex.findall('Cell: 415-555-1212 Work: 212-555-0000')

# mo2 = phone_num_regex.search('My number us 445-1212')


print(mo1)
# print(mo2.group())


# hero_regex = re.compile(r"Batman|Tina Fey")
# mo = hero_regex.search("Batman and Tina Fey")
#
# print(mo.group())
#
# mo1 = hero_regex.search('Tina Fey and Batman')
#
# print(mo1.group())


# bat_regex = re.compile(r"Bat(man|mobile|coper|bat)")
#
# mo = bat_regex.search("Batmobile lost a wheel")
#
# print(mo.group(1))

# bat_regex = re.compile(r"Bat(wo)?man")
#
# mo1 = bat_regex.search("The adventures of Batman")
# mo2 = bat_regex.search("The adventures of Batwoman")
#
# print(mo1.group())
# print(mo2.group())


# bat_regex = re.compile(r"Bat(wo)*man")
#
# mo1 = bat_regex.search("The Adventures of Batman")
# mo2 = bat_regex.search("The Adventures of Batwoman")
# mo3 = bat_regex.search("The Adventures of Batwowowoman")
#
# print(mo1.group())
# print(mo2.group())
# print(mo3.group())

#
# ha_regex = re.compile(r"(Ha){3}")
# mo1 = ha_regex.search("HaHaHa")
# print(mo1.group())
#
# mo2 = ha_regex.search('Ha')
# # mo2 == None
# print(mo2)




