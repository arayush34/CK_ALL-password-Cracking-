#!/usr/bin/python3
import hashlib,os,pdfplumber,colorama,time,random,zipfile,msoffcrypto,io,threading,chardet
from itertools import product
from rarfile import RarFile

#creating a class for taking the values from the user and generating an answer from it 

class start_section_gen_value_case:
    
    # This is the case of Random Function which uses all the values .......
    def Random(mine,values,minimum,maximum,checker):
        characters = list(set(list(values)))
        for i in range(checker):
            answer = ""
            for ii in range(random.randint(minimum,maximum)):
                random.shuffle(characters)
                answer=answer+str(characters[0])
            yield answer

    #This is a case of Brute Froce function where it takes the value and yield the answer
    def Bforce(self,my_str,min,max):
        for i in range(min,max+1):
            for w in product(my_str,repeat=i):
                answer = "".join(w)
                yield answer

    #This is the Dictionary Attack Function which uses the created dictionary and the file path to crack it 
    def cdict(self,file_name_or_path):            
        f = open(file_name_or_path,"rb")
        the_list_of_password = f.readlines()
        f.close()
        for i in the_list_of_password:
            get = chardet.detect(i)
            cypher = get["encoding"]
            try:
                yield i.decode(cypher).replace("\n","")
            except:pass



# Here the class Helps to select values for different file format and settings for the system .........
class set_key_case:

    #The scerario is it takes PDF value checks for its for its cases 
    def set_pdf_case(self,name_of_file,answer):
        try:
            with pdfplumber.open(name_of_file,password=answer) as pdf:
                return True
        except pdfplumber.pdfminer.pdfdocument.PDFPasswordIncorrect:
            return False

    #RAR file is taken as an input and delivers the output ........................
    def set_rar_case(self,name_of_file,password):
        file_value = RarFile(name_of_file)
        decent = file_value.namelist()
        try:
            file_value.read(decent[0],pwd=str(password).encode())
            file_value.close()
            return True
        except:
            file_value.close()
            return False

    #Zip is taken with try and except for the case if location matches try else except ..............
    def set_zip_case(self,name_of_file,answer):
        file_value = zipfile.ZipFile(name_of_file)
        decent = file_value.filelist[0]
        try:
            file_value.read(decent.filename,pwd=str(answer).encode())
            file_value.close()
            return True
        except:
            file_value.close()
            return False

    #this is the function for selecting the office files and documents ..................
    def set_ms_office_case(self,object_of_the_file,asnwer):
        mine_self_file_case = msoffcrypto.OfficeFile(object_of_the_file)
        mine_self_file_case.load_key(password=str(asnwer))
        try:
            mine_self_file_case.decrypt(io.BytesIO())
            return True
        except msoffcrypto.exceptions.InvalidKeyError:
            return False
        
    #A function to Select the hash values and Generate the results for the same .........
    def set_hash_case(self,value_hash_case,solution,value_of_number):
        h = genetatro_value_of_hash_case(solution)
        # A if Else condition for different cases of HASH values and there different methods ........
        if value_of_number == "1":
            if h.blake2s() == value_hash_case:
                return True
            else:
                return False
        elif value_of_number =="2":
            if h.blake2b() == value_hash_case:
                return True
            else:
                return False
        elif value_of_number =="3":
            if h.sha512() == value_hash_case:
                return True
            else:
                return False
        elif value_of_number =="4":
            if h.sha384() == value_hash_case:
                return True
            else:
                return False
        elif value_of_number =="5":
            if h.sha256() == value_hash_case:
                return True
            else:
                return False
        elif value_of_number =="6":
            if h.sha224() == value_hash_case:
               return True
            else:
                return False
        elif value_of_number =="7":
            if h.sha1() == value_hash_case:
                return True
            else:
                return False
        elif value_of_number =="8":
            if h.md5() == value_hash_case:
                return True
            else:
                return False


