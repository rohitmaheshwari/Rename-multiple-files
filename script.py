# Python3 code to rename multiple files in a directory
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    
    for count, filename in enumerate(os.listdir("C:/Users/rohit/OneDrive/Desktop/dataset1/demo/")):
	# start renaming from str(count + 1) i.e 1
        dest = str(count + 1) + ".jpg"
        src = 'C:/Users/rohit/OneDrive/Desktop/dataset1/demo/' + filename 
        dest = 'C:/Users/rohit/OneDrive/Desktop/dataset1/demo/' + dest 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dest) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
