// Program to convert amount( in words )into amount(number)
// Name : Vikas More
// Roll : 539
// College : Ferguson College (Autonomous), FC road, Pune.
// Course  : Master Of Computer Science.
// Year of study : 1st year
// Language: Python3.7


one = [ "", "one ", "two ", "three ", "four ", 

        "five ", "six ", "seven ", "eight ", 

        "nine ", "ten ", "eleven ", "twelve ", 

        "thirteen ", "fourteen ", "fifteen ", 

        "sixteen ", "seventeen ", "eighteen ", 

        "nineteen "]; 


ten = [ "", "", "twenty ", "thirty ", "forty ", 

        "fifty ", "sixty ", "seventy ", "eighty ", 

        "ninety "]; 

  
 

def numToWords(n, s): 

  

    str = "";

    if (n > 19): 

        str += ten[n // 10] + one[n % 10]; 

    else: 

        str += one[n];  

    if (n): 

        str += s; 

  

    return str; 
 

def convertToWords(n): 

    out = ""; 

    out += numToWords((n // 10000000),  

                            "crore "); 

    out += numToWords(((n // 100000) % 100), 

                                   "lakh "); 
 

    out += numToWords(((n // 1000) % 100),  

                             "thousand "); 

  

    out += numToWords(((n // 100) % 10),  

                            "hundred "); 
    if (n > 100 and n % 100): 

        out += "and "; 

    out += numToWords((n % 100), ""); 
    return out; 


n=int(input("Enter the amount :"))
print(convertToWords(n));  
 
