"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(7) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 
"""

def diamond(size):
  print(" "*(size-1) + "*")
  for i in range (1, size):
    print (" "*(size-i-1) + "*" + " "*(2*i-1)+"*")
  for j in range (1, size-1):
    print (" "*(size+j-(size)) + "*" + " "*(size-2*j+(size-3))+"*")
  print(" "*(size-1) + "*")
  