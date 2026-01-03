from flask import Flask,render_template,request,redirect
import os
app=Flask(__name__)
current_expression="0"#For saving and adding logic and condition from expression displayed expression(Also for showing result combined with the before expressin and newer.)
answer="0"#for (Ans)
@app.route("/",methods=["GET","POST"]) 
#Main function                                                         
def mainfunc():
    #Global vaiables can be used anywhere:
    global expression
    global current_expression
    global funcer
    global answer
    #For instructions.
    if request.method=="POST":
        numbers=request.form.get("num_button")
        oper=request.form.get("op_button")
        func=request.form.get("func_button")
        expected_option= numbers or oper or func
        expression=request.form.get("display_box") or current_expression
        #If any options/buttons are pressed.
        if expected_option:
            #Checking for number (options/buttons).
            if expected_option == numbers:
                if expression=="0" and expected_option!=".":
                    current_expression=expression.replace("0",expected_option)
                elif expected_option=="." and expression[-1] in "1234567890" or expression[-1]=="3.14":#type:ignore
                    current_expression= expression + expected_option
                else:
                    current_expression=expression + expected_option
            #Checking for operator (options/buttons).
            elif expected_option == oper:
                if expression [-1] in "+-*/":
                    current_expression= expression+expected_option
                elif expression[-1] in "1234567890":
                    current_expression=expression+expected_option
            #Checking for functionalble (options/buttons).
            elif expected_option == func:
            #Checking for (AC/Clear all) (options/buttons).
                if expected_option =="AC":
                    current_expression="0"
            #Checking for (Del/Delete) (options/buttons).
                elif expected_option=="Del":
                    if expression!="0" and  len(expression)>1:
                        current_expression= expression[:-1]
                    else:
                        current_expression="0"  
            #Checking for (Ans/Anwer holder) (options/buttons).
                elif expected_option=="Ans":
                    if expression[-1] in "+-/*":
                        current_expression=expression+ answer
                    elif expression =="0":
                        current_expression = answer
            #Checking for (Calc/Calculating)(options/buttons),Main function.
                elif expected_option=="Calc":
                    try:#For handling aswell as displaying errors!
                        funcer="="
                        the_result=str(eval(expression))                   
                        current_expression=the_result#Giving output in diplay_box
                        answer=the_result#Saving the result.
                    except ValueError as vale:
                        print("Value Eror",vale)
                        current_expression="#Value Error!"
                    except ZeroDivisionError as zero:
                        print("Zero Division Error!",zero)
                        current_expression="#Zero Division Error!"
                    except SyntaxError as sin:
                        print("Invalid Syntax!",sin)
                        current_expression="#Syntax Error!"
                    except Exception as el:
                        print("Unknown Error Ocuured!",el)
                        current_expression="#Unknown Error Ocuured!"
        return redirect("/")#For handling refresh and redirecting program to main.
    return render_template("App.html",expression=current_expression,answer=answer)
#Logic to run the app in the certain port and by he ceratin file only.(Makes it secure and private)
if __name__=="__main__":
    ported=int(os.environ.get("PORT",3021))
    app.run(debug=False,port=ported,host="0.0.0.0")#Running function!

