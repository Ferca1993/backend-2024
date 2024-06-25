# Type hints

string = "Ivan"
print(string)
print(type(string))

string_number = 12
print(string_number)
print(type(string_number))


#When We're working with fastapi it ask for us typing each variable in order for slog up better along with.
#Although it's not demand but it'd help to carry out operation prompter,and if it doesn't accomplish FastApi doesn't go ahead with the request
typed_variable = "My typed variable" # No OK
typed_variable: str = "My typed variable" #  OK
print(typed_variable)
print(type(typed_variable))


