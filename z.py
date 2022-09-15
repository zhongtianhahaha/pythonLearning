"""Exercise 2: Write another program thatprompts for а list of numbers as aboveand at the end prints out both the

maximum and minimum of the numbersinstead of the average.
"""
Max = None
Min = None
while True:
   n= input( 'Enter a number :')
         if n == 'done':
                break
         try:
            n = float(n)
         except:
               print( '%s is not a number '%n)
               continue
  if Max is None or Max<n:
      Max = n
if Min is None or Min > n:
    Min = n
print( ' Maximum: ' , Max, "Minimum:",Min)
