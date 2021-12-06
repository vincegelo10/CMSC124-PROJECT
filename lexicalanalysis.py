from variables import *
import re 

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
					print(token, "-Code delimeter")
				elif re.search("^KTHXBYE$", token):
					print(token, "-Code delimeter")
				elif re.search("^ITZ$", token):
					print(token, "-variable initialization")
				elif re.search("^R$", token):
					print(token, "-variable assignment")
				elif re.search("^NOT$", token):
					print(token, "-negation")
				elif re.search("^SAEM$", token):
					if BOTH_SAEM:
						BOTH_SAEM = BOTH_SAEM + " SAEM"
						print(BOTH_SAEM,"-comparison op")
				elif re.search("^DIFFRINT$", token):
					print(token, "-comparison op")
				elif re.search("^SMOOSH$", token):
					print(token, "-concatenation")
				elif re.search("^MAEK$", token):
					print(token,"-typecast")
				elif re.search("^VISIBLE$", token):
					print(token,"-print keyword")
				elif re.search("^MEBBE$", token):
					print(token,"-else-if condition")
				elif re.search("^OIC$", token):					#check for if-else or loops
					if if_else:
						print(token,"-if-then delimeter")
						if_else = False
					elif switch_case:
						print(token,"-loop delimeter")
						switch_case = False
				elif re.search("^WTF?$", token):
					print(token,"-switch-case delimeter")
					switch_case = True
				elif re.search("^OMG$", token):
					print(token,"-switch-case condition")
				elif re.search("^OMGWTF$", token):
					print(token,"-switch-case default condition")
				elif re.search("^UPPIN$",token):
					print(token,"-loop-increment")
				elif re.search("^NERFIN$",token):
					print(token,"-loop-decrement")
				elif re.search("^TIL$",token):
					print(token,"-loop-condition")
				elif re.search("^WILE$",token):
					print(token,"-loop-condition")
				elif re.search("^(WIN|FAIL)$", token):
					print(token, "TROOF")
				elif re.search("^(TROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE)$",token):
					print(token,"TYPE LITERAL")
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
					elif IM_OUTTA_YR:
						IM_OUTTA_YR = IM_OUTTA_YR + " YR"
				elif re.search("^OUTTA$",token):
					if IM_OUTTA_YR:
						IM_OUTTA_YR = IM_OUTTA_YR + " OUTTA"
						IM_IN_YR = ""
				elif re.search("^O$",token):
					O_RLY = O_RLY + "O"
				elif re.search("^RLY?$",token):
					if O_RLY:
						O_RLY = O_RLY + " RLY?"
						print(O_RLY,"if-then delimeter")
						O_RLY = ""
						if_else = True
				elif re.search("^YA$",token):
					YA_RLY = YA_RLY + "YA"
				elif re.search("^RLY$",token):
					if YA_RLY:
						YA_RLY = YA_RLY + " RLY"
						print(YA_RLY,"-if-statement")
						YA_RLY = ""
				elif re.search("^NO$",token):
					NO_WAI = NO_WAI + "NO"
				elif re.search("^WAI$",token):
					if NO_WAI:
						NO_WAI = NO_WAI + " WAI"
						print(NO_WAI,"-else-statement")
						NO_WAI = ""

				elif re.search("^I$", token):
					I_HAS_A = token
				elif re.search("^HAS$", token):
					I_HAS_A = I_HAS_A + " HAS"
				elif re.search("^A$", token):
					if I_HAS_A:
						I_HAS_A = I_HAS_A + " A"
						print(I_HAS_A, "-variable declaration")
						I_HAS_A = ""
					elif IS_NOW_A:
						IS_NOW_A = IS_NOW_A + " A"
						print(IS_NOW_A,"-typecast")
						IS_NOW_A = ""
					else:
						print(token,"-A")
				elif re.search("^BTW$", token):
					print(token, "-single-line comment delimeter")
					singlelinecomment = True
				elif re.search("^GIMMEH$",token):
					print(token,"-input statement" )
				elif re.search("^OBTW$", token):
					print(token, "-multi-line comment delimeter")
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
				elif re.search("^BOTH$",token):		#can be BOTH SAEM or BOTH OF
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
						print(SUM_OF,"-Math Op")
						SUM_OF = ""
					elif DIFF_OF:
						DIFF_OF = DIFF_OF + " OF"
						print(DIFF_OF,"-Math Op")
						DIFF_OF = ""
					elif PRODUKT_OF:
						PRODUKT_OF = PRODUKT_OF + " OF"
						print(PRODUKT_OF,"-Math Op")
						PRODUKT_OF = ""
					elif QUOSHUNT_OF:
						QUOSHUNT_OF = QUOSHUNT_OF + " OF"
						print(QUOSHUNT_OF,"-Math Op")
						QUOSHUNT_OF = ""
					elif MOD_OF:
						MOD_OF = MOD_OF + " OF"
						print(MOD_OF,"-Math Op")
						MOD_OF = ""
					elif BIGGR_OF:
						BIGGR_OF = BIGGR_OF + " OF"
						print(BIGGR_OF,"-Math Op")
						BIGGR_OF = ""
					elif SMALLR_OF:
						SMALLR_OF = SMALLR_OF + " OF"
						print(SMALLR_OF,"-Math Op")
						SMALLR_OF = ""
					elif BOTH_OF:
						BOTH_OF = BOTH_OF + " OF"
						print(BOTH_OF,"-Boolean Op")
						BOTH_OF = ""
						BOTH_SAEM = ""
					elif EITHER_OF:
						EITHER_OF = EITHER_OF + " OF"
						print(EITHER_OF, "-Boolean Op")
						EITHER_OF = ""
					elif WON_OF:
						WON_OF = WON_OF + " OF"
						print(WON_OF, "-Boolean Op")
						WON_OF = ""
					elif ANY_OF:
						ANY_OF = ANY_OF + " OF"
						print(ANY_OF, "-Boolean Op")
						ANY_OF = ""
					elif ALL_OF:
						ALL_OF = ALL_OF + " OF"
						print(ALL_OF, "-Boolean Op")
						ALL_OF = ""
				elif re.search("^-?[0-9]+$", token):
					print(token,"-NUMBR")
				elif re.search("^-?[0-9]+\.[0-9]+$",token):
					print(token,"-NUMBAR")
				elif re.search('^"[^"]+"$',token):
					print(token,"-YARN")
				elif re.search('^"[^"]*$',token):
					YARN = YARN + token
					isString = True
				elif re.search("^[A-Za-z][A-Za-z0-9_]*$", token):
					print(token, "-identifier")
			elif isString:
				if re.search('^[^"]*"$',token):
					YARN = YARN + " " + token
					print(YARN, "YARN")
					YARN = ""
					isString = False
				else:
					YARN = YARN + " " + token
			elif singlelinecomment:
				print(token, "-single-line comment word")
				
			elif multilinecomment:
				if re.search("^TLDR$", token):
					print(token, "-multi-line comment delimeter")
					multilinecomment = False
				else:
					print(token,"-multi-line comment word")

		singlelinecomment = False

	fileHandle.close()
lexicalAnalysis()