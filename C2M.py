# -*- coding: utf-8 -*-
import re
import pandas as pd
global list_of_predifine
list_of_predifine=['printf']
logical_operator=[(' && ','AND'),(' || ','OR'),('!','NOT'),(' & ','bitwiseAND')]
relational_operator=[('  ','equalto'),('! ','notequalto'),(' > ','greatethan'),(' < ','lessthan'),('<=','lessthanequalto'),('>=','greaterthanequalto')]
arithmetic_operator=[(' - ','Sub'),(' + ','Sum'),(' * ','product'),(' / ','Divide')]

global outputfilename
outputfilename='specify the name of output file that you want to generate here' 
import pandas as pd
global internals_signals
global const_list 
global temp_const
temp_const=0
global temp_digit_const
temp_digit_const=0
global inut_port_list
global temp_var_const
global switch_const_if
switch_const_if=[]
global switch_ref_if
switch_ref_if=[]
global switch_const_else
switch_const_else=[]
global switch_ref_else
switch_ref_else=[]
temp_var_const=[]
global float_const_ac
float_const_ac=[]
global float_const_ref
float_const_ref=[]
global lhs_list_done
lhs_list_done=[]
global const_count
const_count=0
global unit_delay_pair
unit_delay_pair=[('xyz','abc')]
global const_count_static_cond
const_count_static_cond=10000
global const_count_1
const_count_1=2000
def generate_mfile(input_sig,output,const_list):
    global internals_signals
    global temp_const
    global temp_digit_const
    output=output.strip()
    logical_operation=0
    # unitdelay=0
    arithmetic_operation=0
    relational_operation=0
    pairwise_logic=list(zip(*logical_operator))
    pairwise_relation=list(zip(*relational_operator))
    pairwise_arithmetic=list(zip(*arithmetic_operator))
    global inut_port_list
    global float_const_ref
    global unit_delay_pair
    constant_block=0
    input_sig=input_sig.strip()
    unity_blok=0
    memory_blok=0

    for logic in pairwise_logic[0]:
        if logic in output:
            output_val=output.split(logic)
            if '' in output_val:    
                output_val.remove('')
            logical_operation=1
            break

    for relation in pairwise_relation[0]:
        if relation in output:
            output_val=output.split(relation)
            if '' in output_val:    
                output_val.remove('')
            relational_operation=1
            break
        
        
        
    for aritmetic in pairwise_arithmetic[0]:
        if aritmetic in output:
            output_val=output.split(aritmetic)
            if '' in output_val:    
                output_val.remove('')
            arithmetic_operation=1
            break
    
    if logical_operation==1:
        if (logic==" && " or logic=="&&"):
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Logical Operator','mymodel/"+input_sig+"','Operator','AND','Inputs','"+str(len(output_val))+"');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if logic==" || ":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Logical Operator','mymodel/"+input_sig+"','Operator','OR','Inputs','"+str(len(output_val))+"');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if logic=="!":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Logical Operator','mymodel/"+input_sig+"','Operator','NOT','Inputs','"+str(len(output_val))+"');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if logic==" & ":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Logical Operator','mymodel/"+input_sig+"','Operator','Logical AND','Inputs','"+str(len(output_val))+"');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
       # print(output_val)
            
            
            
    if relational_operation==1:           
        if relation=="  ":
            #print(input_sig)
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Relational Operator','mymodel/"+input_sig+"','Operator','==');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if relation==" > ":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Relational Operator','mymodel/"+input_sig+"','Operator','>');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if relation==' >= ':
                with open(str(outputfilename),'a') as f:
                    f.write("add_block('simulink/Logic and Bit Operations/Relational Operator','mymodel/"+input_sig+"','Operator','>=');"+"\n")
                    f.close()
                lhs_list_done.append(input_sig)
        if relation==" < ":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Relational Operator','mymodel/"+input_sig+"','Operator','<');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if relation==' <= ':
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Relational Operator','mymodel/"+input_sig+"','Operator','<=');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        
            
    if arithmetic_operation==1:
        if aritmetic==" - ":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Math Operations/Add','mymodel/"+str(input_sig)+"','Inputs','+-');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if aritmetic==" + ":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Math Operations/Add','mymodel/"+str(input_sig)+"','Inputs','+-');"+"\n")
                f.close()
            lhs_list_done.append(input_sig)
        if aritmetic==" * ":
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Math Operations/Product','mymodel/"+str(input_sig)+"','Inputs','2')\n")
                f.close()
            lhs_list_done.append(input_sig)
        if aritmetic==" / ":
            #print(output_val,input_sig)
            with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Math Operations/Divide','mymodel/"+str(input_sig)+"','Inputs','*/')\n")
                f.close()
            lhs_list_done.append(input_sig)
           
            
    if ('UnitDelay' in input_sig) :
        with open(str(outputfilename),'a') as f:
            f.write("add_block('simulink/Discrete/Unit Delay','mymodel/"+str(input_sig)+"'"+");"+"\n")
            f.close()
        unity_blok=1
        lhs_list_done.append(input_sig)
        
    if ('FlipFlop' in input_sig):
        with open(str(outputfilename),'a') as f:
            f.write("add_block('simulink/Discrete/Unit Delay','mymodel/"+str(input_sig)+"'"+");"+"\n")
            f.close()
        unity_blok=1
        lhs_list_done.append(input_sig)
        
        
    if 'Memory' in input_sig:
        with open(str(outputfilename),'a') as f:
            f.write("add_block('simulink/Discrete/Memory','mymodel/"+str(input_sig)+"'"+");"+"\n")
            f.close()
        memory_blok=1
        lhs_list_done.append(input_sig)
        
    for num in range(len(list(zip(*unit_delay_pair))[1])):
        output1=output.split('->')
        if list(zip(*unit_delay_pair))[1][num] in input_sig:
            with open(str(outputfilename),'a') as f:
                f.write("add_line('mymodel','"+str(output1[1][:-1])+"/1','"+str(list(zip(*unit_delay_pair))[0][num])+"/"+str(1)+"')\n")
                f.close()
            break
            
            
    if unity_blok==1:
        number=output.split('S')[1][0:6].replace(', ','')
        unit_delay_pair.append((input_sig,number))
    
    
    
    
    
    if (relational_operation==1 or logical_operation==1 or arithmetic_operation==1):
        
        for sig in output_val:
            if True:
                #print(sig)
                internals=0
                constant=0
                sig=sig.strip()
                if "(" in sig:
                    sig=sig.replace("(","")
                if ")" in sig:
                    sig=sig.replace(")","")
                if ";" in sig:
                    sig=sig.replace(";","")
                constant_block=0
                if sig.lstrip('+-').replace('.', '', 1).isdigit():
                    temp_digit_const=temp_digit_const+1
                    constant_block==1
                    with open(str(outputfilename),'a') as f:
                        f.write("add_block('simulink/Sources/Constant','mymodel/const"+str(temp_digit_const)+"',"+"'Value',"+"'"+str(sig)+"');"+"\n")
                        f.close()
                    float_const_ac.append(sig)
                    float_const_ref.append("const"+str(temp_digit_const))    
                    
                 
               # print(sig)
                for val in internals_signals:
                    if "(" in sig:
                         sig=sig.replace("(","")
                    if ")" in sig:
                        sig=sig.replace(")","")
                    if val in sig:
                        
                        if sig in inut_port_list:
                            pass
                        else:
                            if sig not in lhs_list_done:
                                print(lhs_list_done)
                                print(sig)
                                internals=1
                                #print(val)
                                with open(str(outputfilename),'a') as f:
                                    f.write("add_block('simulink/Sources/In1','mymodel/"+str(val)+"')"+"\n")
                                    f.close()
                                lhs_list_done.append(sig)
                                inut_port_list.append(sig)
                                break
                            
                
                if internals==0:
                    for val1 in const_list:
                        temp_const=temp_const+1
                        if "(" in sig:
                             sig=sig.replace("(","")
                        if ")" in sig:
                            sig=sig.replace(")","")
                        if ";" in sig:
                            sig=sig.replace(";","")
                        if val1 == sig:
                            if sig in lhs_list_done:
                                constant=1
                                with open(str(outputfilename),'a') as f:
                                    f.write("add_block('simulink/Sources/Constant','mymodel/"+str(sig)+str(temp_const)+"',"+"'Value',"+"'"+str(sig)+"');"+"\n")
                                    f.close()
                                lhs_list_done.append(sig)
                                temp_var_const.append(str(sig)+str(temp_const))
                                break
                
                if (internals == 0 and constant== 0):
                    sig=sig.split('->')
                    #print(sig)
                    #print(inut_port_list)
                    if len(sig)>1:
                        if len(inut_port_list)==0:
                            if (('Logic[' in sig[1]) or ('Logic_' in sig[1])):
                                #print(sig[1])
                                with open(str(outputfilename),'a') as f:
                                       # print(sig)
                                    f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig[1])+"','BackgroundColor','red')"+"\n")
                                    f.close()
                                lhs_list_done.append(sig[1])
                                
                            else:
                                with open(str(outputfilename),'a') as f:
                                       # print(sig)
                                    f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig[1])+"')\n")
                                    f.close()
                                lhs_list_done.append(sig[1])
                                
                        
                        
                        if len(inut_port_list)>0:
                            for sf in inut_port_list:
                                if sf not in sig[1]:
                                    if sig[1] not in internals_signals:
                                       # print(sig[1])
                                        if sig[1] not in lhs_list_done:
                                            if (('Logic[' in sig[1]) or ('Logic_' in sig[1])):
                                                #print(sig[1])
                                                with open(str(outputfilename),'a') as f:
                                                       # print(sig)
                                                    f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig[1])+"','BackgroundColor','red')"+"\n")
                                                    f.close()
                                                lhs_list_done.append(sig[1])
                                                break
                                            else:
                                                with open(str(outputfilename),'a') as f:
                                                       # print(sig)
                                                    f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig[1])+"')\n")
                                                    f.close()
                                                lhs_list_done.append(sig[1])
                                                break
                                            
                                        
                                
                    if len(sig)==1:
                        if constant_block==0:
                            sig=sig[0]
                            sig=sig.split('_')
                            if len(sig)>2:    
                                sig='_'.join(sig[1:])
                            else:
                                sig='_'.join(sig)
                            if sig not in internals_signals:
                               if sig not in lhs_list_done:
                                    with open(str(outputfilename),'a') as f:
                                       # print(sig)
                                        f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig)+"')"+"\n")
                                        f.close()
                                    lhs_list_done.append(sig)
             
    ########################For Adding lines##########################################
            
        for inputs in range(len(output_val)):
            #if relational_operation==1:
            line_internal=0
            line_constant=0
            val_sig=output_val[inputs]
            val_sig=val_sig.strip()
            if "(" in val_sig:
                 val_sig=val_sig.replace("(","")
            if ")" in val_sig:
                val_sig=val_sig.replace(")","")
            if ";" in val_sig:
                val_sig=val_sig.replace(";","")
            
            
            val_sig=val_sig.split('->')
            if len(val_sig)>1:
                val_sig=val_sig[1]
            else:
                val_sig=val_sig[0]
            
            
            
            
            if val_sig in const_list:
                for temp_var in temp_var_const:
                    if val_sig in temp_var:
                        with open(str(outputfilename),'a') as f:
                            f.write("add_line('mymodel','"+str(temp_var)+"/1','"+str(input_sig)+"/"+str(inputs+1)+"')\n")
                            f.close()
                            line_constant=1
                            break
                            
                          
            elif val_sig in float_const_ac:
               for values in range(len(float_const_ac)):
                   if val_sig in float_const_ac[values]:
                       with open(str(outputfilename),'a') as f:
                           f.write("add_line('mymodel','"+str(float_const_ref[values])+"/1','"+str(input_sig)+"/"+str(inputs+1)+"')\n")
                           f.close()
                           line_constant=1
                           break
                           
                           
            for x in internals_signals:
                    if x in val_sig:
                        with open(str(outputfilename),'a') as f:
                            f.write("add_line('mymodel','"+str(x)+"/1','"+str(input_sig)+"/"+str(inputs+1)+"')\n")
                            f.close()
                            line_internal=1
                            break
            else:
                if (line_internal==0 and line_constant==0):
                    print(val_sig)
                    with open(str(outputfilename),'a') as f:
                        f.write("add_line('mymodel','"+str(val_sig)+"/1','"+str(input_sig)+"/"+str(inputs+1)+"')\n")
                        f.close()
                
