from flask import Flask,render_template,request,redirect,session
import os
import re
app=Flask(__name__)
app.secret_key="Maths3021"
def guard_of_eval(exp):
    return re.sub(r'[^0-9+\-*/.]', '', exp)
@app.route("/",methods=["GET","POST"]) 
#Main function   
def mainfunc():
    #Initializing the values by deafult.
    #current_expression is for the newer value.
    current_expression= session.get("current_expression","0")#0 as deafult
    expression= session.get("expression","0")#0 as deafult
    #expression is for the first and the starting value.
    answer= session.get("answer","0") #0 as deafult
    if request.method=="POST":
        numbers=request.form.get("num_button")
        oper=request.form.get("op_button")
        func=request.form.get("func_button")
        expected_option= numbers or oper or func
        session["expression"]=request.form.get("display_box") or session["current_expression"] 
        #If any options/buttons are pressed.
        if expected_option:
            print("POSTED")
            #Checking for number (options/buttons).
            if expected_option == numbers:
                if session["expression"]=="0" and expected_option!=".":
                    session["current_expression"]=session["expression"].replace("0",expected_option)
                elif expected_option=="." and session["expression"][-1] in "1234567890" or session["expression"][-1]=="3.14":#type:ignore
                    session["current_expression"]= session["expression"] + expected_option
                else:
                    session["current_expression"]=session["expression"] + expected_option
            #Checking for operator (options/buttons).
            elif expected_option == oper:
                if session["expression"] [-1] in "+-*/":
                    session["current_expression"]= session["expression"]+expected_option
                elif session["expression"][-1] in "1234567890":
                    session["current_expression"]=session["expression"]+expected_option
            #Checking for functionalble (options/buttons).
            elif expected_option == func:
            #Checking for (AC/Clear all) (options/buttons).
                if expected_option =="AC":
                    session["current_expression"]="0"
            #Checking for (Del/Delete) (options/buttons).
                elif expected_option=="Del":
                    if session["expression"]!="0" and  len(session["expression"])>1:
                        session["current_expression"]= session["expression"][:-1]
                    else:
                        session["current_expression"]="0"  
            #Checking for (Ans/Anwer holder) (options/buttons).
                elif expected_option=="Ans":
                    if session["expression"][-1] in "+-/*":
                        session["current_expression"]=session["expression"]+session["answer"]
                    elif session["expression"] =="0":
                        session["current_expression"] = session["answer"]
            #Checking for (Calc/Calculating)(options/buttons),Main function.
                elif expected_option=="Calc":
                    try:#For handling aswell as displaying errors!
                        the_result=str(eval(guard_of_eval(session["expression"])))                   
                        session["current_expression"]=the_result#Giving output in diplay_box
                        session["answer"]=the_result#Saving the result.
                    except ValueError as vale:
                        print("Value Eror",vale)
                        session["current_expression"]="#Value Error!"
                    except ZeroDivisionError as zero:
                        print("Zero Division Error!",zero)
                        session["current_expression"]="#Zero Division Error!"
                    except SyntaxError as sin:
                        print("Invalid Syntax!",sin)
                        session["current_expression"]="#Syntax Error!"
                    except Exception as el:
                        print("Unknown Error Ocuured!",el)
                        session["current_expression"]="#Unknown Error Ocuured!"
            #Modifying the session and updating the values.
            # session["current_expression"]=current_expression the session gets changed.
            current_expression=session["current_expression"]#the varibale gets changed.
            session["expression"]=current_expression#updating older value by newer value
            answer =session.get("answer","0")   
            session.modified=True                                               
        return redirect("/")#For handling refresh and redirecting program to main.
    print(expression)
    return render_template("App.html",expression=expression,answer=answer)
#Logic to run the app in the certain port and by he ceratin file only.(Makes it secure and private)
if __name__=="__main__":
    ported=int(os.environ.get("PORT",3021))
    app.run(debug=False,port=ported,host="0.0.0.0")#Running function!

