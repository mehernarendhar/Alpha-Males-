#Email Sanitizer
def sanitize_email(raw_input: str) -> str:
    count=0
    if '@' not in raw_input:
        return '"Invalid Email"'
    else:
        for i in raw_input:
            if i == '@':
                count+=1            
    if count>1:
        return '"Invalid Email"'
    else:
        return f'"{raw_input.strip().lower()}"'
print(sanitize_email("  User@Example.com  "))
print(sanitize_email("test@domain.org"))
print(sanitize_email("myname-website.com"))
print(sanitize_email("admin@@company.com"))
print(sanitize_email("  "))