def addingswitchblocks(switch):
     f=switch.find("/*")
     s=switch.find("*/")
     line_created=switch.replace(switch[f:s+2], '')
     if_else=line_created.split('else')
     ci1=if_else[0].find("(")
     ci2=if_else[0].find(")")
     ci_part1=if_else[0].find("{")
     ci_part2=if_else[0].find("}")
     if_part=if_else[0][ci_part1:ci_part2+1]
     conditoin_sig=if_else[0][ci1:ci2+1]
     ce1=if_else[1].find("{")
     ce2=if_else[1].find("}")
     else_part=if_else[1][ce1:ce2+1]
     name=if_part.split('=')
     global const_count
     global const_count_static_cond
     name_else=else_part.split('=')
     flaot_sig=0
     if_cond=0
     else_cond=0
     global switch_const_if
     global switch_ref_if
     global switch_const_else
     global switch_ref_else
     global const_count_1
     global lhs_list_done
     
     if len(name)>1:
         if '->' in name[0]:
             name=name[0].split('->')
             namef=name[1]
     

     sig_if=if_part.split('=')
     sig_else=else_part.split('=')
     
     
     if '->' in sig_if[1][:-2]:
         sig_iff=sig_if[1][:-2].split('->')[1]
     else:
         sig_iff=sig_if[1][:-2]
         
     if '->' in sig_else[1][:-2]:
         sig_elsef=sig_else[1][:-2].split('->')[1]
     else:
         sig_elsef=sig_else[1][:-2]
         
     

    
     with open(str(outputfilename),'a') as f:
        f.write("add_block('simulink/Signal Routing/Switch','mymodel/"+str(namef.strip())+"');\n")
        f.close()
        lhs_list_done.append(namef.strip())
         
        
     if '->' in conditoin_sig:
         
         if "(" in conditoin_sig:
                 conditoin_sig=conditoin_sig.replace("(","")
         if ")" in conditoin_sig:
                conditoin_sig=conditoin_sig.replace(")","")
         if ";" in conditoin_sig:
                conditoin_sig=conditoin_sig.replace(";","")
         #print(conditoin_sig)
         conditoin_sig=conditoin_sig.split('->')
         if len(conditoin_sig)>1:
             conditoin_sig=conditoin_sig[1]
         else:
            conditoin_sig=conditoin_sig[0]
            
         if conditoin_sig not in internals_signals:
             if conditoin_sig not in lhs_list_done:
                with open(str(outputfilename),'a') as f:
                    f.write("add_block('simulink/Sources/In1','mymodel/"+str(conditoin_sig)+"')"+"\n")
                    f.close()
                lhs_list_done.append(conditoin_sig)
         with open(str(outputfilename),'a') as f:
            f.write("add_line('mymodel','"+str(conditoin_sig)+"/1','"+str(namef.strip())+"/"+str(2)+"')\n")
            f.close()
                
     if '0.0 >= 1.0' in conditoin_sig:
         if "(" in conditoin_sig:
                 conditoin_sig=conditoin_sig.replace("(","")
         if ")" in conditoin_sig:
                conditoin_sig=conditoin_sig.replace(")","")
         if ";" in conditoin_sig:
                conditoin_sig=conditoin_sig.replace(";","")
                
         with open(str(outputfilename),'a') as f:    
            f.write("add_block('simulink/Sources/Constant','mymodel/constswitch"+str(const_count_static_cond)+"',"+"'Value',"+"'"+str(0)+"');"+"\n")
            f.close()
         with open(str(outputfilename),'a') as f:    
            f.write("add_block('simulink/Sources/Constant','mymodel/constswitch"+str(const_count_1)+"',"+"'Value',"+"'"+str(1)+"');"+"\n")
            f.close()
         with open(str(outputfilename),'a') as f:
                f.write("add_block('simulink/Logic and Bit Operations/Relational Operator','mymodel/"+str(const_count_static_cond)+"switch','Operator','>=');"+"\n")
                f.close()
         with open(str(outputfilename),'a') as f:
            f.write("add_line('mymodel','"+"constswitch"+str(const_count_static_cond)+"/1','"+str(const_count_static_cond)+"switch/"+str(1)+"')\n")
            f.close()
         with open(str(outputfilename),'a') as f:
            f.write("add_line('mymodel','"+"constswitch"+str(const_count_1)+"/1','"+str(const_count_static_cond)+"switch/"+str(2)+"')\n")
            f.close()
         with open(str(outputfilename),'a') as f:
            f.write("add_line('mymodel','"+str(const_count_static_cond)+"switch"+"/1','"+str(namef.strip())+"/"+str(2)+"')\n")
            f.close()
         const_count_static_cond=const_count_static_cond+1        
         const_count_1=const_count_1+1
     if sig_iff.strip().lstrip('+-').replace('.', '', 1).isdigit():
         if_cond=1
         flaot_sig=1
         const_count=const_count+1
         with open(str(outputfilename),'a') as f:   
             f.write("add_block('simulink/Sources/Constant','mymodel/constswitch"+str(const_count)+"',"+"'Value',"+"'"+str(sig_iff.strip())+"');"+"\n")
             f.close()
         switch_const_if.append(sig_iff)
         switch_ref_if.append("constswitch"+str(const_count))
         
         ####Adding line##########
         
         with open(str(outputfilename),'a') as f:
          f.write("add_line('mymodel','"+"constswitch"+str(const_count)+"/1','"+str(namef.strip())+"/"+str(1)+"');\n")
          f.close()
         
     if sig_elsef.strip().lstrip('+-').replace('.', '', 1).isdigit():
         else_cond=1
         const_count=const_count+1
        # print(sig_elsef)
         with open(str(outputfilename),'a') as f:   
             f.write("add_block('simulink/Sources/Constant','mymodel/constswitch"+str(const_count)+"',"+"'Value',"+"'"+str(sig_elsef.strip())+"');"+"\n")
             f.close()
         switch_const_else.append(sig_elsef)
         switch_ref_else.append("constswitch"+str(const_count))
         with open(str(outputfilename),'a') as f:   
             f.write("add_line('mymodel','"+"constswitch"+str(const_count)+"/1','"+str(namef.strip())+"/"+str(3)+"');\n")
             f.close()

         
     if True:
        if if_cond==1 and else_cond==1:
            pass
        if if_cond==1 and else_cond==0:
            sig_list=[sig_elsef]
            sig_num=2
            for sig in range(len(sig_list)):
                if sig_list[sig] not in internals_signals:
                    if sig_list[sig] not in lhs_list_done:
                        with open(str(outputfilename),'a') as f:
                            f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig_list[sig].strip())+"')"+"\n")
                            f.close()
                with open(str(outputfilename),'a') as f:
                   if sig_num==2:    
                       f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(3)+"')\n")
                   else:
                       if sig==0:    
                           f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(1)+"')\n")
                       else:
                           f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(3)+"')\n")
                   f.close()
                lhs_list_done.append(sig_list[sig].strip())
        if else_cond==1 and if_cond==0:
            sig_list=[sig_iff]
            sig_num=2
            for sig in range(len(sig_list)):
                if sig_list[sig] not in internals_signals:
                    if sig_list[sig] not in lhs_list_done:
                        with open(str(outputfilename),'a') as f:
                            f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig_list[sig].strip())+"')"+"\n")
                            f.close()
                with open(str(outputfilename),'a') as f:
                   if sig_num==2:    
                       f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(1)+"')\n")
                   else:
                       if sig==0:    
                           f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(1)+"')\n")
                       else:
                           f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(1)+"')\n")
                   f.close()
                lhs_list_done.append(sig_list[sig].strip())
            #print(lhs_list_done)
        if if_cond==0 and else_cond==0:
            sig_list=[sig_iff,sig_elsef]
            sig_num=1
            for sig in range(len(sig_list)):
                if sig_list[sig] not in internals_signals:
                    if sig_list[sig] not in lhs_list_done:
                        with open(str(outputfilename),'a') as f:
                            f.write("add_block('simulink/Sources/In1','mymodel/"+str(sig_list[sig].strip())+"')"+"\n")
                            f.close()
                with open(str(outputfilename),'a') as f:
                   if sig_num==2:    
                       f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(3)+"')\n")
                   else:
                       if sig==0:    
                           f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(1)+"')\n")
                       else:
                           f.write("add_line('mymodel','"+str(sig_list[sig].strip())+"/1','"+str(namef.strip())+"/"+str(3)+"')\n")
                   f.close()
                lhs_list_done.append(sig_list[sig].strip())
        
            
