%{
#include <stdio.h>
#include <stdlib.h>

int yyerror(char *s);

#define YYDEBUG 1
%}

%token INT;
%token STR;
%token CHAR;
%token READ;
%token IF;
%token ELSE;
%token PRINT;
%token WHILE;
%token AND;
%token START;

%token plus;
%token mod;
%token minus;
%token times;
%token div;
%token less;
%token lessOrEqual;
%token equal;
%token notEqual;
%token biggerOrEqual;
%token equalEqual;
%token bigger;
%token assignType;
%token assignVar;

%token leftBracket;
%token rightBracket;
%token semicolon;
%token roundLeftBracket;
%token roundRightBracket;
%token curlyLeftBracket;
%token curlyRightBracket;
%token comma;

%token ID;
%token INT_CONSTANT;
%token STRING_CONSTANT;

%start program

%%

program: START curlyLeftBracket compound_statement curlyRightBracket  { printf("PARSER: Program -> start { compound_statement }\n"); }
;

compound_statement : statement semicolon compounds statement { printf("PARSER: compound_statement -> statement ; compound_statement\n"); }
	| statement semicolon   { printf("PARSER: compound_statement -> Statement ;\n"); }
;

statement :declaration_statement     { printf("PARSER: Statement -> declaration_statement\n"); }
          | assignmentStatement     { printf("PARSER: Statement -> assignmentStatement\n"); }
          | ifStatement     { printf("PARSER: Statement -> ifStatement\n"); }
          | whileStatement     { printf("PARSER: Statement -> whileStatement\n"); }
          | printStatement     { printf("PARSER: Statement -> printStatement\n"); }
          | readStatement     { printf("PARSER: Statement -> readStatement\n"); }
          ;
          
declaration_statement : ID Type comma declaration_statement     { printf("PARSER: declaration_statement -> ID ( Type ) , declaration_statement\n"); }
         | ID  Type      { printf("PARSER: declaration_statement -> ID ( Type )\n"); }
         ;
         
Term : Term TIMES Factor     { printf("PARSER: Term -> Term * Factor\n"); }
| Term DIV Factor     { printf("PARSER: Term -> Term / Factor\n"); }
| Factor     { printf("Term -> Factor\n"); }
;
         
Relation : less     { printf("PARSER: Relation -> <\n"); }
         | lessOrEqual     { printf("PARSER: Relation -> <=\n"); }
         | equalEqual     { printf("PARSER: Relation -> ==\n"); }
         | notEqual     { printf("PARSER: Relation -> <>\n"); }
         | biggerOrEqual     { printf("PARSER: Relation -> >=\n"); }
         | bigger     { printf("PARSER: Relation -> >\n"); }
         ;

         
         %%
int yyerror(char *s) {
    printf("PARSER: Error: %s", s);
}

extern FILE *yyin;

int main(int argc, char** argv) {
    if (argc > 1) 
        yyin = fopen(argv[1], "r");
    if (!yyparse()) 
        fprintf(stderr, "\tOK\n");
}