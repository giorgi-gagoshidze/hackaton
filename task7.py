#შექმენით რაიმე string ტიპის ცვლადი და დაprint'ეთ ამ ცვლადის გამოყენებით ამავე სტრინგის შებრუნებული ვერსია.
user = input('print something: ')
def backwards(string):
    return string[::-1]
print(backwards(user))
