'''Grundläggande övningar.'''


def sum_of_digits(x):
    '''Summera alla värdesiffrorna i ett heltal.

    Exempel: 389 består av 3, 8 och 9 och resultatet blir 3 + 8 + 9 = 20
    '''
    results = 0
    while x > 0:
        remainder = x % 10
        results += remainder
        x = (x-remainder) / 10
    return results


def binary_string_to_int(s):
    '''Översätt en sträng med ett binärt tal till ett heltal.
    '''
    return int(s, 2)


def count_numbers_and_letters(s):
    '''Räkna antalet bokstavstecken och siffersymboler i strängen `s`.

    Resultatet returneras som en dictionary med nycklarna 'letters' och
    'numbers'.
    '''
    dict = {'letters': 0,'numbers': 0}
    dict['letters'] = sum(c.isalpha() for c in s)
    dict['numbers'] = sum(c.isdigit() for c in s)
    return dict


def sum_of_cubes(x):
    '''Summera all kuber (i^3) av heltalen från 1 till och med `x`.

    Exempel:
    x = 4: 1^3 + 2^3 + 3^3 + 3^4 = 100
    '''
    return sum(i**3 for i in range(1,x+1))


def savings_calculator(inital_amount, monthly_deposit, annual_interest, years):
    '''Beräkna värdet för ett månadssparande efter `years` år.

    Sparandet startas med beloppet `intial_amount` kronor och varje månad
    inbetalas beloppet `monthly_deposit` kronor.

    Räntan utbetalas månadsvis (`annual_interest` / 12). Räntan anges i procent.
    Argumentet `years` anger hur många hela år sparandet kommer att fortgå.
    '''
    pass
