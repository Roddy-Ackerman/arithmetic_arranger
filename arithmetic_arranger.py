def error_check(number_1,operator,number_2):
  error_msg_num = "Error: Numbers must only contain digits."
  error_msg_num_len = "Error: Numbers cannot be more than four digits."
  error_msg_operator = "Error: Operator must be '+' or '-'."
  #Check numbers are digits
  try:
    int(number_1)
  except:
    return error_msg_num
  try:
    int(number_2)
  except:
    return error_msg_num
  # check that the numbers are not greater than 4 digits
  try:
    if len(number_1) > 4 or len(number_2) > 4:
      raise BaseException
  except:
    return error_msg_num_len
  #Check to make sure operator is a "+" or a "-"
  try:
    if operator != "+" and operator != "-":
      raise BaseException
  except:
    return error_msg_operator
  return ""


def arithmetic_arranger(problems,answer=False):
  start = True
  spacing = "    "
  line1 = line2 = line3 = line4 =""
  try:
    if len(problems) > 5:
      raise BaseException
  except:
    return "Error: Too many problems."

  #Seperating the problems
  for prob in problems:
    temp_array = prob.split()
    #store the first number
    number_1 = temp_array[0]
    #store the operator
    operator = temp_array[1]
    #store the second number
    number_2 = temp_array[2]
    check_errors = error_check(number_1,operator,number_2)

    if check_errors != "":
      return check_errors    

    line_spacing = max(len(number_1),len(number_2))
    if operator == "+":
      add1 = int(number_1)
      add2 = int(number_2)
    else:
      sub1 = int(number_1)
      sub2 = int(number_2)

    #First problem arrangement
    if start == True:
      line1 += number_1.rjust(line_spacing + 2)
      line2 += operator + " " + number_2.rjust(line_spacing)
      line3 += "-" * (line_spacing + 2)
      if operator == "+":
          line4 += str(add1 + add2).rjust(line_spacing + 2)
      else:
        line4 += str(sub1 - sub2).rjust(line_spacing + 2)
      start = False
    
    #All other problems that are not the first
    else: 
      line1 += number_1.rjust(line_spacing + 6)
      line2 += operator.rjust(5) + " " + number_2.rjust(line_spacing)
      line3 += spacing + "-" * (line_spacing + 2)
      if answer == True:
        if operator == "+":
          line4 += spacing + str(add1 + add2).rjust(line_spacing + 2)
        else:
          line4 += spacing + str(sub1 - sub2).rjust(line_spacing + 2)

  #Check if answer is to be displayed or not
  if answer == True:
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
  return line1 +"\n" + line2 + "\n" + line3 