import re

def extract_contact_info(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\d{10}', text)

    return {
        "email": email[0] if email else "Not Found",
        "phone": phone[0] if phone else "Not Found"
    }


# 🧠 Extract Name (simple logic: first line)
def extract_name(text):
    lines = text.split("\n")
    for line in lines:
        if len(line.strip()) > 3:
            return line.strip()
    return "Not Found"


# 📊 Extract Experience (like 2 years, 3 yrs)
def extract_experience(text):
    exp = re.findall(r'(\d+)\+?\s*(years|yrs)', text.lower())
    
    if exp:
        return exp[0][0] + " years"
    
    return "Not Found"