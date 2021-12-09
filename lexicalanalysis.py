import re 

class lex:
    def __init__(self,token,type):
        self.token = token
        self.type = type
    def printLex(self):
        print(self.token+" : "+self.type)

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

LEXICAL_ANALYSIS_ERROR = False

def lexicalAnalysis():

	global LEXICAL_ANALYSIS_ERROR
	
	if_else = False
	switch_case = False
	singlelinecomment = False
	multilinecomment = False
	isString = False
	lexeme_with_space = False
	
	LEXEMES_SPACES2 = []

	for lexeme in LEXEMES_SPACES:
		lexeme = lexeme.split()
		for token in lexeme:
			LEXEMES_SPACES2.append(token)

	line_count = 0
	fileHandle = open("arith.lol",'r')
	for line in fileHandle:
		line = line.split()
		lexeme = ""
		YARN = ""
		line_count += 1
		lexeme_in_line = []
		for token in line:
			if not singlelinecomment and not multilinecomment and not lexeme_with_space and not isString:
				if re.search("^HAI$",token):
					lexeme_in_line.append(lex(token,"Code delimiter"))
				elif re.search("^KTHXBYE$", token):
					lexeme_in_line.append(lex(token,"Code delimiter"))
				elif re.search("^ITZ$", token):
					lexeme_in_line.append(lex(token,"Variable Initialization"))
				elif re.search("^R$", token):
					lexeme_in_line.append(lex(token,"Variable assignment"))
				elif re.search("^NOT$", token):
					lexeme_in_line.append(lex(token,"Negation"))
				elif re.search("^DIFFRINT$", token):
					lexeme_in_line.append(lex(token,"Comparison Op"))
				elif re.search("^SMOOSH$", token):
					lexeme_in_line.append(lex(token,"Concatenation"))
				elif re.search("^MAEK$", token):
					lexeme_in_line.append(lex(token,"Typecast"))
				elif re.search("^VISIBLE$", token):
					lexeme_in_line.append(lex(token,"Print"))
				elif re.search("^MEBBE$", token):
					lexeme_in_line.append(lex(token,"Else-if condition"))
				elif re.search("^AN$", token):
					lexeme_in_line.append(lex(token,"Operand Separator"))
				elif re.search("^OIC$", token):					
					if if_else:
						lexeme_in_line.append(lex(token,"If-then delimiter"))
						if_else = False
					elif switch_case:
						lexeme_in_line.append(lex(token,"Switch-case delimiter"))
						switch_case = False
				elif re.search("^WTF?$", token):
					lexeme_in_line.append(lex(token,"Switch-case delimiter"))
					switch_case = True
				elif re.search("^OMG$", token):					
					lexeme_in_line.append(lex(token,"Switch-case condition"))
				elif re.search("^OMGWTF$", token):
					lexeme_in_line.append(lex(token,"Switch-case default condition"))
				elif re.search("^UPPIN$",token):
					lexeme_in_line.append(lex(token,"Loop Increment"))
				elif re.search("^NERFIN$",token):
					lexeme_in_line.append(lex(token,"Loop Decrement"))
				elif re.search("^TIL$",token):
					lexeme_in_line.append(lex(token,"Loop Condition"))
				elif re.search("^WILE$",token):
					lexeme_in_line.append(lex(token,"Loop Condition"))
				elif re.search("^GIMMEH$",token):
					lexeme_in_line.append(lex(token,"Input"))
				elif re.search("^(WIN|FAIL)$", token):
					lexeme_in_line.append(lex(token,"Troof"))
				elif re.search("^(TROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE)$",token):
					lexeme_in_line.append(lex(token,"Type Literal"))
				elif re.search("^BTW$", token):
					lexeme_in_line.append(lex(token,"Single-line comment delimiter"))
					singlelinecomment = True
				elif re.search("^OBTW$", token):
					lexeme_in_line.append(lex(token,"Multi-line comment delimiter"))
					multilinecomment = True
				elif token in LEXEMES_SPACES2:
					lexeme = token
					lexeme_with_space = True
				elif re.search("^-?[0-9]+$", token):
					lexeme_in_line.append(lex(token,"NUMBR"))
				elif re.search("^-?[0-9]+\.[0-9]+$",token):
					lexeme_in_line.append(lex(token,"NUMBAR"))
				elif re.search('^"[^"]+"$',token):
					lexeme_in_line.append(lex(token,"YARN"))
				elif re.search('^"[^"]*$',token):
					YARN = YARN + token
					isString = True
				elif re.search("^[A-Za-z][A-Za-z0-9_]*$", token):
						lexeme_in_line.append(lex(token,"Identifier"))
				
			elif lexeme_with_space:
				lexeme = lexeme + " " + token
				if lexeme in LEXEMES_SPACES:
					if lexeme in ARITHMETIC_OP:
						lexeme_in_line.append(lex(lexeme,"Arithmetic Op"))
						lexeme = ""
					elif lexeme in BOOLEAN_OP:
						lexeme_in_line.append(lex(lexeme,"Boolean Op"))
						lexeme = ""
					elif lexeme in COMPARISON_OP:
						lexeme_in_line.append(lex(lexeme,"Comparison Op"))
						lexeme = ""
					elif lexeme in VARIABLE_DECLARATION:
						lexeme_in_line.append(lex(lexeme,"Variable declaration"))
						lexeme = ""
					elif lexeme in TYPECAST:
						lexeme_in_line.append(lex(lexeme,"Typecast"))
						lexeme = ""
					elif lexeme in LOOP_DELIM:
						lexeme_in_line.append(lex(lexeme,"Loop delimiter"))
						lexeme = ""
					elif lexeme in IF_THEN_LEXEMES:
						if lexeme == IF_STATEMENT_DELIM:
							lexeme_in_line.append(lex(lexeme,"If statement delimiter"))
							if_else = True
							lexeme = ""
						elif lexeme == IF_STATEMENT:
							lexeme_in_line.append(lex(lexeme,"If statement"))
							lexeme = ""
						elif lexeme == ELSE_STATEMENT:
							lexeme_in_line.append(lex(lexeme,"Else statement"))
							lexeme = ""
					lexeme_with_space = False
	
			elif isString:
				if re.search('^[^"]*"$',token):
					YARN = YARN + " " + token
					if not re.search('^" +"$',YARN):
						lexeme_in_line.append(lex(YARN,"YARN"))
					isString = False
					YARN = ""
				else:
					YARN = YARN + " " + token
			elif singlelinecomment:
				lexeme_in_line.append(lex(token,"Single-line comment word"))
				
			elif multilinecomment:
				if re.search("^TLDR$", token):
					lexeme_in_line.append(lex(token,"Multi-line comment delimiter"))
					multilinecomment = False
				else:
					lexeme_in_line.append(lex(token,"Multi-line comment word"))


		singlelinecomment = False

		if len(lexeme) !=0:
			print("Lexical Analysis Error")
			print("Error on line ",line_count," at ", lexeme)
			LEXICAL_ANALYSIS_ERROR = True
			break

		if len(lexeme_in_line) == 0:
			continue
		else:
			classified_lexemes.append(lexeme_in_line)
	fileHandle.close()