#A creator of Hash Values and check for the same ........................ 
class genetatro_value_of_hash_case:

    def __init__(self,input_of_structural_data):
        self.hash_str = input_of_structural_data 
    def sha512(self):
        return hashlib.sha512(self.hash_str.encode('utf-8')).hexdigest()
    def blake2b(self):
        return hashlib.blake2b(self.hash_str.encode('utf-8')).hexdigest()
    def blake2s(self):
        return hashlib.blake2s(self.hash_str.encode('utf-8')).hexdigest()
    def sha1(self):
        return hashlib.sha1(self.hash_str.encode('utf-8')).hexdigest()
    def sha256(self):
        return hashlib.sha256(self.hash_str.encode('utf-8')).hexdigest()
    def sha384(self):
        return hashlib.sha384(self.hash_str.encode('utf-8')).hexdigest()
    def sha224(self):
        return hashlib.sha224(self.hash_str.encode('utf-8')).hexdigest()
    def md5(self):
        return hashlib.md5(self.hash_str.encode('utf-8')).hexdigest()
    
   
    


# Here is The section which helps in cracking the password of the system and its function and process for the same is done in this class ...........................
class crack_password_section_case:
    def __init__(self):
        self.gen = start_section_gen_value_case()
        self.key = set_key_case()
        #-------------------- value of the colors of the system selected as ----------------------------------
        self.value_color_green_case = colorama.Fore.GREEN
        self.value_color_yellow_case = colorama.Fore.YELLOW
        self.value_color_blue_case = colorama.Fore.BLUE
        self.value_color_red_case = colorama.Fore.RED
        self.value_color_reset_case = colorama.Fore.RESET

        self.value_color_bright_case = colorama.Style.BRIGHT
        self.value_color_dim_case = colorama.Style.DIM
        self.value_color_normal_case = colorama.Style.NORMAL
        self.value_color_reset_all_case = colorama.Style.RESET_ALL


        #---------------------------starting the Code for GUI --------------------------------------------


        self.main_value_for_intorduction = f"""  
        {self.value_color_red_case}""CKALL !! ""(Cracking for All){self.value_color_yellow_case} 
        {self.value_color_green_case} A Complete Solution to Password Cracking 
        (With all Features !)                
        Creator - ({self.value_color_blue_case} ISM_Team 1 {self.value_color_green_case}){self.value_color_reset_all_case}
        """

    #value of password cracked is obtained from the backend and presented over here .........................
    def value_of_password_cracked(self,value_tar_case_shift,value_of_ans,time_of_the_object_case):
        main.clear()
        print(self.main_value_for_intorduction)
        value_style_test_case = "-"*len(value_of_ans)
        value_sy2_test_case = "-"*len(value_tar_case_shift)
        value_of_hrs_case,value_of_mins_case,value_of_s_case = main.the_system_of_timer_clock_to_check(time_of_the_object_case)

        value_of_time_case_length = "-"*len(f"{value_of_hrs_case}{value_of_mins_case}{value_of_s_case}")

        show_key = f"""{self.value_color_bright_case}{self.value_color_red_case}
        ---------------{value_of_time_case_length}---------------

    {self.value_color_green_case}Value_of_time_taken: 
    {self.value_color_red_case}[{self.value_color_green_case}{value_of_hrs_case}{self.value_color_green_case}:
    {self.value_color_red_case}{value_of_mins_case}{self.value_color_green_case}:
    {self.value_color_red_case}{value_of_s_case}{self.value_color_green_case}]  

        ------------------{value_of_time_case_length}---------------


        {self.value_color_green_case}*****************************{self.value_color_green_case}


        ---------------{value_style_test_case}{value_sy2_test_case}---------------

        {self.value_color_green_case}The Password Found From The Search:  
        {self.value_color_blue_case}Value_of_Target : {self.value_color_red_case}
        [{self.value_color_green_case}{value_tar_case_shift}{self.value_color_red_case}] 
        {self.value_color_blue_case}Password_cracked : {self.value_color_red_case}
        [{self.value_color_green_case}{value_of_ans}{self.value_color_red_case}]   

        ---------------{value_style_test_case}{value_sy2_test_case}---------------
        {self.value_color_reset_all_case}
        """
        
        print(show_key)


    #Defining the function for the case of Dictionary here we create a dictionary scenario .................
    def the_created_dict_from_gene(self,value_tar_case_shift,value_of_answer,chnage_of_object_time):
        main.clear()
        print(self.main_value_for_intorduction)
        value_style_test_case = "-"*len(value_of_answer)
        value_sy2_test_case = "-"*len(value_tar_case_shift)
        vla_for_hrs_case,vla_for_min_case,vla_for_s_case = main.the_system_of_timer_clock_to_check(chnage_of_object_time)

        vlaue_fo_length_of_time = "-"*len(f"{vla_for_hrs_case}{vla_for_min_case}{vla_for_s_case}")
        value_of_key_get = f"""{self.value_color_bright_case}{self.value_color_red_case}

        -----------{vlaue_fo_length_of_time}---------------,
         {self.value_color_green_case}Value_of_time_taken: {self.value_color_red_case}
         [{self.value_color_green_case}{vla_for_hrs_case}{self.value_color_red_case}:
         {self.value_color_green_case}{vla_for_min_case}{self.value_color_red_case}:
         {self.value_color_green_case}{vla_for_s_case}{self.value_color_red_case}]         
        ---------------{vlaue_fo_length_of_time}-----------
        
        {self.value_color_bright_case}*********************************************{self.value_color_red_case}


        ---------------------{value_style_test_case}{value_sy2_test_case}----------------


        {self.value_color_green_case}Location of Dictionary created At:  
        {self.value_color_blue_case}Value_of_Target : {self.value_color_red_case}
        [{self.value_color_green_case}{value_tar_case_shift}{self.value_color_red_case}] 
        {self.value_color_blue_case}Place where File is Saved: {self.value_color_red_case}
        [{self.value_color_green_case}{value_of_answer}{self.value_color_red_case}]  


        ------------------------{value_style_test_case}{value_sy2_test_case}----------------
        {self.value_color_reset_all_case}
        """
        print(value_of_key_get)


    def clear(self):
        os.system("clear")

    def the_system_of_timer_clock_to_check(self,when_the_time_starts):
        the_total_time_taken = time.time() - when_the_time_starts 
        value_of_min_case= the_total_time_taken // 60
        value_of_sec_case = the_total_time_taken % 60
        value_of_hour_case = value_of_min_case // 60
        value_of_min_case = value_of_min_case % 60 

        return int(value_of_hour_case),int(value_of_min_case),int(value_of_sec_case)

    def value_gen_disp_dictionary(self):
        while self.the_case_where_its_stop:
            for i in ["\\","|","/","-"]:
                time.sleep(0.4)
                value_of_d_case = i*3
                print()
                print(f"\033[A{self.value_color_bright_case}{self.value_color_red_case}Genrating{value_of_d_case} {self.value_color_reset_all_case}\033[A")


    def vallue_case_insist_trying_to_solve(self,key,obj_time_time):
        value_of_hrs_case,value_of_min_case_alert,alert_sec_case = main.the_system_of_timer_clock_to_check(obj_time_time)
        length_of_val = " "*int(20-len(key))
        print()
        print(f"\033[A{self.value_color_bright_case}{self.value_color_red_case}Trying [{self.value_color_green_case}{key}{self.value_color_red_case}]{length_of_val}[{self.value_color_blue_case}{value_of_hrs_case}:{value_of_min_case_alert}:{alert_sec_case}{self.value_color_red_case}] [{self.value_color_blue_case}To Kill the Process(Ctrl+C){self.value_color_red_case}]{self.value_color_reset_all_case}\033[A")


    def Value_of_start_section(self):
        main.clear()
        print(self.main_value_for_intorduction)
        print(f"{self.value_color_green_case}Choose_the_Value -> {self.value_color_blue_case}[1]{self.value_color_red_case} RandomCrackingTech {self.value_color_blue_case}[2]{self.value_color_red_case} DictionayAttack {self.value_color_blue_case}[3]{self.value_color_red_case} BruteForceAttack {self.value_color_blue_case}[0]{self.value_color_red_case} Leave")

        commands = input(f"{self.value_color_bright_case}{self.value_color_green_case}CK{self.value_color_red_case}*{self.value_color_green_case}ALL->{self.value_color_reset_all_case} ")


        if commands =="0":
            print(f"{self.value_color_green_case}Thank You{self.value_color_green_case}This is Created by Ayush Raj  (Happy Cracking !){self.value_color_reset_all_case}")
            exit()


        #*************************************************************************************************************************************************************************************************************************************************************************************************************************    

        elif commands == "1":
            print(f"{self.value_color_green_case}Value to Choose(file Format) -> {self.value_color_blue_case}[1]{self.value_color_red_case} In PDF {self.value_color_blue_case}[2]{self.value_color_red_case} In RAR {self.value_color_blue_case}[3]{self.value_color_red_case} In ZIP {self.value_color_blue_case}[4]{self.value_color_red_case}In MS_Office")

            print(f"{self.value_color_blue_case}       {self.value_color_blue_case}[5]{self.value_color_red_case} Hash Cases {self.value_color_blue_case}[6]{self.value_color_red_case} Create A Dictionary {self.value_color_red_case}[0]{self.value_color_blue_case} Leave{self.value_color_reset_all_case}")
            value_of_comm_b = input(f"{self.value_color_bright_case}{self.value_color_red_case}CK{self.value_color_green_case}*{self.value_color_red_case}ALL ->{self.value_color_reset_all_case} ")


            if value_of_comm_b == "1":
                value_of_pdf_b = input(f"{self.value_color_red_case}Write the Location of PDF File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                value_of_limit_b = int(input(f"{self.value_color_red_case}Total TestCases u want to Check(Limit) ->{self.value_color_reset_all_case}"))

                val_of_time_when_start = time.time()
                for i in self.gen.Random(value_of_str_b,value_of_min_b,value_of_max_b,value_of_limit_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_pdf_case(value_of_pdf_b,i) == True:
                        main.value_of_password_cracked(value_of_pdf_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "2":
                value_of_rar_b = input(f"{self.value_color_red_case}Write the Location of RAR File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                value_of_limit_b = int(input(f"{self.value_color_red_case}Total TestCases u want to Check(Limit) ->{self.value_color_reset_all_case}"))
                val_of_time_when_start = time.time()
                for i in self.gen.Random(value_of_str_b,value_of_min_b,value_of_max_b,value_of_limit_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_rar_case(value_of_rar_b,i) == True:
                        main.value_of_password_cracked(value_of_rar_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()


            elif value_of_comm_b == "3":
                value_of_zip_b = input(f"{self.value_color_red_case}Write the Location of ZIP File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                value_of_limit_b = int(input(f"{self.value_color_red_case}Total TestCases u want to Check(Limit) ->{self.value_color_reset_all_case}"))
                val_of_time_when_start = time.time()

                for i in self.gen.Random(value_of_str_b,value_of_min_b,value_of_max_b,value_of_limit_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_zip_case(value_of_zip_b,str(i)) == True:
                        main.value_of_password_cracked(value_of_zip_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()
            
            elif value_of_comm_b == "4":
                value_of_b_F = input(f"{self.value_color_red_case}Write the Location of Office File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                value_of_limit_b = int(input(f"{self.value_color_red_case}Total TestCases u want to Check(Limit) ->{self.value_color_reset_all_case}"))
                value_of_ms_bas = open(value_of_b_F,"rb")
                val_of_time_when_start = time.time()
                for i in self.gen.Random(value_of_str_b,value_of_min_b,value_of_max_b,value_of_limit_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_ms_office_case(value_of_ms_bas,str(i)) == True:
                        main.value_of_password_cracked(value_of_b_F,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "5":
                value_of_hash_b =input(f"{self.value_color_red_case}Write the Encrypted Value ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.value_color_red_case}Choose Values : [1]BLAKE2S [2]BLAKE2B  [3]SHA512 [4]SHA384 [5]SHA256 [6]SHA224 [7]SHA1[8]MD5 Type ->{self.value_color_reset_all_case}")
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                value_of_limit_b = int(input(f"{self.value_color_red_case}Total TestCases u want to Check(Limit) ->{self.value_color_reset_all_case}"))

                val_of_time_when_start = time.time()
                for i in self.gen.Random(value_of_str_b,value_of_min_b,value_of_max_b,value_of_limit_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_hash_case(value_of_hash_b,str(i),hash_type) == True:
                        main.value_of_password_cracked(value_of_hash_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()


            elif value_of_comm_b == "6":
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                value_of_limit_b = int(input(f"{self.value_color_red_case}Total TestCases u want to Check(Limit) ->{self.value_color_reset_all_case}"))

                value_of_path_b = input(f"{self.value_color_red_case}Write The Location of File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()

                val_of_time_when_start = time.time()
                b_list = open(value_of_path_b,"w")
                th = threading.Thread(target=main.value_gen_disp_dictionary)
                self.the_case_where_its_stop = True
                th.start()
                for i in self.gen.Random(value_of_str_b,value_of_min_b,value_of_max_b,value_of_limit_b):
                      b_list.write(str(i)+"\n")
                b_list.close()
                self.the_case_where_its_stop = False
                time.sleep(2)
                main.the_created_dict_from_gene(value_of_str_b,value_of_path_b,val_of_time_when_start)
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()
           
        #***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************** 

        elif commands == "2":
            print(f"{self.value_color_green_case}Value to Choose(file Format) -> {self.value_color_blue_case}[1]{self.value_color_red_case} In PDF {self.value_color_blue_case}[2]{self.value_color_red_case} In RAR {self.value_color_blue_case}[3]{self.value_color_red_case} In ZIP {self.value_color_blue_case}[4]{self.value_color_red_case}In MS_Office")

            print(f"{self.value_color_blue_case}       {self.value_color_blue_case}[5]{self.value_color_red_case} Hash Cases {self.value_color_blue_case}[6]{self.value_color_red_case} Create A Dictionary {self.value_color_red_case}[0]{self.value_color_blue_case} Leave{self.value_color_reset_all_case}")
            value_of_comm_b = input(f"{self.value_color_bright_case}{self.value_color_red_case}CK{self.value_color_green_case}*{self.value_color_red_case}ALL ->{self.value_color_reset_all_case} ")

            if value_of_comm_b == "1":
                value_of_pdf_b = input(f"{self.value_color_red_case}Write the Location of PDF File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                
                value_of_dict_b = input(f"{self.value_color_red_case}Location of Dictionary File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()

                val_of_time_when_start = time.time()
                for i in self.gen.cdict(value_of_dict_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_pdf_case(value_of_pdf_b,i) == True:
                        main.value_of_password_cracked(value_of_pdf_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "2":
                value_of_rar_b = input(f"{self.value_color_red_case}Write The Location of RAR File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()

                value_of_dict_b = input(f"{self.value_color_red_case}Location of Dictionary File ->{self.value_color_reset_all_case}")

                val_of_time_when_start = time.time()
                for i in self.gen.cdict(value_of_dict_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_rar_case(value_of_rar_b,i) == True:
                        main.value_of_password_cracked(value_of_rar_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "3":
                value_of_zip_b = input(f"{self.value_color_red_case}Write Location of ZIP File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()

                value_of_dict_b = input(f"{self.value_color_red_case}Location of Dictionary File ->{self.value_color_reset_all_case}")

                val_of_time_when_start = time.time()
                for i in self.gen.cdict(value_of_dict_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_zip_case(value_of_zip_b,str(i)) == True:
                        main.value_of_password_cracked(value_of_zip_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "4":
                value_of_b_F = input(f"{self.value_color_red_case}Write the Location of Office Files ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_dict_b = input(f"{self.value_color_red_case}Location of Dictionary File ->{self.value_color_reset_all_case}")
                value_of_ms_bas = open(value_of_b_F,"rb")
                val_of_time_when_start = time.time()
                for i in self.gen.cdict(value_of_dict_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_ms_office_case(value_of_ms_bas,str(i)) == True:
                        main.value_of_password_cracked(value_of_b_F,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "5":
                value_of_hash_b =input(f"{self.value_color_red_case}Write a Hash Code ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.value_color_red_case}Choose Values : [1]BLAKE2S [2]BLAKE2B  [3]SHA512 [4]SHA384 [5]SHA256 [6]SHA224 [7]SHA1[8]MD5 Type ->{self.value_color_reset_all_case}")
                value_of_dict_b = input(f"{self.value_color_red_case}Location of Dictionary File ->{self.value_color_reset_all_case}")
                val_of_time_when_start = time.time()
                for i in self.gen.cdict(value_of_dict_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_hash_case(value_of_hash_b,i,hash_type) == True:
                        main.value_of_password_cracked(value_of_hash_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

        #*****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************

        elif commands == "3":
            print(f"{self.value_color_green_case}Value to Choose(file Format) -> {self.value_color_blue_case}[1]{self.value_color_red_case} In PDF {self.value_color_blue_case}[2]{self.value_color_red_case} In RAR {self.value_color_blue_case}[3]{self.value_color_red_case} In ZIP {self.value_color_blue_case}[4]{self.value_color_red_case}In MS_Office")
            print(f"{self.value_color_blue_case}       {self.value_color_blue_case}[5]{self.value_color_red_case} Hash Cases {self.value_color_blue_case}[6]{self.value_color_red_case} Create A Dictionary {self.value_color_red_case}[0]{self.value_color_blue_case} Leave{self.value_color_reset_all_case}")

            value_of_comm_b = input(f"{self.value_color_bright_case}{self.value_color_red_case}CK{self.value_color_green_case}*{self.value_color_red_case}ALL ->{self.value_color_reset_all_case} ")

            if value_of_comm_b == "1":
                value_of_pdf_b = input(f"{self.value_color_red_case}Write the Location of PDF File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                
                val_of_time_when_start = time.time()
                for i in self.gen.Bforce(value_of_str_b,value_of_min_b,value_of_max_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_pdf_case(value_of_pdf_b,i) == True:
                        main.value_of_password_cracked(value_of_pdf_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "2":
                value_of_rar_b = input(f"{self.value_color_red_case}Write the Location of RAR File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))

                val_of_time_when_start = time.time()
                for i in self.gen.Bforce(value_of_str_b,value_of_min_b,value_of_max_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_rar_case(value_of_rar_b,i) == True:
                        main.value_of_password_cracked(value_of_rar_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "3":
                value_of_zip_b = input(f"{self.value_color_red_case}Write the Location of ZIP File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
               
                val_of_time_when_start = time.time()
                for i in self.gen.Bforce(value_of_str_b,value_of_min_b,value_of_max_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_zip_case(value_of_zip_b,str(i)) == True:
                        main.value_of_password_cracked(value_of_zip_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "4":
                value_of_b_F = input(f"{self.value_color_red_case}Write the Location of Office File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))

                value_of_ms_bas = open(value_of_b_F,"rb")
                val_of_time_when_start = time.time()
                for i in self.gen.Bforce(value_of_str_b,value_of_min_b,value_of_max_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_ms_office_case(value_of_ms_bas,str(i)) == True:
                        value_of_ms_bas.close()
                        main.value_of_password_cracked(value_of_b_F,i,val_of_time_when_start)
                        break
                    else:
                        pass
                value_of_ms_bas.close()
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "5":
                value_of_hash_b =input(f"{self.value_color_red_case}Write the Encrypted Value ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.value_color_red_case}Choose Values : [1]BLAKE2S [2]BLAKE2B  [3]SHA512 [4]SHA384 [5]SHA256 [6]SHA224 [7]SHA1[8]MD5 Type ->{self.value_color_reset_all_case}")
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))

                val_of_time_when_start = time.time()
                for i in self.gen.Bforce(value_of_str_b,value_of_min_b,value_of_max_b):
                    main.vallue_case_insist_trying_to_solve(i,val_of_time_when_start)
                    if self.key.set_hash_case(value_of_hash_b,str(i),hash_type) == True:
                        main.value_of_password_cracked(value_of_hash_b,i,val_of_time_when_start)
                        break
                    else:
                        pass
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

            elif value_of_comm_b == "6":
                value_of_str_b = input(f"{self.value_color_red_case}The Data Input (Range) ->{self.value_color_reset_all_case}")
                value_of_min_b = int(input(f"{self.value_color_red_case}Password's Minimum Len ->{self.value_color_reset_all_case}"))
                value_of_max_b = int(input(f"{self.value_color_red_case}Password's Maximum Len ->{self.value_color_reset_all_case}"))
                value_of_path_b = input(f"{self.value_color_red_case}Write The Location of File ->{self.value_color_reset_all_case}").replace("'","").replace('"',"").lstrip().rstrip()

                val_of_time_when_start = time.time()
                b_list = open(value_of_path_b,"w")
                th = threading.Thread(target=main.value_gen_disp_dictionary)
                self.the_case_where_its_stop = True
                th.start()
                for i in self.gen.Bforce(value_of_str_b,value_of_min_b,value_of_max_b):
                    b_list.write(str(i)+"\n")
                b_list.close()
                self.the_case_where_its_stop = False
                time.sleep(2)
                main.the_created_dict_from_gene(value_of_str_b,value_of_path_b,val_of_time_when_start)
                input(f"{self.value_color_green_case}Press Enter to Main ->{self.value_color_reset_all_case}")
                main.Value_of_start_section()

        #=================================================================================================================================================================================================================================== 


if __name__ == "__main__":
    while True:
        try:
            main = crack_password_section_case()
            main.Value_of_start_section()
        except KeyboardInterrupt:
            pass
