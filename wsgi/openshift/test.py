from wordlibrary import *
if __name__=="__main__":    
    syn_list = find_synonyms("sdf,sdfs")
    para_strings = read_para("sdf sdf  df sdf.")
    response =""
    for all_syn in syn_list:
        gl_line_num = 1
        num_occurance_file = 0
        response += '%s :<br/>' % all_syn[0]
        for para_num, para in enumerate(para_strings):
            num_occurance_para = 0
            for syn in all_syn:
                num_occurance_para += GetNumOccurances(para, syn)
            
            line_strings = read_line(para)
            line_strings_list = []
            for i in line_strings:
                if i is not '':
                    line_strings_list.append(i) 
 
            
            for line_num, line in enumerate(line_strings_list):
                num_occurance_line = 0
                line_num += 1 
                for syn in all_syn:
                    num_occurance_line  += GetNumOccurances(para, syn)
                num_occurance_file += num_occurance_line
                
                response += 'line %d = %d<br/>' %(gl_line_num, num_occurance_line)
                gl_line_num += 1
            response += 'para %d = %d<br/>' %(para_num + 1, num_occurance_para)
            
        response += 'Total per file : %d<br/>' %(num_occurance_file) 
    print response
