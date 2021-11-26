import re 

def lexicalAnalysis():
	fileHandle = open("sample.txt",'r')
	lolcode = fileHandle.read()		
	fileHandle.close()

	obtw = re.findall(r"OBTW[\s\S]+TLDR", lolcode, re.MULTILINE)  # multi-line comment
	multi_line_comment = []

	for c in obtw:
		lolcode = lolcode.replace(c, "")


	for c in obtw:
		c = c.replace("OBTW", "")
		c = c.replace("TLDR", "")
		multi_line_comment.append(c)

	if multi_line_comment:
		obtw = ["OBTW"]
		tldr = ["TLDR"]

	btw = re.findall(r"BTW.+", lolcode, re.MULTILINE)
	single_line_comment = []

	for s in btw:
		lolcode = lolcode.replace(s, "")
		single_line_comment.append(s[4:])
	if btw:
		btw = ["BTW"]

	yarn = re.findall(r"\".+\"",lolcode, re.MULTILINE)
	for s in yarn:
		lolcode = lolcode.replace(s,"")

	HAI = re.findall(r"HAI",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("HAI","")							

	KTHXBYE = re.findall(r"KTHXBYE",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("KTHXBYE","")

	i_has_a = re.findall(r"I HAS A",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("I HAS A","")
	i_has_a = list(dict.fromkeys(i_has_a))

	itz = re.findall(r"ITZ",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("ITZ","")
	itz= list(dict.fromkeys(itz))

	sum_of = re.findall(r"SUM OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("SUM OF","")
	sum_of = list(dict.fromkeys(sum_of))

	diff_of = re.findall(r"DIFF OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("DIFF OF","")
	diff_of = list(dict.fromkeys(diff_of))

	produkt_of = re.findall(r"PRODUKT OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("PRODUKT OF","")
	produkt_of = list(dict.fromkeys(produkt_of))

	quoshunt_of = re.findall(r"QUOSHUNT OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("QUOSHUNT OF","")
	quoshunt_of = list(dict.fromkeys(quoshunt_of))

	mod_of = re.findall(r"MOD OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("MOD OF","")
	mod_of = list(dict.fromkeys(mod_of))

	biggr_of = re.findall(r"BIGGR OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("BIGGR OF","")
	biggr_of = list(dict.fromkeys(biggr_of))

	smallr_of = re.findall(r"SMALLR OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("SMALLR OF","")
	smallr_of = list(dict.fromkeys(smallr_of))

	both_of = re.findall(r"BOTH OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("BOTH OF","")
	both_of = list(dict.fromkeys(both_of))

	either_of = re.findall(r"EITHER OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("EITHER OF","")
	either_of = list(dict.fromkeys(either_of))

	won_of = re.findall(r"WON OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("WON OF","")
	won_of = list(dict.fromkeys(won_of))

	nott = re.findall(r"NOT",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("NOT","")
	nott = list(dict.fromkeys(nott))

	any_of = re.findall(r"ANY OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("ANY OF","")
	any_of = list(dict.fromkeys(any_of))

	all_of = re.findall(r"ALL OF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("ALL OF","")
	all_of = list(dict.fromkeys(all_of))

	both_saem = re.findall(r"BOTH SAEM",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("BOTH SAEM","")
	both_saem = list(dict.fromkeys(both_saem))

	diffrint = re.findall(r"DIFFRINT",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("DIFFRINT","")
	diffrint = list(dict.fromkeys(diffrint))

	smoosh = re.findall(r"SMOOSH",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("SMOOSH","")
	smoosh = list(dict.fromkeys(smoosh))

	maek = re.findall(r"MAEK",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("MAEK","")
	maek= list(dict.fromkeys(maek))

	is_now_a = re.findall(r"IS NOW A",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("IS NOW A","")
	is_now_a = list(dict.fromkeys(is_now_a))

	visible = re.findall(r"VISIBLE",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("VISIBLE","")
	visible = list(dict.fromkeys(visible))

	gimmeh = re.findall(r"GIMMEH",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("GIMMEH","")
	gimmeh= list(dict.fromkeys(gimmeh))

	o_rly = re.findall(r"O RLY\?",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("O RLY?","")
	o_rly = list(dict.fromkeys(o_rly))

	ya_rly = re.findall(r"YA RLY",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("YA RLY","")
	ya_rly = list(dict.fromkeys(ya_rly))

	mebbe = re.findall(r"MEBBE",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("MEBBE","")
	mebbe= list(dict.fromkeys(mebbe))

	no_wai = re.findall(r"NO WAI",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("NO WAI","")
	no_wai= list(dict.fromkeys(no_wai))

	oic = re.findall(r"OIC",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("OIC","")
	oic = list(dict.fromkeys(oic))

	omg_wtf = re.findall(r"OMGWTF",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("OMGWTF","")
	omg_wtf = list(dict.fromkeys(omg_wtf))

	wtf = re.findall(r"WTF\?",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("WTF?","")
	wtf = list(dict.fromkeys(wtf))

	omg = re.findall(r"OMG",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("OMG","")
	omg = list(dict.fromkeys(omg))

	im_in_yr= re.findall(r"IM IN YR",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("IM IN YR","")
	im_in_yr= list(dict.fromkeys(im_in_yr))

	im_outta_yr = re.findall(r"IM OUTTA YR",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("IM OUTTA YR","")
	im_outta_yr = list(dict.fromkeys(im_outta_yr))

	uppin = re.findall(r"UPPIN",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("UPPIN","")
	uppin = list(dict.fromkeys(uppin))

	nerfin = re.findall(r"NERFIN",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("NERFIN","")
	nerfin = list(dict.fromkeys(nerfin))

	yr = re.findall(r"YR",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("YR","")
	yr = list(dict.fromkeys(yr))

	til = re.findall(r"TIL",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("TIL","")
	til = list(dict.fromkeys(til))

	wile = re.findall(r"WILE",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("WILE","")
	wile = list(dict.fromkeys(wile))

	mkay = re.findall(r"MKAY",lolcode, re.MULTILINE)
	lolcode = lolcode.replace("MKAY", "")
	mkay = list(dict.fromkeys(mkay))

	an = re.findall(r"AN", lolcode, re.MULTILINE)
	lolcode = lolcode.replace("AN","")
	an = list(dict.fromkeys(an))

	troof = re.findall(r"WIN|FAIL",lolcode, re.MULTILINE)
	for t in troof:
		lolcode = lolcode.replace(t,"")
	troof = list(dict.fromkeys(wile))

	type = re.findall(r"TROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE",lolcode, re.MULTILINE)
	for t in type:
		lolcode = lolcode.replace(t,"")
	type = list(dict.fromkeys(type))

	a = re.findall(r"A", lolcode, re.MULTILINE)
	lolcode = lolcode.replace("A", "")
	a = list(dict.fromkeys(a))

	r = re.findall(r"R", lolcode, re.MULTILINE)
	lolcode = lolcode.replace("R", "")
	r = list(dict.fromkeys(r))

	var_identifier = re.findall(r"[A-Za-z][A-Za-z0-9_]*",lolcode, re.MULTILINE)
	var_identifier.sort()			#sorts by length
	var_identifier.reverse()			#reverse, so from higher strlength to lower strlength, 
										#to avoid problems in removing variable identifiers

	var_identifier = list(dict.fromkeys(var_identifier))  #remove duplicates

	for var in var_identifier:
		lolcode = lolcode.replace(var,"")

	numbar = re.findall(r"-?[0-9]+\.[0-9]+",lolcode, re.MULTILINE)
	for num in numbar:
		lolcode = lolcode.replace(num,"")

	numbr = re.findall(r"-?[0-9]+",lolcode, re.MULTILINE)
	for num in numbr:
		lolcode = lolcode.replace(num,"")

	fileHandle = open("sample.txt",'r')
	lolcode = fileHandle.read()		
	fileHandle.close()

	print(lolcode)

	print("KEYWORDS")
	print("HAI: ",HAI)
	print("KTHNXBYE: ",KTHXBYE)
	print("BTW: ", btw)
	print("OBTW: ",obtw)
	print("TLDR: ", tldr)
	print("I HAS A: ", i_has_a)
	print("ITZ: ", itz)
	print("R: ", r)
	print("SUM OF: ", sum_of)
	print("DIFF OF: ",diff_of)
	print("PRODUKT OF: ",produkt_of)
	print("QUOSHUNT OF: ",quoshunt_of)
	print("MOD OF: ", mod_of)
	print("BIGGR OF: ", biggr_of)
	print("SMALLR OF: "	,smallr_of)
	print("BOTH OF: ", both_of)
	print("EITHER OF: ",either_of)
	print("WON OF: ", won_of)
	print("NOT: ",nott)
	print("ANY OF: ",any_of)
	print("ALL OF: ",all_of)
	print("BOTH SAEM: ",both_saem)
	print("DIFFRINT: ",diffrint)
	print("SMOOSH: ",smoosh)
	print("MAEK: ",maek)
	print("A: ", a)
	print("IS NOW A: ",is_now_a)
	print("VISIBLE: ",visible)
	print("GIMMEH", gimmeh)
	print("O RLY?: ",o_rly)
	print("YA RLY: ",ya_rly)
	print("MEBBE: ",mebbe)
	print("NO WAI: ",no_wai)
	print("OIC: ", oic)
	print("WTF?: ", wtf)
	print("OMG: ", omg)
	print("OMGWTF: ", omg_wtf)
	print("IM IN YR: ", im_in_yr)
	print("UPPIN: ", uppin)
	print("NERFIN: ",nerfin)
	print("YR: ", yr)
	print("TIL: ", til)
	print("WILE: ",wile)
	print("IM OUTTA YR: ", im_outta_yr)

	print("COMMENTS")
	print("SINGLE LINE COMMENT: ",single_line_comment)
	print("MULTI LINE COMMENT: ",multi_line_comment)

	print("IDENTIFIERS")
	print("IDENTIFIER: ", var_identifier)

lexicalAnalysis()