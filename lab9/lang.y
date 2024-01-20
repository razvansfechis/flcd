%{
#include <stdio.h>
#include <stdlib.h>

int yyerror(char *s);

#define YYDEBUG 1
%}

%token INTEGER;
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
%token DIV;
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

%start Program

%%
Program: START curlyLeftBracket compound_statement curlyRightBracket  { printf("PARSER: Program -> start { compound_statement }\n"); }
;

compound_statement : statement semicolon compound_statement { printf("PARSER: compound_statement -> statement ; compound_statement\n"); }
	| statement semicolon   { printf("PARSER: compound_statement -> Statement ;\n"); }
;

statement :declaration_statement     { printf("PARSER: Statement -> declaration_statement\n"); }
          | assignment_statement     { printf("PARSER: Statement -> assignmentStatement\n"); }
          | if_statement     { printf("PARSER: Statement -> ifStatement\n"); }
          | while_statement     { printf("PARSER: Statement -> whileStatement\n"); }
          | print_statement     { printf("PARSER: Statement -> printStatement\n"); }
          | read_statement     { printf("PARSER: Statement -> readStatement\n"); }
          ;
          
declaration_statement : ID type comma declaration_statement     { printf("PARSER: declaration_statement -> ID ( type ) , declaration_statement\n"); }
         | ID  type      { printf("PARSER: declaration_statement -> ID ( Type )\n"); }
         ;

type : INTEGER     { printf("PARSER: Type -> integer\n"); }
| STR     { printf("PARSER: Type -> str\n"); }
| CHAR     { printf("PARSER: Type -> char\n"); }
;

assignment_statement : ID equal expression     { printf("PARSER: AssignmentStatement -> ID = Expression\n"); }
                    ;
         
expression : expression plus term     { printf("PARSER: Expression -> Expression + Term\n"); }
           | expression minus term     { printf("PARSER: Expression -> Expression - Term\n"); }
           | term     { printf("PARSER: Expression -> Term\n"); }
           ;
         
term : term times factor     { printf("PARSER: term -> term * factor\n"); }
| term DIV factor     { printf("PARSER: term -> term / factor\n"); }
| factor     { printf("term -> factor\n"); }
;

factor : roundLeftBracket expression roundRightBracket     { printf("PARSER: factor -> ( expression )\n"); }
       | ID     { printf("PARSER: factor -> ID\n"); }
       | INT_CONSTANT     { printf("PARSER: Factor -> INT_CONSTANT\n"); }
       | minus ID     { printf("PARSER: factor -> - ID\n"); }
       ;

expression_list : expression comma expression_list    { printf("PARSER: expression_list -> Expression , ExpressionList\n"); }
| expression    { printf("PARSER: expression_list -> expression\n"); }
;

if_statement : IF condition roundLeftBracket compound_statement roundRightBracket  { printf("PARSER: IfStatement -> if Expression { compound_statement }\n"); }
            | IF condition roundLeftBracket compound_statement roundRightBracket ELSE roundLeftBracket compound_statement roundRightBracket  { printf("PARSER: IfStatement -> if expression { compound_statement } else { compound_statement }\n"); }
            ;
print_statement : PRINT roundLeftBracket expression roundRightBracket     { printf("PARSER: print_statement -> print ( Expression )\n"); }
| PRINT roundLeftBracket STRING_CONSTANT roundRightBracket     { printf("PARSER: print_statement -> print ( STRING_CONSTANT )\n"); }
;
read_statement : READ roundLeftBracket ID roundRightBracket     { printf("PARSER: read_statement -> read ( ID )\n"); }
;
            
while_statement : WHILE condition curlyLeftBracket compound_statement curlyRightBracket  { printf("PARSER: WhileStatement -> while Expression { compound_statement }\n"); }
   ;
         
condition : expression relation expression     { printf("PARSER: Condition -> Expression Relation Expression\n"); }
;
         
relation : less     { printf("PARSER: Relation -> <\n"); }
         | lessOrEqual     { printf("PARSER: Relation -> <=\n"); }
         | equalEqual     { printf("PARSER: Relation -> ==\n"); }
         | notEqual     { printf("PARSER: Relation -> <>\n"); }
         | biggerOrEqual     { printf("PARSER: Relation -> >=\n"); }
         | bigger     { printf("PARSER: Relation -> >\n"); }
         | assignType { printf("PARSER: AssignType -> >\n"); }
         | assignVar { printf("PARSER: AssignVar -> >\n"); }
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