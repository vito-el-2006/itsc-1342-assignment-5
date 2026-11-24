# Vittorio Enzo Lester - Assignment 5

def sanitize_ip_list(ip_list, blocked_ip):
    # TODO: Clean up the IP list according to the prompt instructions.
    # Note: Pay close attention to how items are iterated or removed!
    clean_list = []
    for ip in ip_list[:]:
        if ip == blocked_ip:
            ip_list.remove(ip)
        elif ip == "invalid":
            clean_list.append("0.0.0.0")
        else:
            clean_list.append(ip)
            
    return clean_list