def classifyIdentifiers():

	global LEXICAL_ANALYSIS_ERROR

	for i in range(0,len(classified_lexemes)):
		for j in range(0,len(classified_lexemes[i])):
			if classified_lexemes[i][j].type == "Identifier":
					if classified_lexemes[i][j-1].type == "Variable declaration":
						classified_lexemes[i][j].type = "Variable identifier"
					elif classified_lexemes[i][j-1].type == "Loop delimeter":
						classified_lexemes[i][j].type= "Loop identifier"
					else:
						if classified_lexemes[i][j].token == "IT":
							classified_lexemes[i][j].type = "Implicit variable"
						else:
							print("Error on: ",classified_lexemes[i][j].token,"not recognized")
							LEXICAL_ANALYSIS_ERROR = True

					current_variable = classified_lexemes[i][j].token
					current_variable_type = classified_lexemes[i][j].type 

					if current_variable != "IT":
						for line in classified_lexemes:
							for lexeme in line:
								if current_variable == lexeme.token:
									lexeme.type = current_variable_type

				

def printLexemes():
	print("----------LEXEMES----------")
	for line in classified_lexemes:
		for lexeme in line:
			lexeme.printLex()
		

lexicalAnalysis()
classifyIdentifiers()

if not LEXICAL_ANALYSIS_ERROR:
	printLexemes()
