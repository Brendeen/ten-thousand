can you simplify this code?  def calculate_score(roll):

(pasted code from calculate_score into chatgpt)

Certainly, here's a simplified version of the code:

python
Copy code
def calculate_score(roll):
    roll_sum = 0
    lst = [roll.count(i) for i in range(1, 7)]
    straight_counter = lst.count(1) == 6

    for freq, count in enumerate(lst):
        if count >= 3:
            if freq == 0:
                roll_sum += (count - 2) * 1000
            else:
                roll_sum += (freq + 1) * 100 * (count - 2)
        elif freq == 0:
            roll_sum += count * 100
        elif freq == 4:
            roll_sum += count * 50

    if straight_counter or lst.count(2) == 3 or lst.count(3) == 2:
        return 1500 if straight_counter else 1200 if lst.count(3) == 2 else 1500
    return roll_sum
The code uses a list comprehension to create a list of the frequencies of each number in the roll. 
It also uses the enumerate() function to iterate over both the index and the value of each frequency in the list, 
avoiding the need to index into the list.

The if/else statements have been combined into a single for loop, which reduces redundancy and makes the code more concise. 
The code also checks for the straight, triplets, and three pairs conditions in a more efficient way, by using the count() function 
to count the number of occurrences of each frequency.

Lastly, the code uses a conditional expression to simplify the return statement, making it easier to read and understand.