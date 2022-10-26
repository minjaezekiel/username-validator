def CodelandUsernameValidation(strParam):
  a = len( strParam )
  if a > 4 and a < 25:
    print ("True")
    #start with letter check
    letter_check = str(strParam)
    bool(letter_check)
    # create a set of allowed characters
    allowed_chars = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"))
    string = strParam
    validator = set((string))

    if validator.issubset(allowed_chars):
      print ("true")
    else:
        print ("false") 
    
  # code goes here
  return strParam

# keep this function call here 
print(CodelandUsernameValidation(input()))