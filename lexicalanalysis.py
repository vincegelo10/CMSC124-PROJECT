import re 

classified_lexemes = []

#HERE ARE THE LEXEMES WITH SPACES
LEXEMES_SPACES = ["SUM OF","DIFF OF","PRODUKT OF","QUOSHUNT OF","MOD OF","BIGGR OF","SMALLR OF","BOTH OF","EITHER OF","WON OF","ANY OF","ALL OF","BOTH SAEM","I HAS A","IS NOW A","O RLY?","YA RLY","NO WAI","IM IN YR","IM OUTTA YR"]
ARITHMETIC_OP = ["SUM OF","DIFF OF","PRODUKT OF","QUOSHUNT OF","MOD OF","BIGGR OF","SMALLR OF"]
BOOLEAN_OP = ["BOTH OF","EITHER OF","WON OF","ANY OF","ALL OF"]
COMPARISON_OP = ["BOTH SAEM"]
VARIABLE_DECLARATION = ["I HAS A"]
TYPECAST = ["IS NOW A"]
IF_THEN_LEXEMES = ["O RLY?","YA RLY","NO WAI"]
IF_STATEMENT_DELIM = "O RLY?"
IF_STATEMENT = "YA RLY"
ELSE_STATEMENT = "NO WAI"
LOOP_DELIM = ["IM IN YR","IM OUTTA YR"]


def lexicalAnalysis():
	
	if_else = False
	switch_case = False
	singlelinecomment = False
	multilinecomment = False
	isString = False
	lexeme_with_space = False
	expecting_identifier = False
	Error = False
	
	LEXEMES_SPACES2 = []
	VARIABLE_IDENTIFIERS = []

	for lexeme in LEXEMES_SPACES:
		lexeme = lexeme.split()
		for token in lexeme:
			LEXEMES_SPACES2.append(token)


	fileHandle = open("sample.txt",'r')
	for line in fileHandle:
		line = line.split()
		lexeme = ""
		YARN = ""
		for token in line:
			if not singlelinecomment and not multilinecomment and not lexeme_with_space and not isString:
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
				elif re.search("^OIC$", token):					
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
				elif re.search("^GIMMEH$",token):
					classified_lexemes.append({"token": token, "type": "Input"})
				elif re.search("^(WIN|FAIL)$", token):
					classified_lexemes.append({"token": token, "type": "Troof"})
				elif re.search("^(TROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE)$",token):
					classified_lexemes.append({"token": token, "type": "Type Literal"})
				elif re.search("^BTW$", token):
					classified_lexemes.append({"token": token, "type": "Single-line comment delimeter"})
					singlelinecomment = True
				elif re.search("^OBTW$", token):
					classified_lexemes.append({"token": token, "type": "Multi-line comment delimeter"})
					multilinecomment = True
				elif token in LEXEMES_SPACES2:
					lexeme = token
					lexeme_with_space = True
				elif re.search("^-?[0-9]+$", token):
					classified_lexemes.append({"token": token, "type": "NUMBR"})
				elif re.search("^-?[0-9]+\.[0-9]+$",token):
					classified_lexemes.append({"token": token, "type": "NUMBAR"})
				elif re.search('^"[^"]+"$',token):
					classified_lexemes.append({"token": token, "type": "YARN"})
				elif re.search('^"[^"]*$',token):
					YARN = YARN + token
					isString = True
				elif expecting_identifier:
					if re.search("^[A-Za-z][A-Za-z0-9_]*$", token):
						classified_lexemes.append({"token": token, "type": "Identifier"})
						VARIABLE_IDENTIFIERS.append(token)
						expecting_identifier = False
				elif token in VARIABLE_IDENTIFIERS:
					classified_lexemes.append({"token": token, "type": "Identifier"})
				else:
					Error = True
					print("Error on: ",token)
					break
			elif lexeme_with_space:
				lexeme = lexeme + " " + token
				if lexeme in LEXEMES_SPACES:
					if lexeme in ARITHMETIC_OP:
						classified_lexemes.append({"token": lexeme, "type": "Arithmetic Op"})
						lexeme = ""
					elif lexeme in BOOLEAN_OP:
						classified_lexemes.append({"token": lexeme, "type": "Boolean Op"})
						lexeme = ""
					elif lexeme in COMPARISON_OP:
						classified_lexemes.append({"token": lexeme, "type": "Comparison Op"})
						lexeme = ""
					elif lexeme in VARIABLE_DECLARATION:
						classified_lexemes.append({"token": lexeme, "type": "Variable declaration"})
						lexeme = ""
						expecting_identifier = True
					elif lexeme in TYPECAST:
						classified_lexemes.append({"token": lexeme, "type": "Typecast"})
						lexeme = ""
					elif lexeme in LOOP_DELIM:
						classified_lexemes.append({"token": lexeme, "type": "Loop delimeter"})
						lexeme = ""
						expecting_identifier = True
					elif lexeme in IF_THEN_LEXEMES:
						if lexeme == IF_STATEMENT_DELIM:
							classified_lexemes.append({"token": lexeme, "type": "If statement delimeter"})
							if_else = True
							lexeme = ""
						elif lexeme == IF_STATEMENT:
							classified_lexemes.append({"token": lexeme, "type": "If statement"})
							lexeme = ""
						elif lexeme == ELSE_STATEMENT:
							classified_lexemes.append({"token": lexeme, "type": "Else statement"})
							lexeme = ""
					lexeme_with_space = False
	
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

		if len(lexeme) !=0:
			print("Error on: ", lexeme)
			break
		if Error:
			break

	fileHandle.close()

def classifyIdentifiers():
	for i in range(0,len(classified_lexemes)):
		if classified_lexemes[i]["type"] == "Identifier":
			if classified_lexemes[i-1]["type"] == "Variable declaration":
				classified_lexemes[i]["type"] = "Variable identifier"
				for j in range(i+1,len(classified_lexemes)):
					if classified_lexemes[i]["token"] == classified_lexemes[j]["token"]:
						classified_lexemes[j]["type"] = "Variable identifier"
			elif classified_lexemes[i-1]["type"] == "Loop delimeter":
				classified_lexemes[i]["type"] = "Loop identifier"
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


