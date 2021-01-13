
gifts= [
        "partridge in a pear tree", "turtle doves", "french hens", "calling birds", "gold rings", "geese a-laying", "swans a-swimming", "maids a-milking", "ladies dancing", "lords a-leaping", "pipers piping","drummers drumming"
    ]
x=0
while x == 0:
    try:
        day = input('What day are you on?\n')
        if int(day) > 0 and int(day) < 13:
            x +=1
        else:
            print('Not a valid day.')
    except:
        print('Not a number.')
   
   
        
x=0

while x == 0:
    gift = input('What gift do you want to know the count of?\n ').lower()
    for in_gift in gifts:
            if gift in in_gift:        
               gift_count = (int(gifts.index(in_gift))+1) *(int(day) - int(gifts.index(in_gift)))
               if gift_count < 1:
                   print ('You have not received that gift yet.')
                   continue
               x +=1
               break
            elif gift not in in_gift:
                continue
            else:
                print('Could not find matching gift.')    
                print(gift)
                                    
        


#gift_count = (int(gifts.index(days))+1) *(int(day) - int(gifts.index(days)))
print ('You got ' + str(gift_count) +' ' + in_gift+ ' on day ' + str(day)+'.')

