import re 

classified_lexemes = []

def lexicalAnalysis():
	
	I_HAS_A = ""		
	IS_NOW_A = ""		
	SUM_OF = ""			
	DIFF_OF = ""		
	PRODUKT_OF = ""		
	QUOSHUNT_OF = ""	
	MOD_OF = ""			
	BIGGR_OF = ""		
	SMALLR_OF = ""		
	BOTH_OF = ""		
	EITHER_OF = ""		
	WON_OF = ""			
	ANY_OF = ""			
	ALL_OF = ""			
	BOTH_SAEM = ""
	O_RLY = ""
	YA_RLY = ""
	NO_WAI = ""
	IM_IN_YR = ""
	IM_OUTTA_YR = ""
	YARN = ""

	singlelinecomment = False
	multilinecomment = False
	isString = False

	if_else = False
	switch_case = False
	
	fileHandle = open("sample.txt",'r')
	for line in fileHandle:
		line = line.split()
		for token in line:
			if not singlelinecomment and not multilinecomment and not isString:
				if re.search("^HAI$",token):
					classified_lexemes.append({"token": token, "type": "Code delimeter"})
				elif re.search("^KTHXBYE$", token):
					classified_lexemes.append({"token": token, "type": "Code delimeter"})
				elif re.search("^ITZ$", token):
					classified_lexemes.append({"token": token, "type": "Variable Initializaton"})
				elif re.search("^R$", token):
					classified_lexemes.append({"token": token, "type": "Variable assignment"})
				elif re.search("^NOT$", token):
					classified_lexemes.append({"token": token, "type": "Negation"})
				elif re.search("^SAEM$", token):
					if BOTH_SAEM:
						BOTH_SAEM = BOTH_SAEM + " SAEM"
						classified_lexemes.append({"token": token, "type": "Comparison Op"})
				elif re.search("^DIFFRINT$", token):
					classified_lexemes.append({"token": token, "type": "Comparison Op"})
				elif re.search("^SMOOSH$", token):
					classified_lexemes.append({"token": token, "type": "Concatenation"})
				elif re.search("^MAEK$", token):
					classified_lexemes.append({"token": token, "type": "Typecast"})
				elif re.search("^VISIBLE$", token):
					classified_lexemes.append({"token": token, "type": "Print"})
				elif re.search("^MEBBE$", token):
					classified_lexemes.append({"token": token, "type": "Else-if condition"})
				elif re.search("^AN$", token):
					classified_lexemes.append({"token": token, "type": "Operand Separator"})
				elif re.search("^OIC$", token):					#check for if-else or delimeter
					if if_else:
						classified_lexemes.append({"token": token, "type": "If-then delimeter"})
						if_else = False
					elif switch_case:
						classified_lexemes.append({"token": token, "type": "Switch-case delimeter"})
						switch_case = False
				elif re.search("^WTF?$", token):
					classified_lexemes.append({"token": token, "type": "Switch-case delimeter"})
					switch_case = True
				elif re.search("^OMG$", token):					
					classified_lexemes.append({"token": token, "type": "Switch-case condition"})
				elif re.search("^OMGWTF$", token):
					classified_lexemes.append({"token": token, "type": "Switch-case default condition"})
				elif re.search("^UPPIN$",token):
					classified_lexemes.append({"token": token, "type": "Loop Increment"})
				elif re.search("^NERFIN$",token):
					classified_lexemes.append({"token": token, "type": "Loop decrement"})
				elif re.search("^TIL$",token):
					classified_lexemes.append({"token": token, "type": "Loop Condition"})
				elif re.search("^WILE$",token):
					classified_lexemes.append({"token": token, "type": "Loop Condition"})
				elif re.search("^(WIN|FAIL)$", token):
					classified_lexemes.append({"token": token, "type": "Troof"})
				elif re.search("^(TROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE)$",token):
					classified_lexemes.append({"token": token, "type": "Type Literal"})
				elif re.search("^IM$",token):
					IM_IN_YR = IM_IN_YR + "IM"
					IM_OUTTA_YR = IM_OUTTA_YR + "IM"
				elif re.search("^IN$",token):
					if IM_IN_YR:
						IM_IN_YR = IM_IN_YR + " IN"
						IM_OUTTA_YR = ""
				elif re.search("^YR$",token):
					if IM_IN_YR:
						IM_IN_YR = IM_IN_YR + " YR"
						classified_lexemes.append({"token": IM_IN_YR, "type": "Loop delimeter"})
						IM_IN_YR = ""
					elif IM_OUTTA_YR:
						IM_OUTTA_YR = IM_OUTTA_YR + " YR"
						classified_lexemes.append({"token": IM_OUTTA_YR, "type": "Loop delimeter"})
						IM_OUTTA_YR = ""
				elif re.search("^OUTTA$",token):
					if IM_OUTTA_YR:
						IM_OUTTA_YR = IM_OUTTA_YR + " OUTTA"
						IM_IN_YR = ""
				elif re.search("^O$",token):
					O_RLY = O_RLY + "O"
				elif re.search("^RLY?$",token):
					if O_RLY:
						O_RLY = O_RLY + " RLY?"
						classified_lexemes.append({"token": O_RLY, "type": "If-then delimeter"})
						O_RLY = ""
						if_else = True
				elif re.search("^YA$",token):
					YA_RLY = YA_RLY + "YA"
				elif re.search("^RLY$",token):
					if YA_RLY:
						YA_RLY = YA_RLY + " RLY"
						classified_lexemes.append({"token": YA_RLY, "type": "If statement"})
						YA_RLY = ""
				elif re.search("^NO$",token):
					NO_WAI = NO_WAI + "NO"
				elif re.search("^WAI$",token):
					if NO_WAI:
						NO_WAI = NO_WAI + " WAI"
						classified_lexemes.append({"token": NO_WAI, "type": "Else statement"})
						NO_WAI = ""
				elif re.search("^I$", token):
					I_HAS_A = token
				elif re.search("^HAS$", token):
					I_HAS_A = I_HAS_A + " HAS"
				elif re.search("^A$", token):
					if I_HAS_A:
						I_HAS_A = I_HAS_A + " A"
						classified_lexemes.append({"token": I_HAS_A, "type": "Variable Declaration"})
						I_HAS_A = ""
					elif IS_NOW_A:
						IS_NOW_A = IS_NOW_A + " A"
						classified_lexemes.append({"token": IS_NOW_A, "type": "Typecast"})
						IS_NOW_A = ""
					else:
						print(token,"-A")
				elif re.search("^BTW$", token):
					classified_lexemes.append({"token": token, "type": "Single-line comment delimeter"})
					singlelinecomment = True
				elif re.search("^GIMMEH$",token):
					classified_lexemes.append({"token": token, "type": "Input"})
				elif re.search("^OBTW$", token):
					classified_lexemes.append({"token": token, "type": "Multi-line comment delimeter"})
					multilinecomment = True
				elif re.search("^IS$",token):
					IS_NOW_A = IS_NOW_A + "IS"
				elif re.search("^NOW$",token):
					IS_NOW_A = IS_NOW_A + " NOW"
				elif re.search("^SUM$",token):
					SUM_OF = SUM_OF + "SUM"
				elif re.search("^DIFF$",token):
					DIFF_OF = DIFF_OF + "DIFF"
				elif re.search("^PRODUKT$",token):
					PRODUKT_OF = PRODUKT_OF + "PRODUKT"
				elif re.search("^QUOSHUNT$",token):
					QUOSHUNT_OF = QUOSHUNT_OF + "QUOSHUNT"
				elif re.search("^MOD$",token):
					MOD_OF = MOD_OF + "MOD"
				elif re.search("^BIGGR$",token):
					BIGGR_OF = BIGGR_OF + "BIGGR"
				elif re.search("^SMALLR$",token):
					SMALLR_OF = SMALLR_OF + "SMALLR"
				elif re.search("^BOTH$",token):		
					BOTH_OF = BOTH_OF + "BOTH"
					BOTH_SAEM = BOTH_SAEM + "BOTH"
				elif re.search("^EITHER$",token):		
					EITHER_OF = EITHER_OF + "EITHER"
				elif re.search("^WON$",token):		
					WON_OF = WON_OF + "WON"
				elif re.search("^ANY$",token):		
					ANY_OF = ANY_OF + "ANY"
				elif re.search("^ALL$",token):		
					ALL_OF = ALL_OF + "ALL"
				elif re.search("^OF$", token):
					if SUM_OF:
						SUM_OF = SUM_OF + " OF"
						classified_lexemes.append({"token": SUM_OF, "type": "Math Op"})
						SUM_OF = ""
					elif DIFF_OF:
						DIFF_OF = DIFF_OF + " OF"
						classified_lexemes.append({"token": DIFF_OF, "type": "Math Op"})
						DIFF_OF = ""
					elif PRODUKT_OF:
						PRODUKT_OF = PRODUKT_OF + " OF"
						classified_lexemes.append({"token": PRODUKT_OF, "type": "Math Op"})
						PRODUKT_OF = ""
					elif QUOSHUNT_OF:
						QUOSHUNT_OF = QUOSHUNT_OF + " OF"
						classified_lexemes.append({"token": QUOSHUNT_OF, "type": "Math Op"})
						QUOSHUNT_OF = ""
					elif MOD_OF:
						MOD_OF = MOD_OF + " OF"
						classified_lexemes.append({"token": MOD_OF, "type": "Math Op"})
						MOD_OF = ""
					elif BIGGR_OF:
						BIGGR_OF = BIGGR_OF + " OF"
						classified_lexemes.append({"token": BIGGR_OF, "type": "Math Op"})
						BIGGR_OF = ""
					elif SMALLR_OF:
						SMALLR_OF = SMALLR_OF + " OF"
						classified_lexemes.append({"token": SMALLR_OF, "type": "Math Op"})
						SMALLR_OF = ""
					elif BOTH_OF:
						BOTH_OF = BOTH_OF + " OF"
						classified_lexemes.append({"token": BOTH_OF, "type": "Boolean Op"})
						BOTH_OF = ""
						BOTH_SAEM = ""
					elif EITHER_OF:
						EITHER_OF = EITHER_OF + " OF"
						classified_lexemes.append({"token": EITHER_OF, "type": "Boolean Op"})
						EITHER_OF = ""
					elif WON_OF:
						WON_OF = WON_OF + " OF"
						classified_lexemes.append({"token": WON_OF, "type": "Boolean Op"})
						WON_OF = ""
					elif ANY_OF:
						ANY_OF = ANY_OF + " OF"
						classified_lexemes.append({"token": ANY_OF, "type": "Boolean Op"})
						ANY_OF = ""
					elif ALL_OF:
						ALL_OF = ALL_OF + " OF"
						classified_lexemes.append({"token": ALL_OF, "type": "Boolean Op"})
						ALL_OF = ""
				elif re.search("^-?[0-9]+$", token):
					classified_lexemes.append({"token": token, "type": "NUMBR"})
				elif re.search("^-?[0-9]+\.[0-9]+$",token):
					classified_lexemes.append({"token": token, "type": "NUMBAR"})
				elif re.search('^"[^"]+"$',token):
					classified_lexemes.append({"token": token, "type": "YARN"})
				elif re.search('^"[^"]*$',token):
					YARN = YARN + token
					isString = True
				elif re.search("^[A-Za-z][A-Za-z0-9_]*$", token):
					classified_lexemes.append({"token": token, "type": "Identifier"})
			elif isString:
				if re.search('^[^"]*"$',token):
					YARN = YARN + " " + token
					if not re.search('^" +"$',YARN):
						classified_lexemes.append({"token": YARN, "type": "YARN"})
					isString = False
					YARN = ""
				else:
					YARN = YARN + " " + token
			elif singlelinecomment:
				classified_lexemes.append({"token": token, "type": "Single-line comment word"})
				
			elif multilinecomment:
				if re.search("^TLDR$", token):
					classified_lexemes.append({"token": token, "type": "Multi-line comment delimeter"})
					multilinecomment = False
				else:
					classified_lexemes.append({"token": token, "type": "Multi-line comment word"})

		singlelinecomment = False

	fileHandle.close()

def classifyIdentifiers():
	for i in range(0,len(classified_lexemes)):
		if classified_lexemes[i]["type"] == "Identifier":
			if classified_lexemes[i-1]["type"] == "Variable Declaration":
				classified_lexemes[i]["type"] == "Variable identifier"
				for j in range(i+1,len(classified_lexemes)):
					if classified_lexemes[i]["token"] == classified_lexemes[j]["token"]:
						classified_lexemes[j]["type"] = "Variable identifier"
			elif classified_lexemes[i-1]["type"] == "Loop delimeter":
				classified_lexemes[i]["type"] == "Loop identifier"
				for j in range(i+1,len(classified_lexemes)):
					if classified_lexemes[i]["token"] == classified_lexemes[j]["token"]:
						classified_lexemes[j]["type"] = "Loop identifier"

def printLexemes():
	print("----------LEXEMES----------")
	for i in range(0, len(classified_lexemes)):
		print(classified_lexemes[i]["token"]+": "+classified_lexemes[i]["type"])


lexicalAnalysis()
classifyIdentifiers()
printLexemes()