def list_of_fuctions(Data,const_list):
    list_of_functions_lhs=[]
    list_of_functions_rhs=[]
    combinator_line_nmber=[]
    Memory_line_number=[]
    skip=0
    last_line=0
    start_switch=0
    combinatory_count=0
    for i in range(len(Data)):
        
        Data[i]=Data[i].strip()
        if Data[i].endswith(';'):
            if '=' in Data[i]:
                if skip==0:
                    list_imp=Data[i].split("=")[0]
                    if '->' in list_imp:    
                        signal_name=list_imp.split('->')[1]
                    else:
                        signal_name=list_imp.split('->')[0]
                    list_of_functions_lhs.append(signal_name)
                    list_of_functions_rhs.append(''.join(Data[i].split("=")[1:]))
                last_line=i
                skip=0
                generate_mfile(signal_name,''.join(Data[i].split("=")[1:]),const_list)
            else:
                line_created=' '.join(Data[last_line+1:i+1])
                if 'CombinatorialLogic' in line_created:
                    pass
                else:
                    #print(line_created)
                    f=line_created.find("/*")
                    s=line_created.find("*/")
                    if (f==-1 and s==-1):
                        pass
                    else:    
                        line_created=line_created.replace(line_created[f:s+2], '')
                    list_imp=line_created.split("=")[0]
                    signal_name=list_imp.split('->')
                    if len(signal_name)>1:
                        signal_name=signal_name[1]
                    else:
                        signal_name=signal_name[0]
                    list_of_functions_lhs.append(signal_name)
                    list_of_functions_rhs.append(''.join(line_created.split("=")[1:]))
                    last_line=i
                    generate_mfile(signal_name,''.join(line_created.split("=")[1:]),const_list)
            
            
            
        if '/* Switch' in Data[i]:
            start_switch=i
        if 'End of Switch' in Data[i]:
            end_switch=i
            total_switch=''.join(Data[start_switch:end_switch+1])
            addingswitchblocks(total_switch)
        if 'CombinatorialLogic' in Data[i]:
            combinatory_count=combinatory_count+1
            combinator_line_nmber.append(i)
        if 'Memory' in Data[i]:
            pass
    print('Number of Combinatory box/boxes are',combinatory_count,'line numbers',combinator_line_nmber)
def number_of_parameters(result_functions):
    pass



def removing_printf(list_func):
    global list_of_predifine
    for keyword in list_of_predifine:
        for func in list(list_func):
            if keyword in func:
                list_func.remove(func)
    return(list_func)


def creating_constant_blocks(data):
    const_list=[]
    for i in data:    
        if 'Constant'in i:
            const=i.split('/')
            if "'" in const[-1]:
                val=const[-1].replace("'","")
            const_list.append(val.rstrip("\n"))
    return(const_list)

            
if __name__=="__main__":
    path='Specify your C code file path here'
    file="Code_Analysis.c"
    inut_port_list=[]
    internals_signals=[]  ###Signals that you want to specifically monitor
    with open(path+file,'r+') as f:
        data=f.readlines()
        f.close()
    const_list=creating_constant_blocks(data)
    result_funcitons=list_of_fuctions(data,const_list)
    with open(str(outputfilename),'a') as f:
         f.write("Simulink.BlockDiagram.arrangeSystem('myModel');\n")
         f.close()
