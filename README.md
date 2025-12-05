This is our MP for the Theory of Programming Languages Class

Created by Ong & Tan

### HOW TO
At its core, it is a simple interpreted language, using a mix of Filipino words as the primary Keywords. Debating whether to upload the docs or not. 

Don't forget to install the Antlr library:
`pip install antlr4-tools`

If you want to change the grammar, run:
`antlr4 -Dlanguage=Python3 -visitor FilipinoCode.g4`
This will regenerate all of Antlr's stuff. 

If you want to change how the interpreter works, edit `FilipinoInterpreter2.py`. You can also edit the symbol table and the extra `accounts` class/datatype.

### Scoring
| #  | Feature                                                     | Score        | Notes                                                                                          |
|----|-------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------|
| 1  | Error Handling (Lexical and Syntax)                         | **5/5**      |                                                                                                |
| 2  | Primitive Data Types and Variable Implementation            | **8/8**      | Int, Float, String (Python `str`), Char, Bool                                                  |
| 3  | Type Checking                                               | **16/16**    |                                                                                                |
| 4  | Runtime Memory Management (Scope and Address)               | **10/10**    | Mostly scoping; limited per `{ <code> }` block; blocks required even for single lines         |
| 5  | Arithmetic Expressions                                      | **26/26**    | PEMDAS                                                                                        |
| 6  | Logical Expressions                                         | **16/16**    |                                                                                                |
| 7  | Assignment Statements                                       | **26/26**    |                                                                                                |
| 8  | Conditional Statements                                      | **26/26**    |                                                                                                |
| 9  | Iterative Statements (For loop, While loop)                 | **26/26**    | Loop inside the loop; Break and Continue (idk if required)                                     |
| 10 | Input/Output System                                         | **26/26**    |                                                                                                |
| 11 | Subprograms / Subroutines (Functions)                       | **16/16**    | Must implement with recursion                                                                  |
| **EXTRA FEATURES** |                                             |              |                                                                                                |
| 12 | Collection Data Types / ADTs / OOP                          | **+5/10**    | `accounts` datatype                                                                            |
| 13 | Exception Handling                                          | **+4/8**     | try-catch; buggy in functions and possibly scoping                                             |
| 14 | Auxiliary Features                                          | **+8/16**    | Simple debugger; coercion; `"kind"`                                                            |
|    | **TOTAL**                                                   | **218/200**  |                                                                                                |

Looking back, I thought that we got bonus points for adding short circuiting in logicals/conditionals. I guess not? I swear I read it though.

### Other notes: 
- The "kind" keyword basically adds an attribute to each node CONTEXT `ctx`, so that the interpreter does not have to traverse the full tree to check what kind of `ctx` it is.
- Technically there's also some sort of memory chaching for functions, but I did not test it (nor did I demo it because I dont know how to show that it's faster. It works though).
- Negative number assignment works. Don't forget to allow this. 
- Interpreter extends Visitor, which extends ParseTree. 
- Error recovery is important. Antlr has some built in, but it can make your code run funny. 
- Check for zero division! (especially with I/O in try catch)
- Make a test that does recursion already. So that there's no live coding of Fibonacci or whatever.
- Technically, Python allows expression (AND/OR) expression, so putting numbers on either side (any number) will work. Java does not allow this. We chose to make it 0 and 1 only. 

### Major(ish) Issues:
- Try Catch is buggy
- No implementation of `++` and `--`
- Does not implement complex data types
- The tree parsing/node visiting can be shortened; there are techniques to do so. We did not implement this.
- Try adding a domain layer on top of this. Like make it a language specialzied for something else.
- Try adding other constructs.
- No implementation of the `None` that Python has... Well technically, it's in the grammar, just not implemented to work.
- 
