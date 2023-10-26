class Category:


  def __init__(self, category):
    self.category = category
    self.ledger = []


  def deposit(self, amount, description = ''):
    send = {"amount": amount, "description": description}
    self.ledger.append(send)


  def withdraw(self, amount, description = ''):
    current_balance = self.get_balance()
    if current_balance >= amount:
     
      send = {"amount": amount - amount - amount, "description": description}
      self.ledger.append(send)
      return True
    else:
      return False
   

  def get_balance(self):
    balance = 0.0
    for entry in self.ledger:
      balance = entry['amount'] + balance
    return balance
    

  def transfer(self, amount, category):
    current_balance = self.get_balance()
    if current_balance >= amount:
      self.withdraw(amount, "Transfer to " + category.category)
      category.deposit(amount, "Transfer from " + self.category)
      return True
    else:
      return False
    

  def check_funds(self, amount):
    current_bal = self.get_balance()
    if amount > current_bal:
      return False
    else: 
      return True


  def __str__(self):
    st = ''
    final = ''

    category_length = len(self.category)
    asterisk_num = round((30 - category_length) / 2)
    final = '*' * asterisk_num + self.category + '*' * asterisk_num 
    
    current_balance = self.get_balance()
    
    for file in self.ledger:
      
      cost = str(file['amount'])
      
      if len(str(file['amount'])) < 4:
        cost = str(file['amount']) + ".00"
        
      word_length = len(file['description'])
      num_spaces = 29 - word_length - len(cost)
      
      
      final = final + '''
''' + file['description'][:23] + " " + " " * num_spaces + cost[:7]
      

    st =  st + final + '''
''' + 'Total: ' + str(current_balance)
    return st



def create_spend_chart(categories):

  str = ''
  running_total = 0
  longest = ['', 0]
  count = 0;
  one = ['', '','','','','','','','','','','']
  two = ['', '','','','','','','','','','','']
  three = ['', '','','','','','','','','','','']
  new_categories = []

  for category in categories:
    if len(category.category) > longest[1]:
      longest[1] = len(category.category)
      longest[0] = category

  for category in categories:
    new_category = category.category
    while len(new_category) < longest[1]:
      new_category = new_category + " "
    new_categories.append(new_category)


  x = []
  for category in new_categories:
    hello = [*category]
    x.append(hello)
  
  new_string = ''
  for m, n, z in zip(*x):
    new_string = new_string + '''
     ''' + m + " " + " " + n + " " + " " + z + " " + " "

  
  categories_ledgers = []
  for category in categories:
    for ledger in category.ledger:
      if ledger['amount'] < 0:
        categories_ledgers.append([category.category, ledger['amount']])
        running_total = running_total - ledger['amount']

  individual_total = ''

  curr_category = ""
  for category in categories:
    loop = []
    count = count + 1
    curr_category = category.category

    individual_total = 0
    for hi in categories_ledgers:
      if hi[0] == curr_category:
        individual_total = individual_total - hi[1]

    current_percentage = round(int(individual_total / running_total * 100))

    word = curr_category
    

    if count == 1:
      lists = [one]
      one[0] = word
    elif count == 2:
      lists = [two]
      two[0] = word
    else:
      lists = [three]
      three[0] = word

    for loop in lists:
        percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        for percent in percentages:
          if current_percentage >= percent:
            num = percentages.index(percent) + 1
            loop[num] = 'o'

  
  
  hi = '''Percentage spent by category
100|''' + ' ' + one[11] + ' ' + ' ' + ' ' + two[11] + ' ' + three[11] + ' ' + ' ' + ' ' + ' ' + ''' 
 90|''' + ' ' + one[10] + ' ' + ' ' + ' ' + two[10] + ' ' + ' ' + three[10] + ' ' + ' ' + ' ' + ' ' + '''
 80|''' + ' ' + one[9] +  ' ' + ' ' + ' ' + two[9] + ' ' + ' ' + three[9] + ' ' + ' ' + ' ' + ' ' + '''
 70|''' + ' ' + one[8] + ' ' + ' ' + ' ' + two[8] + ' ' + ' ' + three[8] + ' ' + ' ' + ' ' + '''
 60|''' + ' ' + one[7] + ' ' + ' ' + ' ' + two[7] + ' ' + three[7] + ' ' + ' ' + ' ' + ' ' + '''
 50|''' + ' ' + one[6] + ' ' + ' ' +  ' ' + two[6] + ' ' + ' ' + ' ' + ' ' + three[6] + ' ' +  '''
 40|''' + ' ' + one[5] + ' ' + ' ' + ' ' + two[5] + ' ' + ' ' +  three[5] + ' ' + ' ' + ' ' + '''
 30|''' + ' ' + one[4] + ' ' + ' ' + ' ' + two[4] + ' ' + ' ' +  three[4] + ' ' + ' ' + ' ' + '''
 20|''' + ' ' + one[3] + ' ' + ' ' + ' ' + two[3] + ' ' + ' ' +  three[3] +  ' ' + ' ' + '''
 10|''' + ' ' + one[2] + ' ' + ' ' + ' ' + two[2] + ' ' + ' ' +  three[2] +   ' ' + ' ' + '''
  0|''' + ' ' + one[1] + ' ' + ' ' + two[1] + ' ' + ' ' + three[1] + ' ' + ' ' + '''
    ----------''' + new_string + ''''''

  
  str = str + hi
    

  return str